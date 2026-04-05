from collections import deque


def read_vals(path="tree.txt"):
    with open(path, "r", encoding="utf-8") as f:
        t = f.read().split()

    vals = []
    for x in t:
        if x.lower() in ("none", "null", "#"):
            vals.append(None)
        else:
            vals.append(int(x))
    return vals


def build_tree(vals, NodeClass):
    if not vals:
        return None

    nodes = [None if x is None else NodeClass(x) for x in vals]

    for i in range(len(nodes)):
        if nodes[i] is None:
            continue
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < len(nodes):
            nodes[i].l = nodes[li]
        if ri < len(nodes):
            nodes[i].r = nodes[ri]

    return nodes[0]


def load_tree(path, NodeClass):
    return build_tree(read_vals(path), NodeClass)


def load_tree_rev(path, NodeClass):
    vals = read_vals(path)
    vals.reverse()
    return build_tree(vals, NodeClass)


def print_tree_levels(root):
    if root is None:
        print("empty")
        return

    q = deque([root])
    while q:
        n = len(q)
        line = []
        any_child = False

        for _ in range(n):
            cur = q.popleft()
            if cur is None:
                line.append("None")
                q.append(None)
                q.append(None)
            else:
                line.append(str(cur.v))
                if cur.l is not None or cur.r is not None:
                    any_child = True
                q.append(cur.l)
                q.append(cur.r)

        print(" ".join(line))

        if not any_child:
            break


def print_tree_side(root):
    if root is None:
        print("empty")
        return
    _print_side(root, 0)


def _print_side(n, d):
    if n is None:
        return
    _print_side(n.r, d + 1)
    print("   " * d + str(n.v))
    _print_side(n.l, d + 1)