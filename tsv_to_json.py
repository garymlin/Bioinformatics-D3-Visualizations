import csv
import json

nodes = []
drug_list = []
pair_dict = {}
effect_list = []

links = []

group_number = 1
# num_lines = 0
with open("twosides_every20_first50000.tsv") as tsv:
	next(tsv)
	for line in csv.reader(tsv, dialect="excel-tab"):
		# num_lines += 1
		# if num_lines % 50 == 0:

		drug1 = line[2]
		drug2 = line[3]
		value = line[7]
		if drug1 not in drug_list:
			drug_list.append(drug1)
			drug_dict = {"name": drug1, "group": group_number}
			pair_dict[drug1] = drug2
			pair_dict[drug2] = drug1
			nodes.append(drug_dict)
			group_number += 1

with open("twosides_every20_first50000.tsv") as tsv:
	next(tsv)
	for line in csv.reader(tsv, dialect="excel-tab"):
		drug1 = line[2]
		drug2 = line[3]
		value = line[7]

		try:
			drug1_index = drug_list.index(drug1)
			drug2_index = drug_list.index(drug2)
		except ValueError:
			continue

		links_dict = {"source": drug1_index, "target": drug2_index, "value": value}
		if links_dict not in links:
			links.append(links_dict)


data = {"nodes": nodes, "links": links}

with open('templates/drugs_effects_twosides_first50000.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, separators=(',', ': '))



