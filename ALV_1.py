import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def add(root, x):
    if root is None:
        return Node(x)

    current = root

    while True:
        if x < current.key:
            if current.left is None:
                current.left = Node(x)
                current.left.parent = current
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(x)
                current.right.parent = current
                break
            current = current.right

    return root


def find(root, x):
    while root is not None:
        if root.key == x:
            return root
        elif x < root.key:
            root = root.left
        else:
            root = root.right

    return None


def rotate_left(root, a):
    b = a.right
    parent = a.parent

    a.right = b.left
    if b.left is not None:
        b.left.parent = a

    b.left = a
    a.parent = b
    b.parent = parent

    if parent is None:
        root = b
    elif parent.left == a:
        parent.left = b
    else:
        parent.right = b

    return root


def rotate_right(root, a):
    b = a.left
    parent = a.parent

    a.left = b.right
    if b.right is not None:
        b.right.parent = a

    b.right = a
    a.parent = b
    b.parent = parent

    if parent is None:
        root = b
    elif parent.left == a:
        parent.left = b
    else:
        parent.right = b

    return root


def preorder(root, result):
    if root is None:
        return

    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)


input = sys.stdin.readline

n = int(input())
keys = list(map(int, input().split()))

root = None
for x in keys:
    root = add(root, x)

m = int(input())
answers = []

for _ in range(m):
    command, x = input().split()
    x = int(x)

    node = find(root, x)

    if command == "left":
        root = rotate_left(root, node)
    else:
        root = rotate_right(root, node)

    result = []
    preorder(root, result)
    answers.append(" ".join(result))

print("\n".join(answers))
