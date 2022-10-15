from trietree.trietree import loader

tree = loader.initialize_fit_tree()

print(tree.query('D'))