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

    def __repr__(self) -> str:
        return "'" + self.__brand + ", " + self.__model + "," + self.__drive + \
               "," + self.__fuel + "," + self.__stnd + \
               ", Fuel efficiency: City " + str(self.__city) + \
               "mpg and highway " + str(self.__hwy) + "mpg'"


def read_vehicles() -> Dict[str, List[Car]]:
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
