from random import randint
from os import system, name

def cls():
    system('cls' if name=='nt' else 'clear')

HIDDEN_CARD = [
"┌─────────┐",
"│░░░░░░░░░│",
"│░░░░░░░░░│",
"│░░░░░░░░░│",
"│░░░░░░░░░│",
"│░░░░░░░░░│",
"│░░░░░░░░░│",
"│░░░░░░░░░│",
"└─────────┘"]

name_to_symbol = {
        'Spades':   '\u2660',
        'Diamonds': '\u2662',
        'Hearts':   '\u2661',
        'Clubs':    '\u2663',
    }

ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

EMPTY_SPOT = [
    "┌─────────┐",
    "│         │",
    "│         │",
    "│         │",
    "│         │",
    "│         │",
    "│         │",
    "│         │",
    "└─────────┘"
]

class solitaire():

    def get_ascii(self, suit, rank)-> list:
        card = [
        "┌─────────┐",
        "│{}     {}│".format(f'{rank:<2}', f'{suit:<2}'),
        "│         │",
        "│         │",
        "│    {}   │".format(f'{suit:<2}'),
        "│         │",
        "│         │",
        "│{}     {}│".format(f'{suit:<2}',f'{rank:>2}'),
        "└─────────┘",]
        return card

    def __init__(self):
        deck = self.create_deck()
        deck = self.shuffel(deck)
        self.on_table = [deck[0:1],deck[1:3],deck[3:6],deck[6:10],deck[10:15],deck[15:21], deck[21:28]]
        self.fliped_cards = [cards[-1] for cards in self.on_table]
        self.drawn_cards = []
        self.un_drawn_cards = deck[28:52]
        self.ordered_stack = [EMPTY_SPOT for i in range(4)]

    def create_deck(self)->list:
        deck = [(rank, suit) for suit in [name_to_symbol[key]for key in name_to_symbol] for rank in ranks]
        # for some reason jack, qeen and king of clubs always apear first in the deck
        deck.append(deck.pop(0))
        deck.append(deck.pop(0))
        deck.append(deck.pop(0))
        return deck

    def shuffel(self, deck:list):
        deck = deck.copy()
        result = []
        while len(result) < 52:
            rand_int = randint(0, len(deck)-1)
            rand_card = deck.pop(rand_int)
            result.append(rand_card)
        
        return result

    def show_on_tab(self):
        top_cards = [self.get_ascii(rank=card[-1][0], suit=card[-1][1]) for card in self.on_table]
        empty = '           '
        stacks = []
        drawn_card = []
        if self.drawn_cards != []:
            drawn_card = self.drawn_cards[-1]
            drawn_card = self.get_ascii(rank=drawn_card[0], suit=drawn_card[1])

        for index in range(len(self.on_table)):
            stack = []
            cards = self.on_table[index]
            height = len(self.on_table[index])
            top_card = top_cards[index]

            for card in cards:
                if cards.index(card)+1 == height:
                    for line in top_card:
                        stack.append(line)
                else:
                    stack.append(HIDDEN_CARD[0])
                    stack.append(HIDDEN_CARD[1])

            while len(stack) < 22:
                stack.append(empty)
            
            stacks.append(stack)

        for index in range(22):
            print(stacks[0][index], stacks[1][index], stacks[2][index], stacks[3][index], 
                stacks[4][index], stacks[5][index], stacks[6][index], sep=' ')
        
        for index in range(9):
            if drawn_card != []:
                print(HIDDEN_CARD[index], drawn_card[index], empty, self.ordered_stack[0][index], 
                      self.ordered_stack[1][index], self.ordered_stack[2][index], self.ordered_stack[3][index])
            else:
                print(HIDDEN_CARD[index], empty, empty, self.ordered_stack[0][index], 
                      self.ordered_stack[1][index], self.ordered_stack[2][index], self.ordered_stack[3][index])

    def draw(self):
        if len(self.un_drawn_cards) == 0:
            self.un_drawn_cards = self.drawn_cards
            self.drawn_cards = []
        else:
            card = self.un_drawn_cards.pop()
            self.drawn_cards.append(card)

    def stack(self, card1:str, card2:str):
        card1 = card1.split(',')
        card2 = card2.split(',')
        match card1[0]:
            case 'A':
                card1 = [1, card1[1]]
            case 'J':
                card1 = [11, card1[1]]
            case 'Q':
                card1 = [12, card1[1]]
            case 'K':
                card1 = [13, card1[1]]
            case _:
                card1 = [int(card1[0]), card1[1]]

        match card2[0]:
            case 'A':
                card2 = [1, card2[1]]
            case 'J':
                card2 = [11, card2[1]]
            case 'Q':
                card2 = [12, card2[1]]
            case 'K':
                card2 = [13, card2[1]]
            case _:
                card2 = [int(card2[0]), card2[1]]
        

        if card1[1] == '♠' and card2[1] == '♣' or card1[1] == '♣' and card2[1] == '♠' or\
            card1[1] == '♦' and card2[1] == '♥' or card1[1] == '♥' and card2[1] == '♦' :
            return 'these suits do not stack'
    
        if int(card1[0]) != int(card2[0])-1:
            return 'the rank of card1 is not one smaller than the rank of card2'
        
        self.fliped_cards[card2[0]].append([str(card1[0]), card1[1]])
        self.fliped_cards.pop(card1[0])

        


deck = solitaire()
while True:
    cls()
    deck.show_on_tab()
    responce = input('cards should be written as "rank, suit" examples "ace, spades", "1, clubs", "king, hearts", "jack, diamonds"\
                     \nempty spots are formated as "t" for table and "o" for ordered spot and 1-4 for "o" spots and 1-7 for "t" spots\
                     \nso t7 for 7th spot on the table and o3 for 3rd spot on the orderes spots\
                     \ns + "card1 - card2" = stack card 1 on card 2\
                     \nm + "card - spot"= move card to spot\
                     \nd = draw card from pile\
                     \nq = quit\
                     \n:')
    if responce.lower() == 'q':
        break
    if responce.lower() == 'd':
        deck.draw()
    if responce.lower()[0] == 'm':
        card1, card2 = responce.lower().split('-')[0], responce.lower().split('-')[1]
        deck.stack(card1, card2)
# show_cards(deck)
