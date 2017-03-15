from random import randint
check = randint(0,9)

def check_nr():
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
        #check = randint(0,9)
        print (check)
        number = int(number)
        if number < check:
            print("Sisestatud number on väiksem, kui kontrollarv")
            check_nr()
        elif number > check:
            print("Sisestatud number on suurem, kui kontrollarv")
            check_nr()
        else:
            print("Palju õnne! Minge auhinnale järgi.")
    else:
        print("Numbrit taheti sa igavene tainas")
        check_nr()

check_nr()