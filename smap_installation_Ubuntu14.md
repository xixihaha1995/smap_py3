# Files and Documentation

[Google Code Archive - Long-term storage for Google Code Project Hosting.](https://code.google.com/archive/p/smap-data/downloads)

git@github.com:SoftwareDefinedBuildings/smap.git

git@github.com:immesys/powerdb2.git

git@github.com:stevedh/readingdb.git

[sMAP: the Simple Measurement and Actuation Profile — sMAP 2.0 documentation (pythonhosted.org)](https://pythonhosted.org/Smap/en/2.0/index.html)

https://launchpad.net/~stevedh/+archive/ubuntu/smap/+packages

# Commands

```shell
find / -type d -name 'httpdocs'
find . -name "foo*"
sudo monit start readingdb
sudo monit start archiver
sudo lsof -i -P -n | grep LISTEN
chmod a+x [binaries]
```

# Usage
python manage.py runserver
curl http://localhost:8080/data/+ | jprint
http://localhost:8080/docs
# Procedures

## Ubuntu 20.04 -> Failed

```py
virtualenv venv --python=python2.7
```

 pip install smap

## Ubuntu 11.10 -> Cannot install this OS

docker pull lpenz/ubuntu-oneiric-amd64-minbase

[Index of /releases/11.10 (ubuntu.com)](http://old-releases.ubuntu.com/releases/11.10/)

# Ubutun 14.04

[Install Python 2.7.14 on Ubuntu 14.04 (github.com)](https://gist.github.com/pigeonflight/39e7513e46b419b8b51f8671445c4ea2)

```shell
sudo apt-get update
sudo apt-get install build-essential checkinstall -y
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y
cd /usr/src
sudo wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz
sudo tar -xvzf Python-2.7.14.tgz
cd Python-2.7.14
sudo ./configure --enable-optimizations
sudo make install
```



[How to Install Pip on Ubuntu 14.04 LTS - Liquid Web](https://www.liquidweb.com/kb/how-to-install-pip-on-ubuntu-14-04-lts/)

```shell
curl "https://bootstrap.pypa.io/pip/2.7/get-pip.py" -o "get-pip.py"
python get-pip.py
# /usr/bin/pip --pip1.5.4
# ~/.local/bin/pip --pip-20.3.4
alias pip_20='~/.local/bin/pip'
alias vir_20='~/.local/bin/virtualenv'
```



pip install virtualenv

virtualenv smap_env

pip install smap
To avoid this exception, use Avro v1.8.1

git clone git@github.com:xixihaha1995/sources.git

sudo apt-get install monit

```shell
#uncommented
set httpd port 2812 and
    use address localhost
    allow localhost
```

sudo /etc/init.d/monit restart

sudo apt update

sudo apt install software-properties-common

```
sudo add-apt-repository ppa:stevedh/smap
sudo apt-get update
sudo apt-get install readingdb readingdb-python

$ sudo monit reload
$ sudo monit start readingdb
```

```
apt-get install postgresql postgresql-contrib python-psycopg2

sudo systemctl start postgresql.service
```
```
root@box$ sudo su postgres
postgres@box$ psql
postgres=# CREATE USER archiver WITH PASSWORD 'password';
postgres=# CREATE DATABASE archiver WITH OWNER archiver;
postgres=# \q
postgres@box$ psql archiver
postgres=# CREATE EXTENSION hstore;
postgres=# \q
postgres@box$ exit

#sudo -u postgres psql
```

```
$ sudo apt-get install subversion python-django
$ sudo pip install avro python-dateutil django-piston
#avro==1.8.1 djago==1.3

sudo apt-get install python-psycopg2
pip install psycopg2-binary 
pip install httplib2
pip install numpy
# sql folder including psql scripts (from ScientifciBuildingSmap git)?
python manage.py syncdb

python manage.py createsuperuser
#lichen, wulicheneason@gmail.com, password
 python manage.py runserver
#/home/lichen/sources/powerdb2/templates/admin/login.html (File does not exist)
# cp from./smap_env/django/contrib/admin/templates/admin/
http://localhost:8000/
http://localhost:8000/admin/smap/subscription/add
```

```
added SoftwaredDefinedBuilding/smap
$ cd smap-data-read-only/python
$ sudo python setup.py install
$ sudo mkdir /etc/smap
$ sudo cp conf/archiver.ini /etc/smap
$ sudo cp monit/archiver /etc/monit/conf.d
$ monit reload
$ monit start archiver
```

# Archiver (MongoDB, Realtime serices db)
https://btrdb.readthedocs.io/en/latest/quick-start.html