count = 0
total = 0
while True:
    prompt = input('Enter a number: ')
    if prompt == 'done':
        break
    try:
        float(prompt)
    except:
        print('Innvallid input')
        continue
    count = count + 1
    total = int(prompt) + total

average = total / count
print(total,count,average)
