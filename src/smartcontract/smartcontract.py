from   web3 import  Web3
def voting_data(_):
    eth_url= "#"
    web3 = Web3(Web3.HTTPProvider(eth_url))
    print(web3.is_connected())

    polling_station, polling_clerk,votes_counted,date_transmitted = [], []
    event_signature = "LogData(uint256,string,address,uint256)"

    logs = web3.eth.get_logs(
        {
            "address": "eth_address", #to be added
            "fromBlock": 1444600, # to be added from eth dashboard
            "toBlock": 1587223,  # to be added from eth dashboard
            "topics": [web3.keccak(text=event_signature).hex()],
        }
    )

    for log in logs:
        print(log)
        event_data = {
            "polling_station": web3.to_text(log["data"][-64:]),
            "polling_clerk": web3.to_text(log["data"][-64:]),
            "votes_counted": int.from_bytes(log["topics"][1], byteorder="big"),
            "date_transmitted": web3.to_text(log["data"][-64:]),
        }

        print(event_data["polling_station"], event_data["polling_clerk"],event_data["votes_counted"], event_data["date_transmitted"])
