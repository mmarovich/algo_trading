from web3 import Web3
from dotenv import load_dotenv
import os
import time
from Modules.uniswap_abi import router_abi

load_dotenv()

w3 = Web3(Web3.HTTPProvider(f"https://goerli.infura.io/v3/{os.getenv('INFURA_KEY')}"))
print(w3.isConnected())

eth_wallet = w3.toChecksumAddress(os.getenv('ETH_ADDRESS'))
private_key = os.getenv('MM_PRIVATE_KEY')
eth_address_goerli = w3.toChecksumAddress("0x7af963cF6D228E564e2A0aA0DdBF06210B38615D")
weth_address_goerli = w3.toChecksumAddress("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
amount_to_swap = 0.3


def get_eth_balance():
    balance = w3.eth.get_balance(eth_wallet)
    return w3.fromWei(balance, "ether")

# result = get_eth_balance()
# print(result)


def uniswap_swap_function(wallet_address, from_token, to_token, amount):
    router_address = w3.toChecksumAddress("0xb4fbf271143f4fbf7b91a5ded31805e42b2208d6") # Goerli Testnet Uniswap Contract
    uniswap_abi = router_abi
    router_contract = w3.eth.contract(router_address, abi=uniswap_abi)
    
    nonce = w3.eth.getTransactionCount(wallet_address)
    
    swap_transaction = router_contract.functions.swapExactETHForTokens(
        0, # uint amountOutMin
        [from_token, to_token], # from token, to token, 
        wallet_address, # address to, 
        int(time.time()) + (60*20) # uint deadline current time + 10 mins
    ).buildTransaction({
        'nonce': nonce,
        'gas': 200000,
        'gasPrice': w3.eth.gas_price,
        'from': wallet_address,
        'value': w3.toWei(amount, 'ether')
    })
    
    gas_estimate = w3.eth.estimateGas(swap_transaction)
    
    print(f"The gas fee will be {gas_estimate}")
    
    #sign transaction & send
    sign_transaction = w3.eth.account.sign_transaction(swap_transaction, private_key)
    
    send_transaction = w3.eth.sendRawTransaction(sign_transaction.rawTransaction)
    
    #transaction hash
    print(f"Swapping {from_token} for {to_token}; TX hash: {w3.toHex(send_transaction)}")
    

uniswap_swap_function(eth_wallet, eth_address_goerli, weth_address_goerli, amount_to_swap)