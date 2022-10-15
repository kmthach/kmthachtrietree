from trietree.trietree import loader

tree = loader.initialize_fit_tree()

result = tree.query('D')
print(result)