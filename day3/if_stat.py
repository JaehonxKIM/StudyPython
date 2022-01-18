#if 구문 - 흐름 제어
#if 구문 하위집합 줄 맞추기 *중요
#name = '승기'
#in name = 리스트로 사용가능

name = ['승기', '태경', '기영', '광조']

#if name == '재홍' or name == '승기' : 
if '승기' in name:
    print('의사를 만나러 갑니다.')
    print('의사선생님에게 인사합니다.')
elif name == '다원' :
    print('주사실로 갑니다.')
else : 
    print('호출할때까지 대기합니다.')

x = 2
if x != 10 :
    pass
else :
    pass
    
