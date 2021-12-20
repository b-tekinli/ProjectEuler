a = 1
b = 2
sum = b

while b <= 4000000:
    b, a = a+b, b
    if b % 2 == 0:
        sum += b
print(sum)