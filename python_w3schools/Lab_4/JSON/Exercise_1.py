import json

f = open('/Users/octofort/Desktop/University/PP2/python/python_w3schools/Lab_4/JSON/sample-data.json')

filee = json.load(f)

print("Interface Status")
print("============================================================================================")
print("DN                                                 Description           Speed        MTU  ")
print("-------------------------------------------------- --------------------  -------      ------")

for i in range(len(filee['imdata'])):
    print(filee['imdata'][i]['l1PhysIf']['attributes']['dn'], '\t\t\t\t', filee['imdata'][i]['l1PhysIf']['attributes']['speed'], '    ', filee['imdata'][i]['l1PhysIf']['attributes']['mtu'])

f.close()