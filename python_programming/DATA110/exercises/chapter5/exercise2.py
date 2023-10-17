count = 0
total = 0
smalest = None
largest = None
while True:
    prompt = input('Enter a number: ')
    if prompt == 'done':
        break

    try:
        float(prompt)
    except:
        print('Innvallid input')
        continue

    if smalest is None or int(prompt) < smalest:
        smalest = int(prompt)
    if largest is None or int(prompt) > largest:
        largest = int(prompt)

    count = count + 1
    total = int(prompt) + total

print(total,count,smalest,largest)
