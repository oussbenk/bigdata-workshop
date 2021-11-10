#!/usr/bin/python
import sys
salesTotal = 0
oldKey = None
maxSales = 0	# Variable de recherche de max de ventes

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	thisKey, thisSale = data
	if oldKey and oldKey != thisKey:
		# Comparer les ventes totales avec le max intermédiaire
		# Si dépasse max, mettre à jour clé max (nom magasin) et ventes
		if salesTotal>maxSales:
			maxKey = oldKey
			maxSales = salesTotal
		salesTotal = 0
	
	oldKey = thisKey
	salesTotal += float(thisSale)

if oldKey != None:
	if salesTotal>maxSales:
		maxKey = oldKey
		maxSales = salesTotal

print "{0}\t{1}".format(maxKey, maxSales)