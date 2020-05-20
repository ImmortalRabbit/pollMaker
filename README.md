# pollMaker
Задача: спроектировать и разработать API для системы опросов пользователей


Installation requirements
  python3.7
  Django2.2.10
  djangorestframework3.11.0

Installation guide
  `pip install -r requirements`
  `python manage.py makemigrations`
  `python manage.py migrate`
  `python manage.py runserver`
<br />
API guide<br />
  To get user token:<br />
    ```
    curl --location --request GET 'http://localhost:8000/api/login/' \
    --form 'username=admin' \
    --form 'password=admin'
    ```
  To create new poll:<br />
    ```
    curl --location --request POST 'http://localhost:8000/api/poll/create/' \
    --header 'Authorization: Token 74514e4ecccd9d86f40b501f125d5823ee8a43a4' \
    --form 'poll_name=poll_name' \
    --form 'pub_date=2020-04-20 00:01:46' \
    --form 'end_date=2020-04-25 00:01:46' \
    --form 'poll_description=poll_description'
    ```


  
