x = [5, 6, 7, 8] #second set of list
def double(sequence):#Defining the function
    result = []
    for element in sequence:
        result = result + [element * 2]
    print result
double([1, 2, 3, 4]) #first set of list
double(x)
#print double
y = double ([5, 9, 2, 1]) #third set of list
#print y
