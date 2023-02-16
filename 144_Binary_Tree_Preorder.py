class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        bt = []
        def findValue(root):
            if not root: return
            bt.append(root.val)
            findValue(root.left)
            findValue(root.right)
            
        findValue(root) 
        
        return bt
        