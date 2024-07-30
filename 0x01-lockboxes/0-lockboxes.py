#!/usr/bin/python3

'''
Prototype: def canUnloclAll(boxes)
@boxes: list of lists
A key with the same number as a box opens that box,
You can assume all keys will be +ve ints:
    there can be keys without boxes
The first box boxes[0] is unlocked
@Return: True if all boxes can be opened, else return false
'''


def canUnlockAll(boxes):
    # this is a method to determine if all boxes can be unlocked

    if not boxes:
        print('No boxes provided')
        return False

    # set to keep track of the collected keys
    keys = set(boxes[0])

    # set to keep track of the opened boxes
    # it is an index representing the position(key) the box
    open_boxes = set([0])  # the first box is open always

    while keys:
        # iterate through the boxes to gather more keys
        new_keys = set()

        # go through the collected keys: box indexes
        for key in keys:
            # check the length of the passed iterable: boxes
            # if the key exceeds the length, it is unreachable
            if key < len(boxes) and key not in open_boxes:
                # checks if key(box_index) is reachable and not yet recorded
                open_boxes.add(key)
                new_keys.update(boxes[key])  # update the set of new keys found

        # difference bwn sets, keys that are in new_keys not in keys
        if not new_keys - keys:
            # if no new boxes can be opened, break the loop
            break

        # update the list of keys found
        keys.update(new_keys)

    # check if the lenghth of opened boxes matches that of initial boxes
    return len(open_boxes) == len(boxes)  # return boolean, True or False
