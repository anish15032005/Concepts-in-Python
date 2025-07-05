#O(1) Constant
def func_constant(values):
    print(values[0])
    
func_constant([1,2,3])#the size of list will not have any effect on the computation

#O(n) Linear
def func_list(lst):
    for val in lst:
        print(val)
func_list([1,2,3])

#O(n^2) Quadratic, for n inputs we will get n^2 outputs
def func_quad(lst):
    for item_1 in lst:
        for item_2 in lst:
            print(item_1,item_2)
lst = [1,2,3]
func_quad(lst)






