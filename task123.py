class Math:
    def __init__(self, value):
        self.value = value

    def get_factorial(self):
        factor = list(map(lambda x, y: x * y, self.value))
        return factor

    def get_sum(self):
        summa = list(map(lambda x, y: x + y, self.value))
        return summa

    def get_mul_table(self):
        list_ = []
        for num in range(1, 11):
            result = num * self.value
            list_.append(f'{self.value}x{num}={result}\n')
        return ''.join(list_)

a = Math(25)

print(a.get_factorial())
print(a.get_sum())
print(a.get_mul_table())