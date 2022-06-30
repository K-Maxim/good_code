# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit1:
    def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
class Unit:
    def __init__(self, x, y, is_fly=True):
        self._is_fly = is_fly
        self._speed = 1
        self._x = x
        self._y = y

    def _get_speed(self):
        if self._is_fly:
            return self._speed * 2
        else:
            return self._speed * 0.5

    def move(self, way):
        if way == 'UP':
            return self._x + self._get_speed(), self._y
        elif way == 'DOWN':
            return self._x + self._get_speed(), self._y
        elif way == 'LEFT':
            return self._x, self._y - self._get_speed()
        elif way == 'RIGHT':
            return self._x, self._y + self._get_speed()



