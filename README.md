# multi-agent-trains-env

A new environment simulate motion of a number of trains on a railway network is presented. This environmnet is developed to be suitable for testing and development of new multi-agent reinforcement learning algorithms.

<img src="./images_for_animation/animation.gif" width="50%">

## Problem statement
The environment consists of a number of trains (agents) which are moving on a rail-network. The goal of the agents are to take their passangers **safely** and **efficiently** to their destinations. The defintions of the safety and efficiency are mentioned below. 

Each train has:
* an origin (where it starts from), 
* a destination (where it goes to), and 
* a number of passangers on-board.

**Safety**: A safe solution is a solution with zero number of *conflicts*. Here, a conflict occurs when more than one trains are on the the same rail segment. For the railway network implemented here, the agents would only have conflicts when they get to the middle part of the network. In principle, if that segment is occupied by a train, all the other trains behind it should avoid getting on that segment, until the segment becomes free. 

**Efficiency**: A solution is efficient if the total amount of waiting time of all the passangers is minimized. Naturally, this leads to higher priority for the trains with larger number of agents.



An animation of an instance of the environment for four agents is shown above. The numbers shown on top of the trains represent the number of passangers, and destinations are represented by blue squares. 

## The enviornment

In the environment the agents are presented by their state which changes by the actions they take. As a result of taking actions, the environment produces a reward.

### 1- Agent state
The state of each agent is a tuple:
* an integer number specifying is the position of agent on the track, and
* an integer number representing the number of passangers on the train.

The global state is the concatnation of the states of all agents.

### 2- Agent actions

Each agent can take two actions:

* stay at the current position (action number 0)
* advance one step forward (action number 1).

### 3- Reward Engineering

This is the most tricky part! Here I have 

