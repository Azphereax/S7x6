#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

print("\n\n### CodetoShell ###\n\n")

taille_Reg=8 # 8 ou 16

print("\n\n"+str(4*taille_Reg)+" bits \n\n")

Code=""
Shell = []
# 1 ligne a recopier
Shell.append('VALUE')

for a in Shell:
	Code+="".join(reversed(["\\x"+a[i:i+2] for i in range(0, len(a), 2)]))
print(Code)
