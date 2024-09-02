http://localhost:8000 has the page serving static html content

The git url is at https://github.com/airmig/capstone-project-backend

The project uses the python mysql conector install
pip install mysql-connector-python

mysql settings are
        'ENGINE': 'mysql.connector.django',
        "NAME": 'reservations',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'admindjango',
        'PASSWORD': 'employee@123!'

menu api url
http://localhost:8000/api/menu-items/

booking api url
http://localhost:8000/api/booking/tables/

user registration
http://localhost:8000/auth/users/

user authentication
http://localhost:8000/auth/token/login

unit tests in the tests directory
