"""
��ǰ��������������й��������
����һ������ǰ�������������������������

ע��:
����Լ�������û���ظ���Ԫ�ء�

���磬����

ǰ����� preorder = [3,9,20,15,7]
������� inorder = [9,3,15,20,7]
�������µĶ�������

    3
   / \
  9  20
    /  \
   15   7
��Ŀ���ӣ�https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

# ˼·���ݹ鷨
def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root