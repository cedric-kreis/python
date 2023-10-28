# -*- coding: utf-8 -#
#-------------------------------------------------------------------------------
#
# Auteur        : Pirate Studio
#
# Programme     : CharToBin
#
# Fonctions     : Ce programme convertie les lettres de l'alphabète de la
#                 table ASCII en code binaire sur un octet.
#
#                 Si il y a plus de deux caractères ceux-ci sont séparé
#                 par un "-".
#
# Création      : 09.10.2021
# Modifié le    : 15.03.2021
# Version       : 1.1
#
#-------------------------------------------------------------------------------


#Déclaration de la variable pour contenir la lettre/chaîne de caractère entrée
z = ""
tc = ""

#Déclaration du caratère qui va séparé les octets
suffix = "-"

#Denande à l'utilisateur d'entrer un caractère ou d'un texte
print "Insérer une lettre ou une phrase :"
print ""
text = raw_input(" -> ")



#Boucle de conversion du caractère ou du texte en binaire
for i in range (0,len(text)):

  #La fonction "ord" permet de connaître l'emplacement du caractère
  #dans la table ASCII
  x = ord(text[i])

#converti les int en binaire
  if (x < 65) :
    y = bin(x)
    #Remplace les deux premier caratère pour supprimer le "b"
    x = y.replace('0b', '00' )
  else :
    y = bin(x)
    #Remplace le premier caratère pour supprimer le "b"
    x = y.replace('0b', '0' )

    #
    tc += x + suffix

    
    #Fonction "len" qui compte la longueur de "tc"
    var = len(tc)

    #Convertion de "tc" (string) en -> tc INT
    z = int(var)

    #Addition de l'octet + le suffix
    zz = z


#Supression du dernier caractère "-" avec "[:-1]"
myfinal = tc[:-1]

#Affichage de la variable my avec toutes les conditions implémentées en amont
print myfinal

#Opération pour afficher la longueur de la châine en supprimant le dernier
#caractère
print (zz - 1)
