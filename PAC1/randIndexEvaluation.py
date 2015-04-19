import sklearn.metrics as metrics

# Builds the resultGrouping array, from the results tuple
def buildResultingGroupingArray(resultTuple):
	resultGrouping = []
	
	for i in range(1,len(resultTuple[0])+1):
		resultGrouping.append(resultTuple[0].get(i))

	return resultGrouping


# Evaluates the Adjusted Rand index from two different arrays
def evalRandIndex(resultGrouping, realGrouping):

	index = metrics.adjusted_rand_score(resultGrouping, realGrouping)
	return index
	