import random

testcase_number = int(input())
testcase = {}
random_numbers = []

for i in range(testcase_number):
    testcase[i] = random.randint(0,10000)
    print testcase