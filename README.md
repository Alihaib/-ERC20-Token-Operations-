# **Store Smart Contract**

This repository contains the `Store` smart contract, a token-based decentralized application (dApp) that enables users to purchase items using the contract's custom ERC-20 token, `StoreToken (STK)`. Users can also mint tokens, exchange ETH for tokens, and receive rewards for purchases.

---

## **Features**
- **Token Minting:** The owner can mint `StoreToken` and distribute them.
- **Item Purchase:** Users can buy predefined items (e.g., burger, fries, chicken) using tokens.
- **Rewards:** Buyers receive a 10% Ether reward for every purchase.
- **Ether and Token Management:**
  - Users can exchange Ether for tokens at a defined rate.
  - The owner can withdraw tokens and Ether from the contract.
- **Item Prices:** The owner can set or update item prices.
- **Ownership Tracking:** Tracks which items users own and in what quantities.
- **Fallback and Receive Functions:** Allows the contract to accept Ether directly.

---

## **Contract Details**
- **Token Name:** StoreToken
- **Symbol:** STK
- **Initial Supply:** 100,000 STK minted to the owner.
- **Item Prices:**
  - **Burger:** 0.2 ETH equivalent in tokens.
  - **Fries:** 0.35 ETH equivalent in tokens.
  - **Chicken:** 0.97 ETH equivalent in tokens.

---

## **How to Use**
1. **Compile the Contract:**
   - Use [Remix IDE](https://remix.ethereum.org) to compile the contract.
   - Ensure the Solidity compiler version is set to `^0.8.0`.

2. **Deploy the Contract:**
   - Deploy the contract on the desired Ethereum network.
   - Verify the contract's owner address upon deployment.

3. **Interact with the Contract:**
   - **Purchase Items:**
     - Call the `buyItem(string itemName, uint256 quantity)` function.
     - Ensure you send enough Ether to cover the item cost.
   - **Mint Tokens:**
     - Only the owner can call `mintTokens(address to, uint256 amount)`.
   - **Set Item Prices:**
     - The owner can update prices using `setItemPrice(string itemName, uint256 price)`.
   - **Withdraw Ether/Tokens:**
     - The owner can withdraw Ether or tokens from the contract balance.

---

## **Events**
- `ItemPurchased(address buyer, string item, uint256 quantity)`: Emitted when an item is purchased.
- `TokensMinted(address to, uint256 amount)`: Emitted when tokens are minted.
- `TokensExchanged(address buyer, uint256 ethAmount, uint256 tokenAmount)`: Emitted when tokens are bought with ETH.
- `RewardGiven(address to, uint256 rewardAmount)`: Emitted when a reward is given.
- `EtherTransferred(address from, address to, uint256 amount)`: Emitted when Ether is transferred from the contract.

---

## **Security Notes**
- Ensure the contract is deployed by a trusted owner.
- Be cautious when setting item prices or minting tokens to prevent inflation or misuse.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
- [OpenZeppelin Contracts](https://github.com/OpenZeppelin/openzeppelin-contracts) for the ERC-20 implementation.
- Ethereum development tools such as [Remix](https://remix.ethereum.org) and [Metamask](https://metamask.io).
