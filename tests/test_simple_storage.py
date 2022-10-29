from brownie import SimpleStorage , accounts

def test_deploy():
    # arrange 
    # acting 
    # assert
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    starting_value = simple_storage.retrive()
    expected = 0
    
    # assert
    assert starting_value == expected 
    
def test_updating_storage():
    
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from" : account})
    # acting 
    expected = 15
    simple_storage.store(expected , {"from":account})
    # assert
    assert expected==simple_storage.retrive()
    # brownie test -k  test_updating_storage
    # brownie test --pdb  : directly open python shell in terminal 
    
    
    
    