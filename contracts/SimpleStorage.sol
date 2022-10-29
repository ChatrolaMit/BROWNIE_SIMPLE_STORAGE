// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {

    uint favouriteNumber ;
    bool favouriteBool ;

    struct People{
        uint256 favouriteNumber;
        string name;
    }

    People[] public people ;
    mapping(string => uint256) public nameToFavouriteNumber ;

    function store(uint256 _favoriteNumber) public {
        favouriteNumber = _favoriteNumber;
    }

    function retrive() public view returns(uint256){
        return favouriteNumber;
    }

    function addPerson(string memory _name , uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber , _name));
        nameToFavouriteNumber[_name] = _favoriteNumber;
    }


}