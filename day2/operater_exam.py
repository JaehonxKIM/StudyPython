# 연산자(사칙연산)
import string


a = 11
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# 문자열 연산
stat1 = 'hello'
stat2 = 'world'
res = stat1+stat2
print(res)
print(stat1 , stat2)
print(stat1 + stat2)
res = stat1 , stat2
print(res)

print(stat1 + stat2)
# print(stat1 - stat2) #문자열엔 빼기 없음
print(stat1 * 5)
# print(stat1/ 3) #문자열 나누기 없음
# print(stat1 * stat2) #문자열끼리 곱하기 없음
print(len(stat1))
stat3 = '안녕하세요'
print(len(stat3))

# 문자열 인덱스, 리스트와 동일한 작업, 0부터 시작
print(stat3[0])
print(stat3[1])
print(stat3[2])
print(stat3[3])
print(stat3[4])
# print(stat3[5]) #예외발생 절대 불가능

# stat3[0] = '저'
# stat3[0] = '리'
# print(stat3)

print(stat3[-1])
print(stat3[-2])
print(stat3[-3])
print(stat3[-4])
print(stat3[-5])

#문자열 자르기 
일시 = '2022-01-17 14:39:25'

print(일시[:4],'년')
print(일시[5:7],'월')
print(일시[8:10],'일')
print(일시[11:13],'시')
print(일시[14:16],'분')
print(일시[17:],'초')

list_a =[1,2,3,4,5]
list_a[1] = 19
print(list_a)

print(stat3)
stat4 = '저리가' + stat3[3:]
print(stat4)

#문자열 포맷팅
str1 = "I'm happy {0} see U. aren't {1}?".format('2','U')
print(str1)

첫번째 = '2'
두번째 = 'U'
세번째 = 'U'
str2 = "I'm happy {첫번째} see {두번째}. aren't {세번째}?"

##숫자 천단위 콤마 

money = 10000000000000
print(format(money, ',d'))

from datetime import datetime 
now = datetime.now() #현재일시 생성
print(now)
print(now.strftime('%Y년 %m월 %d일 %H:%M:%S'))

import math 

myPi = math.pi
print(myPi)

print('{0}'.format(myPi))
print('{0:0.2f}'.format(myPi))
print(f'{myPi:0.6f}') #포맷 축약

full_name = 'Eric JH Kim'
age = 28
greeting = f'''안녕하세요. 저는{full_name}입니다.
나이는{age : 0.1f}살 이구요.''' 
print(greeting)

#이름 분리하기
part_name = full_name.split()
print(part_name)

test ='Hey guys'
print(test.split(','))

# |
code = 'Test|2022|01|17|f45678'
split_codes = code.split('|')
print(split_codes)

#이름 대체하기
print(full_name.replace('Eric JH', 'Harry kane'))

# 여백 없애기
aaa = '      hello, world       '
print(aaa.lstrip()) #왼쪽공백
print(aaa.rstrip()) #오른쪽공백
print(aaa.strip())

#글자 찾기
print(full_name.index('K')) 
print(full_name.index('H')) 
print(full_name.index('i')) 
print(full_name.index('E')) 
print(full_name.find('K'))
print(full_name.count('K'))

#대소문자 바꾸기
print('-'.join(full_name))
print(full_name.upper()) #대문자
print(full_name.lower()) #소문자
