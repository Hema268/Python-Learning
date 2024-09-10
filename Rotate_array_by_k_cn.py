def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    while k:
        arr.append(arr[0])
        arr.pop(0)
        k -= 1
    return arr
