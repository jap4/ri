# -*- coding: utf-8 -*-
import os
import sys
import platform
import time
from xlpy import *
import base64

g = "\033[36;1m"
gt = "\033[0;36m"
bt = "\033[34;1m"
b = "\033[31;1m"
m = "\033[32;1m"
c = "\033[0m"
p = "\033[36;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

W = '\x1b[0m'
R = '\x1b[32m'
G = '\x1b[1;36m'
O = '\x1b[33m'
B = '\x1b[34m'
P = '\x1b[35m'
C = '\x1b[31m'
GR = '\x1b[36m'

def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
def lodprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7.0/90)

sugaldo=(gt+"""
()======================================()
 ###  #   #  ###   ###  #     ####   ###
#     #   # #     #   # #     #   # #   #
 ###  #   # # ### ##### #     #   # #   #
    # #   # #   # #   # #     #   # #   #
####   ###   #### #   # ##### ####   ###
()======================================()
""")
l="entenono jo.."

def main_menu():
    clear()
    slowprints(sugaldo)
    print(p+
        "     Tembak Xl    " +
        "\n  Menu:"
        "\n  [1] Pesen paket" + 
        "\n  [2] Njaluk Otp" +
        "\n  [3] utem"
    )
    choice = str(input(" ex:1👉 "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    lodprint(l)
    clear()
    print(sugaldo)
    print(p+"Tuku Paket")
    msisdn = str(input("ublem No 62xx 👉 "))
    clear()
    print(sugaldo)
    po = str(input(p+"ublemno Otp 👉 "))
    clear()
    print(sugaldo)
    print (p+" 1.Xtra Kuota 30GB/bln  11.9K")
    print (p+" 2.Xtra lite  3GB/bln   22.9K")
    print (p+" 3.Xtra lite  5GB/bln   32.9K")
    print (p+" 4.Xtra lite  9GB/bln   52.9K")
    print (p+" 5.Hot diskon 3gb/bln     30K")
    print (p+" 6.hot diskon 6gb/bln     50K")
    print (p+" 7.Combo Promo 6gb/bln    27K")
    print (p+" 8.Combo Promo 6gb/bln    31K")
    print (p+" 9.Combo Promo 6gb/bln    35K")
    print (p+" 10.Combo Promo 10gb/bln  41K")
    print (p+" 11.Combo Promo 10gb/bln  47K")
    print (p+" 12.Combo Promo 10gb/bln  53K")
    print (p+" 13.Combo Promo 20gb/bln  62K")
    print (p+" 14.Combo Promo 20gb/bln  71K")
    print (p+" 15.Combo Promo 30gb/bln  90K")
    print (p+" 16.Combo Promo 40gb/bln 103K")
    print (p+" 17.Waze & Chat 1hr       500")
    print (p+" 18.Waze & Chat 3hr        1K")
    print (p+" 19.Waze & Chat 7hr      2.5K")
    print (p+" 20.ComLite 3GB/bln     19.9K")
    print (p+" 21.ComLite 3.5GB/bln   22.9K")
    print (p+" 22.xtra 10GB/bln         59K")
    print (p+" 23.Tambah aktif/hr      Rp.1")
    print (p+" 24.Telepon 3 Hari       free")
    print (p+" 25.X-life 2gb/bln 1thn   60K")
    print (p+" 26.Fb unlimited/hari    free")
    print (p+" 27.Internet unli 1hr     500")
    print (p+" 28.Xtragram 5GB/3hr     free")
    print (p+" 29.VivoV9 10gb/bln        9K")
    print (p+" 30.XTRA YouTub 1GB/bln  free")
    print (p+" 31.Paket WA/hr           500")
    print (p+" 32.YU Khusus 15GB/bln     1K")
    print (p+" 33.Manual service id")
    pkt = str(input("Pilih nomer ae >> "))
    
    if pkt == '1':
        i = '8110671'
    elif pkt == '2':
        i = '8211010'
    elif pkt == '3':
        i = '8211011'
    elif pkt == '4':
        i = '8211012'
    elif pkt == '5':
        i = '8211108'
    elif pkt == '6':
        i = '8211109'
    elif pkt == '7':
        i = '8211472'
    elif pkt == '8':
        i = '8211477'
    elif pkt == '9':
        i = '8211482'
    elif pkt == '10':
        i = '8211473'
    elif pkt == '11':
        i = '8211478'
    elif pkt == '12':
        i = '8211483'
    elif pkt == '13':
        i = '8211474'
    elif pkt == '14':
        i = '8211479'
    elif pkt == '15':
        i = '8211475'
    elif pkt == '16':
        i = '8211480'
    elif pkt == '17':
        i = '8211369'
    elif pkt == '18':
        i = '8211370'
    elif pkt == '19':
        i = '8211371'
    elif pkt == '20':
        i = '8210882'
    elif pkt == '21':
        i = '8211121'
    elif pkt == '22':
        i = '8211183'
    elif pkt == '23':
        i = '1210026'
    elif pkt == '24':
        i = '8110490'
    elif pkt == '25':
        i = '8211034'
    elif pkt == '26':
        i = '8110529'
    elif pkt == '27':
        i = '8110528'
    elif pkt == '28':
        i = '8110624'
    elif pkt == '29':
        i = '8110619'
    elif pkt == '30':
        i = '8210949'
    elif pkt == '31':
        i = '8110531'
    elif pkt == '32':
        i = '8110649'
    elif pkt == '33':
        i = str(input("ublemno id nang 👉"))
    else:
        print("ganok pilihan")
    lodprint(l)
    serviceid = i
    xl = XL(msisdn)
    r = xl.loginWithOTP(po)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
        decision = str(input(p+"baleni opo gak [Y/N]? 👉 "))
        menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
        
def menu_2():
    lodprint(l)
    clear()
    print(sugaldo)
    print(p+"njaluk OTP")
    msisdn = str(input("ublem nomor 62xx👉"))
    lodprint(l)
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input(p+"baleni opo gak[Y/N]? 👉 "))
    menu_actions['main']() if(decision in ['N','n']) else menu_2()

def menu_4():
    clear()
    print("di delok sik")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqPassword()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['3']()
    return

def menu_3():
     lodprint(l)
     sys.exit()


def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
