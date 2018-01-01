def multiples(mult1, mult2, total):

    #sort multiples so smallest is first
    mult_list=[mult1, mult2]
    mult_list.sort()
    mult1=mult_list[0]
    mult2=mult_list[1]

    list_mult1=[]
    list_mult2=[]
    list_mult1mult2=[]
    for x in range(1,total+1):
        #print(x)
        if x%(mult1*mult2)==0:
            list_mult1mult2.append(x)
        elif x%mult1==0:
            list_mult1.append(x)
        elif x%mult2==0:
            list_mult2.append(x)

    print(sum(list_mult1mult2)+sum(list_mult1)+sum(list_mult2))



multiples(3,5,999)
