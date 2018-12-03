# Django Library Rest - Api
## Introduction
Applikasi ini menggunakan framework django python 3

## Setup for deployment local
1. Clone atau Fork terlebih dahulu repository git ini
2. Pastikan anda sudah menginstall python 3 dan sudah meng setup environment variable nya terlebih dahulu pada pc anda
3. install virtualenv 'pip install virtualenv'
4. bila sudah dilakukan langkah pada point 2 dan 3, selanjutnya mengaktifkan virtualenv pada root project
5. buka 'cmd' arahkan root ke project folder , lalu ketik '/myenv/Scripts/active'
6. setelah sukses maka anda sudah mengaktifkan virtualenv pada cmd anda dan itu berguna untuk menjalankan program ini sekaligus langkah development
7. lakukan migrasi data ke database anda
8. buka cmd ketik 'python manage.py makemigrations'
9. setelah itu ketik kembali di cmd 'python manage.py migrate'
10. buat super user terlebih dahulu ketik kembali di cmd 'python manage.py createsuperuser' dan lengkapi optional yang ada
11. buka cmd kembali dan ketik 'python manage.py runserver' <- command ini berarti anda menjalakan dengan port default yaitu '8000'
