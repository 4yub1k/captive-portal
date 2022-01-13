# captive-portal
Django based portal\
This is sample Login portal which logs the username and password. Modify as you requirement.

It is SQlite base, So just download and run. redirect user to your server.(Dnsmasq)\
**Installation :**
```
Linux:
    pip3 install django
    python3 manage.py runserver
Windows:
    pip install django
    python manage.py runserver
```
### Login Page :
<img src="https://user-images.githubusercontent.com/45902447/149328452-5cf3b882-c1f4-428e-8923-2c7a5decccd9.png" width="800" height="400">
<img src="https://user-images.githubusercontent.com/45902447/149328882-1d1bfdcf-ba07-40b8-b5d5-37908625fc27.png" width='800' height="400">

### User login page :
```
Default username : salah
        password : salah
http://127.0.0.1:8000/admin

To change host :
E:\Projects\captive-portal\portal\portal\settings.py
ALLOWED_HOSTS = ['127.0.0.1'] ---> ALLOWED_HOSTS = ['<host_ip>'] or ['*'] for all hosts
```
<img src="https://user-images.githubusercontent.com/45902447/149329161-88e0042e-716b-42fd-a84d-5c6e0f8dd461.png" width='400' height="300">

goto Login Data,

<img src="https://user-images.githubusercontent.com/45902447/149329615-8c915b89-b76e-404b-a0e4-647fce3d00d0.png" width='800' height="150">

Note : Copy the Source data of portal you want to copy to their respective places.

To modiy : Header and Footer
```
captive-portal\portal\templates\base.html
```
To modify : Body
```
captive-portal\portal\templates\pages\login.html
```

To modity : css
```
captive-portal\portal\portal\static\css\style.css
```