'''
Functionality in play sound after performing a command or activity in terminal.
You can set alias for this script in this way:(write in your shell startup script)
alias beep="python ~/say_beep.py" ,and call it `beep` or `&& beep` or `beep <number>` -> 1-7
Author: github.com/rezarezaeedev
1: Won
2: Bot
3: alarm -> default
4: Served
5: Reward
6: New level
7: Screaming

'''
import os, sys
try:
    import beepy 
except ImportError:
    answer=input('Cant import beepy module. if you want install it enter (Y) else any key')
    if answer=="Y":
        os.system('pip install beepy')
        print('\n\nInstallition complete to using.')
default_sound=3
try:
    sound =int (sys.argv[1]) if len(sys.argv)>1 else default_sound
    if sound < 0 or sound > 7:
        raise ValueError("Number not between 1-7")
except ValueError as error:
    sound = default_sound

beepy.beep(sound)



