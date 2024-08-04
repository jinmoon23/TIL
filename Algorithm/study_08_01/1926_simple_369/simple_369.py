'''

'''
def simple_369_game(N):
    list_of_369 = ['33','36','39','63','66','69','93','96','99']
    str_number_list = list(map(str,range(1,N+1)))

    for index,string in enumerate(str_number_list):
        if string in list_of_369:
            str_number_list[index] = '--'
            continue
        if '3' in string or '6' in string or '9' in string:
            str_number_list[index] = '-'

    return ' '.join(str_number_list)



N = int(input())
print(simple_369_game(N))