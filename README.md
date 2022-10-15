# Kmthachtrietree

This project is the implementation of trie tree (prefix tree) using Python.

The project use the tutorial code at below link.

---
**Documentation**: [https://albertauyeung.github.io/2020/06/15/python-trie.html/](https://albertauyeung.github.io/2020/06/15/python-trie.html/)
---
## Installation

Clone repository to your project directory using below bash:

``` bash
git clone https://github.com/kmthach/kmthachtrietree.git
```

## Usage

Use can look at the example in the given test.py:

```
from trietree.trietree import loader

tree = loader.initialize_fit_tree()

result = tree.query('D')
top5 = result['result']
time = result['inference_time']
print(f'result: {top5} time: {time}')
>>> result: ['death at a funeral', 'deception', 'dawn of the dead', 'dark water', 'django'] time: 0.0015811920166015625

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
