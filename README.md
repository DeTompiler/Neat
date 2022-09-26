# Neat

## About the algorithm
NEAT (NeuroEvolution of Augmenting Topologies) is a genetic algorithm for the generation of evolving artificial neural networks
developed by Kenneth Stanley.
The algorithm alters both the weights and structure of the neural network.
To dive deeper into the algorithm see the [original paper](https://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf).

This project implements the NEAT algorithm as a library using python. Using this library, you will be able to solve a wide variety of problems.

## Introduction to Neat
The core structure of the Neat library is the `Genome` structure, each genome has its own neural network which consists of several Genes. 
There are two types of genes: node genes and connection genes. Each type of gene has different properties, besides an `innovation number` which
both have (see visualization of a genome's network below).

Node Gene:
- An output
- A list of outgoing connections from the node
- An activation function
- A layer number
- An innovation number

Connection Gene:
- An input node
- An output node
- A weight
- A switch (Enabled / Disabled)

Each genome contributes to the final output of the neural network. During training the genomes are mutated, new genomes are created and some
genomes 'die', all according to their `fitness` value, which represents how well they have succeeded at a given problem - the better the fitness of
a genome compared to others the better survivability it has.

If you would like to see an example, please see this [project](https://github.com/Tompil3r/flappybird-neat) of mine. Which uses this neat library
in order to train a genome to play the famous Flappy Bird game.

---
An arbitrary representation of a genome's neural network
![genome](https://user-images.githubusercontent.com/67478051/192347330-50ee406c-5553-40b6-b7c0-5b41cbd64789.png)
