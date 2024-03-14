def indexof(text,chars):
    for i in range(0,len(text)):
        if text[i]==chars:
            return i
f=open("g.txt","r")
f2=open("gn.txt","w")

for r in f.readlines():
    g1=""
    g2=""
    if r[0]==r[2]:
            x=indexof(r,"|")
            g1=r[0]+r[1]
            for k in  range(x+1,len(r)-1):
                g1=g1+r[k]
            g1=g1+r[0]+"'"
            g2=r[0]+"'"+r[1]
            for k in range(3,x):
                g2=g2+r[k]
            g2=g2+"|"+"e"
            f2.write(g1+"\n")
            f2.write(g2+"\n")
    else:
        f2.write(r+"\n")
f.close()
f2.close()
            
    
            
    
     