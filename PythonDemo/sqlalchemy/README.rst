http://flask-sqlalchemy.pocoo.org

# pip install sqlalchemy

install mysql in centos7
# yum -y install mariadb mariadb-server mariadb-devel MySQL-python
# systemctl enable mariadb.service
# systemctl start mariadb.service
# mysql_secure_installation
# mysql -uroot -p
MariaDB [(none)]> CREATE DATABASE sqlalchemy;
MariaDB [(none)]> GRANT ALL PRIVILEGES ON sqlalchemy.* TO 'sqlalchemy'@'localhost' IDENTIFIED BY 'passw0rd';
MariaDB [(none)]> GRANT ALL PRIVILEGES ON sqlalchemy.* TO 'sqlalchemy'@'%' IDENTIFIED BY 'passw0rd';
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'passw0rd';
MariaDB [(none)]> FLUSH PRIVILEGES;

install sqlite3 in centos7
# yum -y install sqlite sqlite-devel
# sqlite3 sqlalchemy.db
sqlite>.help
sqlite>.tables
sqlite>.schema users

# neet to disable the iptables.service

test1.py
test2.py
test3.py


