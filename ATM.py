import os
import time

counter = 0  # Checks how many times the user has entered their pin start at zero

a_pin = 1965  # pin number
while counter < 3:  # this iterates over the counter variable
    pin = int(input('Please enter your pin number: '))
    counter += 1  # this is an incrementer

    if pin == a_pin:
        print(f'\nThat pin matched!\n')

    # This breaks when you enter the pin wrong 3 times without going to the next line
    else:
        print(f'Invalid pin, only 3 attemps, please try again!\n')
        print(f'You have {3-counter} attempts left')
        if counter < 3:
            continue
        else:
            print(f'Your account has been blocked...\n'.upper())
            break

    print(f'...Choose your preferred option below...\n\n (B) for balance\n (W) for withdrawal\n (C) for cancel')
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
        os.system('clear')
        quit()
