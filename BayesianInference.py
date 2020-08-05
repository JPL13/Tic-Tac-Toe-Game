"""
Class: Stat232C
Project 1: Bayesian inference
Name: 
Date: April 2020

"""

def getPosterior(priorOfA, priorOfB, likelihood):
	
##################################################
#		Your code here
##################################################
    marginalOfA= {key: None for key in priorOfA}
    marginalOfB= {key: None for key in priorOfB}
    temp ={key: None for key in likelihood}
    #print (priorOfB)
    
    
    for key, value in likelihood.items():
        temp[key] = value * priorOfA[key[0]] * priorOfB[key[1]] 
        #print(priorOfB[key[1]])
    
    marginalOfData=sum(temp.values())
            
    for a in marginalOfA:
        
        marginalOfA[a]= sum(d for k, d in temp.items() if k[0] == a) /marginalOfData
    
   
    for b in marginalOfB:
        
        marginalOfB[b]= sum(d for k, d in temp.items() if k[1] == b) /marginalOfData            
    

    return([marginalOfA, marginalOfB])



def main():
    exampleOnePriorofA = {'a0': .5, 'a1': .5}
    exampleOnePriorofB = {'b0': .25, 'b1': .75}
    exampleOneLikelihood = {('a0', 'b0'): 0.42, ('a0', 'b1'): 0.12, ('a1', 'b0'): 0.07, ('a1', 'b1'): 0.02}
    print(getPosterior(exampleOnePriorofA, exampleOnePriorofB, exampleOneLikelihood))

    exampleTwoPriorofA = {'red': 1/10. , 'blue': 4/10., 'green': 2/10., 'purple': 3/10.}
    exampleTwoPriorofB = {'x': 1/5., 'y': 2/5., 'z': 2/5.}
    exampleTwoLikelihood = {('red', 'x'): 0.2, ('red', 'y'): 0.3, ('red', 'z'): 0.4, ('blue', 'x'): 0.08, ('blue', 'y'): 0.12, ('blue', 'z'): 0.16, ('green', 'x'): 0.24, ('green', 'y'): 0.36, ('green', 'z'): 0.48, ('purple', 'x'): 0.32, ('purple', 'y'): 0.48, ('purple', 'z'): 0.64}
    print(getPosterior(exampleTwoPriorofA, exampleTwoPriorofB, exampleTwoLikelihood))




if __name__ == '__main__':
    main()
