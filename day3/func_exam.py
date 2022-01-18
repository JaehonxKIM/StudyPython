# 함수 선언 및 사용

# 더하기 함수 선언
from re import I


def add(a, b):
    res = a + b

    return res 

# 함수 사용
print(add(4322, 417))

mid_val = add(3, 4)
print(mid_val * 3)


# 함수 종류
#(1) 매개변수가 없는 형태
def say_hello():
    return 'hello~'

print(say_hello())
print(say_hello(), 'my friend')

val = say_hello()
print(val.replace('o~',''))

#(2) 결과값이 없는 형태
def say_hello(name):
    print(f'hello~ {name}')
    return   # none은 생략
say_hello('Eric')

#(3) 둘 다 없는 경우
def say_goodbye():
    print('Bye bye~')
say_goodbye()    

#(4) 매개변수 지정
def multi(a,b):
    return a * b
print(multi(2, 9))
print(multi(9, 2))

#(5) 매개변수 개수가 가변적일때(매개변수가 하나여도 상관없음)
def plus(*args):
    res = 0

    for i in args:
        res+= i
    return res

print(plus(1,2,3))
print(plus(1,2,3,4,5,6,7))
print(plus(1))

#(6) 리턴값이 하나 이상일 경우
def mul_and_div(x, y):
    mul= x * y
    div =x / y

    return(mul, div) #튜플
(res1,res2) = mul_and_div(7 , 8)
print(res1,res2)

def 사칙연산(x,y):
    return(x+y, x-y, x/y, x*y)

res1, res2, res3, res4 = 사칙연산 (9 , 5)
print(res1, res2, res3, res4)
print(type(사칙연산 (1 , 2)))








 


  

