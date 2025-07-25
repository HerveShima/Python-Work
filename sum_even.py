a = input("Enter the numbers: ")

b = [int(num) for num in a.split(" ")]

def con(tw):
    even = 0
    odd = 0
    for i in len(tw):
        if tw[i] % 2 == 0:
            even += tw[i]
        else:
            odd += tw[i]
    return (odd,even)
res = con(b)
print(res)
