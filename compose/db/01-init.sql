CREATE DATABASE blst;
CREATE USER blstuser WITH PASSWORD 'DaumGilgewurgI6';
ALTER ROLE blstuser SET client_encoding TO 'utf8';
ALTER ROLE blstuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE blstuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE blst TO blstuser;
