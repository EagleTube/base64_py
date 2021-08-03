import base64
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init()

msg_error = [Fore.RED+"No Input",Fore.RED+"No Input detected!\n--h/help for help",
             Fore.LIGHTYELLOW_EX+'-----Usage-----\n-e/Encode for base64 Encode, \n-d/Decode for base64 Decode, \n-O/outfile for File Ouput, \n--h for help\n\nEg : ecdc.py -e "hello world" -o hell.txt\nEg : ecdc.py -d "Q2FpIGdpbGE=" -o hell.txt\n',
             "\n\n\t\t########################\n\t\t    Encode n Decode\n\t\t  Created by Eagle Eye\n\t\t########################\n",
             Fore.RED+"Not base64 string"]

def checkArr3():
    if len(sys.argv) >= 5:
        return True
    else:
        return False
def checkArgs():
    if len(sys.argv) < 2:
        sys.exit(msg_error[3])

def checkInput():
    if len(sys.argv) >= 3:
        return True
    else:
        return False


def base64stringencode(input):
    if len(input) >= 4:
        encoded = base64.b64encode(input.encode('ascii')).decode('utf-8') 
        return encoded
    else:
        sys.exit(msg_error[4])

def base64stringdecode(input):
    if len(input) > 4:
        decoded = base64.b64decode(sys.argv[2]).decode('utf-8') 
        return decoded
    else:
        sys.exit(msg_error[4])

def outFile(input1,input2):
    file = open(input1,'a')
    file.write(input2+'\n')
    file.close()

checkArgs()

if checkArr3() and checkInput() and sys.argv[3].upper()=='-O' and len(sys.argv)==5:
        if sys.argv[1].upper()=='-D' or sys.argv[1].lower()=='-decode':
            dec = base64stringdecode(sys.argv[2])
            outFile(sys.argv[4],dec)

        elif sys.argv[1].upper()=='-E' or sys.argv[1].lower()=='-encode':
            enc = base64stringencode(sys.argv[2])
            outFile(sys.argv[4],enc)

        elif sys.argv[1].upper()=='--H' or sys.argv[1].lower()=='-help':
            print(msg_error[2])

        else:
            print(msg_error[1])

else:
        if len(sys.argv) >= 1 and checkInput() and sys.argv[1].upper()=='-D' or sys.argv[1].lower()=='-decode':
            dec = base64stringdecode(sys.argv[2])
            print("Base64 Decoded String : "+Fore.GREEN+dec)
        elif len(sys.argv) >= 1 and checkInput() and sys.argv[1].upper()=='-E' or sys.argv[1].lower()=='-encode':
            enc = base64stringencode(sys.argv[2])
            print("Base64 Encoded String : "+Fore.GREEN+enc)
        elif len(sys.argv) >= 1 and sys.argv[1].upper()=='--H' or sys.argv[1].lower()=='-help':
            print(msg_error[3])
            print(msg_error[2])
        else:
            print(msg_error[1])
