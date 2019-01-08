'''
题目：对一个数n，每步可执行以下操作之一：
1) 如果是3的倍数，除以3
2）如果是2的倍数，除以2
3）加1
4）减1
求把n变成1的最小步数
'''

end = 10000

#  不对
def func1():
    result = [-1, 0]
    for i in range(2, end + 1):
        if i % 3 == 0:
            result.append(1 + result[int(i / 3)])
            continue
        temp = []
        if i % 2 == 0:
            temp.append(1 + result[int(i / 2)])
        if i % 3 == 1:
            temp.append(1 + result[int(i - 1)])
        if i % 3 == 2:
            temp.append(2 + result[int((i + 1) / 3)])
        result.append(min(temp))

    return result

#对的
def func2():
    result = [-1, 0]
    for i in range(2, end + 1):
        temp = []
        if i % 3 == 0:
            temp.append(1 + result[int(i / 3)])
        if i % 2 == 0:
            temp.append(1 + result[int(i / 2)])
        temp.append(1 + result[int(i - 1)])
        if (i + 1) % 3 == 0:
            temp.append(2 + result[int((i + 1) / 3)])
        if (i + 1) % 2 == 0:
            temp.append(2 + result[int((i + 1) / 2)])
        result.append(min(temp))

    return result

def calStep(num):
    step = 0
    while(num > 1):
        if num % 3 == 0:
            num = num / 3
        elif num % 9 == 1:
            num = num - 1
        elif num % 9 == 8:
            num = num + 1
        elif num % 2 == 0:
            num = num / 2
        elif num % 3 == 1:
            num = num - 1
        elif num % 3 == 2:
            num = num + 1
        step = step + 1

    return step

# 不对
def func3():
    result = [-1, 0]
    for i in range(2, end + 1):
         result.append(calStep(i))

    return result

# result1 = func1()
# result2 = func2()
# for i in range(2, end + 1):
#     if result1[i] != result2[i]:
#         print("not same: {0:d}: {1:d}-{2:d}".format(i, result1[i], result2[i]))

def func1WithSteps():
    result = {}
    result[1] = {"step": 0, "steps": []}
    for i in range(2, end + 1):
        temp = []
        if i % 3 == 0:
            preNum = int(i / 3)
            pre = result[preNum]
            steps = [preNum] + pre['steps']
            temp.append({"step": 1 + pre['step'], "steps": steps})
        if i % 2 == 0:
            preNum = int(i / 2)
            pre = result[preNum]
            steps = [preNum] + pre['steps']
            temp.append({"step": 1 + pre['step'], "steps": steps})
        if i % 3 == 1:
            preNum = i - 1
            pre = result[preNum]
            steps = [preNum] + pre['steps']
            temp.append({"step": 1 + pre['step'], "steps": steps})
        if i % 3 == 2:
            preNum = int((i + 1) / 3)
            pre = result[preNum]
            steps = [i + 1, preNum] + pre['steps']
            temp.append({"step": 2 + pre['step'], "steps": steps})
        temp = sorted(temp, key = lambda x: x['step'])
        result[i] = temp[0]

    return result

def func2WithSteps():
    result = {}
    result[1] = {"step": 0, "steps": []}
    for i in range(2, end + 1):
        temp = []
        if i % 3 == 0:
            preNum = int(i / 3)
            pre = result[preNum]
            steps = [preNum] + pre['steps']
            temp.append({"step": 1 + pre['step'], "steps": steps})
        if i % 2 == 0:
            preNum = int(i / 2)
            pre = result[preNum]
            steps = [preNum] + pre['steps']
            temp.append({"step": 1 + pre['step'], "steps": steps})

        preNum = i - 1
        pre = result[preNum]
        steps = [preNum] + pre['steps']
        temp.append({"step": 1 + pre['step'], "steps": steps})

        if (i + 1) % 3 == 0:
            preNum = int((i + 1) / 3)
            pre = result[preNum]
            steps = [i + 1, preNum] + pre['steps']
            temp.append({"step": 2 + pre['step'], "steps": steps})

        if (i + 1) % 2 == 0:
            preNum = int((i + 1) / 2)
            pre = result[preNum]
            steps = [i + 1, preNum] + pre['steps']
            temp.append({"step": 2 + pre['step'], "steps": steps})
        temp = sorted(temp, key = lambda x: x['step'])
        result[i] = temp[0]

    return result

resultWithSteps1 = func1WithSteps()
resultWithSteps2 = func2WithSteps()
for i in range(1, end + 1):
    if resultWithSteps1[i]['step'] != resultWithSteps2[i]['step']:
        print("not same: " + str(i))
        print(resultWithSteps1[i])
        print(resultWithSteps2[i])
