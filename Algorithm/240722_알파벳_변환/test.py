t = list(input()) # [A,B,C...] 
alpa_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def check(t):
    result_list = []
    for i in t: # 내가 입력한 값
        for char in alpa_list: # 비교를 위해 설정한 값
            if i == char:
                result_list.append(alpa_list.index(i)+1)
    result = ' '.join(map(str, result_list))
    return_test = result.rstrip()
    return return_test

print(check(t))