# 기본 for문
# arr = list(range(1,101))

# for i in arr:
#    print(f'{i:2.1f}')

# 튜플로 for문
# arr2 = ('me','my','friend','Jane')

# for item in arr2:
#    print(f'{item:>10}')

# 합계 for문
# numbers = list(range(1,11)) #1~10
# res = 0
# for item in numbers :
#     res += item
# print(f'{numbers[-1]}까지의 총 합은 {res}입니다')

# 홀수짝수 구분
# numbers = list(range(1,21)) #1~20

# for item in numbers : 
#     if item % 2 == 0 :  # if item % 2 != 0 : 홀수
#         print(f'{item}은 짝수')

# numbers = list(range(1,21)) #1~20

# 13이상이면 탈출 또는 계속 (break,continue)
# numbers = list(range(1,21)) #1~20까지
# for item in numbers :
#     if item == 15:
#         continue #break

#     if item % 2 == 1 :  # if item % 2 != 0 : 홀수
#         print(f'{item}은 홀수')

# 구구단
# print('구구단 프로그램')
# for i in range(2, 10): #2~9
#     print(f'{i}단 시작')
#     for j in range(1, 10): #1~9
#         print(f'{i} x {j} = {i*j:2d}', end= '    ')
#     print('')

#inline for문
a = [1,2,3,4]
result = [i * 3 for i in a]
print(result)

#기존 for문
t = []
for i in a :
    t.append(i * 3)
print(t)
