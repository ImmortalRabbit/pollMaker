# pollMaker
Задача: спроектировать и разработать API для системы опросов пользователей


Installation requirements
  python3.7
  Django2.2.10
  djangorestframework3.11.0
<br />
Installation guide
  `pip install -r requirements`
  `python manage.py makemigrations`
  `python manage.py migrate`
  `python manage.py runserver`
<br />
API guide<br />
<br />
<br />
  To get user token:<br /><br />
    ```
    curl --location --request GET 'http://localhost:8000/api/login/' \<br />
    --form 'username=admin' \<br />
    --form 'password=admin'
    ```
    <br />
    <br />
  To create new poll:<br /><br />
    ```
    curl --location --request POST 'http://localhost:8000/api/poll/create/' \<br />
    --header 'Authorization: Token 74514e4ecccd9d86f40b501f125d5823ee8a43a4' \<br />
    --form 'poll_name=poll_name' \<br />
    --form 'pub_date=2020-04-20 00:01:46' \<br />
    --form 'end_date=2020-04-25 00:01:46' \<br />
    --form 'poll_description=poll_description'<br />
    ```
<br />

  
