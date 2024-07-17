import random

testcase_number = 3
testcase = {}
random_list = []

for i in range(10):    
    random_list.append(random.randint(0,10000))

for j in range(testcase_number):
    testcase[j] = random_list
    
print(testcase)
