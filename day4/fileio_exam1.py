# OPEN 하면 무조건 CLOSE 해야 함

# 파일 쓰기
f = open('writefile.txt','w', encoding = 'utf-8')

f.write('저는 한국사람입니다.\n')

texts = ['저는 한국사람이죠\n' , '이번엔 2022년이 되었습니다.\n']
f.writelines(texts)

# f.close()

# 내용 추가 'a'
f = open('writefile.txt','a', encoding = 'utf-8')
f.write('내용 추가할게요.')
f.close()

f = open ('writefile.txt', 'r', encoding= 'utf-8')

for line in f:
    print(line)
f.close()