# ���� O��n��
class Solution: 
    def inorderTraversal(self, root: TreeNode)->List[int]: 
        res, stack = [], [] 
        while True: 
            while root: 
                stack.append(root) 
                root = root.left 
            if not stack: 
                return res 
            node = stack.pop() 
            res.append(node.val) 
            root = node.right
            
# �ݹ� O��n��
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res
    
def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)