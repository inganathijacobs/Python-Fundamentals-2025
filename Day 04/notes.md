# Notes

- `Snake case is used in python`
- `if and elif statements return boolean`
- `positive over negative scenarios `

## `Refactoring`

- code quality improves, functionality remains the same
- less things can go wrong
- if something goes wrong, it is easier to find it

## Control followers

1. Decision tree
   1. `if ..else`
   2. `if..elif.. else`

## Loops

- Purpose: Simply repeating statements
- While true it will continue looping(infinite loop)

```py
i = 1

while i <= 3:
    print("Vote for Jevan")

```

```py
print("Vote for Jevan")
print("Vote for Jevan")
print("Vote for Jevan")
```

- Increment the i variable by 1 in order to end infinite loop and the printing will come to an end once it meets condition
- Executes statement until condition is false

```py

while i <= 3:
    print("Vote for Jevan")
    i = i + 1
```

## for loop

- it starts from 0
- range excludes last value(end)
  ```py
  for i in range(3):
    print(i)
  ```
- above will print (0,1,2)
- `RANGE IS LIKE THE SLICE METHOD`
- `range(start,end,step)`

```py
for i in range(1,11)
print(i)
```

- above will start from 1 to 10

## GIT

- U stands for Untracked

1. git init
2. Stage all
3. Provide message- Why?> What? (Explain why you did something)
4. When to commit
   1. Commit atleast 3 times in an hour
   2. Logical commit - Complete commit (no bugs)
   3. Small commit - Don't commit > 10 files
5. Sync to github(online)
