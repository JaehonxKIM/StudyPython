# Random 함수
import random

print(random.choice(range(1,7))) #주사위


# 간단한 lottery 프로그램 만들기
import random

numbers = list(range(1, 46))
lottery = [] #list

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)
