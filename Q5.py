def divided_by_1_20(limit):

    #loop numbers and increase by 2 each time it fails test

    for x in range(20,limit,20):
        if mod_test(x,2)==True:
            if mod_test(x,3) == True:
                if mod_test(x, 4) == True:
                    if mod_test(x, 5) == True:
                        if mod_test(x, 6) == True:
                            if mod_test(x, 7) == True:
                                if mod_test(x, 8) == True:
                                    if mod_test(x, 9) == True:
                                        if mod_test(x, 10) == True:
                                            if mod_test(x, 11) == True:
                                                if mod_test(x, 12) == True:
                                                    if mod_test(x, 13) == True:
                                                        if mod_test(x, 14) == True:
                                                            if mod_test(x, 15) == True:
                                                                if mod_test(x, 16) == True:
                                                                    if mod_test(x, 17) == True:
                                                                        if mod_test(x, 18) == True:
                                                                            if mod_test(x, 19) == True:
                                                                                if mod_test(x, 20) == True:
                                                                                    print("Number is", x)
                                                                                    break



def divided_by_1_10(limit):

    #loop numbers and increase by 2 each time it fails test

    for x in range(20,limit,20):
        if mod_test(x,2)==True:
            if mod_test(x,3) == True:
                if mod_test(x, 4) == True:
                    if mod_test(x, 5) == True:
                        if mod_test(x, 6) == True:
                            if mod_test(x, 7) == True:
                                if mod_test(x, 8) == True:
                                    if mod_test(x, 9) == True:
                                        if mod_test(x, 10) == True:
                                            print("Number is", x)
                                            break



def mod_test(dividend, divisor):
    if dividend%divisor==0:
        return True
    else:
        return False

#y=mod_test(20,6)
#print(y)

divided_by_1_20(300000000)
#divided_by_1_10(3000)
