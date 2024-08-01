num_list = [1,2,3,5,6,7,8,9,10]

def binary_search(input_list, low, high, key):
    if low > high:
        return False

    mid = (low+high) // 2

    if key == input_list[mid]:
        return input_list[mid]
    elif key > input_list[mid]:
        return binary_search(input_list,mid+1,high,key)
    elif key < input_list[mid]:
        return binary_search(input_list,low,mid-1,key)

print(binary_search(num_list,0,len(num_list)-1,4))