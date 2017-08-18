import glob,re

list1=[]

def cl(s):
    a = re.match("^ ip address (.+) (.+)", m)
    if bool(a) == True:
        #               print(a.groups())
        return ("IP", a.group(1), a.group(2))

    b = re.match("^hostname (.+)", m)
    if bool(b) == True:
        return ("HOST", b.group(1))

    c = re.match("^interface (.+)", m)
    if bool(c) == True:
        return("INT", c.group(1))

    return ("UNCLASSIFIED", )

x = glob.glob("C:\\Users\\aa.znamenskiy\\Seafile\\p4ne_training\\p4ne_training\\config_files\\*.txt")
for i in x:
    with open(i) as f:
        strlist=list(f)
       # print (strlist)
        for m in strlist:
           s = cl(m)
           if s[0] != 'UNCLASSIFIED':
               print(s)
