import time
import os


class User:

   username = ""
   password = ""
  
   @staticmethod
   def GirisBilgileriYazdır(username, password):
      print(f'Merhaba, {username}')
      print(f'Hesap Şifresi: {password}')
   
   @staticmethod
   def KayıtBilgisiYazdır(username, password):
      print("-----------------------------------")
      print("Hesabınız Başarıyla Oluşturuldu.")
      print("-----------------------------------")
      time.sleep(1,)
      print(f'Hesap Kullanıcı Adı: {username}')
      print(f'Giriş İçin Kullanılacak Hesap Şifresi: {password}')

@staticmethod
def clear():
    """
       konsol temizleme metodu
    """   
    if os.name == 'nt':
        _ = os.system('cls')    
    else:
        _ = os.system('clear')


 