a = 10 
b = 20
c = 30
d = 40



rank:int = int(input('enter the rank secured:\n'))

if rank <= a:
    print("go to group A")

elif rank > a and rank <= b:
    print ('go to group B')

elif rank > b and rank < c:
    print('go to group C')
else:
    print('go to group D') 
