largest_sofar=-1
print('Before',largest_sofar)
for the_num in [3,4,45,8,97,15]:
    if the_num>largest_sofar:
        largest_sofar=the_num
    print(the_num,largest_sofar)
print('After', largest_sofar)