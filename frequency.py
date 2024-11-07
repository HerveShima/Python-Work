a = input("Write a sentence: ")
frequency = {}
b = a.lower().replace('.','')
words = b.split()

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)
