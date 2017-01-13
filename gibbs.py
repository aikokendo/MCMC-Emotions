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
        #P(x given mb(X)) = P(x given parents(X)) multiplied by the multiplication
        # of all children Z with formula P(Z given parents(Z))
        probParent = bn.get_prob(z)
        probChild =  bn.get_prob_children(z)
        return bn.def_new_state(probParent*probChild, z)


    def formatted_result(self,x,e,bn,N):
        result = self.gibbs_ask(x,e,bn,N)
        nodeLabels = {'s':'sunny','w':'windy','c':'cloudy','r':'rainy','e':'energized','p':'pleasant','sp':'sports',
                      'co':'community','cl':'clubs','le':'learn','ar':'arts','st':'st','m':'male','a':'adult'}
        text = "probability of '" +  nodeLabels[bn.nodes[x].label] + "' given "
        for item in e:
            text += nodeLabels[item[0]] + "=" + str(e[item]) + ", "
        text = text + " is: " + str(result)
        return text

