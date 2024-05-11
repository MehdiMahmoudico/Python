
def countdown(number):
    print(list(range(number,-1,-1)))

countdown(9)
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([4,3]))

def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))


def values_greater_than_second(list):
    if len(list) < 2:
        return False
    else:
        a = []
        for i in range(0,len(list)):
             if list[i]>list[1]:
                a.append(list[i])
        print(len(a))
        return a
print(values_greater_than_second([5,2,3,2,1,4,2,1,0]))
print(values_greater_than_second([3]))

def length_and_value (size,value):
    a = []
    a.append(value)
    return a*size
print(length_and_value(9,9))