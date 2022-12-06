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

## key of max value

```python
di = {'a': 1, 'b': 2, 'c': 3}
max(di, key=di.get) # 'c'
```

# String

## check alphanumeric

```python
chars.isalnum() # chars.isalpha() and chars.isnumeric()
```

## change case

```python
chars.lower() # check: chars.islower()
```

## encoding

representation: UTF-8 (variable-width, Python 3~)

internal: fixed-width encoding (based on character range)

## longest common substring

dynamic programming, O(n^2)

```python
    common_len = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s_rev[j]:
                common_len[i][j] = (common_len[i - 1][j - 1] if i and j else 0) + 1
```

# regex

## replace non-alphanumeric

```python
s = 'a, a, a, a, b,b,b,c, c'
re.sub(r'[^\w]', ' ', s) # 'a  a  a  a  b b b c  c'
```

# sorting

## sorted()

Python sorted(): use Timsort algorithm (Insertion sort + Merge sort heuristically)

Best case: O(n), Average case: O(n log n), Worst case: O(n log n)

```python
sorted(iterable, key=lambda x: x, reverse=True) # iterable -> list
```

## list.sort()

```python
list.sort() # method of list, sort list itself
```
