
my_list = [3,6,8,9,3,11]
character_set = ['a','b','c']
n = 3

def find_min(my_list):
    """The function uses recursion to fin the lowest int in a list"""

    if my_list == []: #if list is empty return -1
        return -1
    for k in my_list: #if list has a non numerical value return -1
        if type(k) == str:
            return -1
    if len(my_list) == 1: #when only one number(minimum) in list, return the list. This is the termination statement.
        return my_list[0]
    elif my_list[0] > my_list[1]: #the recursion statement using pop().
        my_list.pop(0)
    elif my_list[0] <= my_list[1]:
        my_list.pop(1)
        
    return find_min(my_list)

    
def sum_all(my_list):

    """The function uses recursion to find a sum of intergers in a list"""
    index = []
    if my_list == []: #if list is empty return -1
        return -1
    for k in my_list: #if list has a non numerical value return -1
        if type(k) == str:
            return -1
    if  len(my_list) == 1: #when only one number(sum) in list, return the list. This is the termination statement.
        return my_list[0]
        print(my_list[0])
    elif len(my_list) > 1:
        my_list[0] = my_list[0] + my_list[1] 
        my_list.pop(1) 
        return sum_all(my_list)
        

def find_possible_strings(character_set, n):
    """the recursion function finds all possible strings of a charactor set"""
    empty_list = []
    for i in character_set:
        if type(i) == int:
            return empty_list
    else:
        rec(character_set, n, '')
        return character_set

def rec(character_set, n, prefix):
    if n == 0:
        return prefix
        print(prefix) 
    else:
        for i in character_set:
            string = rec(character_set, n-1, prefix + i) 
                   


if __name__ == "__main__":
    find_min(my_list)
    sum_all(my_list)
    find_possible_strings(character_set, n)