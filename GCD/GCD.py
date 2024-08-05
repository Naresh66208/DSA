def gcd(m,n):
    fm = []
    for i in range(1,m+1):
        fm.append(i)

    fn = []
    for i in range(1,n+1):
        fn.append(i)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return cf[-1]

result = gcd(8,12)
print("The Greatest COmmon Divisor of 8 and 12 is : \n",result)