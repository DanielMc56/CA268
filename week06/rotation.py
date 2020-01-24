def rotation_type(bst):
    r_type = ""
    ptr = bst.root
    while ptr != None:
        if ptr.left == None and ptr.right == None:
            return r_type
        if ptr.left == None:
            r_type += "r"
            ptr = ptr.right
        else:
            r_type += "l"
            ptr = ptr.left
    return r_type