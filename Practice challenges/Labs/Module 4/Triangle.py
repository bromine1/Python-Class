def is_a_triangle(a, b, c):
    # sort list so order does not matter
    sides = [a, b ,c]
    sides.sort()
    # check 2 smallest sums agains't largest sum. If this works, then the others will too
    if sum(sides[0:2]) > sides[-1]:
        return True
    else:
        return False



print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
exit()