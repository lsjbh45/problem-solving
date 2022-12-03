# type hint

## composite data type

```python
from typing import List, Dict, Tuple, Set
def count(lst: List[Tuple[int, str]]) -> Dict[Tuple[int, str], int]:
    return Counter(lst)
```

# dictionary

## default dictionary

```python
from collections import defaultdict

default_dict = defaultdict(list)  # defaultdict(lambda: [])
default_dict['a'].append(1) # defaultdict(<class 'list'>, {'a': [1]}
default_dict['b'] # []
```

## ordered dictionary

```python
from collections import OrderedDict
ordered_dict = OrderedDict({'a': 1, 'b': 2, 'c': 3})
```

## counter

```python
from collections import Counter # extending dictionary
counter = Counter([(1, 'a'), (1, 'b'), (1, 'a')]) # {((1, 'a'), 2), ((1, 'b'), 1)}
counter[(1, 'a')] += 1 # {((1, 'a'), 3), ((1, 'b'), 1)}
counter = counter + Counter([(2, 'a')]) # {((1, 'a'), 3), ((1, 'b'), 1), ((2, 'a'), 1)}
counter.most_common(2) # [((1, 'a'), 3), ((1, 'b'), 1)]
```
