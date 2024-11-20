// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.8.0/contracts/token/ERC20/ERC20.sol";

contract Store is ERC20 {
    address public owner;
    mapping(string => uint256) public itemPrices; // Prices in tokens 
    mapping(address => mapping(string => uint256)) public itemOwnership;

    event ItemPurchased(address indexed buyer, string item, uint256 quantity);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensExchanged(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event RewardGiven(address indexed to, uint256 rewardAmount);
        event EtherTransferred(address indexed from, address indexed to, uint256 amount); // Declare this event


    constructor() ERC20("StoreToken", "STK") {
        owner = msg.sender;
        _mint(owner, 100000 * (10 ** uint256(decimals()))); // Mint initial supply to the owner

        // Initialize store items and their prices in Wei
        itemPrices["burger"] = 200 * 10**15; // 0.2 ETH equivalent in token
        itemPrices["fries"] = 350 * 10**15; // 0.35 ETH equivalent in token
        itemPrices["chicken"] = 970 * 10**15; // 0.97 ETH equivalent in token
    }

    function transferEther(address payable recipient, uint256 amount) public {
        require(address(this).balance >= amount, "Insufficient balance in the store");
        
        recipient.transfer(amount);

        emit EtherTransferred(address(this), recipient, amount);
    }


    
    // Buy an item using rokens
    function buyItem(string memory itemName, uint256 quantity) public payable {
        require(itemPrices[itemName] > 0, "Item does not exist");
        uint256 cost = itemPrices[itemName] * quantity;
        require(msg.value >= cost, "Insufficient Wei sent to purchase item");

        // Add item to buyer's ownership
        itemOwnership[msg.sender][itemName] += quantity;

        // The store retains the cost (tokens sent remains in the contract)
        // Send excess Ether back to the buyer if overpaid
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }

        // Reward the buyer with Ether from the store's balance
        uint256 reward = (cost * 10) / 100; // 10% of the cost as reward
        require(address(this).balance >= reward, "Store has insufficient Ether to reward");
        payable(msg.sender).transfer(reward);

        // Emit events for purchase and reward
        emit ItemPurchased(msg.sender, itemName, quantity);
        emit RewardGiven(msg.sender, reward);
    }


    // Set or update item prices (only the owner)
    function setItemPrice(string memory itemName, uint256 price) public payable {
        require(msg.sender == owner, "Only the owner can set item prices");
        itemPrices[itemName] = price;
    }

    // View item ownership
    function getItemOwnership(address user, string memory itemName) public view returns (uint256) {
        return itemOwnership[user][itemName];
    }

    // Withdraw tokens (only the owner)
    function withdrawTokens(uint256 amount) public payable {
        require(msg.sender == owner, "Only the owner can withdraw tokens");
        require(balanceOf(address(this)) >= amount, "Not enough tokens in contract");
        _transfer(address(this), owner, amount);
    }

    // Mint tokens to a specific address (only the owner)
    function mintTokens(address to, uint256 amount) public  payable {
        require(msg.sender == owner, "Only the owner can mint tokens");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // Buy tokens with ETH (1 ETH = 10 Tokens for example)
    function buyTokens() public payable {
        require(msg.value > 0, "Must send ETH to buy tokens");
        uint256 tokenAmount = msg.value * 10; // Example conversion rate
        _mint(msg.sender, tokenAmount);

        emit TokensExchanged(msg.sender, msg.value, tokenAmount);
    }

    // Withdraw Ether (only the owner)
    function withdrawEther() public payable {
        require(msg.sender == owner, "Only the owner can withdraw Ether");
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }

    // Fallback and receive functions to accept Ether
    fallback() external payable {}

    receive() external payable {}
}
