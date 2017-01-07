#!/usr/bin/python
from random import shuffle

class Gibbs:
    def __init__(self):
        print("initializing")

    def gibbs_ask(self,x,e,bn,N):
        #returns an estimate of P(x|e)
        for i in range(N):
            #create uniform random sample to select a Zj per iteration
            x = [i for i in range(10)] #to change to size of BN - size of Evidence
            shuffle(x)
            for z in x:
                print('Set value of Zj in z by sampling from P(Zj|mb(Zj))')
                print('N[x] = N[x] + 1 where x is the value of X in z')
        print('return normalized(N)')

    def mb(self,z,bn):
        #returns probability of Z in the markov blanket space in BN
        print("Z")


