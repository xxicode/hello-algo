"""
File: binary_search_tree.py
Created Time: 2022-12-20
Author: a16su (lpluls001@gmail.com)
"""

import sys, os.path as osp

sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from modules import *


class BinarySearchTree:
    """二叉搜索树"""

    def __init__(self, nums: list[int]) -> None:
        """构造方法"""
        nums.sort()
        self.__root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(
        self, nums: list[int], start_index: int, end_index: int
    ) -> TreeNode | None:
        """构建二叉搜索树"""
        if start_index > end_index:
            return None

        # 将数组中间节点作为根节点
        mid: int = (start_index + end_index) // 2
        root = TreeNode(nums[mid])
        # 递归建立左子树和右子树
        root.left = self.build_tree(
            nums=nums, start_index=start_index, end_index=mid - 1
        )
        root.right = self.build_tree(
            nums=nums, start_index=mid + 1, end_index=end_index
        )
        return root

    @property
    def root(self) -> TreeNode | None:
        return self.__root

    def search(self, num: int) -> TreeNode | None:
        """查找节点"""
        cur: TreeNode | None = self.__root
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在 cur 的右子树中
            if cur.val < num:
                cur = cur.right
            # 目标节点在 cur 的左子树中
            elif cur.val > num:
                cur = cur.left
            # 找到目标节点，跳出循环
            else:
                break
        return cur

    def insert(self, num: int) -> None:
        """插入节点"""
        # 若树为空，直接提前返回
        if self.__root is None:
            return

        # 循环查找，越过叶节点后跳出
        cur, pre = self.__root, None
        while cur is not None:
            # 找到重复节点，直接返回
            if cur.val == num:
                return
            pre = cur
            # 插入位置在 cur 的右子树中
            cur = cur.right if cur.val < num else cur.left
        # 插入节点 val
        node = TreeNode(num)
        if pre.val < num:
            pre.right = node
        else:
            pre.left = node

    def remove(self, num: int) -> None:
        """删除节点"""
        # 若树为空，直接提前返回
        if self.__root is None:
            return

        # 循环查找，越过叶节点后跳出
        cur, pre = self.__root, None
        while cur is not None:
            # 找到待删除节点，跳出循环
            if cur.val == num:
                break
            pre = cur
            # 待删除节点在 cur 的右子树中
            cur = cur.right if cur.val < num else cur.left
        # 若无待删除节点，则直接返回
        if cur is None:
            return

        # 子节点数量 = 0 or 1
        if cur.left is None or cur.right is None:
            # 当子节点数量 = 0 / 1 时， child = null / 该子节点
            child = cur.left or cur.right
            # 删除节点 cur
            if pre.left == cur:
                pre.left = child
            else:
                pre.right = child
        # 子节点数量 = 2
        else:
            # 获取中序遍历中 cur 的下一个节点
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            # 递归删除节点 tmp
            self.remove(tmp.val)
            # 用 tmp 覆盖 cur
            cur.val = tmp.val


"""Driver Code"""

if __name__ == "__main__":
    # 初始化二叉搜索树
    nums = list(range(1, 16))  # [1, 2, ..., 15]
    bst = BinarySearchTree(nums=nums)
    print("\n初始化的二叉树为\n")
    print_tree(bst.root)

    # 查找节点
    node = bst.search(7)
    print(f"\n查找到的节点对象为: {node}，节点值 = {node.val}")

    # 插入节点
    bst.insert(16)
    print("\n插入节点 16 后，二叉树为\n")
    print_tree(bst.root)

    # 删除节点
    bst.remove(1)
    print("\n删除节点 1 后，二叉树为\n")
    print_tree(bst.root)

    bst.remove(2)
    print("\n删除节点 2 后，二叉树为\n")
    print_tree(bst.root)

    bst.remove(4)
    print("\n删除节点 4 后，二叉树为\n")
    print_tree(bst.root)
