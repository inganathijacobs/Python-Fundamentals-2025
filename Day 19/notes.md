## DML

- Data Manipulation Language

## DDL

- Data Definition Language

## Data Types

- ![alt text](image-2.png)
- `Char`- few letters (10) -> M or F
- `VARCHAR`- sentences(250)
- `Text`- paragraphs
- Date and DateTime
- Blob -> stores any binary data
- We don't store images or videos directly in the database
- It takes up space
- They are stored in D/ =C drive and then path is provided in the DB

## Table constraints

1. PRIMARY KEY
   1. unique identifier
   2. cannot be null value
   3. only one PK in a table
2. AUTOINCREMENT
3. UNIQUE
   1. null is allowed
   2. can have mutiple uniques
4. NOT NULL
5. CHECK(EXPRESSION) -> Check is age>18 for driving test
6. FOREIGN KEY
   ![alt text](image-3.png)

## CREATE TABLE

- SCHEMA/ BLUEPRINT

# DON'T USE "" IN SSMS!!!

## CAN'T USE IF NOT EXISTS

# LEARN MORE ABOUT SQL

- group by tsql -> choose Microsoft option (Learn Microsoft)
- https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver16
