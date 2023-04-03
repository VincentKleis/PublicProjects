import time

def make_list(length):
    a = [x+1 for x in range(0,length)]
    b = [x+1 for x in range(0,length)]
    c = [x+1 for x in range(0,length)]
    d = [x+1 for x in range(0,length)]
    return a,b,c,d

def test_1(a,b,c,d):
    total_time = time.perf_counter()
    result = [x+y+z+q for x in a for y in b for z in c for q in d]
    print(f'time list comp:{time.perf_counter_ns()-total_time}ns')

def test_2(a,b,c,d):
    total_time = time.perf_counter()
    def add_4(a,b,c,d):
        return a+b+c+d
    result = map(add_4(a,b,c,d), a)
    print(f'time map: {time.perf_counter_ns()-total_time}ns')

test_lengths = [1,2,4,8,16,32,64,128,256]

for i in test_lengths:
    a,b,c,d = make_list(i)
    print(f'test of list length {i}')
    test_1(a,b,c,d)
    test_2(a,b,c,d)