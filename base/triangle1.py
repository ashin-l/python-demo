class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    # 静态方法
    # @staticmethod
    # def is_valid(a, b, c):
        # """判断三条边长能否构成三角形(静态方法)"""
        # return a + b > c and b + c > a and a + c > b

    # 类方法
    @classmethod
    def is_valid(cls, a, b, c):
        """判断三条边长能否构成三角形(类方法)"""
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

a, b, c = 3, 4, 5
# a, b, c = 3, 1, 2
if Triangle.is_valid(a, b, c):  # 判断是否能构成三角形
    t = Triangle(a, b, c)
else:
    raise ValueError('无法构成三角形')
print(f'周长: {t.perimeter()}')
print(f'面积: {t.area()}')