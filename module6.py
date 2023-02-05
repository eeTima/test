class multiplication_table():
    """Определение пересечений в списках"""

    def __init__(self, multi_t):
        """Инициализирует значения"""
        self.multi_t = multi_t


    def m_t(self):
        """Создание таблицы умножения"""
        for i in range(1, self.multi_t + 1):
            for j in range(1, multi_t + 1):
                print("{:>3}".format(i * j), end='')
            print()

multi_t = int(input())

t = multiplication_table(multi_t)
t.m_t()




