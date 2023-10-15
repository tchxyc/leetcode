class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch not in root:
                root[ch] = dict()
            root = root[ch]
        root["#"] = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root:
                return False
            root = root[ch]
        return "#" in root

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch not in root:
                return False
            root = root[ch]
        return True


# class Trie:
#     L = 31

#     def __init__(self):
#         self.left = self.right = None

#     def insert(self, x):
#         node = self
#         for i in range(Trie.L)[::-1]:
#             bit = x >> i & 1
#             if bit == 0:
#                 if not node.left:
#                     node.left = Trie()
#                 node = node.left
#             else:
#                 if not node.right:
#                     node.right = Trie()
#                 node = node.right

#     def search(self, x):
#         res = 0
#         node = self
#         for i in range(Trie.L)[::-1]:
#             bit = x >> i & 1
#             check = False
#             if bit == 0:
#                 if node.right:
#                     node = node.right
#                     check = True
#                 else:
#                     node = node.left
#             else:
#                 if node.left:
#                     node = node.left
#                     check = True
#                 else:
#                     node = node.right
#             if check:
#                 res |= 1 << i
#         return res
