## Foreign key

- column that helps join two tables together
- is a primary key in another table
- repetition is allowed (cannot be unique)
- can be null

## Join

- if joining tables and some values don't have values then they will be equal to `null`

## syntax

- SELECT
- FROM tableA
- INNER JOIN tableB
- ON PK=FK

- specify table name when stating the PK and FK
- PK/FK line -> order does not matter
- .\* -> everything

## SQL

- `EACH` -> YOU MUST HAVE GROUP BY
- sample size matters -> choose higher sample size( amount of times something has happened)
- use aggregate functions with GROUP BY
- with no group by it will give you the answer for the entire table
