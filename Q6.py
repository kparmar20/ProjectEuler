def sum_of_square(min_int, max_int):
    list_out=[]
    for x in range(min_int, max_int+1):
        list_out.append(x**2)
    return sum(list_out)

def square_of_sum(min_int, max_int):
    list_out=[]
    for x in range(min_int, max_int+1):
        list_out.append(x)
    return sum(list_out)

#sum of squares
#print(sum_of_square(1,100))

#square of the sum
#print((square_of_sum(1,100))**2)


print(((square_of_sum(1,100))**2)-sum_of_square(1,100))

