from hashlib import md5
# ex 1
# A) Not full, Not perfect, Not complete
# B) Full, Complete, Not perfect
# C) Full, Complete, Perfect

# ex 3
def bruteforce(dor_id:str):
    password = ''
    count = 0
    while len(password) < 4:
        hash = md5((dor_id+str(count)).encode('utf-8')).hexdigest()
        if hash[0] == '0' and hash[1] == '0':
            print(count, ':', hash)
            password += hash[3]
        count += 1
    
    return password

test = bruteforce('cyd')
print(test)