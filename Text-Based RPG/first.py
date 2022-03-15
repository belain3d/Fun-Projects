from enum import Enum, unique, auto

class Sensors(Enum):
    Temperature = 1
    Humidity = 2
    Air = auto()

if __name__ == "__main__":
    # print(Sensors)
    # print(Sensors.Temperature.name)
    # print(Sensors.Temperature.value)
    # print(Sensors.Air.value)
    """""
    """


    for item in Sensors:
        print(item.name, "=", item.value)
    print("\n")
    print(Sensors.__doc__)