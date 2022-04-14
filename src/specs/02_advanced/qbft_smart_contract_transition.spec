# QBFT consensus - Legacy Istanbul to QBFT Smart Contract Validators Network

  Tags: networks/template::qbft-4nodes-smart-contract-transition, pre-condition/no-record-blocknumber, qbft-smart-contract-transition-network

This specification describes backwards compatiblity with legacy istanbul network
 - Starts with a 4 node Legacy Istanbul network
 - Transition to QBFT Smar Contract Consensus at a predifined block

## Verify transition network

  Tags: post-condition/datadir-cleanup, post-condition/network-cleanup

* Start a Quorum Network, named it "mynetwork", consisting of "Node1,Node2,Node3,Node4"
* Verify nodes "Node1,Node2,Node3,Node4" are using "ibft" consensus
* Send some transactions to create blocks in network "mynetwork" and capture the latest block height as "latestBlockHeight"
* Verify nodes "Node1,Node2,Node3,Node4" have a block height less than or equal to "latestBlockHeight"
* Verify nodes "Node1,Node2,Node3,Node4" are using "ibft" consensus
* Wait to catch up block "100"
* Verify nodes "Node1,Node2,Node3,Node4" are using "QBFT" consensus
* Verify nodes "Node1,Node2,Node3,Node4" are using are using smart contract validators
* Send some transactions to create blocks in network "mynetwork" and capture the latest block height as "latestBlockHeight"
* Verify nodes "Node1,Node2,Node3,Node4" are using are using smart contract validators
