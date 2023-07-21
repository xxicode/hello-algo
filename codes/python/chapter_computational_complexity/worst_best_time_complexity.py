"""
File: worst_best_time_complexity.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
"""

import random


def random_numbers(n: int) -> list[int]:
    """生成一个数组，元素为: 1, 2, ..., n ，顺序被打乱"""
    # 生成数组 nums =: 1, 2, 3, ..., n
    nums: list[int] = list(range(1, n + 1))
    # 随机打乱数组元素
    random.shuffle(nums)
    return nums


def find_one(nums: list[int]) -> int:
    """查找数组 nums 中数字 1 所在索引"""
    return next((i for i in range(len(nums)) if nums[i] == 1), -1)


"""Driver Code"""

if __name__ == "__main__":
    n: int = 100
    for _ in range(10):
        nums: list[int] = random_numbers(n)
        index: int = find_one(nums)
        print("\n数组 [ 1, 2, ..., n ] 被打乱后 =", nums)
        print("数字 1 的索引为", index)
