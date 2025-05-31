
# Secure IoMT Fog Node Registration Using Quad Merkle Trees and Zero-Knowledge Proofs

This project implements a privacy-preserving framework for securely registering fog nodes in an Internet of Medical Things (IoMT) environment using **quad Merkle trees**, **Zero-Knowledge Proof (ZKP) commitments**, and **Ethereum smart contracts**. The system ensures that medical sensor data is verified and registered on the blockchain without revealing sensitive information.

---

## 🔍 Overview

Fog nodes process health data from IoMT devices at the edge of the network. This project allows fog nodes to:
- Generate a **Merkle root** from real medical data using a **quad Merkle tree**
- Create a **ZKP-style hash commitment** from the Merkle root
- Submit the Merkle root and commitment to a **smart contract on the Ethereum Sepolia testnet**
- Use a **MetaMask-integrated frontend** to securely send transactions

---

## 📁 Project Structure

```
iotm-secure-framework/
├── backend/
│   └── process_data.py 
│   └── quad_merkle.py
│   └── zkp.py
├── frontend/
│   ├── index.html            # Frontend UI for registration
│   └── script.js             # Ethers.js integration with MetaMask
├── solidity/
│   └── FogNodeRegistry.sol   # Solidity smart contract
└── README.md                 # Project documentation
```

---

## 🧪 Dataset

This project uses the real-world [mHealth dataset](https://archive.ics.uci.edu/ml/datasets/mhealth+dataset), which contains motion and ECG data recorded from wearable sensors during 12 physical activities.

---

## ⚙️ Technologies Used

- **Python** for backend data processing
- **Solidity** for Ethereum smart contracts
- **JavaScript** with `ethers.js` for blockchain interaction
- **HTML** frontend served over `http.server`
- **MetaMask** for wallet integration
- **Ethereum Sepolia testnet** for deployment

---

## 🚀 How to Run

### 1. Backend – Generate Proofs
```bash
cd backend
python process_data.py
```
Copy the generated Merkle root and ZKP commitment.

### 2. Deploy the Smart Contract
- Use [Remix IDE](https://remix.ethereum.org)
- Deploy `FogNodeRegistry.sol` to **Sepolia**
- Note the contract address

### 3. Frontend – Register on Blockchain
```bash
cd frontend
python -m http.server 8000
```
- Open `http://localhost:8000`
- Paste the Merkle root and commitment
- Click **"Register Fog Node"**
- MetaMask will prompt to switch to Sepolia and confirm the transaction

---

## 🛡️ Security Features

- **Merkle Root**: Ensures data integrity (any tampering changes the root)
- **ZKP Commitment**: Proves data possession without revealing it
- **Smart Contract**: Immutable storage of cryptographic proofs on blockchain

---

## 📜 License

This project is for academic and research purposes. Licensed under the MIT License.


---

## 👨‍💻 Author

Developed by [Jaiveer Singh] as part of an academic IoMT security project using real-world datasets and blockchain technologies.
