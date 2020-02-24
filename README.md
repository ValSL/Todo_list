# Todo list

## Installation

Installed virtualenv required

Linux:
```angular2
virtualenv -p python3 .venv
source .venv/bin/activate
pip install requirements.txt
```

Windows:
```angular2
virtualenv env
```
To activate virtualenv on Windows, activate script is in the Scripts folder :
```
full\path\to\env\Scripts\activate.bat
pip install -r requirements.txt
```


## Run

For the first time don't forget:
```
python manage.py makemigrations
python manage.py migrate
```

```angular2
python manage.py runserver
```

## Features
You can sort entries by color, by clicking on the corresponding labels in the upper center of the site header.
