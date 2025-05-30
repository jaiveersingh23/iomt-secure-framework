import hashlib

def hash_data(data: str) -> str:
    """Returns the SHA-256 hash of a string."""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_quad_merkle_tree(data_blocks):
    """
    Constructs a Quad Merkle Tree (4 children per parent) and returns the Merkle root.
    """
    if not data_blocks:
        return None

    # First hash each data block (leaf nodes)
    current_level = [hash_data(block) for block in data_blocks]

    while len(current_level) > 1:
        next_level = []

        for i in range(0, len(current_level), 4):
            # Get 4 hashes (pad with last one if less than 4)
            children = current_level[i:i+4]
            while len(children) < 4:
                children.append(children[-1])
            
            combined = ''.join(children)
            next_hash = hash_data(combined)
            next_level.append(next_hash)

        current_level = next_level

    # Final single root
    return current_level[0]
