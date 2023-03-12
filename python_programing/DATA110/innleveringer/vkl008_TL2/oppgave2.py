prompt = input('Sentence: ')    # ber om setning som den skal måle lengde på
length = len(prompt)
gues = input('Gues the length (including spaces): ')
if length == int(gues):
    print("That's correct!!")
else:
    print("That's false!")
