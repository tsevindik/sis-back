### Production
- Clone project
```
git clone https://github.com/tsevindik/sis-back.git
```
- Set locales
```
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
```
```
sudo locale-gen en_US.UTF-8
sudo dpkg-reconfigure locales
```
- Install required packages
```
cd ./sis-back
sudo apt-get install $(grep -vE "^\s*#" setup/require/linux/common  | tr "\n" " ")
sudo apt-get install $(grep -vE "^\s*#" setup/require/linux/production  | tr "\n" " ")
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
pip3 install -r ./setup/require/venv/production.txt
```
- Set environment variables
```
cp ./setup/env/production.env .env
nano .env
```
- Migrate and test if it works
```
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 config.wsgi:application
```
- Configure gunicorn and test it
```
cp ./setup/config/gunicorn.service /etc/systemd/system/
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service gunicorn status
```
- Configure nginx and test it
```
cp ./setup/config/nginx /etc/nginx/sites-available/sis
sudo ln -s /etc/nginx/sites-available/sis /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```
- And it is hopefully done.
