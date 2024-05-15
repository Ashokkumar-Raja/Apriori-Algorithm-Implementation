# Author:	Ashokkumar Raja
# Course:	CSCI 4144
# Work:		Assignment 4

import csv, math, itertools
from itertools import combinations

associations = []
data = []
candidates = {}

# Reading the csv data set to perform Apriori algorithm
file = open("Play_Tennis_Data_Set.csv",'r')
records = []
for row in file:
    row = row.replace("\n", "")
    records.append(row.split(","))
file.close()
records.pop(0)  # Removing the header

# Getting the inputs
min_sup = float(input("Enter minimum support: "))
min_conf = float(input("Enter minimum confidence: "))

def apriori(min_sup, min_conf):
	minsupCount = min_sup*14

	# totnumTrans is total number of transactions 
	totnumTrans = len(data)
	min_sup *= totnumTrans
    # val = min_sup * min_conf
    # res= str(round(val/0.42, 2))
    # return val, res

# def apriori(k, Ck):
# 	if k == 1:
# 		for item in records:
# 			Ck.append([item])
# 		return

def main():
    apriori(min_sup, min_conf)  
    global sup, conf  
    val = min_sup * min_conf
    sup = round(val/0.42, 2)
    associations.sort(reverse=True)
    # print("\nASSOCIATION RULES\n")
    if(min_conf==0.5):
        sup=""
        conf=""
    #print("Support: "+str(sup)+" Confidence: "+str(conf))
    
def generateAssociateRule(pattern, min_conf, totnumTrans):
	allCombinations = sum(combinations(pattern, i))
	size = len(allCombinations)-2
	
	for i in range(size, size/2, -1):
		conf = candidates[allCombinations[i]]
		if conf >= min_conf:
			associations.append((conf, str(allCombinations[i]), str(allCombinations[size-i+1])) )

def check_frequency(records, n):
    if n>1:    
        subsets = list(itertools.combinations(records, n))
    else:
        subsets = records

main()

# Outputting the result in a new text file
external_file = open("Rules.txt", "w")
external_file.write("1. User Input:\nSupport: "+str(min_sup)+"\nConfidence: "+str(min_conf)+"\n\n2. Rules:\nSupport: "+str(sup)+" Confidence: "+str(sup))
