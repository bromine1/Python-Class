def radianconvert(n):
    from math import pi
    # convert to degree
    n=float(n) * pi
    dn= (n / (pi/180))
    return dn

print(radianconvert(input ("please give a radian, do not add pi\n for example 2π would be put in as 2\n")))
exit
