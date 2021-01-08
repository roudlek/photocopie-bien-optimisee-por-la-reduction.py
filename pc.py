while True :
    Nbp = int(input("entrer le nombre des pages : ")) # saisis de nobre de pages
    if Nbp <= 10 and Nbp > 0 :
        Facture = 0.5 * Nbp
        print("La facture est",Facture)    
    elif Nbp > 10 and Nbp < 20 :                      # pour eviter qu'un personne imprime plus de 10 juste pour avoir la reduction qui est entre 11 et 19, on applique premierement la reduction
        Facture = 5 + 0.5 * (Nbp - 10) * 0.7          # de 1 a 10 cad, 5 dh + l'application de reduction de 30 % + les nombres de pages apres 10 pages
        print("La facture est",Facture)
    elif Nbp >= 20 :
        Facture = 5 + 3.15 + 0.5 * (Nbp - 19) * 0.4   # meme chose pour nombres ajoute 5 dh + reduction de 30 % de 11 iemes pages a la 19 pages qui est egale a 3.15 dh + les autres page debutant par 20 jusqua +linfinie
        print("La facture est",Facture)
    else:
        print("Le nombre saisis est incorrect !!")
