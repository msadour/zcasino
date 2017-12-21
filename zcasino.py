import os
import math
import random
from function_lib import *
import sys

if os.path.getsize('info_player') > 0:
    with open('info_player', 'rb') as file:
        my_depickler = pickle.Unpickler(file)
        users = my_depickler.load()
else:
    users = {}

player = input("veuillez saisir votre nom : ")
if player not in users.keys():
    print("Bonjour et bienvenue dans Zcasino. N'hesitez pas à lire les regle du jeu !")
    account_player = 50
else:
    account_player = users[player]
    account_player = int(account_player)
    print("Content de vous revoir " + player + ". Vous disposez de " + str(account_player) + "€ \n")

list_number_interval = [n for n in range(0,49)]

exit = False
while exit == False:
    good_number = random.randint(0,50)
    print("nombre gagnant : " + str(good_number))
    #We check if the number played is right
    number_is_right = False
    while number_is_right == False:
        number_played = input("Veuillez saisir un nombre sur lequel vous voulez pariez : ")
        number_played = check_choice_is_int(number_played)
        if number_played not in list_number_interval:
            print("Saisie du nombre incorrecte .. Veuillez saisir un nombre entre 0 et 49")
        else:
            number_is_right = True

    sum_good = False
    # We check if the sum played is right
    while sum_good == False:
        sum_bet = input("Veuillez saisir la somme que vous souhaitez parier : ")
        sum_bet = check_choice_is_int(sum_bet)
        if sum_bet > account_player:
             want_buy = input("Vous n'avez plus d'argent .. Voulez vous en racheter? (o/n)")
             if want_buy == "o":
                 how_many = input("Quel montant ? ")
                 how_many = check_choice_is_int(how_many)
                 account_player = account_player + how_many
             else:
                 print("Au revoir !")
                 users[player] = account_player
                 save_account(users)
                 sys.exit()
        elif sum_bet < 0 :
            print("Veuillez saisir une somme positive ..")
        else:
            sum_good = True

    if number_played == good_number:
        print(" \n Bravo, les nombres sont identiques !")
        sum_win = sum_bet * 3
        account_player = account_player + sum_win
    elif number_played % 2 == good_number % 2:
        print(" \n Bravo, les nombres sont de la meme couleur !")
        sum_win = sum_bet * 1.5
        account_player = account_player + math.ceil(sum_win)
    else:
        print(" \n perdu !")
        account_player = account_player - sum_bet

    print("Votre accompte est de " + str(account_player)+" \n")
    users[player] = account_player
    save_account(users)

    want_play_again = input("Voulez vous rejouer (o/n)? ")
    if want_play_again != 'o':
        exit = True