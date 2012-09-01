#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''
Code from Machine Learning in Action.
'''
import csv
from numpy import *
import json

def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def do_train_NB(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pClass1 = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
    p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)          #change to log()
    p0Vect = log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pClass1

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0
    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2] 
    

def prepare_training(left_posts, right_posts):
    docList=[]; classList = []; fullText =[]

    for post in left_posts:
        wordList = textParse(post['clean_text'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)

    for post in right_posts:
        wordList = textParse(post['clean_text'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)

    total = len(left_posts) + len(right_posts)
    vocabList = createVocabList(docList)#create vocabulary
    
    trainingSet = range(total); testSet=[]           #create test set
    test_set_total = int(total * 0.2)
    for i in range(test_set_total):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])  
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) do_train_NB
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pClass1 = do_train_NB(array(trainMat), array(trainClasses))
    
    #testing the platform
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pClass1) != classList[docIndex]:
            errorCount += 1
            #print "classification error",docList[docIndex]
    print 'the error rate is: ',float(errorCount)/len(testSet)
    import pdb;pdb.set_trace()
    return p0V, p1V, pClass1, vocabList




