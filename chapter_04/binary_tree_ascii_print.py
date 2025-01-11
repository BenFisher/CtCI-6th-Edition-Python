class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BinaryTree:
    NodeCls = Node

    def __init__(self):
        self.root = None

    def insert(self, key, parent=None):
        new = self.NodeCls(key)

        if parent is None:
            if self.root is None:
                self.root = new
                return new
            else:
                raise ValueError("Tree already has a root. Provide a parent node for insertion.")

        if parent.left is None:
            parent.left = new
            new.parent = parent
        elif parent.right is None:
            parent.right = new
            new.parent = parent
        else:
            raise ValueError("Parent node already has two children.")

        return new

    def print_ascii(self):
        if not self.root:
            print("<empty tree>")
            return

        def build_tree_string(node, curr_index, include_index=False, delimiter=" -> "):
            """Recursively build the tree structure as a string"""
            if node is None:
                return [], 0, 0, 0

            line1 = []
            line2 = []
            node_repr = f"{node.key}" + (f" ({curr_index})" if include_index else "")

            new_root_width = gap_size = len(node_repr)

            # Get the left and right sub-tree string representation
            l_box, l_box_width, l_root_start, l_root_end = build_tree_string(
                node.left, 2 * curr_index + 1, include_index, delimiter
            )
            r_box, r_box_width, r_root_start, r_root_end = build_tree_string(
                node.right, 2 * curr_index + 2, include_index, delimiter
            )

            # Draw the branch connecting the current root node to the left sub-tree
            if l_box_width > 0:
                l_root = (l_root_start + l_root_end) // 2 + 1
                line1.append(" " * (l_root + 1))
                line1.append("_" * (l_box_width - l_root))
                line2.append(" " * l_root + "/")
                line2.append(" " * (l_box_width - l_root))
                new_root_start = l_box_width + 1
                gap_size += 1
            else:
                new_root_start = 0

            # Draw the representation of the current root node
            line1.append(node_repr)
            line2.append(" " * new_root_width)

            # Draw the branch connecting the current root node to the right sub-tree
            if r_box_width > 0:
                r_root = (r_root_start + r_root_end) // 2
                line1.append("_" * r_root)
                line1.append(" " * (r_box_width - r_root + 1))
                line2.append(" " * r_root + "\\")
                line2.append(" " * (r_box_width - r_root))
                gap_size += 1
            new_root_end = new_root_start + new_root_width - 1

            # Combine the left and right sub-tree boxes with the branches drawn above
            gap = " " * gap_size
            new_box = ["".join(line1), "".join(line2)]
            for i in range(max(len(l_box), len(r_box))):
                l_line = l_box[i] if i < len(l_box) else " " * l_box_width
                r_line = r_box[i] if i < len(r_box) else " " * r_box_width
                new_box.append(l_line + gap + r_line)

            return new_box, len(new_box[0]), new_root_start, new_root_end

        # Build the tree string and print it
        lines, _, _, _ = build_tree_string(self.root, 0, include_index=False)
        for line in lines:
            print(line)

    def traverse_in_order(self, node=None, visit=lambda x: print(f"Visiting {x.key}")):
        if node is None:
            node = self.root
        if node:
            if node.left:
                self.traverse_in_order(node.left, visit)
            visit(node)
            if node.right:
                self.traverse_in_order(node.right, visit)
    
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        if node:
            print(" " * (4 * level) + f"Node({node.key}): Left({node.left.key if node.left else None}), Right({node.right.key if node.right else None})")
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)
                
# Example usage
bt = BinaryTree()
# Insert nodes
root = bt.insert(10)  # Root node
left = bt.insert(5, root)  # Left child
right = bt.insert(15, root)  # Right child

# Insert another layer
bt.insert(3, left)
bt.insert(7, left)

bt.print_ascii()
bt.traverse_in_order()


