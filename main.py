from colorama import Fore, Style, Back
import os
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE

def screen_clear():
    _ = os.system('cls')

screen_clear()

print(f'''
                     {yl}              
 
                                                


███████╗███████╗ ██████╗ 
╚══███╔╝██╔════╝██╔═══██╗
  ███╔╝ █████╗  ██║   ██║
 ███╔╝  ██╔══╝  ██║   ██║
███████╗███████╗╚██████╔╝
╚══════╝╚══════╝ ╚═════╝ 

                                                            {red}    Zeo Version V1
                                                                {wh}          https://anonturkey.com
                                                                                                       
████████  ██████   ██████  ██      ███████ 
   ██    ██    ██ ██    ██ ██      ██      
   ██    ██    ██ ██    ██ ██      ███████ 
   ██    ██    ██ ██    ██ ██           ██ 
   ██     ██████   ██████  ███████ ███████ 
                                           
                                                                                                                                                                      
              {wh}Welcome to ZeO {red}hell{res}                                                                                             
                                                                                                      
                                                                                                     
                                                                                                                     
                             {gr}Active{res} {ble}Reverse{res}, {red} Private Tool{res}   
                                          
                                          
{red}[{yl}1{red}]:{res} REVERSE TOOLS                                 

                      
                                      {red}[{yl}13{red}]:{res} Check Updates..
''')

choice = input(f'{gr}Select Abuse{wh}/{red}Zeo> {gr}${res} ')

if choice == '1':
    os.system('python reverse.py')

if choice == '13':
    print(f'Please Contact {red}Zeo{res} For Updates.\n                   {ble}https://anonturkey.com/Zeo{res}')