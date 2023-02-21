class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        bt = []
        def findValue(root):
            if not root: return
            findValue(root.left)
            bt.append(root.val)
            findValue(root.right)
            
        findValue(root) 
        
        return bt