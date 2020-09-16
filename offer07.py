class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思想：前序遍历：中左右   中序遍历：左中右
# 前序的第一个元素肯定是根节点，找到根节点之后就可以结合中序遍历分出根节点的左右树
# 后面的节点也是利用类似的方法进行查找

class Solution:
    def buildTree(self, preorde, inorder):
        if len(preorde) == 0 or len(inorder) == 0:
            return None
        root_node = TreeNode(preorde[0])
        ind = inorder.index(preorde[0])
        root_node.left = self.buildTree(preorde[1:ind + 1], inorder[:ind])
        root_node.right = self.buildTree(preorde[ind + 1:], inorder[ind + 1:])
        return root_node



