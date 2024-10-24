# You are required to write code demonstrating the application of DFS (Depth First Search) traversal algorithms. Once completed, please upload your code to GitHub or share it in a post on LinkedIn. Ensure that you submit the link by Thursday.


#DFS Binary Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if not current.left:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if not current.right:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def dfs_inorder(self, node):
        if node:
            self.dfs_inorder(node.left)
            print(node.value, end=' ')
            self.dfs_inorder(node.right)

    def dfs_preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.dfs_preorder(node.left)
            self.dfs_preorder(node.right)

    def dfs_postorder(self, node):
        if node:
            self.dfs_postorder(node.left)
            self.dfs_postorder(node.right)
            print(node.value, end=' ')

tree = BinaryTree()
for value in [10, 5, 15, 2, 7, 12, 18]:
    tree.insert(value)

print("DFS Inorder Traversal:")
tree.dfs_inorder(tree.root)
print("\nDFS Preorder Traversal:")
tree.dfs_preorder(tree.root)
print("\nDFS Postorder Traversal:")
tree.dfs_postorder(tree.root)



