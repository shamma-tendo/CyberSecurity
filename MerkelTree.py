import hashlib

class MerkleTree:
    def __init__(self, data_blocks):
        self.leaves = [self._hash(d) for d in data_blocks]
        self.tree = self._build_tree(self.leaves)

    def _hash(self, data):
        return hashlib.sha256(data.encode() if isinstance(data, str) else data).hexdigest()

    def _build_tree(self, leaves):
        tree = [leaves]
        while len(tree[-1]) > 1:
            level = tree[-1]
            next_level = []
            for i in range(0, len(level), 2):
                left = level[i]
                right = level[i+1] if i+1 < len(level) else left
                next_level.append(self._hash(left + right))
            tree.append(next_level)
        return tree

    def root(self):
        return self.tree[-1][0]

    def get_proof(self, index):
        proof = []
        for level in self.tree[:-1]:
            pair_index = index ^ 1
            if pair_index < len(level):
                proof.append((level[pair_index], pair_index % 2 == 0))
            index //= 2
        return proof

data = ["transaction1", "transaction2", "transaction3", "transaction4"]
tree = MerkleTree(data)
print("Merkle Root:", tree.root())
print("Proof for item 0:", tree.get_proof(0))