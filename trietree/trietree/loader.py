from pathlib import Path
import sys
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

data_path = 'data/movies.csv'

from .trietree import TrieTree
import pandas as pd

def initialize_fit_tree():
    trietree = TrieTree()
    root = ROOT.parents[0]
    df = pd.read_csv(root / data_path)
    
    data = df['title'].values.tolist()
    
    for title in data:
        trietree.insert(title)
    
    return trietree