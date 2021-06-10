import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self):
        turn_list = ['Юг', 'Запад', 'Север', 'Восток']
        return f'{self.name} помернула на {random.choice(turn_list)}'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed}'


class TownCar(Car):

    def type_car(self):
        return f'{self.name} городская машина'

    def show_speed(self):
        if self.speed > 60:
            speed = f'Скорость автомобиля {self.name} {self.speed}, больше разрешенной. Разрешена 60'
        else:
            speed = f'Скорость автомобиля {self.name} {self.speed}'

        return speed


class SportCar(Car):

    def type_car(self):
        return f'{self.name} спортивная машина'


class WorkCar(Car):

    def type_car(self):
        return f'{self.name} рабочая машина'

    def show_speed(self):
        if self.speed > 40:
            speed = f'Скорость автомобиля {self.name} {self.speed}, больше разрешенной. Разрешена 40'
        else:
            speed = f'Скорость автомобиля {self.name} {self.speed}'

        return speed


class PoliceCar(Car):

    def type_car(self):
        return f'{self.name} полицейская машина {self.is_police}'


town_car = TownCar(100, 'green', 'Mazda', False)
sport_car = SportCar(80, 'red', 'Ferrari', False)
work_car = WorkCar(50, 'yellow', 'Lada', False)
police_car = PoliceCar(60, 'red', 'Audi', True)

print(work_car.type_car())
print(work_car.go())
print(work_car.stop())
print(work_car.turn())
print(work_car.show_speed())
