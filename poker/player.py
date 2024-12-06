class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    # 摸牌
    def get_one(self, card):
        self.cards.append(card)

    # 整理手牌
    def arrange(self):
        self.cards.sort()
