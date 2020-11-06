
def find_min(element):
    """TODO: complete for Step 1"""
    '''
    Lists the input values for which the base case can return without recursion. If the
    first value is larger than the second value, it equates them and removes the second
    value. If not, it removes the second value. The process is repeated until 1 number
    is left i.e. the lowest.
    '''

    for item in element:
        if not isinstance(item, int):
            return -1

    if len(element) == 0:
        return -1

    elif len(element) == 1:
        return element[0]

    elif element[0] > element[1]:
        element[0] = element[1]
        element.remove(element[1])
        find_min(element)

    else:
        element.remove(element[1])
        find_min(element)
    return element[0]


def sum_all(element):
    """TODO: complete for Step 2"""
    '''
    Checks for invalid elements in the list. Lists the input values for which the base case
    can return without recursion. Adds the second value to the first value and removes the
    second value. The process is repeated until 1 number is left i.e. the sum of the list.
    '''

    for item in element:
        if not isinstance(item, int):
            return -1

    if len(element) == 0:
        return -1

    elif len(element) == 1:
        return element[0]

    else: 
        element[0] += element[1]
        element.remove(element[1])
        sum_all(element)
        return element[0]


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    '''
    Function starts with an empty prefix. Checks for invalid elements in the list. Lists
    the input value for which the base case can return without recursion. Combines the 
    characters in the list to find all possible combinations. Adds the combinations one
    at a time to the prefix. 
    '''
    
    prefix= []
    for item in character_set:
        if isinstance(item, int):
            return prefix

    if n == 1:
        return character_set

    for x in character_set:
        for y in find_possible_strings(character_set, n-1):
            prefix.append(x+y)
    return prefix


#Main used to run code 
'''
if __name__ == "__main__":
    element = [2, 5, 1, 8]
    print((find_min(element)))

    print(sum_all(element))

    character_set= ["a" ,"b"]
    n=3
    print("\n".join(find_possible_strings(character_set,n)))
'''