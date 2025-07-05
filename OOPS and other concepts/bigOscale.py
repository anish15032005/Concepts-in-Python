def print_once(lst):
    for val in lst:
        print(val)
        
lst = ["Sanjay","Raju","Manoj","Afroz"]
# print_once(lst=lst)#we can see its order is O(n)

def print_3(lst):
    for val in lst:
        print(val)
    for val in lst:
        print(val)
    for val in lst:
        print(val)
        
lst2 = [1,2,3,4]
# print_3(lst2)#we will get 12 elements, so this algo has order O(3n) ~= O(n)

def comp(lst):
    print(lst[0])
    
    midpoint = len(lst)//2
    
    for val in lst[:midpoint]:
        print(val)
    for x in range(10):
        print('number')
#order of this function will be O(1+n/2+10) ~= O(n)

