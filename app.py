
from web3 import Web3
import tkinter as tk
from tkinter import messagebox, ttk

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
contract_address = '0x2c753E79afd39b14ffb9cd84a90E56A7256B866B'
contract_abi =[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "EtherTransferred",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "string",
				"name": "item",
				"type": "string"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "quantity",
				"type": "uint256"
			}
		],
		"name": "ItemPurchased",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "rewardAmount",
				"type": "uint256"
			}
		],
		"name": "RewardGiven",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "buyer",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "ethAmount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "tokenAmount",
				"type": "uint256"
			}
		],
		"name": "TokensExchanged",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "TokensMinted",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "value",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"stateMutability": "payable",
		"type": "fallback"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			}
		],
		"name": "allowance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "account",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "itemName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "quantity",
				"type": "uint256"
			}
		],
		"name": "buyItem",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "buyTokens",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "decimals",
		"outputs": [
			{
				"internalType": "uint8",
				"name": "",
				"type": "uint8"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "subtractedValue",
				"type": "uint256"
			}
		],
		"name": "decreaseAllowance",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "itemName",
				"type": "string"
			}
		],
		"name": "getItemOwnership",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "spender",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "addedValue",
				"type": "uint256"
			}
		],
		"name": "increaseAllowance",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "itemOwnership",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "itemPrices",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "mintTokens",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "itemName",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			}
		],
		"name": "setItemPrice",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transfer",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address payable",
				"name": "recipient",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferEther",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "withdrawEther",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			}
		],
		"name": "withdrawTokens",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"stateMutability": "payable",
		"type": "receive"
	}
]

# Load the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)




store_items = {
    "burger: price 200 token": 2,
    "fries: price 350 token": 3.5,
    "chicken: price 970 token": 9.7
}
customer_currency_balance =0
eth_balance = 100 # Default Ethereum balance

# User and owner addresses
current_user_address = "0x9b3D4005acC9487241E867A82454752b20BAAc62"
owner_address = "0x24db4df6289C7a3ACec342c2a63b319474AB6562"

# Functions for smart contract interaction
def is_valid_address(address):
    return w3.isAddress(address)

def transfer_tokens(from_address, to_address, amount):
    try:
        tx = contract.functions.transfer(to_address, amount).transact({'from': from_address})
        w3.eth.wait_for_transaction_receipt(tx)
        messagebox.showinfo("Success", f"Transferred {amount} tokens from {from_address} to {to_address}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def transfer_ether(from_address, to_address, amount_ether):
	try:
		# Convert Ether amount to Wei
		amount_wei = Web3.to_wei(amount_ether, 'ether')

		# Call the smart contract function
		tx = contract.functions.transferEther(to_address, amount_wei).transact({
			'from': from_address
		})

		# Wait for the transaction to complete
		w3.eth.wait_for_transaction_receipt(tx)

		# Notify the user of success
		messagebox.showinfo("Success", f"Transferred {amount_ether} ETH from contract to {to_address}!")
	except Exception as e:
		messagebox.showerror("Error", f"Transaction failed: {str(e)}")


def show_balance(address):
    try:
        token_balance = contract.functions.balanceOf(address).call()
        eth_balance = w3.eth.get_balance(address) / (10 ** 18)  # Convert Wei to ETH
        messagebox.showinfo("Balance", f"Balance of {address}: {token_balance} tokens, {eth_balance:.2f} ETH")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def purchase_item(from_address):
    try:
        # Get selected item name
        item_name = item_combo.get()
        item_price = store_items.get(item_name)  # Price in Ether for user readability

        if item_price is None:
            messagebox.showerror("Error", "Invalid item selected")
            return

        # Convert price to Wei
        item_price_wei = Web3.to_wei(item_price, 'ether')

        # Call the buyItem function with Wei as `value`
        tx = contract.functions.buyItem(item_name.split(':')[0], 1).transact({
            'from': from_address,
            'value': item_price_wei
        })

        # Wait for transaction receipt
        w3.eth.wait_for_transaction_receipt(tx)

        # Reward the user with Ether using the transferEther function
        reward_amount = Web3.to_wei(0.1, 'ether')  # Example reward amount in Ether
        transfer_tx = contract.functions.transferEther(from_address, reward_amount).transact({
            'from': owner_address
        })
        w3.eth.wait_for_transaction_receipt(transfer_tx)

        # Notify user of success
        messagebox.showinfo(
            "Success",
            f"Purchased {item_name} for {item_price_wei} token and rewarded with {Web3.from_wei(reward_amount, 'ether')} ETH!"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Transaction failed: {str(e)}")








def transfer_eth_to_token(from_address, eth_amount):
    try:
        tx = contract.functions.buyTokens().transact({
            'from': from_address,
            'value': Web3.to_wei(eth_amount, 'ether')
        })
        w3.eth.wait_for_transaction_receipt(tx)
        update_currency_display()
        messagebox.showinfo("Success", f"Converted {eth_amount} ETH to tokens")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_currency_display():
    try:
        balance = contract.functions.balanceOf(current_user_address).call()
        currency_label.config(text=f"Currency Balance: {balance} tokens")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def open_store_window():
    store_window = tk.Toplevel()
    store_window.title("Store")
    store_window.geometry("700x200")
    store_window.configure(bg='#34495E')

    # Define styles
    label_font = ('Arial', 14, 'bold')
    entry_font = ('Arial', 12)
    button_font = ('Arial', 12, 'bold')

    # Store Title
    tk.Label(store_window, text="Purchase Item", bg='#34495E', fg='#ECF0F1', font=label_font).pack(pady=10)

    # Frame for purchasing items
    frame_purchase = tk.Frame(store_window, bg='#2C3E50', padx=20, pady=20)
    frame_purchase.pack(pady=10)

    tk.Label(frame_purchase, text="Select Item:", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=0, column=0,
                                                                                                    sticky='e')
    global item_combo
    item_combo = ttk.Combobox(frame_purchase, values=list(store_items.keys()), font=entry_font)
    item_combo.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_purchase, text="Your Address:", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=1, column=0,
                                                                                                     sticky='e')
    address_purchase = tk.Entry(frame_purchase, font=entry_font, width=30, bd=0, relief='flat', bg='#BDC3C7',
                                fg='#2C3E50')
    address_purchase.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(frame_purchase, text="Purchase", bg='#3498DB', fg='#ECF0F1', font=button_font, bd=0, relief='flat',
              command=lambda: purchase_item(address_purchase.get())).grid(row=2, column=0, columnspan=2, pady=10)

def main():
    global currency_label
    root = tk.Tk()
    root.title("ERC20 Token Operations")
    root.geometry("600x770")
    root.configure(bg='#34495E')

    # Define styles
    title_font = ('Arial', 18, 'bold')
    label_font = ('Arial', 14, 'bold')
    entry_font = ('Arial', 12)
    button_font = ('Arial', 12, 'bold')

    # Title Label
    title_label = tk.Label(root, text="ERC20 Token Operations", bg='#34495E', fg='#ECF0F1', font=title_font)
    title_label.pack(pady=20)

    # Frame for Check Balance
    frame_balance = tk.Frame(root, bg='#2C3E50', padx=20, pady=20)
    frame_balance.pack(pady=10)

    tk.Label(frame_balance, text="Check Balance", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=0, column=0,
                                                                                                    columnspan=2,
                                                                                                    pady=10)

    tk.Label(frame_balance, text="Address:", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=1, column=0,
                                                                                               sticky='e')
    address_balance = tk.Entry(frame_balance, font=entry_font, width=30, bd=0, relief='flat', bg='#BDC3C7',
                               fg='#2C3E50')
    address_balance.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(frame_balance, text="Check Balance", bg='#3498DB', fg='#ECF0F1', font=button_font,
              command=lambda: show_balance(address_balance.get()), bd=0, relief='flat').grid(row=2, column=0,
                                                                                             columnspan=2, pady=20,
                                                                                             ipadx=10)

    # Currency Balance Display
    currency_label = tk.Label(root, text=f"Currency Balance: {customer_currency_balance:.2f} tokens",
                               bg='#34495E', fg='#ECF0F1', font=label_font)
    currency_label.pack(pady=20)

    # Frame for Ether to Token Transfer
    frame_transfer = tk.Frame(root, bg='#2C3E50', padx=20, pady=20)
    frame_transfer.pack(pady=10)

    tk.Label(frame_transfer, text="Transfer Ether to Tokens", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=0,
                                                                                                                column=0,
                                                                                                                columnspan=2,
                                                                                                                pady=10)

    tk.Label(frame_transfer, text="Address:", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=1, column=0,
                                                                                                sticky='e')
    address_transfer = tk.Entry(frame_transfer, font=entry_font, width=30, bd=0, relief='flat', bg='#BDC3C7',
                                fg='#2C3E50')
    address_transfer.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_transfer, text="Ether Amount:", bg='#2C3E50', fg='#ECF0F1', font=label_font).grid(row=2, column=0,
                                                                                                     sticky='e')
    eth_amount_entry = tk.Entry(frame_transfer, font=entry_font, width=30, bd=0, relief='flat', bg='#BDC3C7',
                                fg='#2C3E50')
    eth_amount_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(frame_transfer, text="Transfer Ether", bg='#3498DB', fg='#ECF0F1', font=button_font,
              command=lambda: transfer_eth_to_token(address_transfer.get(), float(eth_amount_entry.get())), bd=0,
              relief='flat').grid(row=3, column=0, columnspan=2, pady=20, ipadx=10)

    # Button to open store window
    tk.Button(root, text="Open Store", bg='#1ABC9C', fg='#ECF0F1', font=button_font, bd=0, relief='flat',
              command=open_store_window).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()