dummy_list = list('#++++')
# print(dummy_list)

for i in range(len(dummy_list)): # 0,1,2,3,4
    print(''.join(dummy_list))
    try:
        dummy_list[i+1],dummy_list[i] = dummy_list[i], dummy_list[i+1]
    except:
        None