#자료형
print(None)
print(type(None))

print(0 == None)
a = None
print(a)
print(type(a))

#숫자형
금액 = 12_345_666
print(금액)

#문자열형
bruce_eckel = 'Life is short , You need python'
print(bruce_eckel)

Muhammad_Ali = 'Float like a butterfly.\nAnd sting like a bee.'
print(Muhammad_Ali)

bruce_eckel = 'Life is short.\nYou need python' # /n 탈출문자
print(bruce_eckel)

# \남기기
bruce_eckel = 'Life is short. \\ You need python'
print(bruce_eckel)

#문장 줄 넘기기
bruce_eckel = '''Life is short.
You need python.
난 필요없는데... 파이썬'''
print(bruce_eckel)

#불형
val_sum = 1000
print(val_sum == 1000)
print(val_sum == 999)
#print(val_sum = 10) 오류

bl_true = True
print(type(bl_true))
print(bl_true == True) #True
print(bl_true is True) #True

print(a is None) #True

print(val_sum is 1000) #True

#의미가 있는 bool
print(bool(1)) # True
print(bool(0)) # False

#list
b=[1,2,3,4,5,6,7,8,9,10]
print(b)

b = [i for i in range(10)]
print (b)

# 1차원배열
arr2 =['Life', 'is', 'short','You', 'need', 'Python', 3]
print(arr2)

# 2차원배열
arr3 = [[1,2,3],[4,5,6]]
print(arr3)

#빈 리스트
arr4 = list()
print(arr4)

# 튜플
tuple1 =(1,2,3,4,5)
print(tuple1)

#딕셔너리
spiderman = { 'name' : 'peter parker', 'age': 18, 'weapon' : 'web shooter'}
print(spiderman['weapon'])

