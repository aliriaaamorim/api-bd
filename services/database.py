import pyodbc;

server = 'db-rds-aliria.ceck7eanir5p.us-east-1.rds.amazonaws.com'
port = '5432'
database = 'bdaliria'
username = 'postgres'
password = 'aliriards05'
cnxn = pyodbc.connect('DRIVER={PostgreSQL ANSI(x64)};'
                      'Server=db-rds-aliria.ceck7eanir5p.us-east-1.rds.amazonaws.com;'
                      'Port=5432;'
                      'Database=bdaliria;'
                      'User=postgres;'
                      'Password=aliriards05;'
                      'String Types=ANSI')
cursor = cnxn.cursor()