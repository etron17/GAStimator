from beautifultable import BeautifulTable
from conversionutils import ConversionUtils
from menuutils import MenuUtils
from gas import Gas
from routing import Routing


# MVC pattern - view part
class View(object):
    PROVINCES = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
                 'Newfoundland and Labrador', 'Nova Scotia', 'Ontario',
                 'Prince Edward Island', 'Quebec', 'Saskatchewan']
    PROVINCES_CODE = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC',
                      'SK']
    YES_NO = ["Yes", "No"]

    def ask_meas_type(self):
        """
        Ask for measurement types
        :return: measurement types
        """
        meas_types = ["Imperial", "Metric"]
        meas_choice = MenuUtils.menu_choice("\nSelect measurement type",
                                            meas_types)
        return meas_choice

    def ask_metric_choice(self, meas_choice):
        """
        For metric ask for L/100km or L/km
        :return: Metric choice
        """
        metric_choice = ConversionUtils.MPG
        if meas_choice == ConversionUtils.METRICS:
            metric_types = [ConversionUtils.L_PER_100KM_SUFFIX,
                            ConversionUtils.L_PER_KM_SUFFIX]
            metric_choice = MenuUtils.menu_choice("\nSelect metric mileage type",
                                                  metric_types)
            print(
                f"\nYou're using {metric_types[metric_choice - 1]} measurement units")
        else:
            print("\nYou're using 'MPG' measurement units")
        return metric_choice

    def ask_for_brand(self, cars):
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
        brand_of_car = MenuUtils.menu_choice_nolist(
            "Please select brand of car",
            len(cars.keys()))
        return brand_of_car

    def print_models_and_choose(self, meas_choice, metric_choice, models):
        """
        Print models for that brand
        :return: Model of car
        """
        idx = 1
        model_table = BeautifulTable()
        for model in models:
            model.set_meas_choice(meas_choice)
            model.set_metric_choice(metric_choice)
            model_table.columns.header = ["No.", "Model", "Drive", "Fuel",
                                          "Stnd",
                                          "City", "Hwy"]
            model_table.rows.append(
                [str(idx), model.get_model(), model.get_drive(),
                 model.get_fuel(), model.get_stnd(),
                 model.get_city(),
                 model.get_hwy()])
            idx += 1
        print(model_table)
        model_of_car = MenuUtils.menu_choice_nolist(
            "Please select model of car",
            len(models))
        return model_of_car

    def edit_fuel_efficiency(self, model):
        edit_choice = MenuUtils.menu_choice(
            "\nDo you want to edit fuel efficiency?", self.YES_NO)
        if edit_choice == 1:
            city = float(input("\nPlease enter fuel efficiency for city drive: "))
            hwy = float(input("\nPlease enter fuel efficiency for hwy drive: "))

            model.set_city(city)
            model.set_hwy(hwy)
            print("\nYour selection updated to:", model)


    def find_price(self, gas_prices, prov: int) -> float:
        """
        Find price for province
        :param gas_prices: Gas prices for all provinces
        :param prov: Province to find price for
        :return: Price of gas for province
        """
        view = View()
        for entry in gas_prices:
            if entry['province'] == view.PROVINCES[prov - 1]:
                return entry['price']

        return 0


    def calculate_price(self, meas_choice, metric_choice, model):
        # Get departure and destination
        departure = input("\nEnter departure city: ")
        departure_prov = MenuUtils.menu_choice(
            "\nPlease choose departure's province", self.PROVINCES)
        destination = input("\nEnter destination city: ")
        destination_prov = MenuUtils.menu_choice(
            "\nPlease choose destination's province", self.PROVINCES)
        # Find travel info
        travel_info = Routing.find_dest(
            departure + "," + self.PROVINCES_CODE[departure_prov - 1],
            destination + "," + self.PROVINCES_CODE[
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
        print("\nDistance is", distance)
        # Get gas prices
        gas = Gas()
        gas_prices = gas.get_prices()
        # Get average gas price between departure and destination
        departure_price = self.find_price(gas_prices, departure_prov)
        destination_price = self.find_price(gas_prices, destination_prov)
        median_price = round((departure_price + destination_price) / 2, 2)
        print("\nCurrent gas price is $", median_price)
        # Calculate total cost of gas
        amount_of_gas = 0
        cost = 0
        if meas_choice == ConversionUtils.IMPERIAL:
            amount_of_gas = round(miles / model.get_hwy(), 2)
            print("\nAmount of gas is needed", amount_of_gas, "gallons")
            cost = median_price * amount_of_gas * ConversionUtils.GALLON_VOLUME
        else:
            if metric_choice == ConversionUtils.L_PER_100KM:
                amount_of_gas = round(km * model.get_hwy() / 100, 2)
            else:
                amount_of_gas = round(km * model.get_hwy(), 2)
            cost = median_price * amount_of_gas
            print("\nAmount of gas is needed", amount_of_gas, "liters")
        print("\nTotal cost of gas is $" + str(round(cost, 2)))
        # Check about bills splitting
        split_menu = ["Yes", "No"]
        bill_split = MenuUtils.menu_choice("\nDo you want to split the bill?",
                                           split_menu)
        if bill_split == 1:
            num_of_riders = int(input("\nHow many people share the ride: "))
            price_per_person = round(cost / num_of_riders, 2)
            print("\nPrice per person is $" + str(price_per_person))
        else:
            print("\nTotal cost of gas is $" + str(round(cost, 2)))
