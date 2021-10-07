import time

import acronyms
import alarm
import dice
import oddoreven
import exitApp




func_dict = {}

###Finished example projects
func_dict[1] = dice.rolldice
func_dict[2] = oddoreven.oddoreven
func_dict[3] = acronyms.acronym
func_dict[4] = alarm.setAlarm

func_dict[99] = exitApp.exitapp

def mainMenu():
    command = input(f'>>> Main Menu: \n 1. Roll the dice \n 2. Odd or Even \n 3. Make Acronyms \n 4. Set Alarm \n ')
    func_dict[111] = mainMenu

    func_dict[int(command)]()
    time.sleep(2)
    print(f'\n')
    func_dict[111]()


mainMenu()
















