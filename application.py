#On import les bibliotheques
from Tkinter import *
import time

#On prepare les variables que nous allons utiliser
appTitre = " ... "
appImage = " ... " #Dimension 600x250
appCouleur = " ... "
appFontCouleur = " ... "

#On cree la liste des membres de la famille
ma_famille = {
'...':'... \n...',
'...':'... \n...',
'...':'... \n...'
}

#On cree la page
fenetre = Tk()

#On prepare les fonctions que nous allons utiliser
def recherche():
    texte_saisie=barre_saisie.get() #Je recupere ce qu'il y a dans la barre de saisie
    texte_resultat.delete(0.0, END)
    try:
        membre = ma_famille[texte_saisie]
    except:
        membre =  texte_saisie + " ... "
    texte_resultat.insert(END, membre)

def quitter_fenetre():
    fenetre.quit()

#On donne un titre a la fenetre
fenetre.title(appTitre)
fenetre.configure(background=appCouleur)

#On met une photo en entete de l'application, l'image doit etre en gif ou ppm
photo = PhotoImage(file= appImage)

#On cree le cadre pour l'entete de notre application
Label(fenetre, image=photo, bg=appCouleur).grid(row=0, column=0, sticky = W)

#On cree un nouveau cadre pour notre application et on le place en dessous
Label(fenetre, text=" ... ", bg=appCouleur, fg=appFontCouleur, font= "none 12 bold").grid(row=0, column=0, sticky = W)

#On cree la bar de saisie pour l'utilisateur et on la place en dessous
barre_saisie= Entry(fenetre, width=20, bg="white")
barre_saisie.grid(row=2, column=0, sticky=W)

#On ajoute un bouton
Button(fenetre, text="Valider", width=6, command=recherche).grid(row=3, column=0, sticky=W)

#On cree un nouveau cadre pour notre application et on le place en dessous
Label(fenetre, text="Resulat :", bg=appCouleur, fg=appFontCouleur, font="none 12 bold").grid(row=4, column=0, sticky=W)

#On cree la boite pour le resultat de la recherche et on le place en dessous
texte_resultat = Text(fenetre, height=6, wrap=WORD, background="white")
texte_resultat.grid(row=5, column=0, columnspan=2, sticky=W)

#On cree un nouveau cadre pour quitter l'application
Label(fenetre, text="Cliquer pour quitter :", bg=appCouleur, fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

#On cree un bouton pour quitter l'application
Button(fenetre, text="Quitter", width=14, command=quitter_fenetre).grid(row=6, column=0, sticky=E)

#Lancement de la boucle
fenetre.mainloop()
