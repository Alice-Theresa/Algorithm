
def quickSort(array):
    innerSort(array, 0, len(array) - 1)

def innerSort(array, left, right):
    middle = partition(array, left, right)
    if len(array) > 1:
        if left < middle - 1:
            innerSort(array, left, middle - 1)
        if right > middle:
            innerSort(array, middle, right)

def partition(array, left, right):
    i, j = left, right
    middle = (i + j) // 2
    guard = array[middle]
    while i <= j:
        while array[i] < guard:
            i += 1
        while array[j] > guard:
            j -= 1
        if i <= j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
            j -= 1
    return i


if __name__ == '__main__':
    array = [6, 2, 4, 3, 5, 1]
    quickSort(array)
    print(array)
    