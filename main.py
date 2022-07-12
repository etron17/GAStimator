from termcolor import colored
from pyfiglet import Figlet
from beautifultable import BeautifulTable

from car import read_cars
from routing import find_dest
from gas import get_prices
from conversionutils import ConversionUtils
from menuutils import MenuUtils

PROVINCES = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
             'Newfoundland and Labrador', 'Nova Scotia', 'Ontario',
             'Prince Edward Island', 'Quebec', 'Saskatchewan']
PROVINCES_CODE = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']

YES_NO = ["Yes", "No"]


def find_price(gas_prices, prov: int) -> float:
    """
    Find price for province
    :param gas_prices: Gas prices for all provinces
    :param prov: Province to find price for
    :return: Price of gas for selected province
    """
    for entry in gas_prices:
        if entry['province'] == PROVINCES[prov - 1]:
            return entry['price']

    return 0


def ask_meas_type():
    """
    Ask for measurement types
    :return: Measurement types
    """
    meas_types = ["Imperial", "Metric"]
    meas_choice = MenuUtils.menu_choice("Select measurement type: ", meas_types)
    print(meas_choice)
    return meas_choice


def ask_metric_choice():
    """
    For metric ask for L/100km or L/km
    :return: Metric choice
    """
    metric_choice = ConversionUtils.MPG
    if meas_choice == ConversionUtils.METRICS:
        metric_types = [ConversionUtils.L_PER_100KM_SUFFIX,
                        ConversionUtils.L_PER_KM_SUFFIX]
        metric_choice = MenuUtils.menu_choice("Select metric mileage type",
                                              metric_types)
        print(
            f"We're using {metric_types[metric_choice - 1]} measurement units")
    else:
        print("We're using 'MPG' measurement units")
    return metric_choice

def ask_for_brand():
    """
    Check what kind of car
    :return: Brand of car
    """
    idx = 1
    brand_table = BeautifulTable()
    for brand in cars.keys():
        brand_table.columns.header = ["No.", "Brand"]
        brand_table.rows.append([str(idx), brand])
        idx += 1
    print(brand_table)
    brand_of_car = MenuUtils.menu_choice_nolist("Please select brand of car",
                                                len(cars.keys()))
    return brand_of_car


def print_models_and_choose():
    """
    Print models for that brand
    :return:
    """
    global models
    idx = 1
    model_table = BeautifulTable()
    for model in models:
        model.set_meas_choice(meas_choice)
        model.set_metric_choice(metric_choice)
        model_table.columns.header = ["No.", "Model", "Drive", "Fuel", "Stnd",
                                      "City", "Hwy"]
        model_table.rows.append([str(idx), model.get_model(), model.get_drive(),
                                 model.get_fuel(), model.get_stnd(),
                                 model.get_city(),
                                 model.get_hwy()])
        idx += 1
    print(model_table)
    model_of_car = MenuUtils.menu_choice_nolist("Please select model of car",
                                                len(models))
    return model_of_car


def edit_fuel_efficiency():
    edit_choice = MenuUtils.menu_choice("Do you want to edit fuel efficiency?",
                                        YES_NO)
    if edit_choice == 1:
        city = float(input("Please enter fuel efficiency for city"))
        hwy = float(input("Please enter fuel efficiency for hwy"))

        model.set_city(city)
        model.set_hwy(hwy)
        print("Your selection updated to:", model)


def calculate_price():
    # Get departure and destination
    departure = input("Enter departure city: ")
    departure_prov = MenuUtils.menu_choice("Please choose departure's province",
                                           PROVINCES)
    destination = input("Enter destination city: ")
    destination_prov = MenuUtils.menu_choice(
        "Please choose destination's province",
        PROVINCES)
    # Find travel info
    travel_info = find_dest(
        departure + "," + PROVINCES_CODE[departure_prov - 1],
        destination + "," + PROVINCES_CODE[
            destination_prov - 1])
    miles = 0
    km = 0
    if meas_choice == ConversionUtils.IMPERIAL:
        miles = ConversionUtils.convert_m_to_miles(travel_info[1])
        distance = f"{miles} mi"
    else:
        km = ConversionUtils.convert_m_to_km(travel_info[1])
        distance = f"{km} km"
    print(f"\nThe total travel time from {departure} to {destination} is",
          travel_info[0])
    print("Distance is", distance)
    # Get gas prices
    gas_prices = get_prices()
    # Get average gas price between departure and destination
    departure_price = find_price(gas_prices, departure_prov)
    destination_price = find_price(gas_prices, destination_prov)
    median_price = (departure_price + destination_price) / 2
    print("Gas price is $", median_price)
    # Calculate total cost of gas
    amount_of_gas = 0
    cost = 0
    if meas_choice == ConversionUtils.IMPERIAL:
        amount_of_gas = round(miles / model.get_hwy(), 2)
        print("Amount of gas is", amount_of_gas, "gallons")
        cost = median_price * amount_of_gas * ConversionUtils.GALLON_VOLUME
    else:
        if metric_choice == ConversionUtils.L_PER_100KM:
            amount_of_gas = round(km * model.get_hwy() / 100, 2)
        else:
            amount_of_gas = round(km * model.get_hwy(), 2)
        cost = median_price * amount_of_gas
        print("Amount of gas is", amount_of_gas, "liters")
    print("Cost of gas is $" + str(round(cost, 2)))
    # Check about bills splitting
    split_menu = ["Yes", "No"]
    bill_split = MenuUtils.menu_choice("Do you want to split the bill?",
                                       split_menu)
    if bill_split == 1:
        num_of_riders = int(input("How many people share the ride?"))
        price_per_person = round(cost / num_of_riders, 2)
        print("Price per person is $" + str(price_per_person))


f1 = Figlet(font='standard')

print(colored(f1.renderText('Welcome'), 'green'))
print(colored(f1.renderText('GASmart Estimator'), 'green'))

cars = read_cars()
meas_choice = ask_meas_type()
metric_choice = ask_metric_choice()

brand_of_car = ask_for_brand()

brand_list = list(cars)
models = cars[brand_list[brand_of_car - 1]]
model_of_car = print_models_and_choose()

model = models[model_of_car - 1]
print("Your selection is:", model)

edit_fuel_efficiency()
calculate_price()