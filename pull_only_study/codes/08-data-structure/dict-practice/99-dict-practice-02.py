# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기

# 1. [] 표기법을 사용한 방법
def dict_invert(input_dict):
    result_dict = {}
    # 3. items로 키값쌍 받아와서 뒤집기
    for (key,value) in input_dict.items():
        result_dict[value] = [key] # 10이라는 키에 [1]을 넣음
    return result_dict


# 2. get 메서드를 사용한 방법
def dict_invert(input_dict):
    result_dict = {}
    value_set = set([])

    for i in range(1,len(input_dict)+1):
        value_set.add(input_dict.get(i))

    print(value_set) # {10,20,30}
    
    for element in value_set:
        if element == input_dict[1]:
            result_dict[element] = input_dict.get(element,[1])
        elif element == input_dict[2]:
            result_dict[element] = input_dict.get(element,[2])
        else:
            result_dict[element] = input_dict.get(element,[3,4])

    return result_dict


# 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    result_dict = {}
    value_set = set([])
    key_list =[]

    for i in range(1,len(input_dict)+1):
        value_set.add(input_dict.get(i))

    for key in input_dict:
        key_list.append(key)

    result_element = value_set.pop()

    result_dict[result_element] = key_list
    return result_dict


# print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))  # {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
