#부산버스 노선별 이용건 수
import csv

flie_name = '부산버스정보.csv'
f = open('부산버스정보.csv', mode = 'r', encoding= 'utf-8')

reader = csv.reader(f,delimiter=',')
next(reader) #맨 처음 헤더를 없애주는 역할
for line in reader:
    print(line)

f.close()