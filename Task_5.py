class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        super().draw()
        print(f'отрисовка ручкой: {self.title}')


class Pencil(Stationary):
    def draw(self):
        super().draw()
        print(f'отрисовка карандашом: {self.title}')


class Handle(Stationary):
    def draw(self):
        super().draw()
        print(f'отрисовка маркером: {self.title}')


title_1 = Pen('Добрый день')
title_1.draw()
title_2 = Pencil('Как тебя зовут?')
title_2.draw()
title_3 = Handle('Как дела?')
title_3.draw()
