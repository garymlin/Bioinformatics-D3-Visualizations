import csv
import json

nodes = []
nodes_real = []
links = []
count = {}

reaction_set = set()
node_set = set()
json_data=open("gary.json").read()

data = json.loads(json_data)
# print(link_list)

for reaction in data['nodes']:
  node_set.add(reaction['id'])

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

# print(reaction_set)

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


# print count

# print nodes
data = {"nodes": nodes_real, "links": links}

with open('gary-output.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, separators=(',', ': '))



