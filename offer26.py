# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 如果B为空的话，直接返回false
        if not B:
            return False

        def is_same(rootA, rootB):
            # 定义函数来判断树A是否包含树B

            # 找到相同的节点rootA和rootB之后，进行遍历
            # 如果rootB没有了，说明rootB遍历完了,A包含B，所以返回True
            if not rootB:
                return True
            # 如果rootA遍历完了，但是rootB还没有遍历完，说明A不包含B，返回False
            if not rootA and rootB:
                return False
            # 如果有值不相等的话，直接返回false
            if rootA.val != rootB.val:
                return False
            # 如果上面那些情况都没有发生，则使用递归对左右树进行判断
            return is_same(rootA.left, rootB.left) and is_same(rootA.right, rootB.right)

        def preorder(root):
            # 定义一个函数,用来遍历A的所有节点，然后对每一个节点和B的节点进行比较
            if not root:
                return False
            temp = False
            # 如果节点相同则判断两个节点所对应的树rootA，rootB:ROOTA是否包含ROOTB
            if root.val == B.val:
                temp = is_same(root, B)
            # 如果找的A的节点和B的节点的值不一样的话，则对A的左右子节点进行比较
            return preorder(root.left) or preorder(root.right) or temp

        return preorder(A)

