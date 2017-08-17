import glob

list1=[]

x = glob.glob("C:\\Users\\aa.znamenskiy\\Seafile\\p4ne_training\\p4ne_training\\config_files\\*.txt")
for i in x:
    with open(i) as f:
        strlist=list(f)
       # print (strlist)
        for m in strlist:
            a = m.find('ip address')
            b = m.find('no')
            c = m.find('dhcp')
            if a != -1 and b == -1 and c == -1:
           # if a != -1:
                list1.append(m.strip().replace('ip address ', ''))

print(sorted(list(set(list1))))


