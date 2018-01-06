

#1. set criteria on integer triplet
# c = 1000 - a - b
# a + b < 1000
# a < b < c
for a in range(1,500):
    for b in range (a, 500):
        c=1000-a-b

        # 2. compute pythagorean triplets
        # (a**2) + (b**2) = (c**2)
        if a**2 + b**2 == c**2:
            print ("a",a)
            print ("b",b)
            print ("c",c)
            print ("a2 + b2", a**2 + b**2)
            print ("c2", c**2)
            print ("abc",a*b*c)

