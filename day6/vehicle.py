# vehicle.py
class Car :
    차량번호 = '22나 4444'
    제조사 = '현대'
    차량모델 = '소나타'
    색상 = '흰색'
    연료 = '경유'
    출고년도 = 2018

    
    def __init__(self,차량번호, 색상, 차량모델, 제조사) -> None:
            self.차량번호 = 차량번호
            self.색상 = 색상
            self.차량모델 = 차량모델
            self.제조사 = 제조사 

    def __str__(self) -> str:
        return f'제 차는 {self.출고년도}년도에 만들어진 {self.제조사}의 {self.차량모델}이고 {self.색상} {self.연료} 차량입니다.'

    def 전진한다(self,level):
        print(f'{self.색상}차가 {level} 단으로 앞으로 달린다')

    def 후진한다(self):
        print('뒤로 달린다')

    def 좌회전한다(self):
        print('왼쪽으로 달린다')

    def 우회전한다(self):
        print('오른쪽으로 달린다')

    def 멈춘다(self):
        print('멈춘다')



