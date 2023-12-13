class Table():
    def __init__(self, material: str, shape: str):

        # Конструктор класса Table
        # param material: Материал стола
        # param shape: Форма стола

        self.material = material
        self.shape = shape

    def support_items(self):
        # Метод, описывающий действие стола - поддержка предметов
        # return: информация о том, что стол поддерживает предметы
        return

    def clean_surface(self):

        # Метод, описывающий действие стола - очистка поверхности
        # return: информация о том, что стол имеет чистую поверхность
        return

    def adjust_height(self, height: float):

        # Метод, описывающий действие стола - регулировка высоты
        # param height: Новая высота стола
        # return: информация о том, что высота стола была изменена
        return


class Tree():
    def __init__(self, age: int, height: float):

        # Конструктор класса Tree
        # param age: Возраст дерева в годах
        # param height: Высота дерева в метрах

        self.age = age
        self.height = height

    def grow(self):

        # Метод, описывающий действие дерева - рост
        # return: информация о том, что дерево выросло
        return


    def shed_leaves(self):

        # Метод, описывающий действие дерева - опадение листьев
        # return: информация о том, что дерево потеряло листья
        return


    def get_age(self) -> int:

        # Метод, возвращающий возраст дерева
        # return: Возраст дерева
        return



class Chair():
    def __init__(self, material: str, num_legs: int):

        # Конструктор класса Chair
        # param material: Материал стула
        # param num_legs: Количество ножек стула

        self.material = material
        self.num_legs = num_legs


    def sit(self):

        # Метод, описывающий действие стула - сидение
        # return: информация о том, что кто-то сел на стул
        return


    def adjust_height(self, height: float):
        # Метод, описывающий действие стула - регулировка высоты
        # param height: Новая высота стула
        # return: информация о том, что высота стула была изменена
        return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
