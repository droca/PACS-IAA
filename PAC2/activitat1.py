# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp

# --- Activitat 1  --- #
rawData = fp.readFileData()
print("The number of components needed for the 95% variance acceptance is: ", 
	fp.pcaComponentsCalc(rawData))



