import hashlib
import os

def generate_commitment(data: str):
    """
    Creates a ZKP-style commitment: returns (commitment, nonce)
    """
    nonce = os.urandom(16).hex()  # 16 random bytes, hex encoded
    combined = data + nonce
    commitment = hashlib.sha256(combined.encode('utf-8')).hexdigest()
    return commitment, nonce

def verify_commitment(data: str, nonce: str, commitment: str):
    """
    Verifies the commitment was made from given data + nonce
    """
    combined = data + nonce
    return hashlib.sha256(combined.encode('utf-8')).hexdigest() == commitment
