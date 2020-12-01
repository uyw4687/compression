import time

from bitarray._bitarray import bitarray
from golomb_coding import golomb_coding

mGolombDefault = 5

def decode(value, mGolomb):
    import math

    def decode(x):
        num = 0
        for i in range(len(x)):
            num += (int(x[len(x) - 1 - i]) * (math.pow(2, i)))
        return num

    res = []
    b = int(mGolomb)
    x = value
    i = math.floor(math.log(b, 2))
    d = math.pow(2, i + 1) - b

    p2 = 0
    l = 1
    while (p2 < len(x)-1):
        t = 0
        flag = 0
        r = []
        k = i
        q = 0
        for p in range(p2, len(x)):
            if (x[p] == '0' and flag == 0):
                t += 1
                continue
            if (x[p] == '1' and flag == 0):
                q = t
                flag = 1
                continue
            r.append(x[p])
            k -= 1
            if (k == 0):
                rnum = decode(r)
                if (rnum < d):
                    p2 = p + 1
                    break
            if (k == -1):
                rnum = decode(r)
                rnum = rnum - d
                p2 = p + 1
                break
        ans = q * b + rnum
        l = 0
        res.append(int(ans))
    return res


def compress(filepath, destfilepath, mGolomb):
    result = []
    with open(filepath, 'rb') as input_file:
        data = input_file.read()

    # print(data)
    # print(list(data))
    t1 = time.time()
    for i in range(len(data)):
        for y in golomb_coding(list(data)[i], mGolomb):
            result.append(int(y))

    resultstr = ""
    for i in range(len(result)):
        resultstr += str(result[i])

    t2 = time.time()

    with open(destfilepath, "w", encoding='latin-1') as dest:
        dest.write(resultstr)
    with open(destfilepath, "wb") as dest:
        dest.write(bitarray(resultstr))
    print(bitarray(resultstr))
    return t2 - t1


def decompress(filepath, destfilepath, mGolomb):
    data = bitarray()
    with open(filepath, 'rb') as input_file:
        data.fromfile(input_file)

    # Either me or python is stupid
    datastr = str(data)[10:-1]

    res = []
    for i in range(len(datastr)):
        res.append(str(datastr[i]))

    t1 = time.time()
    result = decode(res, mGolomb)
    t2 = time.time()

    # print(result)

    resbt = bytearray(result)
    # print(resbt)

    with open(destfilepath, 'wb') as input_file:
        input_file.write(resbt)

    return t2 - t1
