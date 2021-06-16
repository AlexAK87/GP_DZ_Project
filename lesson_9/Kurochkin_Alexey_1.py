import time


class TrafficLight:
    counter = 0
    colors_dict = {"red": 7, "yellow": 2, "green": 10}
    colors_print = {"red": "\033[31m {}", "yellow": "\033[33m {}", "green": "\033[32m {}"}

    def __init__(self):
        self.__color = ""

        TrafficLight.counter -= 1

    def running(self):

        if self.__color == "red":
            self.__color = "yellow"
            TrafficLight.counter = self.colors_dict[self.__color]
        elif self.__color == "yellow":
            self.__color = "green"
            TrafficLight.counter = self.colors_dict[self.__color]
        else:
            self.__color = "red"
            TrafficLight.counter = self.colors_dict[self.__color]

        color_print = self.colors_print[self.__color]
        while TrafficLight.counter != 0:
            print(color_print.format(self.__color), TrafficLight.counter)
            time.sleep(1)
            TrafficLight.counter -= 1

        self.running()


t = TrafficLight()
t.running()
