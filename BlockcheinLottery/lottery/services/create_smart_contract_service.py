from web3 import Web3
from web3 import Web3, HTTPProvider
import json
from enum import Enum
# import module
import traceback



_priceFeedAddress = "0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e"
_vrfCoordinator = "0x2Ca8E0C643bDe4C2E08ab1fA0da3401AdAD7734D"
_link = "0x326C977E6efc84E512bB9C30f76E30c160eD06FB"

# 0x160344e2

public_key = "0x132A5031a86e43338D3639071372D7394c26E927"
private_key = ""

url = "https://sepolia.infura.io/v3/763c512993564fab9aaf58f6f126924c"
bytecode = "60806040523480156200001157600080fd5b50604051620010d7380380620010d78339818101604052810190620000379190620000bb565b81600281905550806003819055506001600460006101000a81548160ff021916908360028111156200006e576200006d62000102565b5b0217905550505062000131565b600080fd5b6000819050919050565b620000958162000080565b8114620000a157600080fd5b50565b600081519050620000b5816200008a565b92915050565b60008060408385031215620000d557620000d46200007b565b5b6000620000e585828601620000a4565b9250506020620000f885828601620000a4565b9150509250929050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b610f9680620001416000396000f3fe6080604052600436106100c25760003560e01c80636b68c03c1161007f57806381447999116100595780638144799914610222578063e97dcb621461024d578063f4caee8814610257578063f71d96cb14610294576100c2565b80636b68c03c146101a15780636c082d94146101cc5780637e1a9839146101f7576100c2565b806309bc33a7146100c75780631593a8c7146100f2578063160344e214610109578063473f1ddc146101205780634c2412a21461014b5780634f8c70cf14610176575b600080fd5b3480156100d357600080fd5b506100dc6102d1565b6040516100e9919061092d565b60405180910390f35b3480156100fe57600080fd5b506101076102db565b005b34801561011557600080fd5b5061011e6104bd565b005b34801561012c57600080fd5b50610135610560565b6040516101429190610989565b60405180910390f35b34801561015757600080fd5b5061016061058a565b60405161016d919061092d565b60405180910390f35b34801561018257600080fd5b5061018b610590565b60405161019891906109c5565b60405180910390f35b3480156101ad57600080fd5b506101b66105b6565b6040516101c39190610a57565b60405180910390f35b3480156101d857600080fd5b506101e16105cd565b6040516101ee919061092d565b60405180910390f35b34801561020357600080fd5b5061020c6105d3565b604051610219919061092d565b60405180910390f35b34801561022e57600080fd5b506102376105df565b6040516102449190610a57565b60405180910390f35b6102556105f2565b005b34801561026357600080fd5b5061027e60048036038101906102799190610aa3565b610760565b60405161028b919061092d565b60405180910390f35b3480156102a057600080fd5b506102bb60048036038101906102b69190610afc565b61082e565b6040516102c891906109c5565b60405180910390f35b6000600254905090565b6002600460006101000a81548160ff02191690836002811115610301576103006109e0565b5b02179055506000808054905033444260405160200161032293929190610bc3565b6040516020818303038152906040528051906020012060001c6103459190610c3a565b90506000818154811061035b5761035a610c6b565b5b9060005260206000200160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc479081150290604051600060405180830381858888f1935050505015801561042e573d6000803e3d6000fd5b50600067ffffffffffffffff81111561044a57610449610c9a565b5b6040519080825280602002602001820160405280156104785781602001602082028036833780820191505090505b506000908051906020019061048e92919061086d565b506001600460006101000a81548160ff021916908360028111156104b5576104b46109e0565b5b021790555050565b600160028111156104d1576104d06109e0565b5b600460009054906101000a900460ff1660028111156104f3576104f26109e0565b5b14610533576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161052a90610d26565b60405180910390fd5b6000600460006101000a81548160ff02191690836002811115610559576105586109e0565b5b0217905550565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60035481565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600460009054906101000a900460ff16905090565b60025481565b60008080549050905090565b600460009054906101000a900460ff1681565b60006002811115610606576106056109e0565b5b600460009054906101000a900460ff166002811115610628576106276109e0565b5b14610668576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161065f90610d92565b60405180910390fd5b6106706102d1565b3410156106b2576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106a990610dfe565b60405180910390fd5b600354600080549050106106fb576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004016106f290610e6a565b60405180910390fd5b6000339080600181540180825580915050600190039060005260206000200160009091909190916101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b600080600090505b600080549050811015610823576000818154811061078957610788610c6b565b5b9060005260206000200160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff166040516020016107c49190610eb3565b60405160208183030381529060405280519060200120836040516020016107eb9190610ece565b6040516020818303038152906040528051906020012003610810576001915050610829565b808061081b90610f18565b915050610768565b50600090505b919050565b6000818154811061083e57600080fd5b906000526020600020016000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b8280548282559060005260206000209081019282156108e6579160200282015b828111156108e55782518260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055509160200191906001019061088d565b5b5090506108f391906108f7565b5090565b5b808211156109105760008160009055506001016108f8565b5090565b6000819050919050565b61092781610914565b82525050565b6000602082019050610942600083018461091e565b92915050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600061097382610948565b9050919050565b61098381610968565b82525050565b600060208201905061099e600083018461097a565b92915050565b60006109af82610948565b9050919050565b6109bf816109a4565b82525050565b60006020820190506109da60008301846109b6565b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602160045260246000fd5b60038110610a2057610a1f6109e0565b5b50565b6000819050610a3182610a0f565b919050565b6000610a4182610a23565b9050919050565b610a5181610a36565b82525050565b6000602082019050610a6c6000830184610a48565b92915050565b600080fd5b610a8081610968565b8114610a8b57600080fd5b50565b600081359050610a9d81610a77565b92915050565b600060208284031215610ab957610ab8610a72565b5b6000610ac784828501610a8e565b91505092915050565b610ad981610914565b8114610ae457600080fd5b50565b600081359050610af681610ad0565b92915050565b600060208284031215610b1257610b11610a72565b5b6000610b2084828501610ae7565b91505092915050565b600081905092915050565b50565b6000610b44600083610b29565b9150610b4f82610b34565b600082019050919050565b60008160601b9050919050565b6000610b7282610b5a565b9050919050565b6000610b8482610b67565b9050919050565b610b9c610b9782610968565b610b79565b82525050565b6000819050919050565b610bbd610bb882610914565b610ba2565b82525050565b6000610bce82610b37565b9150610bda8286610b8b565b601482019150610bea8285610bac565b602082019150610bfa8284610bac565b602082019150819050949350505050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b6000610c4582610914565b9150610c5083610914565b925082610c6057610c5f610c0b565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b600082825260208201905092915050565b7f43616e27742073746172742061206e6577206c6f747465727920796574000000600082015250565b6000610d10601d83610cc9565b9150610d1b82610cda565b602082019050919050565b60006020820190508181036000830152610d3f81610d03565b9050919050565b7f4e6f742073746172746564207965742100000000000000000000000000000000600082015250565b6000610d7c601083610cc9565b9150610d8782610d46565b602082019050919050565b60006020820190508181036000830152610dab81610d6f565b9050919050565b7f4e6f7420656e6f75676820455448210000000000000000000000000000000000600082015250565b6000610de8600f83610cc9565b9150610df382610db2565b602082019050919050565b60006020820190508181036000830152610e1781610ddb565b9050919050565b7f546f6f206d616e7920706c617965727300000000000000000000000000000000600082015250565b6000610e54601083610cc9565b9150610e5f82610e1e565b602082019050919050565b60006020820190508181036000830152610e8381610e47565b9050919050565b6000610e9582610b67565b9050919050565b610ead610ea8826109a4565b610e8a565b82525050565b6000610ebf8284610e9c565b60148201915081905092915050565b6000610eda8284610b8b565b60148201915081905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000610f2382610914565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8203610f5557610f54610ee9565b5b60018201905091905056fea26469706673582212202fde3be1b1be0bb6aad4786875f105dc0de7aa7aafc4a7f924453a401633726664736f6c63430008120033"

def create_smart_contract(lottery):
    web3 = Web3(Web3.HTTPProvider(url))

    abi_file = open('/Users/user/Desktop/ВШЭ/Курсовой проект/LotteryProject/BlockcheinLottery/lottery/services/lottery_abi.json')
    abi = json.load(abi_file)

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    # print(contract.functions.getEntranceFee().call())

    nonce = web3.eth.getTransactionCount(public_key)
    print("Create contract")
    print("lottery.gwei_fee: " + str(lottery.gwei_fee) + " " + str(lottery.max_players))
    transaction = contract.constructor(lottery.gwei_fee, lottery.max_players).build_transaction(
        {
            "gasPrice": web3.eth.gas_price,
            "chainId": 11155111,
            "from": public_key,
            "nonce": web3.eth.getTransactionCount(public_key),
        }
    )
    print("sign!!!")
    return transaction["data"]
    # # signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    # tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    # print("HASH")
    # print(tx_hash)
    # tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    # print("RECEIPT")
    # print(tx_receipt)
    # print(tx_receipt["contractAddress"])
    #
    # lottery.address = tx_receipt["contractAddress"]
    # lottery.save()


lottery_state = {
    -1: "Лоттерея еще не создана",
    0: "Лоттерея запущена",
    1: "Лоттерея закрыта",
    2: "Идет раассчет победителей",
}


def get_lottery_info(address, user_address):
    if address == "":
        return lottery_state[-1], 0, 0, 0
    print("Enter get lottery")
    try:
        web3 = Web3(Web3.HTTPProvider(url))
        abi_file = open('/Users/user/Desktop/ВШЭ/Курсовой проект/LotteryProject/BlockcheinLottery/lottery/services/lottery_abi.json')
        abi = json.load(abi_file)
        print("Enter to get " + address)
        contract = web3.eth.contract(address=address, abi=abi)
        print("GOT contract")
        res = contract.functions.getLotteryState().call()
        recent_winner = ""
        try:
            recent_winner = contract.functions.getRecentWinner().call()
        except:
            print("No winner")
        user_address = str(user_address)
        players_size = contract.functions.getPlayersSize().call()
        is_participating = 0
        print(user_address)
        try:
            is_participating = contract.functions.isParticipating(Web3.toChecksumAddress(user_address)).call()
        except:
            traceback.print_exc()
            print("Not started yet")
        print(res)
        print(recent_winner)
        print(players_size)
        print(is_participating)
        return lottery_state[res], recent_winner, players_size, is_participating
    except:
        #0xb19672D8E838442FFb9A354558bea2fd7f2f708b
        #0x8433e03b494ed08936ff8a9f3f9980c1dcba7c74


        traceback.print_exc()
        print("Exception")
        return lottery_state[-1], 0, 0, 0


def start_lottery_transaction(lottery):
    web3 = Web3(Web3.HTTPProvider(url))

    abi_file = open('/Users/user/Desktop/ВШЭ/Курсовой проект/LotteryProject/BlockcheinLottery/lottery/services/lottery_abi.json')
    abi = json.load(abi_file)

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    print("Contract!")
    print(web3.eth.gas_price)
    transaction = contract.functions.startLottery().build_transaction({
        "to": lottery.address,
        "gasPrice": web3.eth.gas_price,
        "chainId": 11155111,
        "from": public_key,
        "nonce": web3.eth.getTransactionCount(public_key),
    })
    print(transaction["data"])
    return transaction["data"]


def enter_lottery_transaction(lottery):
    print("enter_lottery_transaction")
    web3 = Web3(Web3.HTTPProvider(url))

    abi_file = open('/Users/user/Desktop/ВШЭ/Курсовой проект/LotteryProject/BlockcheinLottery/lottery/services/lottery_abi.json')
    abi = json.load(abi_file)

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    print("Contract!")
    print(web3.eth.gas_price)
    transaction = contract.functions.enter().build_transaction({
        "to": lottery.address,
        "gasPrice": web3.eth.gas_price,
        "chainId": 11155111,
        "from": public_key,
        "nonce": web3.eth.getTransactionCount(public_key),
        "value": lottery.gwei_fee
    })
    print(transaction["data"])
    return transaction["data"]


def end_lottery_transaction(lottery):
    web3 = Web3(Web3.HTTPProvider(url))

    abi_file = open(
        '/Users/user/Desktop/ВШЭ/Курсовой проект/LotteryProject/BlockcheinLottery/lottery/services/lottery_abi.json')
    abi = json.load(abi_file)

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    print("end_lottery!")

    transaction = contract.functions.endLottery().build_transaction({
        "to": lottery.address,
        "gasPrice": web3.eth.gas_price,
        "chainId": 11155111,
        "from": public_key,
        "nonce": web3.eth.getTransactionCount(public_key),
    })

    print(transaction["data"])

    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
    print("HASH")
    print(tx_hash)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print("RECEIPT")
    print(tx_receipt)




