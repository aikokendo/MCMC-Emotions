#!/usr/bin/python
from random import shuffle
import copy

class Gibbs:
    def __init__(self):
        print("initializing")

    def gibbs_ask(self,x,e,bn,N):
        #returns an estimate of P(x|e)
        #prepare graph
        result = [0,0]
        bnNew = copy.deepcopy(bn)
        mNodes = bnNew.fill_nodes(e)
        myX = bnNew.get_x_node(x)
        for i in range(N):
            shufList = [i for i in range(len(mNodes))]
            shuffle(shufList)
            for z in shufList:
                ##Set value of Zj in z by sampling from P(Zj|mb(Zj))
                zState = self.mb(mNodes[z],bnNew)
                bnNew.set_state(zState,mNodes[z])
                xState = self.mb(myX,bnNew)
                if xState:
                    result[1] = result[1] + 1
                else:
                    result[0] = result[0] + 1

        total = result[0] + result[1]
        normalizedFalse = result[0]/total
        normalizedTrue = result[1]/total
        return {True: normalizedTrue, False: normalizedFalse}

    def mb(self,z,bn):
        #returns probability of Z in the markov blanket space in BN
        #P(x given mb(X)) = P(x tal que parents(X)) multiplied by the multiplication of all children Z with formula P(Z given parents(Z))
        probParent = bn.get_prob(z)
        probChild =  bn.get_prob_children(z)
        return True if probParent * probChild > 0.5 else False

