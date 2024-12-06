from suite import Suite


class Card:
    def __init__(self, suite, points):
        self.suite = suite
        self.points = points

    def __repr__(self):
        suits = '♠♥♣♦'
        points = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suits[self.suite.value]}{points[self.points]}'

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.points < other.points   # 花色相同比较点数的大小
        return self.suite.value < other.suite.value   # 花色不同比较花色对应的值
