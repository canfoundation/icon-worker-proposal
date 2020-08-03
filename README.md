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

# tbears deploy  worker_proposal/ -k keystore_test1 -p test1_Account
transaction hash: 0xcf2df776c49b265e0b25829671b6a77c770ec4241b5220c6976423d90e582395

# tbears txresult 0xcf2df776c49b265e0b25829671b6a77c770ec4241b5220c6976423d90e582395
Transaction : {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0xcf2df776c49b265e0b25829671b6a77c770ec4241b5220c6976423d90e582395",
        "blockHeight": "0x7b",
        "blockHash": "0x4241cbf72b5847da1c945a615e40243ae99264828e1f3ce4071e13a157fe68d0",
        "txIndex": "0x0",
        "to": "cx0000000000000000000000000000000000000000",
        "scoreAddress": "cx525a1cd872f7478a8be38e5adbfe9a709437201f",
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
```

#### Create list wallet for PRep and deposit some ICX to have a fee to send transaction.

```
# create wallet

# python3

>>> from iconsdk.wallet.wallet import KeyWallet

>>> wallet = KeyWallet.create()
>>> wallet.get_address()
'hxdfd0a643babbe0b8ba8136e8214b5c2762e3ee6b'
>>> wallet.get_private_key()
'cb0ebd5139b98df1b905f1c55a36b744985dfd42b2844a5fdc5a5606a0741c20'
>>> wallet.store('./keystore_test2', 'test2_Account')

>>> wallet = KeyWallet.create()
>>> wallet.get_address()
'hx22f2ce0b544d5b90db1d33542eaeb885994ced45'
>>> wallet.get_private_key()
'a2ae41ee5309944344f73fcc3342c6a9ee65e493626d017258d1cb9770f1f4e3'
>>> wallet.store('./keystore_test3', 'test3_Account')

>>> wallet.get_address()
'hxe3f8037725e52385de52eb235697a84a98b25254'
>>>  wallet.get_private_key()
>>> wallet.get_private_key()
'02f2b5c6fa12c6c95c3d0da033b8c73620ed745c361969b9b1068653fa3ac7e5'
>>> wallet.store('./keystore_test4', 'test4_Account')

>>> wallet = KeyWallet.create()
>>> wallet.get_address()
'hxb3bcc8945b4c77f3ebe8198fe3180f43b50c4767'
>>> wallet.get_private_key()
'0677c6873759e17b4769a8af16391015ddd5579769b5c2a7973788120b9f235a'
>>> wallet.store('./keystore_test5', 'test5_Account')

# transfer fund 

# tbears transfer hxdfd0a643babbe0b8ba8136e8214b5c2762e3ee6b 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hx22f2ce0b544d5b90db1d33542eaeb885994ced45 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hxe3f8037725e52385de52eb235697a84a98b25254 159895481589799999996000 -k keystore_test1 -p test1_Account
# tbears transfer hxb3bcc8945b4c77f3ebe8198fe3180f43b50c4767 159895481589799999996000 -k keystore_test1 -p test1_Account

```


#### config system

```
# tbears sendtx worker_proposal/config_System.json -k keystore_test1 -p test1_Account
Send transaction request successfully.
transaction hash: 0x2da4612dde3bd0573f7acbfd1732a4bed82fb902e8969db4590c82ad86605c50
root@adf55b4838ac:/work# tbears txresult 0x2da4612dde3bd0573f7acbfd1732a4bed82fb902e8969db4590c82ad86605c50
Transaction : {
    "jsonrpc": "2.0",
    "result": {
        "txHash": "0x2da4612dde3bd0573f7acbfd1732a4bed82fb902e8969db4590c82ad86605c50",
        "blockHeight": "0x16c",
        "blockHash": "0x2cd975893999de50c03b4d3e26992a67af99a2827ba10c145430cfb4cfbea7cb",
        "txIndex": "0x0",
        "to": "cx525a1cd872f7478a8be38e5adbfe9a709437201f",
        "stepUsed": "0x52954",
        "stepPrice": "0x2540be400",
        "cumulativeStepUsed": "0x52954",
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
        "approval_pct": "0x45"
    },
    "id": 1234
}

```

#### set PRep list

```
# modify the param prep_address in set_PREP.json as follwoing: hxdfd0a643babbe0b8ba8136e8214b5c2762e3ee6b, hx22f2ce0b544d5b90db1d33542eaeb885994ced45, hxe3f8037725e52385de52eb235697a84a98b25254, hxb3bcc8945b4c77f3ebe8198fe3180f43b50c4767, then call 

tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account
tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account
tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account
tbears sendtx worker_proposal/set_PRep.json -k keystore_test1 -p test1_Account

# tbears call worker_proposal/get_prep.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "preps": [
            "hxdfd0a643babbe0b8ba8136e8214b5c2762e3ee6b",
            "hx22f2ce0b544d5b90db1d33542eaeb885994ced45",
            "hxe3f8037725e52385de52eb235697a84a98b25254",
            "hxb3bcc8945b4c77f3ebe8198fe3180f43b50c4767"
        ]
    },
    "id": 1234
}
```

#### Create propose

```

# tbears call worker_proposal/get_prep.json
response : {
    "jsonrpc": "2.0",
    "result": {
        "preps": [
            "hxdfd0a643babbe0b8ba8136e8214b5c2762e3ee6b",
            "hx22f2ce0b544d5b90db1d33542eaeb885994ced45",
            "hxe3f8037725e52385de52eb235697a84a98b25254",
            "hxb3bcc8945b4c77f3ebe8198fe3180f43b50c4767"
        ]
    },
    "id": 1234
}
```