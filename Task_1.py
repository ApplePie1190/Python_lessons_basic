import time


class TrafficLight:
    __color = {'RED': 7, 'YELLOW': 2, 'GREEN': 4}

    def running(self):
        print('чтобы остановить светофор нажмите Ctrl + F2')
        while True:
            for color, time_work in self.__color.items():
                print(f'\r{color}', end='')
                time.sleep(time_work)


my_traffic_light = TrafficLight()
my_traffic_light.running()