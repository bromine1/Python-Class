def uhoh():
    import random as r
    x=[]
    while True:
        x.append(r.randint(0,999999999999999999999999999))
        if len(x) % 20 == 0:
            x.append(x)
            print(x)

uhoh()
