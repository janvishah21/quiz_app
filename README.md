# Quiz App
A simple quiz application using Django framework. You can add questions as admin and tell your friends/audience to answer them by visiting hosted url. It can be used by teachers to take test, by friends as fun app or for any other purpose.

## Dependencies
Python and Django are needed to be installed

`pip3 install django`

Versions used :

```
Python 3.6.9
Django 3.0.6
```

## Usage
Clone the repository, enter into the directory and run django server

```bash
git clone https://github.com/janvishah21/quiz_app.git
cd quiz_app
python3 manage.py runserver
```

Now, visit http://127.0.0.1:8000/home

## Login
New admin user can be created using 

```bash
python3 manage.py createsuperuser
```

As a admin, you need to add questions manually by visiting http://127.0.0.1:8000/admin and logging in. When hosted, users will visit given url, log/register in and will submit their answers.