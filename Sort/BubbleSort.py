
def bubbleSort(array):
    hasSorted = False
    for i in range(len(array)):
        if hasSorted == True:
            return
        hasSorted = True
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                hasSorted = False

if __name__ == '__main__':
    array = [1, 2, 3, 5, 4]
    bubbleSort(array)
    print(array)