# Leader Election using Bully Algorithm

Leader election is a primary problem in distributed systems wherein nodes collectively choose a leader to coordinate and manage activities. Various algorithms exist for leader election, each with its advantages and limitations. In this code, I have implemented a leader election
algorithm using Python's threading module to simulate a distributed system. 

# Concept
The Bully Algorithm is based on the notion that coordinator is chosen whose node has highest ID in the network. In case a coordinator fails, the other nodes in the network will start an election process to choose a new coordinator.


# Usage

Nodes independently elect a leader amongst themselves using a Bully Algorithm 