CREATE DATABASE blst;
CREATE USER blst WITH PASSWORD 'DaumGilgewurgI6';
ALTER ROLE blst SET client_encoding TO 'utf8';
ALTER ROLE blst SET default_transaction_isolation TO 'read committed';
ALTER ROLE blst SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE blst TO blst;
