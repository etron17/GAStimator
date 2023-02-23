import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.emr_add_steps_operator import EmrAddStepsOperator
from airflow.contrib.sensors.emr_step_sensor import EmrStepSensor

SPARK_STEPS = [
    {
        'Name': 'jden_data_engineer',
        'ActionOnFailure': "CONTINUE",
        'HadoopJarStep': {
            'Jar': 'command-runner.jar',
            'Args': [
                '/usr/bin/spark-submit',
                '--py-files', 's3://ca-gas-libr/job.zip', 's3://{your s3 address}',
                '-p', "{'input_path': '{{task_instance.xcom_pull(task_ids='parse_request', key='s3location')}}', 'name': 'wcd-demo', 'file_type': 'txt', 'output_path': 's3://{your s3 address}', 'partition_column': '{your_column}'}"

                ]
        }
    }

]

CLUSTER_ID = "{your EMR CLUSTER_ID}"

DEFAULT_ARGS = {
    'owner': '{your_name}',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email': ['{your_email'],
    'email_on_failure': False,
    'email_on_retry': False
}

def retrieve_s3_files(**kwargs):
    s3_location = kwargs['dag_run'].conf['s3_location']
    kwargs['ti'].xcom_push(key = 's3location', value = s3_location)


dag = DAG(
    'emr_job_flow_manual_steps_dag',
    default_args = DEFAULT_ARGS,
    dagrun_timeout = timedelta(hours=2),
    schedule_interval = None
)

parse_request = PythonOperator(task_id = 'parse_request',
                                provide_context = True, 
                                python_callable = retrieve_s3_files,
                                dag = dag
                                )

step_adder = EmrAddStepsOperator(
    task_id = 'add_steps',
    job_flow_id = CLUSTER_ID,
    aws_conn_id = "aws_default",
    steps = SPARK_STEPS,
    dag = dag
)

step_checker = EmrStepSensor(
    task_id = 'watch_step',
    job_flow_id = CLUSTER_ID,
    step_id = "{{ task_instance.xcom_pull('add_steps', key='return_value')[0] }}",
    aws_conn_id = "aws_default",
    dag = dag
)

step_adder.set_upstream(parse_request)
step_checker.set_upstream(step_adder)
