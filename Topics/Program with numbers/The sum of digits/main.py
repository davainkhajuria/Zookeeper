number = int(input())
sum_ = 0
while number > 0:
    sum_ = sum_ + number % 10
    number = number // 10
print(sum_)
