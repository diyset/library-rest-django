# Django Library Rest - Api
## Introduction
Applikasi ini menggunakan framework django python 3

## Collection API Postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/collections/a51463bc080b7e30f6cd)
## Setup for deployment local
1. Clone atau Fork terlebih dahulu repository git ini
2. Pastikan anda sudah menginstall python 3 dan sudah meng setup environment variable nya terlebih dahulu pada pc anda
3. install virtualenv `pip install virtualenv`
4. buat environment anda dengan perintah `virutalenv [nama env]`
5. bila sudah dilakukan langkah pada point 2 dan 3, selanjutnya mengaktifkan virtualenv pada root project
6. buka 'cmd' arahkan root ke project folder , lalu ketik `/[nama env]/Scripts/active`, karena saya sudah menambahkan environment saya yang beranama `myenv` bisa juga menggunakan ini
7. jalankan perintah `cmd` dengan command `pip install -r requirements.txt`
8. setelah sukses maka anda sudah menginstall semua library depdencies yang dibutuhkan
9. setelah itu lakukan migrasi data ke database anda
10. karena default saya menggunakan `sqlite3` dan jika anda ingin menggunakan database lain bisa kunjungi ini untuk lebih jelasnya  [DJango Doc Database](https://docs.djangoproject.com/en/2.1/ref/databases/)
10. buka cmd ketik `python manage.py makemigrations`
11. setelah itu ketik kembali di cmd `python manage.py migrate`
12. buat super user terlebih dahulu ketik kembali di cmd `python manage.py createsuperuser` dan lengkapi optional yang ada
13. buka cmd kembali dan ketik `python manage.py runserver` <- command ini berarti anda menjalakan dengan port default yaitu '8000'


## List Depedencies Pyip
1. certifi==2018.11.29
2. chardet==3.0.4
3. colorama==0.4.1
4. defusedxml==0.5.0
5. Django==2.1.3
6. django-braces==1.13.0
7. django-filter==2.0.0
8. django-oauth-toolkit==1.2.0
9. django-oauth2-provider==0.2.6.1
10. django-rest-framework-social-oauth2==1.1.0
11. djangorestframework==3.9.0
12. httpie==1.0.2
13. idna==2.7
14. oauthlib==2.1.0
15. Pygments==2.3.0
16. PyJWT==1.7.0
17. python3-openid==3.1.0
18. pytz==2018.7
19. requests==2.20.1
20. requests-oauthlib==1.0.0
21. shortuuid==0.5.0
22. six==1.11.0
23. social-auth-app-django==3.1.0
24. social-auth-core==2.0.0
25. urllib3==1.24.1
