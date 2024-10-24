# DFS GENERIC CODE 
class GenericNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class GenericTree:
    def __init__(self):
        self.root = None

    def insert(self, value, parent_value=None):
        if not self.root:
            self.root = GenericNode(value)
        else:
            parent_node = self._find(self.root, parent_value)
            if parent_node:
                parent_node.children.append(GenericNode(value))

    def _find(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found = self._find(child, value)
            if found:
                return found
        return None

    def dfs(self, node):
        if node:
            print(node.value, end=' ')
            for child in node.children:
                self.dfs(child)

tree = GenericTree()
tree.insert(1)
tree.insert(2, 1)
tree.insert(3, 1)
tree.insert(4, 2)
tree.insert(5, 2)
tree.insert(6, 3)

print("\nDFS Traversal for Generic Tree:")
tree.dfs(tree.root)
