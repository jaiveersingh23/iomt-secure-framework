import pandas as pd
from quad_merkle import build_quad_merkle_tree
from zkp import generate_commitment, verify_commitment

# Load the dataset
file_path = "mHealth_subject1.log"
df = pd.read_csv(file_path, sep='\s+', header=None)
df = df.head(50)

# Convert each row to a string (for Merkle hashing)
data_blocks = df.apply(lambda row: ','.join(row.astype(str)), axis=1).tolist()

# Build Merkle root
merkle_root = build_quad_merkle_tree(data_blocks)

# Generate ZKP-style commitment
commitment, nonce = generate_commitment(merkle_root)

# Verify it immediately (optional check)
is_valid = verify_commitment(merkle_root, nonce, commitment)

# Output
print(" Processed 50 rows from dataset.")
print(" Merkle Root:", merkle_root)
print(" ZKP Commitment:", commitment)
print(" Nonce:", nonce)
print(" Verification passed?", is_valid)
