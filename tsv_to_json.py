import csv
import json

nodes = []
drug_list = []
effect_list = []

links = []

group_number = 1
with open("offsides_every20.tsv") as tsv:
	next(tsv)
	for line in csv.reader(tsv, dialect="excel-tab"):
		drug = line[1]
		effect = line[3]
		value = line[7]
		if drug not in drug_list:
			drug_list.append(drug)
			drug_dict = {"id": drug, "group": group_number}
			nodes.append(drug_dict)
			group_number += 1
		if effect not in effect_list:
			effect_list.append(effect)
			effect_dict = {"id": effect, "group": group_number}
			nodes.append(effect_dict)
			group_number += 1
		links_dict = {"source": drug, "target": effect, "value": value}
		if links_dict not in links:
			links.append(links_dict)


data = {"nodes": nodes, "links": links}

with open('templates/drugs_effects.json', 'w') as outfile:
    json.dump(data, outfile)



