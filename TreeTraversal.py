def BFS(self):
    current_node = self.root
    results = []
    queue = []
    queue.append(current_node)
    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return results

# BFS_output = [47, 21, 76, 18, 27, 52, 82]

def dfs_pre_order(self):
    results =[]
    def traversal(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traversal(current_node.left)
        if current_node.right is not None:
            traversal(current_node.right)
    traversal(self.root)
    return results

# dfs_pre_order_output = [47, 21, 18, 27, 76, 52, 82]

def dfs_post_order(self):
    results = []
    def traversal(current_node):
        if current_node.left is not None:
            traversal(current_node.left)
        if current_node.right is not None:
            traversal(current_node.right)
        results.append(current_node.value)
    
    traversal(self.root)
    return results

# dfs_post_order_output = [18, 27, 21, 52, 82, 76, 47]

def dfs_inorder(self):
    results = []
    def traversal(current_node):
        if current_node.left is not None:
            traversal(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traversal(current_node.right)

    traversal(self.root)
    return results