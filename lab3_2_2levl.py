from tree import load_tree, load_tree_rev, print_tree_levels, print_tree_side


class BinaryTree:
    def __init__(self, v: int):
        self.v = v
        self.l = None
        self.r = None


def invert_binary_tree(t):
    if t is None:
        return None
    t.l, t.r = t.r, t.l
    invert_binary_tree(t.l)
    invert_binary_tree(t.r)
    return t


if __name__ == "__main__":
    root = load_tree("tree.txt", BinaryTree)

    print("TREE FROM FILE (LEVELS):")
    print_tree_levels(root)
    print("\nTREE FROM FILE (SIDE):")
    print_tree_side(root)

    root_rev = load_tree_rev("tree.txt", BinaryTree)
    print("\nTREE FROM FILE (REVERSED VALUES) (LEVELS):")
    print_tree_levels(root_rev)
    print("\nTREE FROM FILE (REVERSED VALUES) (SIDE):")
    print_tree_side(root_rev)

    invert_binary_tree(root)
    print("\nINVERTED TREE (LEVELS):")
    print_tree_levels(root)
    print("\nINVERTED TREE (SIDE):")
    print_tree_side(root)