from trietree.trietree import loader

tree = loader.initialize_fit_tree()

result = tree.query('D')
top5 = result['result']
time = result['inference_time']
print(f'result: {top5} time: {time}')