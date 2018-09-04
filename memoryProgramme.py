from tkinter import*
from random import*
import tkinter.messagebox


#On crée une fenêtre non redimensionnable avec une icone et on initialise les principales variables

fen=Tk()
fen.title("Memory")
fen.iconbitmap("iconeMem.ico")
fen.config(bg="LIGHTBLUE")
fen.resizable(width=False,height=False)


cX,cY=1000,750

listeXC,listeYC,listeImg=[],[],[]
matMem=[[]]
imgPre,xPre,yPre,effX1,effY1,effX2,effY2=None,None,None,None,None,None,None
compteur,caseTrouv=0,0
carteRetournee,reini,partieLancer,nvRecord=False,False,False,False
varTaille,varTheme = IntVar(),IntVar()

#Fonction initialisant une matrice vide

def initMatVide(nbLigne,nbColonne):
    matriceVide=[None]*nbLigne
    for i in range(nbLigne):
        matriceVide[i]=[None]*nbColonne
    return matriceVide

#On crée une matrice de la taille du plateau du memory, contenant les noms des images en chaque case

def creaMatMem(nbLigne,nbColonne):
    global matMem
    listeNbAlea=[]
                
    theme=varTheme.get()
    
    for i in range(int((nbLigne*nbColonne)/2)):
        listeNbAlea+=[i+theme+1]*2
    
    shuffle(listeNbAlea)
        
    matMem=initMatVide(nbLigne,nbColonne)
    k=0
    
    for j in range(nbColonne):
        for i in range(nbLigne):
            matMem[i][j]=str(listeNbAlea[k])+".gif"
            k+=1
            
#On calcule la position du centre de chaque case du memory, en fonction du nombre de lignes et de la taille du canvas contenant les cases

def positionCentre(cX,cY,nbLigne,nbColonne):
    global listeXC,listeYC

    for i in range (nbLigne):
        listeYC+=[cY/nbLigne*i+cY/(2*nbLigne)+2]
    for j in range (nbColonne):
        listeXC+=[cX/nbColonne*j+cX/(2*nbColonne)+2]
    
#On retourne la case sur laquelle on vient de cliquer, et si une autre a été retournée avant on regarde si elles sont identiques
#Si elles ne le sont pas, au prochain clic la case se retournera à nouveau
#Sinon, les deux cases restent côté face
#Lorsque toutes les cases ont été retournées, la partie est finie. Si on a réussi en moins de coups que le record enregistré, notre record est sauvegardé

def ouvrirImage(posiX,posiY):
    global compteur,listeImg,xPre,yPre,carteRetournee,imgPre,caseTrouv,reini,effX1,effY1,effX2,effY2,imageInt,varTaille,nvRecord
    
    if ((posiX!=xPre or posiY!=yPre) and (matMem[posiY-1][posiX-1]!=None)): 

        if reini==True:
            
            cv.create_image(listeXC[effX1-1],listeYC[effY1-1],image=imageInt)   
            cv.create_image(listeXC[effX2-1],listeYC[effY2-1],image=imageInt)
                
            xPre,yPre=None,None
            reini=False
            


        if (carteRetournee==False):
            carteRetournee=True

            imageCase=PhotoImage(file=matMem[posiY-1][posiX-1])
            listeImg+=[imageCase]
            
            cv.create_image(listeXC[posiX-1],listeYC[posiY-1],image=listeImg[compteur])

            imgPre=matMem[posiY-1][posiX-1]
            xPre,yPre=posiX,posiY
            compteur+=1


        elif (carteRetournee==True):
            carteRetournee=False
                
            imageCase=PhotoImage(file=matMem[posiY-1][posiX-1])
            listeImg+=[imageCase]

            cv.create_image(listeXC[posiX-1],listeYC[posiY-1],image=listeImg[compteur])

            compteur+=1
                            

            if (int(compteur/2)<2):
                    nbActSco1.configure(text=str(int(compteur/2))+" coup")
            else:
                    nbActSco1.configure(text=str(int(compteur/2))+" coups")
                    

        
            if (matMem[posiY-1][posiX-1]!=imgPre):
                reini=True
                effX1,effX2,effY1,effY2=posiX,xPre,posiY,yPre



            elif (matMem[posiY-1][posiX-1]==imgPre):

                matMem[posiY-1][posiX-1],matMem[yPre-1][xPre-1]=None,None
                
                caseTrouv+=2

                if (caseTrouv==len(matMem[0])*len(matMem)):

                    taille=varTaille.get()

                    scoreAct=int(compteur/2)

                    fichier = open("saveScore.txt", "r")

                    scores=str(fichier.read())

                    listeScores=[]


                    for i in range(len(scores)):
                        listeScores+=[int(scores[i])]
                        

                    
                    if taille==0:
                        scoreMax=int(scores[0]+scores[1])
                        

                        if scoreAct<scoreMax:
                            

                            scoreAct=str(scoreAct)

                            listeScores[0],listeScores[1]=int(scoreAct[0]),int(scoreAct[1])


                            chaineScore=""

                            for i in range(len(listeScores)):
                                chaineScore+=str(listeScores[i])
                            
                            fichier=open("saveScore.txt","w")

                            

                            fichier.write(str(chaineScore))

                            fichier.close()

                            record1.configure(text="4*4 : "+scoreAct+" coups")

                            nvRecord=True



                    elif taille==1:
                        scoreMax=int(scores[2]+scores[3])

                        if scoreAct<scoreMax:

                            scoreAct=str(scoreAct)

                            listeScores[2],listeScores[3]=int(scoreAct[0]),int(scoreAct[1])


                            chaineScore=""

                            for i in range(len(listeScores)):
                                chaineScore+=str(listeScores[i])
                            
                            fichier=open("saveScore.txt","w")


                            fichier.write(str(chaineScore))

                            fichier.close()

                            record2.configure(text="4*6 : "+scoreAct+" coups")

                            nvRecord=True

                    elif taille==2:
                        scoreMax=int(scores[4]+scores[5])

                        if scoreAct<scoreMax:

                            scoreAct=str(scoreAct)

                            listeScores[4],listeScores[5]=int(scoreAct[0]),int(scoreAct[1])


                            chaineScore=""

                            for i in range(len(listeScores)):
                                chaineScore+=str(listeScores[i])
                            
                            fichier=open("saveScore.txt","w")

                            fichier.write(str(chaineScore))

                            fichier.close()

                            record3.configure(text="6*6 : "+scoreAct+" coups")

                            nvRecord=True

                   
                    if nvRecord==False:
                        tkinter.messagebox.showinfo("","Vous avez gagné en "+str(scoreAct)+" coups! \n Relancez une partie afin de tenter de battre votre record!")
                    elif nvRecord==True:
                        tkinter.messagebox.showinfo("","Félicitation, vous avez gagné en "+str(scoreAct)+" coups et avez battu votre record! \n Si vous voulez rejouer, relancez une partie!")


#On détecte les clics de souris sur le canvas, et on applique la fonction ouvrir image à la case sur laquelle on vient de cliquer

def coord(event):
    global imageTest2,partieLancer,cX,cY
    
    if (partieLancer==True):
        x,y=event.x,event.y

        
        (o,p)=int(x/(cX/nbColonne))+1,int(y/(cY/nbLigne))+1
        imageTest2=ouvrirImage(o,p)

#On place les cases côté pile sur le plateau        

def initialiserCentre(listeXCentre,listeYCentre):
    global imageInt
    for i in range (nbLigne):
        for j in range (nbColonne):
            cv.create_image(listeXC[j],listeYC[i],image=imageInt)

#On initialise le canvas, on le raccorde à l'évènement "clic bouton gauche" et on importe les images de point d'interrogation et celle d'accueil          

imageAc=PhotoImage(file="imageAc.gif",width=1084,height=748)                     
cv=Canvas(fen,width=cX,height=cY-5,background="LIGHTBLUE")
cv.create_image((cX/2),(cY/2),image=imageAc)
cv.bind("<Button-1>",coord)
cv.pack(side=LEFT)


imageInt1=PhotoImage(file="pointInt1.gif")
imageInt2=PhotoImage(file="pointInt2.gif")
imageInt3=PhotoImage(file="pointInt3.gif")

#On lance une partie, en réinitialisant les variables et en affichant le bon thème et le bon nombre de cases

def lancer():
    
    global partieLancer,nbLigne,nbColonne,cX,cY,matMem,cv,listeXC,listeYC,compteur,caseTrouv,listeImg,imgPre,xPre,yPre,effX1,effY1,effX2,effY2,carteRetournee,reini,partieLancer,imageInt,nvRecord

    taille,theme=varTaille.get(),varTheme.get()

    if theme==0:
        imageInt=imageInt1
    elif theme==15:
        imageInt=imageInt2
    elif theme==30:
        imageInt=imageInt3

    listeXC,listeYC,listeImg=[],[],[]
    imgPre,xPre,yPre,effX1,effY1,effX2,effY2=None,None,None,None,None,None,None
    compteur,caseTrouv=0,0
    carteRetournee,reini,partieLancer,nvRecord=False,False,False,False
    nbActSco1.configure(text="0 coup")


    if (taille==0):
        nbLigne,nbColonne=4,4
        cX,cY=720,576
        
    elif (taille==1):
        nbLigne,nbColonne=4,6    
        cX,cY=1080,576    
        
    elif (taille==2):
        nbLigne,nbColonne=5,6
        cX,cY=1080,720

    cv.config(width=cX,height=cY)   

    partieLancer=True

    creaMatMem(nbLigne,nbColonne)
    positionCentre(cX,cY,nbLigne,nbColonne)
    initialiserCentre(listeXC,listeYC)

        
#On initialise les widgets

police=('Showcard gothic', 13, 'bold')

espace1= Label(fen,bg="LIGHTBLUE")
espace2= Label(fen,bg="LIGHTBLUE")

tailleQ = Label(fen,text="Quel format de jeu \n souhaitez-vous ?",font=police,bg="LIGHTBLUE")
btTaille1=Radiobutton(fen, variable=varTaille, text="4*4", value=0,font=police,bg="LIGHTBLUE")
btTaille2=Radiobutton(fen, variable=varTaille, text="4*6", value=1,font=police,bg="LIGHTBLUE")
btTaille3=Radiobutton(fen, variable=varTaille, text="5*6", value=2,font=police,bg="LIGHTBLUE")

themeQ = Label(fen,text="Quel thème \n voulez-vous ?",font=police,bg="LIGHTBLUE")
btTheme1=Radiobutton(fen, variable=varTheme, text="Grèce Antique", value=0,font=police,bg="LIGHTBLUE")
btTheme2=Radiobutton(fen, variable=varTheme, text="Moyen Âge", value=15,font=police,bg="LIGHTBLUE")
btTheme3=Radiobutton(fen, variable=varTheme, text="Espace", value=30,font=police,bg="LIGHTBLUE")

nbActSco0 = Label(fen,text="Votre nombre de coup(s) \n actuel est :",font=police,bg="LIGHTBLUE")
nbActSco1 = Label(fen,text="0 coup",font=police,bg="LIGHTBLUE")

record0 = Label(fen,text="Records actuels du nombre \n minimum de coups:",font=police,bg="LIGHTBLUE")
fichier = open("saveScore.txt", "r")
scores=str(fichier.read())
record1 = Label(fen,text="4*4 : "+scores[0]+scores[1]+" coups",font=police,bg="LIGHTBLUE")
record2 = Label(fen,text="4*6 : "+scores[2]+scores[3]+" coups",font=police,bg="LIGHTBLUE")
record3 = Label(fen,text="5*6 : "+scores[4]+scores[5]+" coups",font=police,bg="LIGHTBLUE")

boutonLancer = Button(fen,text="Lancer une \n nouvelle partie!",command=lancer,font=police,bg="BLUE",fg="White")

#On place les widgets

tailleQ.pack(side=TOP)
btTaille1.pack(side=TOP)
btTaille2.pack(side=TOP)
btTaille3.pack(side=TOP)
espace1.pack(side=TOP)
themeQ.pack(side=TOP)
btTheme1.pack(side=TOP)
btTheme2.pack(side=TOP)
btTheme3.pack(side=TOP)
espace2.pack(side=TOP)
nbActSco0.pack(side=TOP)
nbActSco1.pack(side=TOP)
record0.pack(side=TOP)
record1.pack(side=TOP)
record2.pack(side=TOP)
record3.pack(side=TOP)
boutonLancer.pack(side=TOP)

fen.mainloop()
