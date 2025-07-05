def matcher(lst,match):
    for item in lst:
        if item == match:
            return True
    return False
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

print(matcher(lst,1))#this is the best case because item seeked is index 0. O(1) Best case becomes a constant.
print(matcher(lst,20))#worst case, entire list must be searched, n elements. O(n) Worst becomes Linear.


#Space Complexity
def memory(n):
    for x in range(n):# TIME COMPLEXITY  O(n)
        print('Memory!')# SPACE COMPLEXITY O(1)
# print(memory(10))