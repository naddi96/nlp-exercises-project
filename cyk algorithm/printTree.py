from treelib import Node, Tree


def print_tree(input):
    root, *tail = input
    tree = Tree()
    node = Node(root)
    tree.add_node(node)

    q = [[node, *tail]]
    while q:
        parent, *children = q.pop()
        for child in children:
            if isinstance(child, list):
                head, *tail = child
                node = tree.create_node(head, parent=parent)
                q.append([node, *tail])
            else:
                tree.create_node(child, parent=parent)

    tree.show()