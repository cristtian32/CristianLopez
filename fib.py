def nombre(n):
    a , b = 0.1

    while a<n:
        print(a,end='')
        a,b=b,a+b
    print()
nombre(1000)


