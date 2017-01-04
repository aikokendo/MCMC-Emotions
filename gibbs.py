#!/usr/bin/python
import random

class Gibbs:
    def __init__(self):
        print("initializing")

    def gibbs_ask(self,x,e,bn,N):
        #returns an estimate of P(x|e)
        print(random.shuffle(['a','b','c']))

        for i in range(N):
            print('choose uniformly random non evidence node Zj')
            print('Set value of Zj in z by sampling from P(Zj|mb(Zj))')
            print('N[x] = N[x] + 1 where x is the value of X in z')
        print('return normalized(N)')

    def mb(self,z,bn):
        #returns probability of Z in the markov blanket space in BN
        print("Z")


