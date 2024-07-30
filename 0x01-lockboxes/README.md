# LOCK BOXES

## python data structures

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.


### Required: write a method to determine if all boxes can be opened

```py
    -   Prototype: def canUnloclAll(boxes)
    -   @boxes: list of lists
    -   A key with the same number as a box opens that box,
    -   You can assume all keys will be +ve ints:
            -   there can be keys without boxes
    - The first box boxes[0] is unlocked
    -   @Return: True if all boxes can be opened, else return false
```


## The Logic
1. Initialize a set for keys you have (starting with the keys in box 0).
2. Use a list to keep track of which boxes have been opened.
3. Iterate through boxes using the keys you collect, adding new keys to your set and marking boxes as opened.
4. Continue this process until no more new boxes can be opened.
5. Check if the number of opened boxes equals the total number of boxes.
