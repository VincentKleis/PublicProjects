# 1.
# n^3 is the fastest growing term, so aproaching infinity the other terms aproach 0 in comparative impact. we say that the big O is O^3

# 2.
# for any C the only relevant term becomes n^4 and the big O becomes O^4. to show this:
# T(n) = n^4 + n^3 + 9*n^2 + n log n + 5 >= n^4
# we test every constant in range 1 to 20 to find if any flipp the inneqality sign
from math import log

testing_constants = [x for x in range(1, 20)]

# function for the right side of the inneqality sign
def inneqality_r(n):
    return n**4 + n**3 + 9*n**2 + n*log(n) + 5

#function for the left side of the inneqality sign
def inneqality_l(n):
    return n*(n**4)

for n in testing_constants:
    print(f'{n} l: {round(inneqality_r(n))} r:{inneqality_l(n)}')

# we see than between the number 11 and 12 the inneqality sign would flipp, we can say that for the constant 12
# T(n) = n^4 + n^3 + 9*n^2 + n log n + 5 <= 12*n^4
# we can say that the big O for t(n) is:
# O(12*n^4) = O(n^4)
# and that T(n) is of order constant of from O(n^4) growth, this is because there is some constant C that would be the 
# difference in growth when aproaching infinty

# 3. 
# (a) O(n^2*sqrt(n)). there is a while loop inside a for loop, the for loop is one pass over every intiger smaler than n and larger or equal to 0, so it has a growth of n, 
# and the while loop inside the for loop sees how many times j can be multiplied by 2 before it surpases the size of the integer from the for 
# loop and therfore has a growth of n*sqrt(n), giving a total groth of n*n*sqrt(n) = n^2*sqrt(n). n^2 is the fastest growing term so aproching infinity O(n^2) would be the same function
# (b) O(nlogn). there is a forloop inside an other for loop, the outer for loop iterates trhough every integer smaler than n-1 and larger or eqal to 0 with one pass so it has a growth of n
# while the inner for loop itterates through every number smaler than n-1-(the outher loops integer) and larger than 0, the inner loop starts of by doing n iterations and ends up doing 0.
# the inner loop has logartmic growth in complexity (logn).
# the total growth is then n*logn = nlogn

# 4.
def solve_problem(S:list):
    A = []
    for i in range(0, len(S)):
        if i == 0:
            A.append(S[i])
        else:
            A.append(S[i]+A[i-1])
    return A
print(solve_problem(testing_constants))
# this function has a Big O of O(n), this is because there is only one loop that passes over the list S once