num = int(input())
num_lst = ['3', '6', '9']
val_lst = [0] * num


for i in range(1, num+1) : # 입력한 숫자마다 검사. 1, 2, 3, ... , 40
    val_lst[i-1] = i

for i in val_lst : # 1부터 40까지
    str_i = str(i)
    bool = False
    for j in num_lst : # 3 6 9마다
        for k in str_i : # 중요! for문에서 문자열의 자리를 뜯어볼 수 있음을 알게 되었음
            if j in k :
                print('-', end='')
                bool = True
            else:
                continue
    if bool == False :
        print(i, end='')
    print(end = ' ')

