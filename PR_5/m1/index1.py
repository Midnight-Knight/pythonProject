import doctest
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
        Вычисляет евклидово расстояние между двумя точками на плоскости.

        Аргументы:
        x1 -- координата x первой точки
        y1 -- координата y первой точки
        x2 -- координата x второй точки
        y2 -- координата y второй точки

        Возвращает:
        Евклидово расстояние между двумя точками на плоскости.

        Примеры:
        >>> distance(0, 0, 3, 4)
        5.0
        >>> distance(1, 1, 1, 1)
        0.0
        >>> distance(0, 0, 0, 1)
        1.0
        >>> distance(1, 2, 3, 4)
        2.8284271247461903
        """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if __name__ == "__main__":
    doctest.testmod()