import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(
        get_height(node.left),
        get_height(node.right)
    )


def balance_factor(node):
    return get_height(node.right) - get_height(node.left)


def rotate_left(a):
    b = a.right
    a.right = b.left
    b.left = a

    update_height(a)
    update_height(b)

    return b


def rotate_right(a):
    b = a.left
    a.left = b.right
    b.right = a

    update_height(a)
    update_height(b)

    return b


def balance(node):
    if node is None:
        return None

    update_height(node)
    bf = balance_factor(node)

    if bf == 2:
        if balance_factor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if bf == -2:
        if balance_factor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    return node


def add(node, x):
    if node is None:
        return Node(x)

    if x < node.key:
        node.left = add(node.left, x)
    elif x > node.key:
        node.right = add(node.right, x)
    else:
        return node

    return balance(node)


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def delete(node, x):
    if node is None:
        return None

    if x < node.key:
        node.left = delete(node.left, x)
    elif x > node.key:
        node.right = delete(node.right, x)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        minimum = find_min(node.right)
        node.key = minimum.key
        node.right = delete(node.right, minimum.key)

    return balance(node)


def exists(node, x):
    while node is not None:
        if x == node.key:
            return True
        elif x < node.key:
            node = node.left
        else:
            node = node.right

    return False


def next_key(node, x):
    result = None

    while node is not None:
        if node.key >= x:
            result = node.key
            node = node.left
        else:
            node = node.right

    return result


def prev_key(node, x):
    result = None

    while node is not None:
        if node.key <= x:
            result = node.key
            node = node.right
        else:
            node = node.left

    return result


def preorder(node, result):
    if node is None:
        return

    result.append(str(node.key))
    preorder(node.left, result)
    preorder(node.right, result)


root = None
answers = []

q = int(input())

for _ in range(q):
    command = input().split()
    operation = command[0]

    if operation == "add":
        root = add(root, int(command[1]))

    elif operation == "del":
        root = delete(root, int(command[1]))

    elif operation == "exists":
        x = int(command[1])
        answers.append("YES" if exists(root, x) else "NO")

    elif operation == "next":
        x = int(command[1])
        result = next_key(root, x)
        answers.append(str(result) if result is not None else "None")

    elif operation == "prev":
        x = int(command[1])
        result = prev_key(root, x)
        answers.append(str(result) if result is not None else "None")

    elif operation == "root":
        answers.append(str(root.key) if root is not None else "Empty")

    elif operation == "height":
        answers.append(str(get_height(root)))

    elif operation == "print":
        result = []
        preorder(root, result)
        answers.append(" ".join(result) if result else "Empty")

print("\n".join(answers))
