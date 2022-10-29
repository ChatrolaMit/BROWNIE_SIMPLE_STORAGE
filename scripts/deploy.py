from brownie import accounts , config , SimpleStorage , network
import os

def deploy_simple_storage() :
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from" : account})
    print(simple_storage)
    
    stored_value = simple_storage.retrive()
    print(stored_value)
    
    transaction = simple_storage.store(15 , {"from" : account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrive()
    print(updated_stored_value)
    
def get_account():
    if network.show_active()=="development" :
        return accounts[0]
    else :
        return accounts.add(config["wallets"]["from_key"])
     
    
    
    

    
    # print(account)
    # account = accounts.load("alive")
    # print(account)
    # account  = accounts.add(os.getenv("PRIVATE_KEY"))
    # account  = accounts.add(config["wallets"]["from_key"])
    # print(account)


def main() : 
    deploy_simple_storage()
        
    