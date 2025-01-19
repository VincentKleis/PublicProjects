for number in range(0,100):
    if number%3 == 0:
        if number%5 == 0:
            print(f"{number} : fizz-buzz")
            continue
        print(f"{number} : fizz")
        continue
    if number%5 == 0:
        print(f"{number} : buzz")
