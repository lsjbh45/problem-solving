# python

## operator precedence

| Operation                                                                     | Description                                                                        |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `(expressions...)`, `[expressions...]`, `{key: value...}`, `{expressions...}` | Binding or parenthesized expression, list display, dictionary display, set display |
| `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute`                | Subscription, slicing, call, attribute reference                                   |
| `await x`                                                                     | Await expression                                                                   |
| `**`                                                                          | Exponentiation                                                                     |
| `+x`, `-x`, `~x`                                                              | Positive, negative, bitwise NOT                                                    |
| `*`, `@`, `/`, `//`, `%`                                                      | Multiplication, matrix multiplication, division, floor division, remainder         |
| `+`, `-`                                                                      | Addition and subtraction                                                           |
| `<<`, `>>`                                                                    | Shifts                                                                             |
| `&`                                                                           | Bitwise AND                                                                        |
| `^`                                                                           | Bitwise XOR                                                                        |
| `\|`                                                                          | Bitwise OR                                                                         |
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`              | Comparisons, including membership tests and identity tests                         |
| `not x`                                                                       | Boolean NOT                                                                        |
| `and`                                                                         | Boolean AND                                                                        |
| `or`                                                                          | Boolean OR                                                                         |
| `if – else`                                                                   | Conditional expression                                                             |
| `lambda`                                                                      | Lambda expression                                                                  |
| `:=`                                                                          | Assignment expression                                                              |

## divmod

```python
carry, sum = divmod(diviend, divisor) # (diviend // divisor, diviend % divisor)
```

## swap

multiple assignment (== C++ std::swap())

```python
a, b = b, a

x += y
y = x - y
x -= y
```

## min, max

```python
import sys
min_value = sys.minsize # float('-inf')
max_value = sys.maxsize # float('inf')
```

## reduce

```python
from functools import reduce
reduce(lambda acc, cur: (acc, cur), iterable, initial)

import operator
# arithmetic: add, sub, mul, truediv
# logical: is_, is_not, and_, or_
# comparison: lt, le, gt, ge, eq
reduce(operator.func, iterable, initial)
```

# type hint

## composite data type

```python
from typing import List, Dict, Tuple, Set
def count(lst: List[Tuple[int, str]]) -> Dict[Tuple[int, str], int]:
    return Counter(lst)
```

## optional

```python
data: Optional[Type] = None # Type | None
```

# list

dynamic array (== C++ std::vector, Java ArrayList) + various type (characteristic of linked list)

| Operation      | Time       |
| -------------- | ---------- |
| len(a)         | O(1)       |
| a[i]           | O(1)       |
| a[i:j]         | O(k)       |
| elem in a      | O(n)       |
| a.count(elem)  | O(n)       |
| a.index(elem)  | O(n)       |
| a.append(elem) | O(1)       |
| a.pop()        | O(1)       |
| a.pop(i)       | O(n)       |
| del a[i]       | O(n)       |
| a.sort()       | O(n log n) |
| min(a), max(a) | O(n)       |
| a.reverse()    | O(n)       |

# dictionary

key-value hash table (== C++ std::unordered_map, Java HashMap)

| Operation      | Time |
| -------------- | ---- |
| len(a)         | O(1) |
| a[key]         | O(1) |
| a[key] = value | O(1) |
| key in a       | O(1) |

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

## dictionary comprehension

```python
{key: value for key, value in dict.items()}
```

# string

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

# array

## prefix sum

$$
p_n = a_0 + a_1 + a_2 + ... + a_n
$$

$$
a_l + a_{l+1} + ... + a_{r-1} + a_r = p_r - p_{l-1}
$$

```python
# implemetation: O(n)
sum_val = 0
prefix_sum = []
for num in nums:
    prefix_sum.append(sum_val)
    sum_val += i

# get subtotal value: O(1)
subtotal = prefix_sum[right] - prefix_sum[left - 1]
```

# linked list

## runner

use two pointers(fast, slow) to find center node

```python
rev = None
slow = fast = head

while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
if fast: # odd number of nodes
    slow = slow.next # len(slow) == len(rev)
```
