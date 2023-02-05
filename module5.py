class intersection():
    """Определение пересечений в списках"""

    def __init__(self, list_1, list_2):
        """Инициализирует значения списков"""
        self.list_1 = list_1
        self.list_2 = list_2


    def intersect(self):
        """Проверяет списки на пересечение и сохраняет в новом"""
        list_3 = list(set(self.list_1) & set(self.list_2))
        return list_3

list_1 = [1,2,6,7,96,2354,23]
list_2 = [2,42,6,7,85,97,24,23]

list_3 = intersection(list_1, list_2)
print(list_3.intersect())

