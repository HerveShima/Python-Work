a = input("Enter a list of string: ")
c = [str(w) for w in a.split(" ")]

def con(tw):
    for word in tw:
        if word in c:
            return {item: len(item) for item in c}
        
res = con(c)
print(res)