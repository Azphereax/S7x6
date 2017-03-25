#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

def conv(Code):
    taille_Reg=len(Code)
    i=taille_Reg
    buf=""
    if(len(Code)%taille_Reg==0):
    	while(1):
    		index=i-1
    		while(index>(i-taille_Reg)):
    			buf+="\\x"+str(Code[index-1])+str(Code[index])
    			index-=2
    		if(i==taille_Reg):
    			break
    		i+=taille_Reg
    return buf

print("\n\n### RoptoShell ###\n\nSample : 0x...")
i=0
status=True
buff=""

while status:
    i+=1
    adr=input("\n\nAdresse "+str(i)+" E(nd) B(oucle)  :")
    if adr=="E":
        status=False
    elif adr=="B":
        boucle=input("\nNombre de fois :")
        print("\n")
        adr=input("Adresse :")

        for e in range(int(boucle,10)):
                buff+=conv(adr[2:])
    else:
        buff+=conv(adr[2:])

print("\n\nTaille (octets) : "+str(len(buff)/2)+"\n\n")
print(buff)
