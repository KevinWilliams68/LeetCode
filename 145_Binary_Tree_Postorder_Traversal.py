class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        bt = []
        def findValue(root):
            if not root: return
            findValue(root.left)
            findValue(root.right)
            bt.append(root.val)
            
        findValue(root) 
        
        return bt