# using set instead of adding dict (for keys) bc we are not counting
# how many times an element repeataed in the array.
# break the loop as soon as an element is found
def contains_duplicate(arr) -> bool:
    numSet = set()

    for num in arr:
        if num not in numSet:
            numSet.add(num)
        else:
            return True

    return False


if __name__ == "__main__":
    print(contains_duplicate([1,1,3,3,4,3,2,4,2]))