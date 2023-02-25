# Gas Price Comparison in Major Cities in Canada before and after COVID-19 - ETL Pipeline
## Introduction
This project aims to analyze the impact of the COVID-19 pandemic on gas prices in major cities in Canada. The project uses an ETL pipeline to process and transform the gas price data CSV to parquet format, and the data is analyzed to provide insights into the changes in gas prices before and after the pandemic. The project also compares the gas price data with the Crude Oil WTI stock data. The pipeline is built using Pyspark, Apache Airflow, and various AWS services, including Lambda, Glue, EMR, Athena, and S3. The final analytics visuals are created using Apache Superset.

## Project Structure
The project is structured into the following main components:
- Data collection and cleaning
- Data processing and analysis
- Workflow Diagram
- Pipeline Design
- Getting Started
- Results and visualization

## Data Collection and Cleaning

The [data](https://github.com/etron17/GAStimator/tree/master/data) used for this project was collected from multiple sources, including government websites and online open data sources. The data was cleaned and processed to ensure its accuracy and consistency. The cleaning process involved removing any missing or duplicate data and standardizing the data format.   
  - [Cities in Canada with Lat Long](https://simplemaps.com/data/canada-cities)
  - [Crude Oil WTI](https://ca.investing.com/commodities/crude-oil-historical-data)
  - [Canada historical gas price](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101&pickMembers%5B0%5D=2.2&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2018&cubeTimeFrame.endMonth=12&cubeTimeFrame.endYear=2022&referencePeriods=20180101%2C20221201)
  - [Canadian 3166—Codes](https://www.iso.org/obp/ui#iso:code:3166:CA)


## Workflow Diagram

At a high level, the workflow diagram for this project is illustrated below.

![Screen Shot 2023-02-22 at 6 33 38 PM](https://user-images.githubusercontent.com/90226898/220787521-862b77fd-5e8c-490b-8e17-0e2a25ce76e8.png)

1. Collecting data from multiple sources:
Data is collected from various sources and stored in a landing zone S3 bucket.

2. Triggering an event notification to Lambda function:
Once data is stored in the S3 bucket, an event notification is triggered to a Lambda function.

3. Triggering Airflow:
The Lambda function triggers Airflow dags.

4. Running PySpark code:
Airflow runs PySpark code, which is used to transform the data into a more usable format. In this case, the PySpark code converts a CSV file to a Parquet format.

5. Storing Parquet file back to S3 bucket:
Once the data is transformed to a Parquet file, it stores back to the S3 bucket.

6. Creating a table schema using Glue:
In this step, we will create a crawler. The crawler will catalog all files in the specified S3 bucket and prefix. All the files should have the same schema. In Glue crawler terminology the file format is known as a classifier. The crawler identifies the most common classifiers automatically including CSV, json and parquet. Our sample file is in the parquet format and will be recognized automatically.

7. Configure AWS Glue

8. Connect Athena to Apache Superset:

## Pipeline Design
<img width="307" alt="P2icture1" src="https://user-images.githubusercontent.com/90226898/220788861-770fbc98-65d6-4422-8b72-ef65b9c4a19f.png">

![Screen Shot 2023-02-22 at 6 45 28 PM](https://user-images.githubusercontent.com/90226898/220789137-0847a0ba-a5de-4fce-98a9-c0e3849f30ca.png)

At a high-level, the data pipeline orchestrates the following tasks:
Triggering pyspark – Tranforming CSV to parque 
1.	parase_request: Reading files from S3 bucket
2.	add_steps: Pyspark script gets triggered
3.	Watch_step: Sending an email when the dag has done

## Lambda Function Overview

![Screen Shot 2023-02-22 at 7 12 53 PM](https://user-images.githubusercontent.com/90226898/220793071-4ed5350a-c028-457c-ad07-841d919429ba.png)



## Getting Started
***1. Create an EC2 instance***

***2. Create a S3 Bucket (input)***
![Screen Shot 2023-02-22 at 8 16 07 PM](https://user-images.githubusercontent.com/90226898/220800532-cded43d9-c73e-428c-a7bf-1e2a1c08e2d7.png)

***3. Create a S3 Bucket (output)***
![Screen Shot 2023-02-22 at 8 17 25 PM](https://user-images.githubusercontent.com/90226898/220800669-fa1c7711-2b40-4659-b75f-4d1a36804197.png)

***4. Create EMR***

***5. Create emr_job_submission.py on EC2 Docker***

***6. Edit [emr_job_submission.py](https://github.com/etron17/GAStimator/blob/master/dags/emr_job_submission.py)***

***7. Trigger Lambda***

[lambda.py](https://github.com/etron17/GAStimator/blob/master/lambda/lambda.py)
<img width="1331" alt="Screen Shot 2023-02-24 at 4 26 58 PM" src="https://user-images.githubusercontent.com/90226898/221296329-ef8babca-67eb-4e6c-bfc9-d7ae585e6f31.png">

***8. Run Airflow***

![Screen Shot 2023-02-22 at 8 37 06 PM](https://user-images.githubusercontent.com/90226898/220802824-a241afdd-136c-43ba-9a4e-c88596d7ca89.png)

***9. Run Pyspark***
![Screen Shot 2023-02-22 at 8 44 53 PM](https://user-images.githubusercontent.com/90226898/220803692-c2851c8c-c6a4-40c9-a57a-c1a7b845c089.png)

***10. Check S3 Bucket (output), file transformation completed (CSV -> Parquet)***

![Screen Shot 2023-02-22 at 8 47 09 PM](https://user-images.githubusercontent.com/90226898/220803977-be6d6853-36ef-43c3-9ca1-e770f8c814a8.png)

***11. Create AWS Glue***
![Screen Shot 2023-02-22 at 8 50 36 PM](https://user-images.githubusercontent.com/90226898/220804415-f8db5f4f-ef27-4b35-907e-14d64405ad11.png)

***12. Create AWS Athena***
![Screen Shot 2023-02-22 at 8 51 35 PM](https://user-images.githubusercontent.com/90226898/220804533-c80c712b-9e01-4faf-9767-18f5fa1c57f0.png)

***13. Install Superset*** 

 https://hub.docker.com/r/apache/superset

## Results and Visualization
The COVID-19 pandemic has significantly impacted gas prices in major cities in Canada, with a substantial decline observed in the first half of 2020. The recovery of gas prices in the latter half of the year indicates a gradual return to normalcy. Comparing the gas price data with the Crude Oil WTI data highlights the significant relationship between the two variables, providing further insights into the impact of the pandemic on the oil and gas industry. The results also show that other factors, such as weather and geopolitical events, influenced gas prices.
![Screen Shot 2023-02-25 at 9 34 34 AM](https://user-images.githubusercontent.com/90226898/221362630-4571bedc-e0cf-46ce-b618-61c9c9f7d307.png)



