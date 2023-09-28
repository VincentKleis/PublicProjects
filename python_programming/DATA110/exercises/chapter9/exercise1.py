txthand = open('exercises/chapter9/words.txt', 'r')

txt_words = {}
count = 0

for line in txthand:
    words = line.split()
    for word in words:
        if word not in txt_words:
            txt_words[str(word)] = str(count)
            count += 1

print(txt_words['else'])