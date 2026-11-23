import sys

class HashTable:
    def __init__(self):
        self.capacity = 8
        self.count = 0
        self.keys = [None] * 8
        self.values = [None] * 8

    def hash_key(self, key):
        h = 0
        for c in key:
            h = (h * 31 + ord(c)) % self.capacity
        return h

    def find(self, key):
        i = self.hash_key(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return i
            i = (i + 1) % self.capacity
        return i

    def put(self, key, value):
        i = self.find(key)
        if self.keys[i] is None:
            self.count += 1
        self.keys[i] = key
        self.values[i] = value
        if self.count * 2 > self.capacity:
            self.resize()

    def get(self, key):
        i = self.find(key)
        return self.values[i] if self.keys[i] == key else "Error"

    def delete(self, key):
        i = self.find(key)
        if self.keys[i] != key:
            return "Error"
        value = self.values[i]
        self.keys[i] = None
        self.values[i] = None
        self.count -= 1
        i = (i + 1) % self.capacity
        while self.keys[i] is not None:
            k, v = self.keys[i], self.values[i]
            self.keys[i] = None
            self.values[i] = None
            self.count -= 1
            self.put(k, v)
            i = (i + 1) % self.capacity
        return value

    def resize(self):
        old_keys, old_values = self.keys, self.values
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.count = 0
        for k, v in zip(old_keys, old_values):
            if k is not None:
                self.put(k, v)


table = HashTable()
q = int(sys.stdin.readline())
result = []

for _ in range(q):
    command = sys.stdin.readline().split()
    if command[0] == "put":
        table.put(command[1], int(command[2]))
    elif command[0] == "get":
        result.append(str(table.get(command[1])))
    elif command[0] == "del":
        result.append(str(table.delete(command[1])))
    else:
        result.append(str(table.count))

print("\n".join(result))
