def gen_fib_term(n):
    #1,1,2,3,5,8

    if (n==1):  # first 2 elements are 1
        return 1
    elif (n==2):
        return 2

    return gen_fib_term(n - 1) + gen_fib_term(n - 2)

#y=gen_fib_term(32)
#print(y)

list_out=[]
for x in range(1,33):
    y=gen_fib_term(x)
    if y%2==0:
        list_out.append(y)
print(sum(list_out))