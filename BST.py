import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def add(root, x):
    if root is None:
        return Node(x)

    if x < root.key:
        root.left = add(root.left, x)
    elif x > root.key:
        root.right = add(root.right, x)

    return root


def exists(root, x):
    while root is not None:
        if root.key == x:
            return True
        elif x < root.key:
            root = root.left
        else:
            root = root.right

    return False


def find_min(root):
    while root.left is not None:
        root = root.left
    return root.key


def delete(root, x):
    if root is None:
        return None

    if x < root.key:
        root.left = delete(root.left, x)
    elif x > root.key:
        root.right = delete(root.right, x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        root.key = find_min(root.right)
        root.right = delete(root.right, root.key)

    return root


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def preorder(root, result):
    if root is None:
        return

    result.append(str(root.key))
    preorder(root.left, result)
    preorder(root.right, result)


root = None
q = int(input())
answers = []

for _ in range(q):
    command = input().split()

    if command[0] == "add":
        root = add(root, int(command[1]))

    elif command[0] == "del":
        root = delete(root, int(command[1]))

    elif command[0] == "exists":
        answers.append("YES" if exists(root, int(command[1])) else "NO")

    elif command[0] == "height":
        answers.append(str(height(root)))

    elif command[0] == "print":
        result = []
        preorder(root, result)
        answers.append(" ".join(result) if result else "Empty")

print("\n".join(answers))