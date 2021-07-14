# create a virtual env
py -m venv jarra_env

# acrivate the virtual env
jarra_env\Scripts\activate.bat

# setup all packages
pip install -r requirements.txt

# create .env file : you need to type this command on the console
cp .example .env

# update .env file with your DATABASE credentials

# migrate the database
python manage.py migrate

# run the project
py manage.py runserver