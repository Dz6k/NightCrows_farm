import win32con
import pygetwindow as gw
from threading import Thread 
from win32gui import SendMessage
from random import randint, choice
from mousekey import MouseKey
from time import sleep
import pyautogui

# variables

POSSIBILITIES = [2,
                 2.05,
                 2.10,
                 2.15,
                 2.20,
                 1.95,
                 2.25,
                 2.30,
                 2.5,
                 2.60,
                 2.75,
                 2.95,
                 3,
                 3.2,
                 3.5,
                 3.6]
contador = 0  

# pega o handle da janela 
def handle_of_windowtitle(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        return window._hWnd
    except IndexError:
        return None
  
#  funcao de iniciar farm  
def stealthfarm():
    
    mkey = MouseKey()
    mkey.enable_failsafekill('ctrl+e')
    # cria o handle da janela alvo
    hwnd =  handle_of_windowtitle("NIGHT CROWS(1)")
    
    #  envia input Q no hexadecimal 0x51
    SendMessage(hwnd, win32con.WM_KEYDOWN, 0x51 , 0)
    sleep(0.01)
    SendMessage(hwnd, win32con.WM_KEYUP, 0x51 , 0)
    sleep(0.2)

    
    while True:
        #  NECESSITA FAZER UMA CONFIGURACAO ANTES DENTRO DO JOGOw
        
        # abre o "procurador de mob"
        # enviar input U no hexadecimal 0x55 
        SendMessage(hwnd,win32con.WM_KEYDOWN, 0x55 , 0)
        sleep(0.01)
        SendMessage(hwnd,win32con.WM_KEYUP, 0x55 , 0)
        
        # laco para iterar sobre os alvos
        for i in range(randint(2,4)):
            #  enviar input TAB no hexadecimla 0x09
            SendMessage(hwnd,win32con.WM_KEYDOWN, 0x09 , 0)
            SendMessage(hwnd,win32con.WM_KEYUP, 0x09 , 0)
            sleep(0.2)
        
        sleep(choice(POSSIBILITIES))
    #  envia input Q no hexadecimal 0x51
    SendMessage(hwnd, win32con.WM_KEYDOWN, 0x51 , 0)
    sleep(0.01)
    SendMessage(hwnd, win32con.WM_KEYUP, 0x51 , 0)
    sleep(0.2) 
       
def main(): 
    global contador
    contador += 1
    if contador > 1:
        pyautogui.alert(title='Acao Bloqueada!',text='Voce ja inicou esta funcao')
    else:        
        # criando threads das funcoes    
        # thread que inica o script
        start_farm = Thread(target=stealthfarm)
        # inicia thread do script
        start_farm.start()
