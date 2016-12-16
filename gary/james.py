import csv
import json


version = "10000"

nodes = []
nodes_real = []
nodes_final = []
links_final = []
links = []
count = {}

reaction_set = set()
node_set = set()

doc1 = "offsides_first" + version + ".json"
json_data=open(doc1).read()

data = json.loads(json_data)
# print(link_list)

### Data sanitization ###
for reaction in data['nodes']:
  node_set.add(reaction['id'])

# print node_set

for link in data['links']:
  if ((link['source'] in node_set) and (link['target'] in node_set)):
    if (float(link['value']) > 0.0001):
      # print (link['value'])
      # print (0.01)
      # print(link['value'] > 0.01)
      links.append(link)

for link in links:
  reaction_set.add(link["source"])
  reaction_set.add(link["target"])

# print reaction_set 

for reaction in data['nodes']:
  if (reaction['id'] in reaction_set):
    nodes.append(reaction)

for link in links:
  if link["source"] in count:
    val = count[link["source"]]
    val = val + 1
    count[link["source"]] = val
  else:
    count[link["source"]] = 1

  if link["target"] in count:
    val2 = count[link["target"]]
    val2 = val2 + 1
    count[link["target"]] = val2
  else:
    count[link["target"]] = 1

for node in nodes:
  if (float(count[node['id']]) > 1):
    node['name'] = node['id']
  nodes_real.append(node)



event_to_umls = {}
umls_to_physio = {}
event_to_physio = {}
physio_to_num = {}
drug_to_stitch = {}
physio_num = 1



# Adding physiological info to event data
doc2 = "offsides_first" + version + ".tsv"
with open(doc2) as tsv:
  next(tsv)
  for line in csv.reader(tsv, dialect="excel-tab"):
    if line[3] not in event_to_physio:
      event_to_umls[line[3]] = line[2]
    if line[1] not in drug_to_stitch:
      drug_to_stitch[line[1]] = line[0]

with open("costart_categories.csv") as csv_obj:
  next(csv_obj)
  for line in csv.reader(csv_obj, dialect="excel"):
    if line[0] not in umls_to_physio:
      umls_to_physio[line[0]] = line[3]
    if line[3] not in physio_to_num:
      physio_to_num[line[3]] = physio_num
      physio_num = physio_num + 1

for event in event_to_umls:
  umls = event_to_umls[event]
  if umls in umls_to_physio:
    event_to_physio[event] = umls_to_physio[umls]

# print event_to_physio

count = 0
for node in nodes_real:
  if node["id"] in event_to_physio:
    node["physio"] = event_to_physio[node["id"]]
    node["color_from_physio"] = physio_to_num[event_to_physio[node["id"]]]
    count = count + 1
  if node["id"] in drug_to_stitch:
    node["display_id"] = node["id"]

# print count

for node in nodes_real:
  if "display_id" in node:
    nodes_final.append(node)
  elif "physio" in node:
    nodes_final.append(node)

for node in nodes_final:
  if "display_id" not in node:
    node["display_id"] = node["physio"] + ": " + node["id"]


nodes_map = {}
for node in nodes_final:
  # print node["id"]
  nodes_map[node["id"]] = "a"


# for physio in physio_to_num:
#   print physio
#   mid = {}
#   mid["id"] = physio
#   mid["display_id"] = physio
#   mid["color_from_physio"] = physio_to_num[physio]
#   nodes_final.append(mid)


for link in links:
  if link["source"] in nodes_map and link["target"] in nodes_map:
    links_final.append(link)
# print len(nodes_final)

# print nodes
data = {"nodes": nodes_final, "links": links_final}

output = "final-" + version + ".json"
with open(output, 'w') as outfile:
    json.dump(data, outfile, indent=4, separators=(',', ': '))



