# icon-worker-proposal

#### Start local node with Docker

```
$ docker pull iconloop/tbears:mainnet

$ docker run -it -p 9000:9000 iconloop/tbears:mainnet

$ docker exec -it tbears-container /bin/bash

# check wallet address
$ tbears keyinfo keystore_test1 -p test1_Account
{
    "address": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
    "publicKey": "0x04855312cefe3b6c7e86bbaec089f79376e9bb3c19c84b73492d0d5e4d2dbdd4bec1c8c9ddc55715b70ed920d08d1621f20ffaf0d09e5afc97fb1d327ea7070084"
}
```

#### Deploy

```

# tbears deploy  worker_proposal/ -c worker_proposal/deploy_contract.json -k keystore_test1 -p test1_Account
transaction hash: 0xab5506d00eda472376a8a054ca3244bf15054eb46d567a466c205e45738c018a

# tbears txresult 0xab5506d00eda472376a8a054ca3244bf15054eb46d567a466c205e45738c018a
Transaction : {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0xab5506d00eda472376a8a054ca3244bf15054eb46d567a466c205e45738c018a",
        "blockHeight": "0x7b",
        "blockHash": "0x4241cbf72b5847da1c945a615e40243ae99264828e1f3ce4071e13a157fe68d0",
        "txIndex": "0x0",
        "to": "cx0000000000000000000000000000000000000000",
        "scoreAddress": "cxa5d3d0a98ec377fdbcc8a75cad70f989d6cb9307",
        "stepUsed": "0x45e6bf3c",
        "stepPrice": "0x2540be400",
        "cumulativeStepUsed": "0x45e6bf3c",
        "eventLogs": [],
        "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "status": "0x1"
    },
    "id": 1234
}

# tbears call worker_proposal/get_configuration.json 
response : {
    "jsonrpc": "2.0",
    "result": {
        "admin_addr": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "voting_period_by_block": "0x7d0",
        "approval_pct": "0x46"
    },
    "id": 1234
}

# to update

# tbears deploy  worker_proposal/ -c worker_proposal/update_contract.json -k keystore_test1 -p test1_Account
```

#### Create list wallet for PRep and deposit some ICX to have a fee to send transaction.

```
# create wallet

# python3
>>> from iconsdk.wallet.wallet import KeyWallet

>>> wallet = KeyWallet.create(); wallet.get_address(); wallet.get_private_key(); wallet.store('./keystore_test2', 'test2_Account')
'hx2e2a15df1f2bd0beb7849d3ef501a5413260081a'
'273527fd433b0d2a8d60119323e5bf38eb458edd8e506ccafccbf9be9b6b655b'

>>> wallet = KeyWallet.create(); wallet.get_address(); wallet.get_private_key(); wallet.store('./keystore_test3', 'test3_Account')
'hx97b16930acf3ff760b4816d2811fffffa72afd8c'
'fb2157fafd7f6a53f2dd3b2027a4927870c14706ac704c22ba0b8bf5ef500a4b'

>>> wallet = KeyWallet.create(); wallet.get_address(); wallet.get_private_key(); wallet.store('./keystore_test4', 'test4_Account')
'hx095c941aef40bbe0e4812463237c610551819e84'
'649a1882c5eca160de1d4ce86fcc6e24f233496b2471e77ee6e84a9f29a37610'

>>> wallet = KeyWallet.create(); wallet.get_address(); wallet.get_private_key(); wallet.store('./keystore_test5', 'test5_Account')
'hx29af0b38aeede2781747fb9603a98cbe9de45828'
'6deeac0b6512d988463194bf73c0ae27080c59bc4433973c675730d9a0f32e99'

>>> wallet = KeyWallet.create(); wallet.get_address(); wallet.get_private_key(); wallet.store('./keystore_test6', 'test6_Account')
'hxc46e0885fa21286e6a415469fc1c7225354c5096'
'361579ace27357c5db9e441e6b9366669dc6fce481b4abcbaa7523fe60ad66fe'

# transfer fund 

# tbears transfer hx2e2a15df1f2bd0beb7849d3ef501a5413260081a 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hx97b16930acf3ff760b4816d2811fffffa72afd8c 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hx095c941aef40bbe0e4812463237c610551819e84 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hx29af0b38aeede2781747fb9603a98cbe9de45828 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hxc46e0885fa21286e6a415469fc1c7225354c5096 159895481589799999996000 -k keystore_test1 -p test1_Account

# trannfer fund to smart contract

# tbears transfer cxa5d3d0a98ec377fdbcc8a75cad70f989d6cb9307 159895481589799999996000 -k keystore_test1 -p test1_Account
```


#### config system

```
# tbears sendtx worker_proposal/config_System.json -k keystore_test1 -p test1_Account
Send transaction request successfully.
transaction hash: 0xef39c629d23c9f5e9a1d9c16041e63ea0e67136e9dc1247e9e2dff077a7237af

# tbears call worker_proposal/get_configuration.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "admin_addr": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "voting_period_by_block": "0x7d0",
        "approval_pct": "0x45"
    },
    "id": 1234
}

```

#### set PRep list

```
# modify the param prep_address in set_PREP.json as follwoing: hx2e2a15df1f2bd0beb7849d3ef501a5413260081a, hx97b16930acf3ff760b4816d2811fffffa72afd8c, hx095c941aef40bbe0e4812463237c610551819e84, hx29af0b38aeede2781747fb9603a98cbe9de45828, hxc46e0885fa21286e6a415469fc1c7225354c5096, then call 

tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account
tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account
tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account
tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account

# tbears call worker_proposal/get_prep.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "preps": [
            "hx2e2a15df1f2bd0beb7849d3ef501a5413260081a",
            "hx97b16930acf3ff760b4816d2811fffffa72afd8c",
            "hx095c941aef40bbe0e4812463237c610551819e84",
            "hx29af0b38aeede2781747fb9603a98cbe9de45828",
            "hxc46e0885fa21286e6a415469fc1c7225354c5096"
        ]
    },
    "id": 1234
}
```

#### Create propose

```
tbears sendtx worker_proposal/create_Proposal.json -k keystore_test1 -p test1_Account

# tbears call worker_proposal/get_proposals.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "proposals": [
            "Propose3"
        ]
    },
    "id": 1234
}

# tbears call worker_proposal/get_proposal.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "owner_address": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "amount": "0x45",
        "cycle_num": "0x5",
        "cycle_duration_by_block": "0x12",
        "current_cycle": "0x0",
        "description": "description",
        "sponsor": "",
        "voting_start_at_block": "0x0",
        "voting_end_at_block": "0x0",
        "voting_list": [],
        "voting_pct": "0x0"
    },
    "id": 1234
}
```

#### Need an PRep sponsor the project

```
tbears sendtx worker_proposal/sponsor_Proposal.json -k keystore_test2 -p test2_Account

# tbears call worker_proposal/get_proposal.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "owner_address": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "amount": "0x45",
        "cycle_num": "0x5",
        "cycle_duration_by_block": "0x12",
        "current_cycle": "0x0",
        "description": "description",
        "sponsor": "hx2e2a15df1f2bd0beb7849d3ef501a5413260081a",
        "voting_start_at_block": "0x4f5",
        "voting_end_at_block": "0xcc5",
        "voting_list": [],
        "voting_pct": "0x0"
    },
    "id": 1234
}
```

#### Vote for sponsored project

```
tbears sendtx worker_proposal/vote_Proposal.json -k keystore_test2 -p test2_Account

tbears sendtx worker_proposal/vote_Proposal.json -k keystore_test3 -p test3_Account

tbears sendtx worker_proposal/vote_Proposal.json -k keystore_test4 -p test4_Account

tbears sendtx worker_proposal/vote_Proposal.json -k keystore_test5 -p test5_Account

# tbears call worker_proposal/get_proposal.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "owner_address": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "amount": "0x45",
        "cycle_num": "0x5",
        "cycle_duration_by_block": "0x12",
        "current_cycle": "0x0",
        "description": "description",
        "sponsor": "hx2e2a15df1f2bd0beb7849d3ef501a5413260081a",
        "voting_start_at_block": "0xb66",
        "last_claim_at_block": "0xb66",
        "voting_end_at_block": "0x1336",
        "voting_list": [
            {
                "name": "hx2e2a15df1f2bd0beb7849d3ef501a5413260081a",
                "status": "0x1"
            },
            {
                "name": "hx97b16930acf3ff760b4816d2811fffffa72afd8c",
                "status": "0x1"
            },
            {
                "name": "hx095c941aef40bbe0e4812463237c610551819e84",
                "status": "0x1"
            },
            {
                "name": "hx29af0b38aeede2781747fb9603a98cbe9de45828",
                "status": "0x0"
            }
        ],
        "voting_pct": 75.0
    },
    "id": 1234
}
```

#### Claim Payment

```
# tbears sendtx worker_proposal/claim_Payment.json -k keystore_test1 -p test1_Account
Send transaction request successfully.
transaction hash: 0xaacff0f8da486f9196cbaa9100456bf020c8df45973191d923ca6552784c0ec3
# tbears txresult 0xaacff0f8da486f9196cbaa9100456bf020c8df45973191d923ca6552784c0ec3
Transaction : {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0xaacff0f8da486f9196cbaa9100456bf020c8df45973191d923ca6552784c0ec3",
        "blockHeight": "0x14a3",
        "blockHash": "0xd28054fede2aa416ee7d1c296be30e3d75fffc7ea474445a434b60394bb454f4",
        "txIndex": "0x0",
        "to": "cxa5d3d0a98ec377fdbcc8a75cad70f989d6cb9307",
        "stepUsed": "0xe49f8",
        "stepPrice": "0x2540be400",
        "cumulativeStepUsed": "0xe49f8",
        "eventLogs": [
            {
                "scoreAddress": "cxa5d3d0a98ec377fdbcc8a75cad70f989d6cb9307",
                "indexed": [
                    "ICXTransfer(Address,Address,int)",
                    "cxa5d3d0a98ec377fdbcc8a75cad70f989d6cb9307",
                    "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
                    "0x45"
                ],
                "data": []
            },
            {
                "scoreAddress": "cxa5d3d0a98ec377fdbcc8a75cad70f989d6cb9307",
                "indexed": [
                    "FundTransfer(Address,int,int)",
                    "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb"
                ],
                "data": [
                    "0x45",
                    "0x5"
                ]
            }
        ],
        "logsBloom": "0x00000000000000000000000100000000840000000000000000000000000000000010000000000000000000000000000000400000000000000000080000000000000000000000000000000000000000000000000000000000000000200000000000000000000002000010000000400000000000000000000000000000000000004000000000000000000000000000000000000000000000000000002000000000001000000000000000000000000000002000000000000000000000010000000000000000000000000000000000000000000000000000000208000000000200800080000000000000000000000000800000000000000000000000000000000000",
        "status": "0x1"
    },
    "id": 1234
}

# tbears call worker_proposal/get_proposal.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "owner_address": "hxe7af5fcfd8dfc67530a01a0e403882687528dfcb",
        "amount": "0x45",
        "cycle_num": "0x5",
        "cycle_duration_by_block": "0x12",
        "current_cycle": "0x5",
        "description": "description",
        "sponsor": "hx2e2a15df1f2bd0beb7849d3ef501a5413260081a",
        "voting_start_at_block": "0xb66",
        "last_claim_at_block": "0xb66",
        "voting_end_at_block": "0x1336",
        "voting_list": [
            {
                "name": "hx2e2a15df1f2bd0beb7849d3ef501a5413260081a",
                "status": "0x1"
            },
            {
                "name": "hx97b16930acf3ff760b4816d2811fffffa72afd8c",
                "status": "0x1"
            },
            {
                "name": "hx095c941aef40bbe0e4812463237c610551819e84",
                "status": "0x1"
            },
            {
                "name": "hx29af0b38aeede2781747fb9603a98cbe9de45828",
                "status": "0x0"
            }
        ],
        "voting_pct": 75.0
    },
    "id": 1234
}
```