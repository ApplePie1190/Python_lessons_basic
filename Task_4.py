class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('авто поехал')

    def stop(self):
        print('авто остановился')

    def turn(self, direction):
        print(f'авто повернул: {direction}')

    def show_speed(self):
        print(f'текущая скорость: {self.speed}')


class TownCar(Car):
    allowed_speed = 60

    def show_speed(self):
        if self.speed > TownCar.allowed_speed:
            print('Превышена допустимая скорость')
        else:
            super().show_speed()


class WorkCar(Car):
    allowed_speed = 40

    def show_speed(self):
        if self.speed > WorkCar.allowed_speed:
            print('Превышена допустимая скорость')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


car_1 = TownCar(65, 'черный', 'Audi')
car_1.go()
car_1.stop()
car_1.turn('налево')
car_1.turn('направо')
car_1.show_speed()
car_2 = TownCar(45, 'белый', 'Mersedes')
car_2.go()
car_2.stop()
car_2.turn('налево')
car_2.turn('направо')
car_2.show_speed()
car_3 = PoliceCar(100, 'синий', 'Volvo', True)
car_3.go()
car_3.stop()
car_3.turn('налево')
car_3.turn('направо')
car_3.show_speed()

