from pyfiglet import Figlet
from termcolor import colored
from car import Car
from view import View


# MVC pattern - controller part
class Controller(object):

    @staticmethod
    def run_simulation():
        """
        Run simulation
        :return: None
        """
        f1 = Figlet(font='standard')
        print(colored(f1.renderText('Welcome'), 'green'))
        print(colored(f1.renderText('GAStimator'), 'green'))
        cars = Car.read_cars()
        view = View()
        meas_choice = view.ask_meas_type()
        metric_choice = view.ask_metric_choice(meas_choice)
        brand_of_car = view.ask_for_brand(cars)
        brand_list = list(cars)
        models = cars[brand_list[brand_of_car - 1]]
        model_of_car = view.print_models_and_choose(meas_choice, metric_choice,
                                                    models)
        model = models[model_of_car - 1]
        print("Your selection is:", model)
        view.edit_fuel_efficiency(model)
        view.calculate_price(meas_choice, metric_choice, model)
