# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# # 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    result_dict = {}
    count_A = blood_types.count('A')
    count_B = blood_types.count('B')
    count_O = blood_types.count('O')
    count_AB = blood_types.count('AB')
    result_dict['A'] = count_A
    result_dict['B'] = count_B
    result_dict['O'] = count_O
    result_dict['AB'] = count_AB
    return result_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    result_dict = {}

    count_A = 0
    count_B = 0
    count_O = 0
    count_AB = 0
    for type in blood_types:
        if type == 'A':
            count_A += 1
        elif type == 'B':
            count_B += 1
        elif type == 'O':
            count_O += 1
        else:
            count_AB += 1
            
    result_dict['A'] = result_dict.get('A',count_A)
    result_dict['B'] = result_dict.get('B',count_B)
    result_dict['O'] = result_dict.get('O',count_O)
    result_dict['AB'] = result_dict.get('AB',count_AB)

    return result_dict

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
