# 1: Determine the Big-O notation
# A) the part of this eqation with the bigest growth rate comes down to either n**2 or 3*2**n, lets test
test_values = [x for x in range(1,101)]
for n in test_values:
    print(f'n**2:{n**2}')
    print(f'3*2**n:{3*2**n}')
# we see clearly that 3*2**n grows fastest.
# 3 and 2 is a constant and is omitted, so we are left with: O**n / O^n

# B) here there is realy only one term (n+5)*(n+20)
# 5 and 20 are constants and are omitted so we are left with n*n wich is eqal to n**2/n^2
# we are left with O^2/O**2

# C) this function computes on one pass and only accepts one input so we can expect no growt of complexity 
# with a big o notation of: O(1)

# D) this function passes the given list of inputt twice and therfore has a exponential growth of x**2,
# this gives the big o notation of: O**2

# E) this function passes the given list of inputt once and therfore has a linier growth fo x,
# this produces a big o of: O

# 2: Proving Big-O
# determin a constant c>0 such that: T(n)<c(n)
# A) show that T(n) = 6n + 4 is o(n)
# if we choose c = 6 then we get that:
# T(n) = 6n + 4 <= 6*n
# so that the big O of T(n):
# O(6*n) = O(n)
# T(n) is an of order constant of linear growth rate O(n)

# B) show that T(n) = n^2 + 5n + 2 is O(n^2)
# if we chose c = 8
# T(n) = n^2 + 5n +2 <= 8*n^2
# so that the big O of T(n):
# O(6*n^2) = O(n^2)
# T(n) is an of order constant of quadratic growth rate O(n^2)

# 3: Yet another task
list_a = [9,8,7,6,5,4,3,2,1]
list_b = [1,2,3,4,5,6,7,8,9,22]
# decypher
def decyphter(list_1, list_2):
    print(f'first list: {list_1}')
    print(f'second list: {list_2}')
    length_1 = len(list_1)
    length_2 = len(list_2)
    print(f'length of first list: {length_1} \n\
length of second list: {length_2}')
    if length_1 == length_2:
        print('they have the same length')
    else:
        print("they don't have the same length")
    
    likenes = 0
    for i in list_1:
        if i in list_2:
            likenes += 1

    if length_2 >= length_1:
        likenes = likenes / length_2
    else: 
        likenes = likenes / length_1

    if likenes > 0.5:
        print('but they are very similar!?')
        print(f'they have a similarity of: %{likenes*100}')
        if likenes >= 0.8 and likenes != 1:
            the_wierd_one = None

            if length_1 < length_2:
                the_wierd_one = 'list_2'
                the_other = 'list_1'
            else:
                the_wierd_one = 'list_1'
                the_other = 'list_2'
            print(f'the wierd one is: {the_wierd_one}')

            the_difference = []
            print(eval(the_wierd_one))
            for i in eval(the_wierd_one):
                if i not in eval(the_other):
                    the_difference.append(i)

            print(f'these make up the difference between the two: {the_difference}')

            for i in the_difference:
                eval(the_wierd_one).pop(eval(the_wierd_one).index(i))

            list_1 = sorted(list_1)
            list_2 = sorted(list_2)
            
            print(f'the two list sorted and with the difference removed:\n\
{list_1}\n{list_2}')

        elif likenes == 1:
            print('they are the same')

# efficient
def ef_decypher(list_1, list_2):
    if len(list_1) > len(list_2):
        the_long_one = 'list_1'
        the_short_one = 'list_2'
    
    elif len(list_1) < len(list_2):
        the_long_one = 'list_2'
        the_short_one = 'list_1'

    else:
        eqal_length = True

    difference = []
    for i in eval(the_long_one):
        if i not in eval(the_short_one):
            difference.append(i)

    eqal_length = False

    if eqal_length is False:
        print(list_1, list_2, difference)
        for i in difference:
            eval(the_long_one).pop(eval(the_long_one).index(i))
    
    return sorted(list_1), sorted(list_2)

print(ef_decypher(list_a, list_b))