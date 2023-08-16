#import os
#import time
#import sys
#import subprocess
import os, time, colorama
from colorama import Fore, Back, Style # here is where we're calling colour function

colorama.init(autoreset=True)

def ATM(): # start of the main function

    os.system('cls') # clear screen before running codes below
    
    lock = 0

    while True: # Exception handling starts here (this won't allow error being thrown on the screen, as users may enter wrong charactor or press enter alone)
        try: # Everything within this will run first

            while lock < 3:
                lock += 1 # this is an incrementer

                counter = 0  # Checks how many times the user has entered their pin start at zero

                a_pin = 1000  # pin number
                while counter < 3:  # this iterates over the counter variable
                    pin = int(input('\nPlease enter your pin number: '))
                    counter += 1  # this is an incrementer

                    if pin == a_pin: 
                        print(f'\nThat pin matched!\n')

                    # This breaks when you enter the pin wrong 3 times without going to the next line
                    else:
                        print(f'Invalid pin, only 3 attemps, please try again!\n')
                        print(f'You have {3-counter} attempts left...') # this counts backward from 2-0 
                        time.sleep(1) # sleep for 1 second before each iteration
                        os.system('cls') 
                        if counter < 3:
                            continue
                        else:
                            
                            if lock == 1: # execute this if password is entered wrong first time
                                print(Fore.RED + '\n\t-------------------------- ---------------------------------')
                                print(Fore.GREEN + '\t    Your account is temporarely blocked for 20 seconds!'.upper())
                                print(Fore.RED + '\t-----------------------------------------------------------\n')

                                time.sleep(20)
                                continue

                            elif lock == 2: # execute this if password is entered wrong second time               
                                print(Fore.RED + '\n\t-----------------------------------------------------------')
                                print(Fore.GREEN + '\t    Your account is temporarely blocked for 30 seconds!'.upper())
                                print(Fore.RED + '\t-----------------------------------------------------------\n')

                                time.sleep(30)
                                continue

                            else: # execute this if password is entered wrong third time               
                                print(Fore.RED + '\n\t-----------------------------------------------------------')
                                print(Fore.GREEN + '\t   Your account is blocked, contact your administrator'.upper())
                                print(Fore.RED + '\t-----------------------------------------------------------\n')
                                time.sleep(5)
                                os.system('cls')
                                #subprocess.run("exit 1", shell=True, check=True)
                                break

                    print(Fore.BLUE + '...Choose your preferred option below...\n\n (B) for balance\n (W) for withdrawal\n (C) for cancel'.upper())
                    view = input('\nYour option please: ').lower()
                    

                    if view == 'b':
                        with open('New.txt', 'r') as f:
                            a = str(f.read())
                            print(f'\nCurrent balance: ' + '£' + a + '\n\nTo deposit select option (D)\n')

                            balance = input('Your option please: ').lower()
                            if balance == 'd':

                                # Read from the file and extract the current balance here
                                with open('New.txt', 'r') as f:
                                    current_balance = float(f.read())

                                    # Enter the amount to be deposited here
                                    deposit = float(input(f'Enter the amount to deposit here: '))

                                    # Now let us work out the new balance including the deposited amount here
                                    new_balance = float(current_balance) + deposit

                                # Now we write our new balance to our file for storage here
                                # Open the file here
                                with open('New.txt', 'w') as f:
                                    # Now write to the file here with the new balance here
                                    f.write(str(new_balance))

                                    print(f'\nYou have deposited: ' + '£' + str(deposit) + '\nYou balance is now: ' + '£' + str(new_balance))
                                    quit()
                            else:
                                break

                    if view == 'w':
                        # Read from the file and extract the current balance here
                        with open('New.txt', 'r') as f:
                            current_balance = float(f.read())
                            print(f'\nCurrent balance: £{current_balance}')

                            # Enter amount to deposit here
                            with_drawal = float(input('How much would you like to withdrawal? '))

                            # Now let us work out the new balance including the amount to be withdrawn here
                            new_balance = float(current_balance) - with_drawal

                            # Now we write our new balance to our file for storage here
                            # Open the file here
                            with open('New.txt', 'w') as f:
                                f.write(str(new_balance))

                                print(f'\nYou have withdrawn: ' + '£' + str(with_drawal) + '\nYour account balance is now: ' + '£' + str(new_balance))
                                quit()

                    if view == 'c':
                        print(f'\nCancelling...')

                        # hold on for 3 seconds, clear the screen and exit
                        time.sleep(3)
                        os.system('cls')
                        quit()

            break # this will run if the user enters a disallowed character or presses enter instead
        except ValueError: # if the "try" section breaks the exception section will run to prevent the error being thrown the screen 
            print(f'Oops.. Try again!')

ATM()
