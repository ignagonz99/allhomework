def check_triangle(a,b,c):

    if a>=b and a>=c:

        maximum =a
        small1=b
        small2 = c

    elif b>= a and b>=c:

        maximum = b
        small1 = c
        small2 = a

    else:

        maximum = c
        small1 = a
        small2 = b

    if maximum<small1+small2

        return True

print(check_triangle(a,b,c))
