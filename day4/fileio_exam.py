#파일 입출력

# 파일 출력
# f = open('new_file.txt', 'w')
# f.close()

# 특정경로에 파일생성
# f = open('C:/Sources/sample/test.txt','w')
# f.close()
# print('파일이 생성되었습니다.')

# newfile.txt 파일 입력(읽어오기)
f = open('newfile.txt', 'r', encoding = 'utf-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close() 

# print(line)
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

#다른 방법
# for line in f:
#     print(line.replace('\n',''))
# f.close()  