def deleteNode(root, data):
    if root is None:
        return root
    if data < root.data:
        root.left_node = deleteNode(root.left_node, data)
        return root

    elif(data > root.data):
        root.right_node = deleteNode(root.right_node, data)
        return root
    if root.left_node is None and root.right_node is None:
        return None
    if root.left_node is None:
        temp = root.right_node
        root = None
        return temp
    elif root.right_node is None:
        temp = root.left_node
        root = None
        return temp
    succParent = root
    succ = root.right_node
    while succ.left_node != None:
        succParent = succ
        succ = succ.left_node
    if succParent != root:
        succParent.left_node = succ.right_node
    else:
        succParent.right_node = succ.right_node
    root.data = succ.data
    return root
