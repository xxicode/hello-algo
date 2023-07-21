"""
File: list.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
"""


"""Driver Code"""
if __name__ == "__main__":
    # 初始化列表
    arr: list[int] = [1, 3, 2, 5, 4]
    print("列表 arr =", arr)

    # 访问元素
    num: int = arr[1]
    print("访问索引 1 处的元素，得到 num =", num)

    # 更新元素
    arr[1] = 0
    print("将索引 1 处的元素更新为 0 ，得到 arr =", arr)

    # 清空列表
    arr.clear()
    print("清空列表后 arr =", arr)

    arr.extend((1, 3, 2, 5, 4))
    print("添加元素后 arr =", arr)

    # 中间插入元素
    arr.insert(3, 6)
    print("在索引 3 处插入数字 6 ，得到 arr =", arr)

    # 删除元素
    arr.pop(3)
    print("删除索引 3 处的元素，得到 arr =", arr)

    count: int = len(arr)
    count: int = len(arr)
    # 拼接两个列表
    arr1: list[int] = [6, 8, 7, 10, 9]
    arr += arr1
    print("将列表 arr1 拼接到 arr 之后，得到 arr =", arr)

    # 排序列表
    arr.sort()
    print("排序列表后 arr =", arr)
