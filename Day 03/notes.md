# Python - Day 03

- Operators ||
- String methods
  - `count()`
  - `find()`
  - `index()`
- List
- List methods

## Shortcuts

- `Alt + ⬆️` ➡️ For moving lines
- `!<tab>` ➡️ Boiler plate
- `win + .` ➡️ emojis
- `ctrl +/` ➡️ comment
- `ctrl + <space>` ➡️ Auto complete
- `ctrl + d` ➡️ Multi cursor (Similar)
- `Hold Alt` ➡️ Multi cursor (Similar)
- `ctrl + ~ ` open and close terminal

## `fstring` - DX⬆️

---

- `{}`➡️ interpolation (substitution)
- `{}`➡️ expressions are alowed
- Auto converts
- Readable

```py
print(f"My age is {age}")
print(f"She has {2 * 1000} followers🎉")
```

> concatenate - **cannot mix** data _type_
>
> `str int ➡️❌

## References

- [Markdown cheat sheet](https://www.markdownguide.org/basic-syntax/#headings)
- [Table](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet#tables)

## Table/ Arithmetic operations

| Operator | Example  | Output |
| -------- | :------: | -----: |
| `//`     | `7 // 2` |      3 |
| `**`     | `7 ** 2` |     49 |
| `%`      | `7 % 2`  |      1 |

## Task Answers

- if variable is constant it must be in capital letters when naming it
- it is an indication to other developers
- "\*" is repeat operator in the REPL (Terminal)
- 20 \* "=" 20 times repeat "="
- exit REPL = "exit()" + enter

## Comparison Operators

- all comparison operators and logital operators return boolean (True or False)

## Logical Operators

- ## `and`
  - if any is `false` then output is `false`

| Operator          | Output  |
| ----------------- | :-----: |
| `True and True`   | `True`  |
| `True and False`  | `False` |
| `False and True`  | `False` |
| `False and False` | `False` |

- ## `or`

| Operator         | Output  |
| ---------------- | :-----: |
| `True or True`   | `True`  |
| `True or False`  | `True`  |
| `False or True`  | `True`  |
| `False or False` | `False` |

## `exercises in class`

```
>>> (3 < 4) and (10 >= 5)
True
>>> (5 != 10) or (800 < 5)
True
>>> ( (80 % 5) == 0) and ( (3 * 6) == 35)
False
>>> ( 7 > 5 ) and (4 != 4 ) or (3 <= 10)
True
>>>

```

- ## `not`

## Strings

- python supports negative indexes

## Chaining

- can only continue chain as long as it is a string
- strip() - returns string
- upper() - returns string
- lower() - returns string
- find()- returns int (only happens on string method)
- count() - returns int

## Lexical order

- dictionary way of looking
- looks at order of number
- 6> 349

## Conditions

- can only have one 'if' and one 'else' and as many 'elif'
- abs() always gives you positive value
