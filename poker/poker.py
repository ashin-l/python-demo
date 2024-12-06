import random

from card import Card
from suite import Suite

# 扑克
class Poker:
    def __init__(self):
        self.current = 0
        self.cards = [Card(suite, points) for suite in Suite for points in range(1, 14)]

    # 洗牌
    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)

    # 发牌
    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card

    # 是否有牌可发
    def has_next(self):
        return self.current < len(self.cards)
