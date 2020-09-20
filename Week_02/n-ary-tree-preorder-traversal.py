class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result