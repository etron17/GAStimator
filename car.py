import mysql.connector
from typing import Dict, List
from conversionutils import ConversionUtils


class Car(object):
    def __init__(self, brand, model, drive, fuel, stnd, city, hwy) -> None:
        super().__init__()
        self.__brand = brand
        self.__model = model
        self.__drive = drive
        self.__fuel = fuel
        self.__stnd = stnd
        self.__city = city
        self.__hwy = hwy
        self.__meas_choice = ConversionUtils.IMPERIAL
        self.__metric_choice = ConversionUtils.MPG

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_drive(self):
        return self.__drive

    def get_fuel(self):
        return self.__fuel

    def get_stnd(self):
        return self.__stnd

    def set_meas_choice(self, meas_choice):
        self.__meas_choice = meas_choice

    def set_metric_choice(self, metric_choice):
        self.__metric_choice = metric_choice

    def get_city(self):
        if self.__meas_choice == ConversionUtils.IMPERIAL:
            return self.__city
        else:
            if self.__metric_choice == ConversionUtils.L_PER_100KM:
                return ConversionUtils.convert_mpg_to_l100km(self.__city)
            else:
                return ConversionUtils.convert_mpg_to_lkm(self.__city)

    def set_city(self, city):
        if self.__meas_choice == ConversionUtils.IMPERIAL:
            self.__city = city
        else:
            if self.__metric_choice == ConversionUtils.L_PER_100KM:
                self.__city = ConversionUtils.convert_l100km_to_mpg(city)
            else:
                self.__city = ConversionUtils.convert_lkm_to_mpg(city)

    def get_hwy(self):
        if self.__meas_choice == ConversionUtils.IMPERIAL:
            return self.__hwy
        else:
            if self.__metric_choice == ConversionUtils.L_PER_100KM:
                return ConversionUtils.convert_mpg_to_l100km(self.__hwy)
            else:
                return ConversionUtils.convert_mpg_to_lkm(self.__hwy)

    def set_hwy(self, hwy):
        if self.__meas_choice == ConversionUtils.IMPERIAL:
            self.__hwy = hwy
        else:
            if self.__metric_choice == ConversionUtils.L_PER_100KM:
                self.__hwy = ConversionUtils.convert_l100km_to_mpg(hwy)
            else:
                self.__hwy = ConversionUtils.convert_lkm_to_mpg(hwy)

    def __repr__(self) -> str:
        return "'" + self.__brand + ", " + self.__model + "," + self.__drive + \
               "," + self.__fuel + "," + self.__stnd + \
               ", Fuel efficiency: City " + str(round(self.get_city(), 2)) + \
               ConversionUtils.get_suffix(self.__metric_choice) + \
               " and highway " + str(round(self.get_hwy(), 2)) + \
               ConversionUtils.get_suffix(self.__metric_choice) + "'"

def read_cars() -> Dict[str, List[Car]]:
    """
    Read data from database and return as dictionary, the key is car producer,
    values are cars from that producer
    :return: Dictionary
    """
    cars: Dict[str, List[Car]] = {}

    # Connect to database
    mydb = mysql.connector.connect(
        host="YOUR KEY",
        user="YOUR KEY",
        passwd="YOUR KEY",
        database="YOUR KEY"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM vehicledb")
    myresult = mycursor.fetchall()

    print(myresult)

    # Fill the dictionary
    for row in myresult:
        brand = row[0]
        car = Car(brand, row[1], row[2], row[3], row[4], row[5], row[6])
        if brand not in cars:
            cars[brand] = []
        cars[brand].append(car)

    return cars
