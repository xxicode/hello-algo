"""
File: time_complexity.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
"""


def constant(n: int) -> int:
    """常数阶"""
    size: int = 100000
    count: int = len(range(size))
    return count


def linear(n: int) -> int:
    """线性阶"""
    count: int = len(range(n))
    return count


def array_traversal(nums: list[int]) -> int:
    """线性阶（遍历数组）"""
    count: int = len(nums)
    return count


def quadratic(n: int) -> int:
    """平方阶"""
    count: int = 0
    # 循环次数与数组长度成平方关系
    for _ in range(n):
        for _ in range(n):
            count += 1
    return count


def bubble_sort(nums: list[int]) -> int:
    """平方阶（冒泡排序）"""
    count: int = 0  # 计数器
    # 外循环：待排序元素数量为 n-1, n-2, ..., 1
    for i in range(len(nums) - 1, 0, -1):
        # 内循环：冒泡操作
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # 交换 nums[j] 与 nums[j + 1]
                tmp: int = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
                count += 3  # 元素交换包含 3 个单元操作
    return count


def exponential(n: int) -> int:
    """指数阶（循环实现）"""
    count: int = 0
    base: int = 1
    # cell 每轮一分为二，形成数列 1, 2, 4, 8, ..., 2^(n-1)
    for _ in range(n):
        for _ in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 + .. + 2^(n-1) = 2^n - 1
    return count


def exp_recur(n: int) -> int:
    """指数阶（递归实现）"""
    return 1 if n == 1 else exp_recur(n - 1) + exp_recur(n - 1) + 1


def logarithmic(n: float) -> int:
    """对数阶（循环实现）"""
    count: int = 0
    while n > 1:
        n /= 2
        count += 1
    return count


def log_recur(n: float) -> int:
    """对数阶（递归实现）"""
    return 0 if n <= 1 else log_recur(n / 2) + 1


def linear_log_recur(n: float) -> int:
    """线性对数阶"""
    if n <= 1:
        return 1
    count: int = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count


def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count: int = sum(factorial_recur(n - 1) for _ in range(n))
    return count


"""Driver Code"""

if __name__ == "__main__":
    # 可以修改 n 运行，体会一下各种复杂度的操作数量变化趋势
    n = 8
    print("输入数据大小 n =", n)

    count: int = constant(n)
    print("常数阶的计算操作数量 =", count)

    count: int = linear(n)
    print("线性阶的计算操作数量 =", count)
    count: int = array_traversal([0] * n)
    print("线性阶（遍历数组）的计算操作数量 =", count)

    count: int = quadratic(n)
    print("平方阶的计算操作数量 =", count)
    nums: list[int] = list(range(n, 0, -1))
    count: int = bubble_sort(nums)
    print("平方阶（冒泡排序）的计算操作数量 =", count)

    count: int = exponential(n)
    print("指数阶（循环实现）的计算操作数量 =", count)
    count: int = exp_recur(n)
    print("指数阶（递归实现）的计算操作数量 =", count)

    count: int = logarithmic(n)
    print("对数阶（循环实现）的计算操作数量 =", count)
    count: int = log_recur(n)
    print("对数阶（递归实现）的计算操作数量 =", count)

    count: int = linear_log_recur(n)
    print("线性对数阶（递归实现）的计算操作数量 =", count)

    count: int = factorial_recur(n)
    print("阶乘阶（递归实现）的计算操作数量 =", count)
