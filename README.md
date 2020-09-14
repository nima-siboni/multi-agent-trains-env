# multi-agent-trains-env

A new environment simulate motion of a number of trains on a railway network is presented. This environmnet is developed to be suitable for testing and development of new multi-agent reinforcement learning algorithms.

<img src="./images_for_animation/animation.gif" width="50%">

## Problem statement
The environment consists of a number of trains (agents) which are moving on a rail-network. The goal of the agents are to take their passangers *safely* and *efficiently* to their destinations. The defintions of the safety and efficiency are mentioned below. 

Each train has:
* an origin (where it starts from), 
* a destination (where it goes to), and 
* a number of passangers on-board.

Here by safety, we mean that the trains do not occupy same segment of railway; in other words, they do not cause any conflict. For the railway network implemented here, the agents would only have conflicts when they get to the middle part of the network. In principle, if that segment is occupied by a train, all the other trains behind it should avoid getting on that segment, until the segment becomes free.

Here is an animation of an instance of the environment for four agents. The agents have different number of passangers (mentioned by the numbers shown on top of them), and aim at reaching the their targets (blue squares). 
Each agent can take two actions:
* stay at the curre
