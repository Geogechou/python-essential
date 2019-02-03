unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

while unprinted_designs:
	current_design=unprinted_designs.pop()
	print("printing model: "+current_design)
	completed_models.append(current_design)
print("\nThe folling models have been printed: ")
for completed_model in completed_models:
	print(completed_models)
