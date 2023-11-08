

# ex1
def recur_factor(n):
    if n <= 1:
        return 1
    return n * recur_factor(n-1)


test = recur_factor(5)
print(test)


# ex2a
def truncation_hash(n):
    number_list = list(str(n))
    result = []
    for i in number_list:
        result.append(int(i))

    number_list = result
    result = []

    for i in range(0, len(number_list)):

        if (i+1) % 3 == 0 or (i+1) % 5 == 0:
            result.append(number_list[i])

    result_str = ''
    for i in result:
        result_str += str(i)

    return int(result_str)


test = truncation_hash(94283641911)
print(test)


# ex2b
def string_hash(string):
    result = 1

    for i in string:
        result *= ord(i)

    return result


test = string_hash('password')
print(test)


# ex3
class PasswordDatabase:

    def __init__(self):
        self.passwords = {}

    # ex5a
    def create_user(self):
        username = input('Write your username: ')
        password = input('Write your password: ')
        password_hash = string_hash(password)
        self.passwords[username] = password_hash

    # ex5b
    def check_passwords(self, username=None, password=None):
        if username is None and password is None:
            username = input('Write your username: ')
            password = input('Write your password: ')
        test = string_hash(password) == self.passwords[username]
        return test

    # ex5c
    def uppdate_passwords(self):
        username = input('Write your username: ')
        password = input('Write your password: ')
        test = self.check_passwords(username, password)
        if test is True:
            new_password = input('Write your new password: ')
            self.passwords[username] = string_hash(new_password)


print('making first user -> password connection')
test = PasswordDatabase()
test.create_user()
test1 = test.passwords
print(test1)
print('test password against input')
test2 = test.check_passwords()
print(test2)
print('change password')
test.uppdate_passwords()
test3 = test.passwords
print(string_hash('password123'))
print(test3)
