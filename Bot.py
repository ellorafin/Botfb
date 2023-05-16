GNU nano 7.2                                   bot.py
from fbthon import Facebook
from fbthon import Web_Login
import os
import time

print ("[CODED BY BGKE04]")
print ("[BOT AUTO KOMEN]")


print ("")



email = "example@gmail.com"  # Ganti email ini dengan email akun Facebook kamu
password = "example" # Ganti password ini dengan password Akun Facebook kamu
login = Web_Login(email,password)
cookie = login.get_cookie_str() #janagn ganti
fb = Facebook(cookie)
print ("SEDANG MENGIRIM KOMEMTAR")
print("")


post = fb.post_parser("LINK POSTIGAN")
post.send_comment("TEXT NYA")
print ("SUCCES")
print ("")
os.system("python bot.py")
