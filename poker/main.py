from poker import Poker
from player import Player

def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            card = poker.deal()
            player.get_one(card)

    for player in players:
        player.arrange()
        print(f'{player.name}: ', end='')
        print(player.cards)

if __name__ == '__main__':
    main()