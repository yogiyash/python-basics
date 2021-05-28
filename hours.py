s1 = "{}:00 \n"
s2= "0"+s1
for i in range(0,24):
    s = s2 if i < 10 else s1
    print(s.format(i))