
a = int(input())
b = int(input())
c = int(input())

def seats(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 + 1

s1 = seats(a)
s2 = seats(b)
s3 = seats(c)
print(s1 + s2 + s3)


