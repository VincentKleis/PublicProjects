import turtle
x = 1
primes = []
turtle.speed(0.0000001)
number_line = range(1, 1001)
for i in number_line:
    # resets color to red for each number
    turtle.color("red")
    primes.append(i)
    for j in number_line:
        if j == 1 or j == i:
            continue
        
        # if i is divisible by j then change the turtle color and draw a line
        if i % j == 0:
            primes.pop(-1)
            turtle.color("blue")
            break
        
        
    turtle.forward(x)
    turtle.left(90)
    x += 1
    print(i)

print(primes)
turtle.mainloop()