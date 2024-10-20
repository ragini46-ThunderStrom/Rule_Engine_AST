# ast_node.py
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left        # Left child
        self.right = right      # Right child
        self.value = value      # For operands, the condition (e.g., age > 30)

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value}, left={self.left}, right={self.right})"
