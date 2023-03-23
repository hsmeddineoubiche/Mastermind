import random 


lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def combinaison_aléatoire(N, NC):
	combinaison = ""
	for i in range(N):
		lettre=lettres[random.randint(0, NC-1)]
		combinaison = combinaison + lettre
	return combinaison

def combinaison_utilisateur(N, NC):
	utilisateur_combinaison = input("entrer votre combinaison:").upper().strip()
	while len(utilisateur_combinaison) != N:
		utilisateur_combinaison = input("entrer votre combinaison:").upper().strip()
	for i in utilisateur_combinaison:
			if lettres.index(i)>=NC:
				combinaison_utilisateur(N,NC)

	return utilisateur_combinaison


def bien_placées(comb_ordi, comb_joueur):
	bien_placé=0
	for i in comb_joueur:
		if comb_joueur.index(i) == comb_ordi.index(i):
			bien_placé=bien_placé+1
	return bien_placé


def jeu(N,NC,NT):
	co=combinaison_aléatoire(N,NC)
	cj=combinaison_utilisateur(N,NC)
	for i in range(NT):
		if co == cj:
			print("tu gagnez!")
			break
		else:
			print("le nombre de caractere juste est:"+str(bien_placées(co,cj)))
			cj=combinaison_utilisateur(N,NC)




print("les regle de jeu:")
N=int(input("N:"))
NC=int(input("NC:"))
NT=int(input("NT:"))
jeu(N,NC,NT)
