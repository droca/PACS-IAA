# Author: daniel roca roca486@gmail.com
# PAC 1 IAA Assets - UOC 2015

def createWebsDict(filename="webs.data"):
	# Intended dictionary output format
	# { usuari_id : 
 	#		{ web_id : { 'pagines': value, 'temps':value, 'likes':value, 'compres':value, 'opinions':value} } }

	with open(filename,'r') as dades:
		lines = [l.strip().split("\t") for l in dades.readlines()]

	dictio = {int(l[1]) : {} for l in lines}

	for l in lines:
		dictio[int(l[1])][int(l[0])] = {'pagines':int(l[2]),'temps':int(l[3]),'likes':int(l[4]),'compres':int(l[5]),'opinions':int(l[6])}

	return dictio

def transformWebsDict(dictionary):
	# Having a dictionary in this format
	# {usuari: {web:{'pagines':value, 'temps':value,... }}}
	# We transform it to a dictionary with format
	# {web: {atribut:[all values],... }}

	dictio={}
	for web in dictionary:
		for usuari in dictionary[web]:
			value_pagines = [dictionary[web][usuari]['pagines']]
			value_temps = [dictionary[web][usuari]['temps']]
			value_likes = [dictionary[web][usuari]['likes']]
			value_compres = [dictionary[web][usuari]['compres']]
			value_opinions = [dictionary[web][usuari]['opinions']]

			if not usuari in dictio:
				dictio[usuari] = {
				'pagines': value_pagines,
				'temps':value_temps,
				'likes':value_likes,
				'compres':value_compres,
				'opinions':value_opinions}
				
			else:
				dictio.get(usuari).get('pagines').extend(value_pagines)
				dictio.get(usuari).get('temps').extend(value_temps)
				dictio.get(usuari).get('likes').extend(value_likes)
				dictio.get(usuari).get('compres').extend(value_compres)
				dictio.get(usuari).get('opinions').extend(value_opinions)
	return dictio

def calculateMean(array):
	mean = sum(array)/len(array)
	return mean

def calculateMeanDictionary(dictionary):
	# Having a dictionary in this format
	# {key1: {key2:[all values],... }}
	# Calculates the mean of the values and returns a dictionary
	# With the following structure
	# {key:[mean of key2 values], ...}

	dictio = {}
	for web in dictionary:
		# Dictionary with the mean of each characteristic
		dictio[web]={
		'pagines':calculateMean(dictionary.get(web).get('pagines')),
		'temps':calculateMean(dictionary.get(web).get('temps')),
		'likes':calculateMean(dictionary.get(web).get('likes')),
		'compres':calculateMean(dictionary.get(web).get('compres')),
		'opinions':calculateMean(dictionary.get(web).get('opinions'))}
	return dictio

#dict1={'usuari_1': {'web_1': {'pagines':1, 'temps':2, 'likes':3, 'compres':4, 'opinions':5}, 'web_2': {'pagines':11, 'temps':12, 'likes':13, 'compres':14, 'opinions':15}},	'usuari_2': {'web_1': {'pagines':21, 'temps':22, 'likes':23, 'compres':24, 'opinions':25}, 'web_3': {'pagines':31, 'temps':32, 'likes':33, 'compres':34, 'opinions':35}}}
#dict2={'web_1': {'pagines':[1,21], 'temps':[2,22], 'likes':[3,23], 'compres':[4,24], 'opinions':[5,25]},'web_2': {'pagines':[11], 'temps':[12], 'likes':[13], 'compres':[14], 'opinions':[15]}}









