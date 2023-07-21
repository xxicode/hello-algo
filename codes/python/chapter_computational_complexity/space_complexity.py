"""
File: space_complexity.py
Created Time: 2022-11-25
Author: Krahets (krahets@163.com)
"""

import sys, os.path as osp

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from modules import *


def function() -> int:
    """函数"""
    # do something
    return 0


def constant(n: int) -> None:
    """常数阶"""
    # 常量、变量、对象占用 O(1) 空间
    a: int = 0
    nums: list[int] = [0] * 10000
    node = ListNode(0)
    c: int = 0
    # 循环中的函数占用 O(1) 空间
    for _ in range(n):
        function()


def linear(n: int) -> None:
    """线性阶"""
    # 长度为 n 的列表占用 O(n) 空间
    nums: list[int] = [0] * n
    # 长度为 n 的哈希表占用 O(n) 空间
    mapp = dict[int, str]()
    for i in range(n):
        mapp[i] = str(i)


def linear_recur(n: int) -> None:
    """线性阶（递归实现）"""
    print("递归 n =", n)
    if n == 1:
        return
    linear_recur(n - 1)


def quadratic(n: int) -> None:
    """平方阶"""
    # 二维列表占用 O(n^2) 空间
    num_matrix: list[list[int]] = [[0] * n for _ in range(n)]


def quadratic_recur(n: int) -> int:
    """平方阶（递归实现）"""
    if n <= 0:
        return 0
    # 数组 nums 长度为 n, n-1, ..., 2, 1
    nums: list[int] = [0] * n
    return quadratic_recur(n - 1)


def build_tree(n: int) -> TreeNode | None:
    """指数阶（建立满二叉树）"""
    if n == 0:
        return None
    root = TreeNode(0)
    root.left = build_tree(n - 1)
    root.right = build_tree(n - 1)
    return root


"""Driver Code"""
if __name__ == "__main__":
    n = 5
    # 常数阶
    constant(n)
    # 线性阶
    linear(n)
    linear_recur(n)
    # 平方阶
    quadratic(n)
    quadratic_recur(n)
    # 指数阶
    root = build_tree(n)
    print_tree(root)
