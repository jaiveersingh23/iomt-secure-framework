// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FogNodeRegistry {

    struct FogNode {
        address nodeAddress;
        string merkleRoot;
        string commitment;
    }

    mapping(address => FogNode) public fogNodes;

    event NodeRegistered(address indexed node, string merkleRoot, string commitment);

    function registerFogNode(string memory _merkleRoot, string memory _commitment) public {
        fogNodes[msg.sender] = FogNode(msg.sender, _merkleRoot, _commitment);
        emit NodeRegistered(msg.sender, _merkleRoot, _commitment);
    }

    function getFogNode(address node) public view returns (string memory, string memory) {
        FogNode memory f = fogNodes[node];
        return (f.merkleRoot, f.commitment);
    }
}
