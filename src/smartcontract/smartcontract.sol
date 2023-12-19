pragma solidity ^0.8.18;

contract Voting {
    address payable public onlineEducator;

    event LogData(
        string polling_station,
        string polling_clerk,
        uint256 indexed votes_counted,
        address donatorAddress,
        uint256 timestamp
    );

}                                                                          