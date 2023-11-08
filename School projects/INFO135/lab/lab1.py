# Classes
# ex 1
import math


class Person:
    def __init__(self, name) -> None:
        self.name = name
    
    def greets(self, person):
        print(f'{self.name}: "Hello, {person.name}"')


alice = Person("Alice")
bob = Person("Bob")
alice.greets(bob)


# ex 2
class Employee:
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = 10000

    def get_fullname(self):
        print(f'{self.firstname}, {self.lastname}')

    def print_email(self):
        print(f'{self.firstname}.{self.lastname}@company.com')

    def increase_salary(self, rate):
        self.salary = self.salary * rate


employee1 = Employee('employ', 'employson')
employee1.get_fullname()
employee1.print_email()
print(employee1.salary)
employee1.increase_salary(0.1)
print(employee1.salary)

# Binary search
# ex 1
# a) 1., 3.,
# b) if i choose the value 1952 from list 3. then binary search would do the following:
# is it larger than or equal index(round(length/2)) (witch is item 5 = 1969) and you would get no
# then the search would know that it has to be a number smaller than 1969, it would identify index(6) as smaller 
# and index(4) as larger. then the search would ask itself: is it larger than or equal 
# index(round(length-length/2+length/4)) (witch would round to index(6) = 1952) and you would get yes
# since index(5) was to large it would then conclude that it found the item in 2 steps


# ex 2
# (a)
def binary_search_big_o(lst):
    length = len(lst)
    result = math.ceil(math.log(length, 2))
    return result


# (b)
def simple_search_big_o(lst):
    length = len(lst)
    return length


# (c)
pi_digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]

tau_digits = [i*2 for i in pi_digits]
for i in tau_digits:
    if i >= 10:
        index = tau_digits.index(i)
        tau_digits[index-1] += 1
        tau_digits[index] -= 10

print(tau_digits)
tau_digits[11] = 9
more_tau = [5, 8, 6, 4, 7, 6, 9, 2, 5, 2, 8, 6, 7, 6, 6, 5, 5, 9, 0, 0, 5, 7, 6, 8, 3, 9, 4, 3]
tau_digits = tau_digits + more_tau

golden_digits = [1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 5]

very_long_tau_digits = tau_digits + [3, 8, 7, 9, 8, 7, 5, 0, 2, 1, 1, 6, 4, 1, 9, 4, 9, 8, 8, 9, 1, 8, 4, 6, 1, 5, 6, 3,
                                     2, 8, 1, 2, 5, 7, 2, 4, 1, 7, 9, 9, 7, 2, 5, 6, 0, 6, 9, 6, 5, 0, 6, 8, 4, 2, 3, 4, 
                                     1, 3, 5, 9, 6, 4, 2, 9, 6, 1, 7, 3, 0, 2, 6, 5, 6, 4, 6, 1, 3, 2, 9, 4, 1, 8, 7, 6, 
                                     8, 9, 2, 1, 9, 1, 0, 1, 1, 6, 4, 4, 6, 3, 4, 5, 0, 7, 1, 8, 8, 1, 6, 2, 5, 6]

print(f'Length pi_digits:{len(pi_digits)}\n\
Binary Big O pi_digits:{binary_search_big_o(pi_digits)}\n\
Simple Big O pi_digits:{simple_search_big_o(pi_digits)}\n')
print(f'Length tau_digits:{len(tau_digits)}\n\
Binary Big O tau_digits:{binary_search_big_o(tau_digits)}\n\
Simple Big O tau_digits:{simple_search_big_o(tau_digits)}\n')
print(f'Length golden_digits:{len(golden_digits)}\n\
Binary Big O golden_digits:{binary_search_big_o(golden_digits)}\n\
Simple Big O golden_digits:{simple_search_big_o(golden_digits)}\n')
