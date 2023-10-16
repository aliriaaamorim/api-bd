import psycopg2;

server = 'db-rds-aliria.ceck7eanir5p.us-east-1.rds.amazonaws.com'
port = '5432'
database = 'bdaliria'
username = 'postgres'
password = 'aliriards05'
cnxn = psycopg2.connect(dbname= "bdaliria", 
                        user= "postgres", 
                        password= "aliriards05", 
                        host= "db-rds-aliria.ceck7eanir5p.us-east-1.rds.amazonaws.com",
                        port="5432")
cursor = cnxn.cursor()