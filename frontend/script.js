async function register() {
    console.log(" Register button clicked");
  
    const root = document.getElementById("merkleRoot").value;
    const commitment = document.getElementById("commitment").value;
    const statusEl = document.getElementById("status");
  
    console.log(" Merkle Root:", root);
    console.log(" Commitment:", commitment);
  
    const contractAddress = "REPLACE_WITH_YOUR_SEPOLIA_CONTRACT_ADDRESS"; //  your Sepolia contract address
  
    const abi = [
      {
        "inputs": [
          { "internalType": "string", "name": "_merkleRoot", "type": "string" },
          { "internalType": "string", "name": "_commitment", "type": "string" }
        ],
        "name": "registerFogNode",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
      }
    ];
  
    if (typeof window.ethereum === "undefined") {
      alert("MetaMask not detected.");
      return;
    }
  
    try {
      //  Force switch to Sepolia testnet
      await window.ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: '0xaa36a7' }] // 11155111 (Sepolia) in hex
      });
  
      //  Request wallet access
      await window.ethereum.request({ method: 'eth_requestAccounts' });
  
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(contractAddress, abi, signer);
  
      statusEl.textContent = " Sending transaction...";
      console.log(" Sending transaction...");
  
      const tx = await contract.registerFogNode(root, commitment);
      console.log(" Transaction sent. Waiting for confirmation...", tx.hash);
  
      await tx.wait();
      console.log(" Confirmed");
  
      statusEl.textContent = " Fog node registered successfully!";
    } catch (error) {
      console.error(" Transaction failed:", error);
      statusEl.textContent = " Transaction failed. See console.";
    }
  }
  
