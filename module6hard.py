"""
{
            "black":    (0, 0, 0),
            "gray": (128, 128, 128),
            "white":    (255, 255, 255),
            "blue": (0, 0, 255),
            "green":    (0, 255, 0),
            "yellow":   (255, 255, 0),
            "red":  (255, 0, 0),
            "purple":   (255, 0, 255),
            "orange":   (255, 165, 0),
            "fuchsia":  (255, 0, 255)
                }
"""
import math


class Figure():
    sides_count = 0
    def __init__(self, RGB_color, *sides):
        if len(sides) != self.sides_count:
            if len(sides) == 1:
                self.__sides = [int(sides[0])]*self.sides_count
            else:
                self.__sides = [1] * self.sides_count
        else:
            if self.__is_valid_sides(*sides):
                self.__sides = list(sides)
            else:
                self.__sides = [1] * self.sides_count

        if self.__is_valid_color(RGB_color):
            self.__color = RGB_color
        else:
            self.__color = (0, 0, 0)    #   black
        self.filled = True  # bool

    def get_color(self):
        print(f'The color is: {self.__color}')
        return self.__color




    def set_color(self,*args):
        RGB_color  = list(args)
        if self.__is_valid_color(RGB_color):
            self.__color = list(RGB_color)
            #print('New color is: ', self.__color)
        else:
            print("The color didn't change.")


    def __is_valid_color(self, RGB_color):
        if all(isinstance(value, int) for value in RGB_color):
            if all(0 <= value <= 255 for value in RGB_color):
                return True
            else:
                #print('Error! The values must be from 0 to 255.')
                return False
        else:
            #print('Error! The values must be the integral numbers from 0 to 255.')
            return False

    def __is_valid_sides(self,*args):
        if all(isinstance(side, int) for side in args):
            if sum(args) >= 0:
                if len(args) == self.sides_count:
                    return True
                else:
                    #print(f'Wrong number of sides {len(args)}. It must be {self.sides_count}.')
                    return False
            else:
                #print('All values must be positive.')
                return False
        else:
            #print('Values must be the integral numbers and positive.')
            return False

    def get_sides(self):
        #print(f'The sides are: {self.__sides}.')
        return self.__sides

    def __len__(self):
        P = sum(self.__sides)
        print(f'Perimeter is {P}.')
        return P

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
            print("The sides were updated.")
        else:
            print("The sides weren't updated.")


class Circle(Figure):

    sides_count = 1

    def __init__(self, RGB_color, *side):
        super().__init__(RGB_color, *side)
        self.__sides = float(self.get_sides()[0])
        self.sides_count = self.sides_count
        self.__radius = self.__sides / (2*math.pi)


    def get_square(self):
        square = math.pi*self.__radius**2
        print('The square is ', square)
        return square


class Triangle(Figure):

    sides_count = 3

    def __init__(self, RGB_color, *side):
        super().__init__(RGB_color, *side)



    def get_square(self):
        a, b, c = self.get_sides()
        p = (a+b+c)/2
        square = p*math.sqrt((p-a)*(p-b)*(p-c))
        print('The square is ', square)
        return square


class Cube(Figure):

    sides_count = 12

    def __init__(self, RGB_color, *side):
        super().__init__(RGB_color, *side)


    def get_volume(self):
        volume = self.get_sides()[0]**3
        print('The volume is ', volume)
        return volume



if __name__ == '__main__':
    figure = Figure("",)
    """
    # Получение текущего цвета
    figure.get_color()

    # Установка нового корректного цвета
    figure.set_color(255, 0, 0)  # Установить красный


    # Попытка установить некорректный цвет
    figure.set_color(256, -10, 300)  # Некорректный цвет

    # Получение текущих сторон
    figure.get_sides()
    len(figure)

    # Установка новых корректных сторон
    figure.set_sides(6, 7, 8)  # Установить новые стороны
    figure.get_sides()
    len(figure)

    # Попытка установить некорректные стороны
    figure.set_sides(6, 7, 8, 7)  # Ошибка: количество сторон не совпадает
"""
    print()

    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    circle1.get_color()
    cube1.set_color(300, 70, 15)  # Не изменится
    cube1.get_color()

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    cube1.get_sides()
    circle1.set_sides(15) # Изменится
    print(*circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    len(circle1)

    # Проверка объёма (куба):
    cube1.get_volume()


