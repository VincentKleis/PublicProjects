# task 1
bills = [("electric", 5000), ("water", 2200), ("wolfram alpha", 150)] 

def quick_sort(array:list):
    if len(array) < 2:
        return array

    pivot = array[0]

    if type(pivot) == int:
        left = [i for i in array[1:] if i <= pivot]
        right = [i for i in array[1:] if i > pivot]
    if type(pivot) == str:
        left = [i for i in array[1:] if ord(i.lower()) <= ord(pivot.lower())]
        right = [i for i in array[1:] if ord(i.lower()) > ord(pivot.lower())]

    return quick_sort(left) + [pivot] + quick_sort(right)

def sort_bills(array):
    price_dict = {}
    for i in array:
        x, y = i
        price_dict[y] = i

    price_list = [y for x, y in array]
    price_list = quick_sort(price_list)
    result = []

    for i in price_list:
        result.append(price_dict[i])

    print(result)

class minibank():
    def __init__(self):
        self.balance = 0
        self.password = None

    def password_protect(self, code_lines:str):
        password_check = input('please enter your password:')
        if self.password == password_check:
            exec(code_lines)
        else:
            print('sorry you entered the wrong password')

    def start_bank(self, answer=None, insertion=None):
        while True:
            if answer is None:
                print(f'press:\n\
1. to add money to minibank\n\
2. to pay a friend\n\
3. add password')
            
                answer = input('press enter to input the number')

            if answer == '1':
                if insertion is None:
                    insertion = input('How much money do you want to add?:')

                self.password_protect(
                'self.balance += insertion')

            elif answer == '2':
                deletion = input('How much would you like to pay your friend?:')

                password_check = input('please enter your password:')
                if self.password == password_check:
                    self.balance -= deletion
                else:
                    print('sorry you entered the wrong password')

            elif answer == '3':
                self.password = input('What would you like for your pasword to be?:')
                repetion = input('Repete the password:')
                if self.password != repetion:
                    print('the two passwords did not match')
                    self.start_bank('3')

# task 2
def fibonatchi(length):
    prev = 0
    current = 1
    for i in range(length):
        print(current)
        hold = current
        current = current + prev
        prev = hold

fibonatchi(1)

# this algorithme is not recursive and the loop does not grow in size only in iterations, so we are probably close to O(n)

# task 3
def a_space_classic(n):
    z=n-1
    x=1
    for i in range(0, n):
        for i in range(0, z):
            print(' ',end='')
        for i in range(0, x):
            print('+',end='')
        for i in range(0, z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()
a_space_classic(5)