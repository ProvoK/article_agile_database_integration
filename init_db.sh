createdb -h localhost -p 5432 -U foobar test
psql postgresql://foobar:thereisnosecure@localhost:5432/test -f init_db.sql
