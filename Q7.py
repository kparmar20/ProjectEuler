#this works, but is pretty slow and not a great solution

def PrimeNumbers(input_int):
    #works out prime numbers for the input number

    primeFactor = 1
    x = 2
    primelist=[]

    while x <= input_int / x:
        if input_int % x == 0:
            primeFactor = x
            input_int=input_int/x

            primelist.append(primeFactor)
        else:
            x=x+1

    if primeFactor < input_int:
        primelist.append(int(input_int))

    #put into set to make unique and output as list format
    return(list(set(primelist)))

def PrimeNumbersElement(primenumber_count):
    #number_count is no. of prime numbers you want

    number_count=[]
    x=0

    while len(concat_list(number_count))<primenumber_count:
        x=x+1
        number_count.append(PrimeNumbers(x))
    #return last element only, rather than whole list
    print(concat_list(number_count)[-1])

def concat_list(list_in):
    #Will concat the list of lists and make it unique
    list_out=[]

    for i in list_in:
        for j in i:
            list_out.append(j)

    list_out=list(set(list_out))
    list_out.sort()

    return list_out

PrimeNumbersElement(10001)
