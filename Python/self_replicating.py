s = 's = %r\nprint(s %% s)'
# print(s % s)

# print("{aba}{aba}_KILLLLLL".format(aba='ima'))
# print(s.__str__())

# print ('%r%r' % (2,2))

# print('%s bla bla bla # %% ' % ('4'))

with open('c:/Users/Yotam/Desktop/Excersises/Python/self_replicating.py') as f:
    c=1
    for line in f:
        print(str(c)+ '\t' +line.rstrip('\n'))
        c+=1