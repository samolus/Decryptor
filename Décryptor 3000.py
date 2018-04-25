def cryptVigenere():
    demande_fichier=input("Voulez vous ouvrir un fichier  (oui ou non) ?: ")
    ##Si l'utilisateur accepte d'ouvrir un fichier :
    if demande_fichier=="oui":
       t=input("lequel ?(doit se trouver dans le meme dossier que ce programme et n'oubliez pas de rajouter .txt): ")
       mon_fichier = open(t, "r")## on place dans la variable "t" le nom du fichier
       l1 = mon_fichier.read()
       mon_fichier.close()
    else :
        ## Demande à l'utilisateur de rentrer un texte
        l1=input("Quel texte voulez vous coder ?")

    
    cle=input("Entrer une clé") ##Clé à entrer par l'utilisateur
    x=0
    l2=""
    l3=""
    for i in range (len(l1)):
        if x >len(cle)-1:
            x=0
        if ord(l1[i])<=64 and ord(l1[i])>=32:##prend le code ascii pour la ponctuation et les nombres :64=@,32="espace"
            l2=l2+(l1[i])##l2 prend tout ce qu'elle est déjà et y ajoute le caractère de l1 correspondant
        elif ord(l1[i])<=90 and ord(l1[i])>=65:##prend le code ascii pour la majuscules :90=Z, 65=A
            l2=l2+cle[x]##l2 prend tout ce qu'elle est déjà et y ajoute la lettre de la clé correspondante
            x=x+1##+1pour que la clé lise la prochaine lettre
        elif ord (l1[i])<=122 and ord(l1[i])>=97:##prend le code ascii pour les miniscules :97=a,122=z
            l2=l2+cle[x]##l2 prend tout ce qu'elle est déjà et y ajoute la lettre de la clé correspondante
            x=x+1##+1pour que la clé lise la prochaine lettre
        elif ord(l1[i])<=96 and ord(l1[i])>=91:##prend le code ascii pour le reste de la ponctuation:96=[ , 91=`
            l2=l2+(l1[i])##l2 prend tout ce qu'elle est déjà et y ajoute le caractère de l1 correspondant
   
    print(l2)    

    for i in range (len(l1)):
        if ord(l1[i])<=90 and ord(l1[i])>=65: ##prend le code ascii pour la majuscules :90=Z, 65=A
            a=ord(l2[i])+(ord(l1[i])-65)      
            if a>90:                        
                a=64+(ord(l2[i])+(ord(l1[i])-65)-90)
            l3=l3+chr(a)##l3 prend tout ce qu'elle est déjà et y ajoute le caractère décoder de l'ascii a correspondant
        elif ord(l1[i])<=64 and ord(l1[i])>=32:##prend le code ascii pour la ponctuation et les nombres :64=@,32="espace"
            l3=l3+l2[i]##l3 prend tout ce qu'elle est déjà et y ajoute le caractère de l2 correspondant
        elif ord(l1[i])<=122 and ord(l1[i])>=97:##prend le code ascii pour les miniscules :97=a,122=z
            a=ord(l2[i])+(ord(l1[i])-97)      
            if a>122:                        
                a=96+(ord(l2[i])+(ord(l1[i])-97)-122)
            l3=l3+chr(a)##l3 prend tout ce qu'elle est déjà et y ajoute le caractère décoder de l'ascii a correspondant
        elif ord(l1[i])<=96 and ord(l1[i])>=91:##prend le code ascii pour le reste de la ponctuation:96=[ , 91=`
            l3=l3+(l2[i])##l3 prend tout ce qu'elle est déjà et y ajoute le caractère de l2 correspondant

    print(l3)
    g=input("Voulez vous enregistrer le texte décodé ? (oui ou non) :")## demande si l'utilisateur veut enregistrer le texte codé
    if g=="oui":                    ##permet d'ouvrir le fichier en question et d'y ecrire le texte codé pour ensuite l'enregistrer dans un fichier .txt
       e=input("Dans quel fichier(precisez .txt)?:")##demande le nom du fichier ou le texte codé sera enregistré
       fichier=open(e,"w")
       fichier.write(l3)
       fichier.close()
       print("fait !")
    if g=="non":
       print("ok")
    print("Merci d'avoir utilisé DECRYPTOR 3000 !")

       
def decryptVigenere():
    demande_fichier=input("Voulez vous ouvrir un fichier  (oui ou non) ?: ")
    ##Si l'utilisateur accepte d'ouvrir un fichier :
    if demande_fichier=="oui":
       t=input("lequel ?(doit se trouver dans le meme dossier que ce programme et n'oubliez pas de rajouter .txt): ")
       mon_fichier = open(t, "r")## on place dans la variable "t" le nom du fichier
       l1 = mon_fichier.read()
       mon_fichier.close()
    else :
        ## Demande à l'utilisateur de rentrer un texte
        l1=input("Quel texte voulez vous coder ?")

    
    cle=input("Entrer une clé")
    x=0
    l2=""
    l3=""
    for i in range (len(l1)):
        if x >len(cle)-1:
            x=0
        if ord(l1[i])<=64 and ord(l1[i])>=32:
            l2=l2+(l1[i])
        elif ord(l1[i])<=90 and ord(l1[i])>=65:
            l2=l2+cle[x]
            x=x+1
        elif ord (l1[i])<=122 and ord(l1[i])>=97:
            l2=l2+cle[x]
            x=x+1
    print(l2)
    ## fonction de décodage propement dit

    for i in range (len(l1)):              
        if ord(l1[i])<=90 and ord(l1[i])>=65: 
            x=64                            
            for j in range (26):            
                x=x+1                        
                a=ord(l2[i])+(x-65)          
                if a>90:
                    a=64+(ord(l2[i])+(x-65)-90)
                if a==ord(l1[i]):
                    break
            l3=l3+chr(x)
        if ord(l1[i])<=122 and ord(l1[i])>=97:
            x=96                            
            for j in range (26):            
                x=x+1                       
                a=ord(l2[i])+(x-97)          
                if a>122:
                    a=96+(ord(l2[i])+(x-97)-122)
                if a==ord(l1[i]):
                    break
            l3=l3+chr(x)
        if ord(l1[i])<=64 and ord(l1[i])>=32:
            l3=l3+(l2[i])
    print(l3)
    g=input("Voulez vous enregistrer le texte décodé ? (oui ou non) :")## demande si l'utilisateur veut enregistrer le texte codé
    if g=="oui":                    ##permet d'ouvrir le fichier en question et d'y ecrire le texte codé pour ensuite l'enregistrer dans un fichier .txt
       e=input("Dans quel fichier(precisez .txt)?:")##demande le nom du fichier ou le texte codé sera enregistré
       fichier=open(e,"w")
       fichier.write(l3)
       fichier.close()
       print("fait !")
    if g=="non":
       print("ok")
    print("Merci d'avoir utilisé DECRYPTOR 3000 !")
    

def decryptAffine():
   def decode_affine(contenue,a,b):
    
       ##Le texte codé initial est vide.
       textedecode=""

       for i in range (len(contenu)):
          ##décodage majuscules.
          if ord(contenu[i])<=90 and ord(contenue[i])>=65:
             x=64
             for j in range (26):
                x=x+1
                v=x-65
                k=a*v+b
                y=k%26
                m=y+65
                if m==ord(contenu[i]):
                   break
             textedecode=textedecode+chr(x)
             ##décodage minuscules
          if ord(contenu[i])<=122 and ord(contenue[i])>=97:
             x=96
             for j in range (26):
                x=x+1
                v=x-97
                k=a*v+b
                y=k%26
                m=y+97
                     
                if m==ord(contenu[i]):
                   break
             textedecode=textedecode+chr(x)
          ## espace non codé
          if ord(contenue[i])==32:
             textedecode=textedecode+" "
             ## decodage ponctution
          if ord(contenu[i])<=47 and ord(contenu[i])>=33:
             x=32
             for j in range (15):
                x=x+1
                v=x-33
                k=a*v+b
                y=k%15
                m=y+33
                if m==ord(contenue[i]):
                   break
             textedecode=textedecode+chr(x)
          ## decodage des nombre
          if ord(contenu[i])<=57 and ord(contenu[i])>=48:
             x=47
             for j in range (10):
                x=x+1
                v=x-48
                k=a*v+b
                y=k%10
                m=y+48
                if m==ord(contenue[i]):
                   break
             textedecode=textedecode+chr(x)
          ## ? non codé
          if ord(contenu[i])==63:
             textedecode=textedecode+ "?"
          ## décodage des autres caractères spéciaux
          if ord(contenu[i])<=168 and ord(contenu[i])>=148:
             x=147
             for j in range (21):
                x=x+1
                v=x-148
                k=a*v+b
                y=k%21
                m=y+65
                if m==ord(contenue[i]):
                   break
             textedecode=textedecode+chr(x)
       return textedecode

         
   ##Demande a l'utilisateur de rentrer les cléfs de chiffrement a et b de la fonction affine.
   a=int(input("Entrez une premiere cléf de chiffrement (comprise entre 1 et 25, non  paire et different de 13) : "))
   b=int(input("Entrez une seconde cléf de chiffrment (compris entre 0 et 25) : "))
   while a%2==0 or a<1 or a>25 or a==13 :
      a=int(input("Vous n'avez pas respecté les consignes, veuillez retaper a="))
   if 1<=a<=25 and a%2!=0 and a!=13:      
      print("Coefficient a valide")

   if b>25 or b<0 :
      while  b<0 or b>25:
         b=int(input("Vous n'avez pas respecté les consignes, veuillez retaper b="))
   else:
      print("Coefficient b valide")


   ##demande a l'utilisateur si il veut ouvrir un fichier
   demande=input("Voulez vous ouvrir un fichier  (oui ou non) ?: ")
   ##Si l'utilisateur accepte d'ouvrir un fichier :
   if demande=="oui":
      t=input("lequel ?(doit se trouver dans le meme dossier que ce programme et n'oubliez pas de rajouter .txt): ")
      mon_fichier = open(t, "r")## on place dans la variable "t" le nom du fichier
      contenu = mon_fichier.read()
      mon_fichier.close()
   else :
      ## Demande à l'utilisateur de rentrer un texte
      contenu=input("Tapez le texte à décoder : ")

   ##decodage
   textedecode = decode_affine(contenu,a,b)
   ## Affichez le texte décodé
   print("Texte décodé:",textedecode)

   g=input("Voulez vous enregistrer le texte codé ? (oui ou non) :")## demande si l'utilisateur veut enregistrer le texte codé
   if g=="oui":                    ##permet d'ouvrir le fichier en question et d'y ecrire le texte codé pour ensuite l'enregistrer dans un fichier .txt
      e=input("Dans quel fichier(precisez .txt)?:")##demande le nom du fichier ou le texte codé sera enregistré
      fichier=open(e,"w")
      fichier.write(textedecode)
      fichier.close()
      print("fait !")
   if g=="non":
      print("ok")
   print("Merci d'avoir utilisé DECRYPTOR 3000 !")


def cryptAffine():

   ##Demande a l'utilisateur de rentrer les cléfs de chiffrement a et b de la fonction affine.
   a=int(input("Entrez une premiere cléf de chiffrement (comprise entre 1 et 25, non  paire et different de 13) :"))
   ##On s'assure que les conditions des coefficients sont respectés
   while a%2==0 or a<1 or a>25 or a==13 :
      a=int(input("Vous n'avez pas respecté les consignes, veuillez retaper a="))
   if 1<=a<=25 and a%2!=0 and a!=13:      
      print("Coefficient a valide")
   b=int(input("Entrez une seconde cléf de chiffrment (compris entre 0 et 25) :"))
   while  b<0 or b>25:
      b=int(input("Vous n'avez pas respecté les consignes, veuillez retaper b="))
   if 0<=b<=25:
      print("Coefficient b valide")
            
             
   ##Le texte codé initial est vide.
   textecode=""
   ##demande a l'utilisateur si il veut ouvrir un fichier
   demande=input("Voulez vous ouvrir un fichier  (oui ou non) ?:")
   ##Si l'utilisateur accepte d'ouvrir un fichier :
   if demande=="oui":
       print("Avant de donner le nom du fichier que vous voulez ouvrir, assurez vous qu'il soit dans le meme dossier que ce programme svp")
       l=input("Tapez ok lorsque vous vous en etes assuré :")
       if l=="ok":
       
          t=input("Quel fichier souhaitez vous ouvrir ?(ne rentrez pas l'esxtension .txt) :")
          mon_fichier = open(t+".txt", "r")## on place dans la variable "t" le nom du fichier
          contenu = mon_fichier.read()
          contenu=contenu.replace("à","a")##On remplace les caracteres avec accents du texte present dans le fichier par d'autres que l'on pourra coder 
          contenu=contenu.replace("é","e")
          contenu=contenu.replace("è","e")
          contenu=contenu.replace("ê","e")
          contenu=contenu.replace("ù","u")
          contenu=contenu.replace("ç","c")
          
          
          if 1<=a<=25 and a%2!=0 and a!=13 and 0<=b<=25 : ##Verification des conditions des coefficients entrés par l'utilisateur
              for i in range (len(contenu)):
              ##Codage des majuscules.
                  if ord(contenu[i])<=90 and ord(contenu[i])>=65:
                     v=ord(contenu[i])-65
                     k=a*v+b
                     y=k%26
                     m=y+65
                     textecode=textecode+chr(m)
              ##Codage des minuscules.
                  if ord(contenu[i])<=122 and ord(contenu[i])>=97:
                     v=ord(contenu[i])-97
                     k=a*v+b
                     y=k%26
                     m=y+97
                     textecode=textecode+chr(m)
              ##Espace non codé.
                  if ord(contenu[i])== 32:
                     textecode=textecode+" "
              ##Codage de la ponctuation.
                  if ord(contenu[i])<=47 and ord(contenu[i])>=33:
                     v=ord(contenu[i])-33
                     k=a*v+b
                     y=k%15
                     m=y+33
                     textecode=textecode+chr(m)
              ##Codage des nombres .
                  if ord(contenu[i])<=57 and ord(contenu[i])>=48:
                     v=ord(contenu[i])-48
                     k=a*v+b
                     y=k%10
                     m=y+48
                     textecode=textecode+chr(m)   
              ##point d'interrogation non codé. 
                  if ord(contenu[i])== 63:
                     textecode=textecode+"?"    

              ##Codage des autres caracteres spéciaux (accent et autres..).
                  if ord(contenu[i])<=168 and ord(contenu[i])>=148:
                     v=ord(contenu[i])-148
                     k=a*v+b
                     y=k%21
                     m=y+65
                     textecode=textecode+chr(m)

              ##Affichage du texte codé.

              print("Texte codé :",textecode)

          else :
              print("Condtion d'entrée des cléfs de chiffrement non respctées")##Si les conditions des coefficients ne sont pas respectées, on averti l'utilisateur.

          mon_fichier.close()    
      
     
   else:
       ##Demande a l'utilisateur de rentrer un texte.
       texte=input("Entrez un texte: ")

       texte=texte.replace("à","a") ##Ici aussi on remplace les lettres mais cette fois ci dans le texte precedemment rentré par l'utilisateur.
       texte=texte.replace("é","e")
       texte=texte.replace("è","e")
       texte=texte.replace("ê","e")
       texte=texte.replace("ù","u")
       texte=texte.replace("ç","c")


       if 1<=a<=25 and a%2!=0 and a!=13 and 0<=b<=25 : ##Verification des conditions des coefficients entrés par l'utilisateur
           for i in range (len(texte)):
           ##Codage des majuscules.
               if ord(texte[i])<=90 and ord(texte[i])>=65:
                  v=ord(texte[i])-65
                  k=a*v+b
                  y=k%26
                  m=y+65
                  textecode=textecode+chr(m)
           ##Codage des minuscules.
               if ord(texte[i])<=122 and ord(texte[i])>=97:
                  v=ord(texte[i])-97
                  k=a*v+b
                  y=k%26
                  m=y+97
                  textecode=textecode+chr(m)
           ##Espace non codé.
               if ord(texte[i])== 32:
                  textecode=textecode+" "
           ##Codage de la ponctuation.
               if ord(texte[i])<=47 and ord(texte[i])>=33:
                  v=ord(texte[i])-33
                  k=a*v+b
                  y=k%15
                  m=y+33
                  textecode=textecode+chr(m)
           ##Codage des nombres .
               if ord(texte[i])<=57 and ord(texte[i])>=48:
                  v=ord(texte[i])-48
                  k=a*v+b
                  y=k%10
                  m=y+48
                  textecode=textecode+chr(m)   
           ##point d'interogation non codé. 
               if ord(texte[i])== 63:
                  textecode=textecode+"?"    

           ##Codage des autres caracteres spéciaux (accent et autres..).
               if ord(texte[i])<=168 and ord(texte[i])>=148:
                  v=ord(texte[i])-148
                  k=a*v+b
                  y=k%21
                  m=y+65
                  textecode=textecode+chr(m)

           ##Affichage du texte codé.

           print("Texte codé :",textecode)

       else :
           print("Condtion d'entrée des cléfs de chiffrement non respctées")##Si les conditions des coefficients ne sont pas respectées, on averti l'utilisateur.

   if 1<=a<=25 and a%2!=0 and a!=13 and 0<=b<=25 : ##Verification des conditions des coefficients entrés par l'utilisateur

       g=input("Voulez vous enregistrer le texte codé ? (oui ou non) :")## demande si l'utilisateur veut enregistrer le texte codé
       
       if g=="oui":                    ##permet d'ouvrir le fichier en question et d'y ecrire le texte codé pour ensuite l'enregistrer dans un fichier .txt
          e=input("Dans quel fichier ?(ne rentrez pas l'extension .txt):")##demande le nom du fichier ou le texte codé sera enregistré
          fichier=open(e+".txt","w")
          fichier.write(textecode)
          fichier.close()
          print("Fait ! Merci d'avoir utilisé CRYPTOR 3000 !")
       if g=="non":
          print("Texte non enregistré. Merci d'avoir utilisé CRYPTOR 3000 !")

   else :
       print("")##ne rien afficher si les conditions des coefficients ne sont pas respectées


def TransfoListe():
    global text
    text=[]
    demande_fichier=input("Voulez vous ouvrir un fichier  (oui ou non) ?: ")
    ##Si l'utilisateur accepte d'ouvrir un fichier :
    if demande_fichier=="oui":
        t=input("lequel ?(doit se trouver dans le meme dossier que ce programme et n'oubliez pas de rajouter .txt): ")
        fichier = open(t, "r")## on place dans la variable "t" le nom du fichier

        fich=1
        while fich!="":
            fich=fichier.read(1)        
    
            text.append(fich)
    
    
    
        
    
    else :
        ## Demande à l'utilisateur de rentrer un texte
        x=input("Quel texte voulez vous coder ?")
    
    
        fichier=open("codage.txt","w")
        
        fichier.write(x)
        fichier.close()
        fich=open("codage.txt","r")
        while fichier!="":
            fichier=fich.read(1)        
            codage=open("codage.txt","a")
            text.append(fichier)
            codage.close()
    
    
        fich.close
    return text
    
    
def testcaracteres():
    global text
    global N
    
    x=(len(text))
    
    text.remove('')
    
    while (len(text)%N)!=0 :
        
        text.append(" ")
    
    return text
       

    
def codage():
    fichier=open("codage2.txt","w")
    fichier.close
    i=0
        
    L=int(((len(text))/N))
    
    
   
    for loop in range (N):
        for n in range (L):
            x=text[i+(n*N)]
            
            fichier=open("codage2.txt","a")
            fichier.write(x)
            fichier.close
            
        i=i+1                    
def lecture ():
    fichier=open("codage2.txt","r")
    l=fichier.read()
    print(l)
    fichier.close
    
    
def decodage():
    global N
    fichier=open("codage2.txt","w")
    fichier.close
    i=0
    
    
    L=int(((len(text))/N))
  
   
    for loop in range (L):
        
        for n in range (N):
            x=text[i+(n*L)]
            
            fichier=open("codage2.txt","a")
            fichier.write(x)
            fichier.close
            
        i=i+1
    
        

def choixCaesar():
    choix=input("decrypter ou crypter")
    ##print("3- pour une double securité")
    

    
    while choix != "crypter" and choix != "decrypter":
        print("recommencez")
        choix=input("recommencez je n'ais pas bien compris")
    if choix=="crypter":
       cryptage()
    else:
        decryptage()
    return choix
def cryptage():
    global N
    print("entrez la clef de cryptage:")
    N=int(input())
    
    
    TransfoListe()
    testcaracteres()
    codage()
    lecture()
    
def decryptage():
    global N
    print("entrez la clef de cryptage:")
    N=int(input())
    
    
    TransfoListe()
    testcaracteres()
    decodage()
    lecture()
def doublet():
    

    decodage()
    lecture()

def choixAffine():
    choix=input("decrypter ou crypter:")
    while choix !="crypter" and choix !="decrypter": 
        print("recommencez")
        choix=input("recommencez je n'ais pas bien compris")
    if choix=="crypter":
       cryptAffine()
    else:
        decryptAffine()


    
def choixVigenere():
    choix=input("decrypter ou crypter:")
    while choix !="crypter" and choix !="decrypter": 
        print("recommencez")
        choix=input("recommencez je n'ais pas bien compris")
    if choix=="crypter":
       cryptVigenere()
    else:
        decryptVigenere()
    


    
def demande():
    demandecrypt=input("Voulez vous crypter en Affine , Cesar ou Vigenere  ?:")
    print(demandecrypt)
    if demandecrypt=="affine" or demandecrypt=="Affine":
        choixAffine()
    elif demandecrypt=="cesar" or demandecrypt=="Cesar" or demandecrypt=="César" or demandecrypt=="césar":
        choixCaesar()
    elif demandecrypt=="vigenere" or demandecrypt=="Vigenère" or demandecrypt=="Vigenere" or demandecrypt=="vigenère":
        choixVigenere()
    return demandecrypt


demande()





