import time

import winnotification

import dummywindow
import acronyms
import alarm
import dice
import exitApp
import oddoreven
import splitmail
import storygenerator
import passwordgenerator

func_dict = {}

###Finished example projects
func_dict[1] = dice.rolldice
func_dict[2] = oddoreven.oddoreven
func_dict[3] = acronyms.acronym
func_dict[4] = alarm.setAlarm
func_dict[5] = splitmail.splitMail
func_dict[6] = storygenerator.generatestory
func_dict[7] = passwordgenerator.generatePassword
func_dict[8] = dummywindow.dummyWindow
func_dict[9] = winnotification.createnotification

func_dict[99] = exitApp.exitapp


def mainMenu():
    command = input(f'>>> Main Menu: \n'
                    f'1. Roll the Dice \n'
                    f'2. Odd or Even \n'
                    f'3. Make Acronyms \n'
                    f'4. Set Alarm \n'
                    f'5. Split Mail \n'
                    f'6. Generate Random Story \n'
                    f'7. Generate Password \n'
                    f'8. Dummy Window \n'
                    f'9. WinNotification \n'
                    f'99. Exit \n')
    func_dict[111] = mainMenu

    func_dict[int(command)]()
    time.sleep(2)
    print(f'\n')
    func_dict[111]()


mainMenu()




#This is the link, where I'm doing this exercises.
#plus, some improvisation
# https://medium.com/coders-camp/60-python-projects-with-source-code-919cd8a6e512