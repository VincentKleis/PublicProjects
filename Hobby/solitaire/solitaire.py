from random import randint
from os import system, name
from time import sleep

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
        'spades':   '\u2660',
        'diamonds': '\u2662',
        'hearts':   '\u2661',
        'clubs':    '\u2663',
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

    def __init__(self):
        deck = self.create_deck()
        deck = self.shuffel(deck)
        self.on_table = [deck[0:1],deck[1:3],deck[3:6],deck[6:10],deck[10:15],deck[15:21], deck[21:28]]
        self.fliped_cards = [[cards[-1]] for cards in self.on_table]
        self.drawn_cards = []
        self.un_drawn_cards = deck[28:52]
        self.ordered_stack = [EMPTY_SPOT for i in range(4)]


    def get_ascii(self, rank, suit)-> list:
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
        """fills the terminal with images of cards representing the current state of the decks on the table
        """
        empty = '           '
        stacks = []
        drawn_card = []
        top_cards = [stack[0] for stack in self.fliped_cards]
        top_cards = [self.get_ascii(card[0], card[1]) for card in top_cards]
        other_flipped = [stack[1:] for stack in self.fliped_cards]
        other_flipped = [self.get_ascii(card[0], card[1]) for card in top_cards]

        if self.drawn_cards != []:
            drawn_card = self.drawn_cards[-1]
            drawn_card = self.get_ascii(rank=drawn_card[0], suit=drawn_card[1])

        for index in range(len(self.on_table)):
            stack = []
            cards = self.on_table[index]
            height = len(self.on_table[index])
            top_card = top_cards[index]
            fliped_stack = other_flipped[index]


            for card in cards:
                if cards.index(card)+1 == height:
                    for line in top_card:
                        stack.append(line)
                elif len(fliped_stack) < 0:
                    stack.append(fliped_stack[0][0])
                    stack.append(fliped_stack[0][1])
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
            # resets the un drawn stack
            self.un_drawn_cards = self.drawn_cards
            self.drawn_cards = []
        else:
            card = self.un_drawn_cards.pop()
            self.drawn_cards.append(card)


    def legal_move(self, card1, card2)->str:
        """test if card1 can stack on card2

        Args:
            card1 (tuple): first card
            card2 (tuple): second card

        Returns:
            str: descriptive error message
        """
        match card1[0]:
            case 'a':
                test1 = [1, card1[1]]
            case 'j':
                test1 = [11, card1[1]]
            case 'q':
                test1 = [12, card1[1]]
            case 'k':
                test1 = [13, card1[1]]
            case _:
                test1 = [int(card1[0]), card1[1]]

        match card2[0]:
            case 'a':
                test2 = [1, card2[1]]
            case 'j':
                test2 = [11, card2[1]]
            case 'q':
                test2 = [12, card2[1]]
            case 'k':
                test2 = [13, card2[1]]
            case _:
                test2 = [int(card2[0]), card2[1]]

        if card1[1] == '\u2660' and card2[1] == '\u2663' or card1[1] == '\u2663' and card2[1] == '\u2660' or\
            card1[1] == '\u2662' and card2[1] == '\u2661' or card1[1] == '\u2661' and card2[1] == '\u2662' :
            return f'{card1[1]}, {card2[1]}these suits do not stack'
    
        if int(test1[0]) != int(test2[0])-1:
            return f'{card1[0]}, {card2[9]}the rank of card1 is not one smaller than the rank of card2'
        
        return None
    
    def on_table(card)->tuple:
        
        

    def stack(self, card1:str, card2:str):
        card1 = card1.split(',')
        card1 = [card1[0].strip().lower(), name_to_symbol[card1[1].strip().lower()]]

        card2 = card2.split(',')
        card2 = [card2[0].strip().lower(), name_to_symbol[card2[1].strip().lower()]]

        # test if it is theoreticaly possible
        responce = self.legal_move(card1, card2)
        if responce != None:
            print(responce)

        index1 = None
        
        # find the cards and remove the first card from it's position if it is found
        for i in range(len(self.fliped_cards)):
            stack = self.fliped_cards[i]
            stack_ranks = [card[0] for card in stack]
            stack_suits = [card[1] for card in stack]

            if card1[0] in stack_ranks and card1[1] in stack_suits:
                indexx = stack_ranks.index(card1[0])
                cardx = stack[indexx]

                if cardx[0] == card1[0] and cardx[1] == card1[1]:
                    index1 = (i, indexx)
                    self.fliped_cards[index1[0]].pop(index1[1])

            if card2[0] in stack_ranks and card2[1] in stack_suits:
                indexx = stack_ranks.index(card2[0])
                cardx = stack[indexx]

                if cardx[0] == card2[0] and cardx[1] == card2[1]:
                    index2 = (i, indexx)

        if self.drawn_cards != []:
            if self.drawn_cards[0][0] == card1[0][0] and self.drawn_cards[0][1] == card1[0][1]:
                print(self.drawn_cards[0])
                index1 = 0
                self.drawn_cards.pop(0)    

        # move the cards
        index2 = None
        for i in range(len(self.fliped_cards)):
            for j in range(len(self.fliped_cards[i])):
                if self.fliped_cards[i][j][0] == card2[0] and self.fliped_cards[i][j][1] == card2[1]:
                    index2 = (i, j)

        if index1 != None:
            self.fliped_cards[index2[0]].append(str(card1[0]), card1[1])
        if index1 == None and index2 != None:
            return f'{card1} is not a card on the board'
        if index1 != None and index2 == None:
            return f'{card2} is not a card on the board'
        if index1 == None and index2 == None:
            return f'{card1} ad {card2} are not cards on the board'

        


deck = solitaire()
while True:
    cls()
    deck.show_on_tab()
    responce = input(f'cards should be written as "s rank1, suit1 - rank2, suit2" examples "s A, spades - K, hearts", \
                     \n"s Q, clubs - J, diamonds", "s 3, clubs - 4, hearts"\
                     \nempty spots are formated as "t" for table and "o" for ordered spot and there are 4 "o" spots and 7 "t" spots\
                     \nso t7 for 7th spot on the table and o3 for 3rd spot on the orderes spots\n\
                     \nhearts={name_to_symbol["hearts"]}, spades={name_to_symbol["spades"]}, clubs={name_to_symbol["clubs"]}, diamonds={name_to_symbol["diamonds"]}\n\
                     \ns + "card1 - card2" = stack card 1 on card 2\
                     \nm + "card - spot"= move card to spot\
                     \nd = draw card from pile\
                     \nq = quit\
                     \n:')
    if responce.lower() == 'q':
        break
    if responce.lower() == 'd':
        deck.draw()
    if responce.lower()[0] == 's':
        responce = responce.lstrip('s')
        card1, card2 = responce.lower().split('-')[0], responce.lower().split('-')[1]
        error = None
        error = deck.stack(card1, card2)
        if error != None:
            cls()
            print(error)
            sleep(3)

