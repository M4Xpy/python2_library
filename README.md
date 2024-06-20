# Library  service

Basic functionality of adding and accounting for books.
Search by authors, titles of works, or library clients.
You can follow the deadlines for returning reading materials.
View debtors' details to contact them.

## installation

Python2 must be already installed

```shell
git clone https://github.com/M4Xpy/python2_library
cd python2_library
virtualenv venv --python=python2.7
source venv/bin/activate
pip install requirements.txt
python library_system/manage.py runserver # starts Django project
```


# Run with docker

Docker should be installed

```shell
 sudo docker compose up --build
```


