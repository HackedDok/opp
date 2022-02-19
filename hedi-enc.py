# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: HEDI-GADER
import os, sys, py_compile, marshal, base64, zlib, time
from os import system
from time import sleep
try:
    import requests
except ImportError:
    print '\nModule Requests Not Installed'
    os.sys.exit()

def boyprint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.01)

logo = """
\033[1;32;40mdb   db d88888b d8888b. d888888b 
\033[1;37;40m88   88 88'     88  `8D   `88'   
\033[1;32;40m88ooo88 88ooooo 88   88    88    
\033[1;37;40m88~~~88 88~~~~~ 88   88    88    
\033[1;32;40m88   88 88.     88  .8D   .88.   
\033[1;37;40mYP   YP Y88888P Y8888D' Y888888P  
 
      \033[41m\033[1;37m Codded by  \033[41m\033[1;37mMr Hedi\x1b[0m                              
                                 
"""


def hedigader():
    system('clear')
    boyprint(logo)
    file = raw_input('\x1b[1;97mnexample > /sdcard/folder/file.py\n\nName File > ')
    
        file.write('"HediGader","HediGader","HediGader","HediGader",\n')

    file.write(')\n')
    file.close()


if __name__ == '__main__':
    hedigader()
