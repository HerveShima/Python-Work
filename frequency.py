a = input("Write a sentence: ")
freq = {}
b = a.lower().replace('.','')
words = b.split()

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)
