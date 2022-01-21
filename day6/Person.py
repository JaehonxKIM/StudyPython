# Person.py
# Person 클래스

class Person:
    name = '' # 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 275
    bloodtype = ''
    
    # 생성자
    def __init__(self,name,age,height,gender,feetsize,bloodtype) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        self.feetsize = feetsize
        self.bloodtype = bloodtype
        print('Person이 생성되었습니다.')

    def 소개한다(self):
        greeting = f'''안녕하세요 저는 {self.name} 입니다. {self.gender} 이구요. {self.age} 살입니다. 
    키는 {self.height}cm이고, 혈액형은 {self.bloodtype} 입니다. 발사이즈는 {self.feetsize}입니다.'''
        print(greeting)

    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹었다.')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일했다.')       


if __name__ == '__main__':
    kjh = Person('김재홍', 28, 177, 'male', 275, 'RH+ B') #__init__(self, name, age):
    kjh.name = '김재홍'
    kjh.age = 28
    kjh.height = 177
    kjh.gender = '남자'
    kjh.feetsize = 275
    kjh.bloodtype = 'RH+ B'
    
    kjh.소개한다()
    kjh.먹는다('돈코츠라멘')
    kjh.일한다('아이스 아메리카노')
    
    # p = Person() # p 라는 Person 객체 생성
    # print(type(p))
    # print(id(p)) # id값

    # p2 = Person() # p2라는 객체 생성
    # print(type(p2))
    # print(id(p2))
