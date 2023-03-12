# shenzen solitair
# the rules are that: cards can only be placed on a card of an oposing color and one number lower than it self,
# there are special cards that no other cards can be placed on and that can not be placed on other cards,
# theese special cards can be putt in the "store" space if 4 of them are on top of individual stacks or in store,
# the "store" spaces are 3 spaces that store anny card and that gett filled upp individualy when a stack of special cards is put on it
# there are 3 solve spaces that are for cards of one suite and where the cards are matched in increasing order,

# test sample = r7 g9 bs b5 r5 g4, b6 g8 bs r1 g7 r6, r3 bs b8 b7 rs, rs rose g1 gs, g2 b3 rs gs, b2 r8 gs, b4 g6 rs g5 gs, g3 r9 r4 r2 b9

class shenzen_solitaire_board():
    ordered_cards = [[],[],[]]
    holding_spots = [[],[],[]]
    card_sequences = []
    board = []
    moves = []

    def __init__(self, board: list = [], holding: list = [], ordered: list = []) -> None:
        if board == []:
            self.board = self.read_stacks()
        else: self.board = board
        if holding == []:
            self.holding_spots = self.read_hold_spots()
        else: self.holding_spots = holding
        if ordered != []:
            self.ordered_cards = ordered
        self.card_sequences = self.find_sequences()
        self.moves = self.find_moves()

    def read_stacks(self)-> list:
        """prompts user to write the stacks in manualy
            and then turns what the user has written into a computer readable list of lists
        """
        card_stacks = []
        board = input("write stacks from top to bottom from left to right\
    with a space between each card\
    Red = R, Green = G, Black = B,\n\
    Rose = Rose, Spesiacl Cards = S, seperate stacks of cards with a comma\
    eksample: R1 R2 R4 R6 RS, BS B5 B6...\n\
    :")
        board = board.lower()
        stacks = board.split(',')
        for stack in stacks:
            cards = stack.lstrip().split(' ')
            card_stacks.append(cards)

        return card_stacks

    def stackable(self, card1:str, card2:str) -> bool:
        """test if two cards are stackable

        Returns:
            bool: if they are stackable or not
        """
        if (card1[0] == card2[0] or card1[1] == 's' or 
        card2[1] == 's' or card1[1] == 'o' or card2 == 'o'):
            return False
        if card1[1] == str(int(card2[1])-1):
            return True


    def read_hold_spots(self):
        cards = input("\nAre there any cards in the holding spots(top left)?\
            \nif so write the card with the previus format, (r/g/b + 1-9) or (r/g/b + s) or rose,\
            \nand the number of the spot they are in, 1-3, with a space in between, seperate\
            \neach card and spot with a comma. if there are no cards in the holding spots leave blank: ")
        
        holding_spots = [[],[],[]]

        if cards != '':
            cards = cards.split(',')

            for card in cards:
                card = card.split()
                index = int(card[1])-1
                print(index, card)
                holding_spots[index] = card[0]
        
        return holding_spots
        

    def find_sequences(self):
        card_sequences = []
        for stack in self.board:
            # adds the first card of the stack to the sequence
            current_seqence = [stack[len(stack)-1]]
            
            # test if a card can be stacked on the card underneeth
            for index in range(len(stack)-1, 1, -1):
                card1 = stack[index]
                card2 = stack[index-1]

                # some wierdnes here
                # the special cards are irrelevant and so is the rose card
                if self.stackable(card1, card2) == False:
                    continue
                else:
                    current_seqence.append(card2)

            card_sequences.append(current_seqence)
        
        return card_sequences

    def find_moves(self) -> list:
        """takes a list of list of curent board positions and makes a list of every move posible in this time frame
        represented as an tuple

        Args:
            board (list): list of lists of the cards on the board

        Returns:
            list: list of posible moves one time frame in the future
        """
        # needs an uppdate
        moves = []
        special_cards = {}
        card_sequences = self.card_sequences
        # finds out if a card in a sequence and all the cards above it can fit on an other card
        for index1 in range(0 ,len(card_sequences)):
            for index2 in range(0, index1):
                if index1 == index2:
                    continue
                
                # when stacking two cards, or a sequence and a card, you need to make shure that the second card is at the top
                for card1 in card_sequences[index1]:
                    card2 = card_sequences[index2][0]

                    if self.stackable(card1, card2) == True:
                        card1_index = card_sequences[index1].index(card1)
                        card1_sequence = card_sequences[index1][0:card1_index]
                        moves.append((card1_sequence, card2, index2))

                    else:
                        continue

        # if there are open holding spots or there are posible ordered moves, add moving cards to either as a possible move.
        for sequence in card_sequences:
            card = sequence[0]
            if len(self.holding_spots[0]) == 0:
                moves.append((card, 'hold0'))
            elif len(self.holding_spots[1]) == 0:
                moves.append((card, 'hold1'))
            elif len(self.holding_spots[2]) == 0:
                moves.append((card, 'hold2'))

            # only look for ordering moves if the current card is not a special or a rose
            if card[1] == 's' or card == 'rose':
                continue

            for spot in self.ordered_cards:
                if spot == []:
                    continue

                if (card[1] == '1' or 
                card == f'{spot[0][0]}{int(spot[0][1])-1}'):

                    match card[0]:
                        case 'r':
                            moves.append((card, 'ordered0'))
                        case 'g':
                            moves.append((card, 'ordered1'))
                        case 'b':
                            moves.append((card, 'ordered2'))

        return moves

# need of fix:
# the indexing on the moves
# look for the posibility of combining the special cards on top of a special spot
# see if any of the cards in the holding spots can be stacked on the rest if so add to the moves
# fix the find sequence function

# current rs r5 g9 gs gs, rs g2 g3 gs b8, rs b2 b5 b7 bs, rs r2 g8 bs r8, g4 r4, g6 bs r6, r3 b1 r7 b9 bs, r9 g7 b3 gs
# holding spott = g5 1, b6 2, b4 3
board = [['rs', 'r5', 'g9', 'gs', 'gs'], ['rs', 'g2', 'g3', 'gs', 'b8'], 
['rs', 'b2', 'b5', 'b7', 'bs'], ['rs', 'r2', 'g8', 'bs', 'r8'], ['g4', 'r4', 'g6', 'bs', 'r6'], 
['r3', 'b1', 'r7', 'b9', 'bs'], ['r9', 'g7', 'b3', 'gs']]
board1 = shenzen_solitaire_board(board , holding= [['g5'], ['b6'], ['b4']], ordered=[['r1'],['g1'],[]])
print(board1.board, '\n', board1.card_sequences)