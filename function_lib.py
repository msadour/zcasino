import pickle

def save_account(u):
    with open('info_player', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(u)

def check_choice_is_int(num):
    """"
    Check if a input number is a number
    """
    is_int = False
    while is_int == False:
        try:
            num = int(num)
        except:
            num = input("Vous devez saisir un entier .. Veuillez reessayez : ")
        else:
            is_int = True
    return num