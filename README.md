# notifier to email

## Bu nima

Ushbu loiha topshirilgan taskni bajarish uchun yaratildi

## Qanday ishga tushirish mumkin ?

1. Kodlarni o'z mashinangizga yuklab olasiz:

  ```git clone https://github.com/anvarjamgirov/notifier.git```
  
2. Boshqa loihalaringizga halal bermaslik uchun **virtual environment** yaratib uni aktivlashtirasiz:

  ```
  virtualenv ven
  source ven/bin/activate
  ```
  
3. Kerakli dasturlarni **requirements.txt**ga asosan **pip** yordamida o'rnatamiz:

  ```pip3 install -r requirements.txt```
  
4. *notifier/settings.py* faylidagi **EMAIL_HOST_USER** va **EMAIL_HOST_PASSWORD** o'zgaruvchilariga kerakli qiymatlarni kiritamiz.

    *Bunda biriktirilayotgan gmail manzili uchun bazi to'g'irlashlarni amalga oshirish kerak:*
    
    **https://support.google.com/mail/answer/7126229?p=BadCredentials da ko'rsatilgan tartibda smtp orqali foydalanishni yoqish zarur.**
    **https://support.google.com/accounts/answer/6010255 da ko'rsatilganidek havfsizligi past bo'lgan dasturlardan foydalanishga ruxsat berish zarur.**
  
5. **migrations** va **migrate** larni amalga oshiramiz:

  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
  
6. Admin paneldan foydalanish uchun **superuser** yaratib olamiz:
 
  ```python3 manage.py createsuperuser```
    
7. Ishga tushiramiz:

  ```python3 manage.py runserver --noreload```
    
*Yuqorida ko'rsatilganlar amalga oshirilgach browserdan admin panelga kirib yangi user, bir qancha bo'lim hamda ularga mahsulotlar qo'shish lozim. Yaratilgan userga kerakli bo'limlar biriktirilgach har soatda uning email manziliga ushbu bo'limlarda mavjud mahsulotlar haqida ma'lumotlar yuborilib turiladi.*
