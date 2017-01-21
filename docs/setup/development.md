### Development
- Clone project
```
git clone https://github.com/tsevindik/sis-back.git
```
- Install required packages
```
cd ./sis-back
sudo apt-get install $(grep -vE "^\s*#" setup/require/linux/common  | tr "\n" " ")
```
- Configure database
```
sudo -u postgres psql
CREATE DATABASE sisdb;
CREATE USER sis WITH PASSWORD '123456';
ALTER ROLE sis SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE sisdb TO sis;
\q
```
- Install virtual environment and configure it
```
sudo pip3 install virtualenvwrapper
nano ~/.bashrc
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc
mkvirtualenv sis
pip3 install -r ./setup/require/venv/local.txt
```
- Set environment variables
```
cp ./setup/env/local.env .env
nano .env
```
- Migrate and test if it works
```
python manage.py migrate
python manage.py test
```
- You can start developing now.
```
python manage.py runserver
```
