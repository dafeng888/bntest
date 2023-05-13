from web3 import Web3
from eth_account import Account
import time
#换usdc
ZKSYNC_NETWORK_URL = "https://mainnet.era.zksync.io"
zksync_web3 = Web3(Web3.HTTPProvider(ZKSYNC_NETWORK_URL))
account = Account.from_key('your private key')
router_abi = """[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "token",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amountTokenDesired",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amountTokenMin",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amountETHMin",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "feeType",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "stable",
				"type": "bool"
			}
		],
		"name": "addLiquidityETH",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "amountToken",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "amountETH",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "liquidity",
				"type": "uint256"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amountIn",
				"type": "uint256"
			},
			{
				"internalType": "address[]",
				"name": "path",
				"type": "address[]"
			},
			{
				"internalType": "bool[]",
				"name": "stable",
				"type": "bool[]"
			}
		],
		"name": "getAmountsOut",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "amounts",
				"type": "uint256[]"
			},
			{
				"internalType": "bool[]",
				"name": "_stable",
				"type": "bool[]"
			},
			{
				"internalType": "uint256[]",
				"name": "fees",
				"type": "uint256[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amountOutMin",
				"type": "uint256"
			},
			{
				"internalType": "address[]",
				"name": "path",
				"type": "address[]"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			},
			{
				"internalType": "bool[]",
				"name": "stable",
				"type": "bool[]"
			}
		],
		"name": "swapExactETHForTokens",
		"outputs": [
			{
				"internalType": "uint256[]",
				"name": "amounts",
				"type": "uint256[]"
			}
		],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "amountOutMin",
				"type": "uint256"
			},
			{
				"internalType": "address[]",
				"name": "path",
				"type": "address[]"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "deadline",
				"type": "uint256"
			},
			{
				"internalType": "bool[]",
				"name": "stable",
				"type": "bool[]"
			}
		],
		"name": "swapExactETHForTokensSupportingFeeOnTransferTokens",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]""" 

pair_abi = """[
	{
		"inputs": [],
		"name": "getReserves",
		"outputs": [
			{
				"internalType": "uint112",
				"name": "reserve0",
				"type": "uint112"
			},
			{
				"internalType": "uint112",
				"name": "reserve1",
				"type": "uint112"
			},
			{
				"internalType": "uint32",
				"name": "blockTimestampLast",
				"type": "uint32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "token0",
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
		"inputs": [],
		"name": "token1",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]"""
erc20_abi = """[
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
				"name": "value",
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
				"name": "owner",
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
	}
]"""

router_address = '0x8B791913eB07C32779a16750e3868aA8495F5964'
WETH_address = '0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91'
USDC_address = '0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4'
WETH = zksync_web3.eth.contract(address=WETH_address, abi=erc20_abi)
USDC = zksync_web3.eth.contract(address=USDC_address, abi=erc20_abi)
router = zksync_web3.eth.contract(address=router_address, abi=router_abi)
pair = zksync_web3.eth.contract(address='0xDFAaB828f5F515E104BaaBa4d8D554DA9096f0e4', abi=pair_abi)

def quote(amountA, reserveA, reserveB):
    return amountA * reserveB / reserveA

def get_usdc_amount(amountEth_wei):    
    token0 = pair.functions.token0().call()
    if token0 == WETH_address:
        reverse = pair.functions.getReserves().call()
        amountOut = quote(amountEth_wei, reverse[0], reverse[1])
    else:
        reverse = pair.functions.getReserves().call()
        amountOut = quote(amountEth_wei, reverse[1], reverse[0])
    return amountOut

def approve_usdc(amount,account):
    nonce = zksync_web3.eth.get_transaction_count(account.address)
    params = {
        "nonce": nonce,
        'from': account.address,
        'gas': 1500000,
        'gasPrice': zksync_web3.eth.gas_price,
    }
    tx = USDC.functions.approve(router_address,amount).build_transaction(params)
    signed_tx = account.sign_transaction(tx)
    tx_hash = zksync_web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash

def add_liqulity(amountEth,account):
    amountEth_wei = zksync_web3.to_wei(amountEth, 'ether')
    amountUsdc =  int(get_usdc_amount(amountEth_wei))
    balance = USDC.functions.balanceOf(account.address).call()
    if balance < amountUsdc:
        return 'USDC not enough'
    allownce = USDC.functions.allowance(account.address,router_address).call()
    if allownce < amountUsdc:
        print('approve')
        tx_hash = approve_usdc(amountUsdc,account)
        zksync_web3.eth.wait_for_transaction_receipt(tx_hash)
    amountOutMin = int(amountUsdc * 0.99)
    deadline = int(time.time()) + 60 * 10
    tx = router.functions.addLiquidityETH(USDC_address,  
                                          amountUsdc,                                                                                
                                       amountOutMin, 
                                       int(amountEth_wei * 0.99),
                                       account.address, 
                                       deadline,
                                        50, 
                                        False).build_transaction({
        'nonce': zksync_web3.eth.get_transaction_count(account.address),
        'from': account.address,
        'value': amountEth_wei,
        'gas': 15000000,
        'gasPrice': zksync_web3.eth.gas_price,
    })
    signed_tx = account.sign_transaction(tx)
    tx_hash = zksync_web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash