
def radixSort(array):
    radix = 10
    length = len(array)
    temp = [0] * radix
    digitLength = max(list(map(lambda x: len(str(x)), array)))
    for r in range(digitLength):

        #每一轮生成一个基数数组
        count = [0] * (radix + 1)

        #为基数数组计数
        for i in range(length):
            count[digitAt(array[i], r) + 1] += 1

        #基数数组累加
        for i in range(radix):
            count[i + 1] += count[i]

        #填入临时数组
        for i in range(length):
            temp[count[digitAt(array[i], r)]] = array[i]
            count[digitAt(array[i], r)] += 1

        #覆盖原数组
        for i in range(length):
            array[i] = temp[i]

def digitAt(value, index):
    return int(value / pow(10, index) % 10)

if __name__ == '__main__':
    array = [1412, 5, 3, 12, 1]
    radixSort(array)
    print(array)