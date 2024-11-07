a = input("Enter the numbers: ")

b = [int(num) for num in a.split(" ")]

def con(tw):
    even = 0
    odd = 0
    for num in tw:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return (even,odd)
res = con(b)
print(res)
