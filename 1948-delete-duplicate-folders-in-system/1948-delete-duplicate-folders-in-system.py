from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.name = ""
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Build the Trie
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = TrieNode()
                    node.children[name].name = name
                node = node.children[name]

        # Serialization map
        subtree_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            # Serialize children sorted by name
            items = []
            for child_name in sorted(node.children.keys()):
                child_node = node.children[child_name]
                items.append(child_name + "(" + serialize(child_node) + ")")
            serialization = "".join(items)
            subtree_map[serialization].append(node)
            return serialization

        serialize(root)

        # Mark duplicate folders for deletion
        for nodes in subtree_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        # Collect remaining paths
        ans = []

        def collect(node, path):
            if node.is_deleted:
                return
            if node.name:
                path.append(node.name)
                ans.append(path.copy())
            for child in node.children.values():
                collect(child, path)
            if node.name:
                path.pop()

        collect(root, [])
        return ans
