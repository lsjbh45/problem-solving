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

## GIL (global interpreter lock)

the reason why python is slow

one thread monopolizes resources

fatal in a multi-core environment

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

## zip

more than 2 sequences -> new tuple sequence

one-to-one correspondence based on the short side

```python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
c = [10, 11, 12]

zip(a, b) # generator
list(zip(a, b)) # [(1, 6), (2, 7), (3, 8), (4, 9)]
list(zip(a, b, c)) # [(1, 6, 10), (2, 7, 11), (3, 8, 12)]
```

## asterisk(\*)

`*`: sequence (tuple, list) unpacking operator
`**`: key-value mapping (dictionary) unpacking operator

```python
def f(*params):
    return sum(params)

f(1, 2, 3, 4) #10

a, *b = [1, 2, 3, 4] # a = 1, b = [2, 3, 4]

info = {'a': 1, 'b': 2, 'c': 3}
new_info = {**info, 'c': 4} # {'a': 1, 'b': 2, 'c': 4}

```

## Nested function

````python
def outer(a: List[int], s: str):
    arr: List[int] = a
    text: str = s

    def inner1():
        a.append(4) # manipulation
        text = 'new' # local reallocation
        print(arr, text) # [1, 2, 3, 4], 'new'

    def inner2():
        print(arr, text) # [1, 2, 3, 4], 'old'

    print(arr, text) # [1, 2, 3]
    inner1()
    inner2()

outer([1, 2, 3], 'old')

# type hint

## composite data type

```python
from typing import List, Dict, Tuple, Set
def count(lst: List[Tuple[int, str]]) -> Dict[Tuple[int, str], int]:
    return Counter(lst)
````

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

dynamic programming, $O(n^2)$

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

## `sorted()`

Python sorted(): use Timsort algorithm (Insertion sort + Merge sort heuristically)

Best case: $O(n)$, Average case: $O(n log n)$, Worst case: $O(n log n)$

```python
sorted(iterable, key=lambda x: x, reverse=True) # iterable -> list
```

## `list.sort()`

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

## add unnecessary root node

to manipulate the list regardless of the presence of the root node

```python
def func() -> Optional[ListNode]
    lst: ListNode = ListNode(-1)

    '''
    while ...:
        lst.next = ...
    '''

    return lst.next
```

# queue

## deque (double-ended queue)

operations of stack adt + queue adt

internally implemented with doubly linked list

```python
from collections import deque

dq = deque()
dq.appendleft()
dq.append()
dq.popleft()
dq.pop()
```

## priority queue

implement with heap (insertion $O(log n)$, deletion $O(log n)$)

python: `heapq` module supports min heap

`PriorityQueue` module is internally implemented with `heapq` module

`PriorityQueue` is thread-safe, so locking overhead exists

```python
import heapq

heap = []
heapq.heappush(heap, data)
heapq.heappop(heap)
heapq.heapify(heap)

# max heap
heapq.heappush(heap, (-data, data))
```

# hash table

hash table (hash map) is an implementation of the associated array (key-value mapping) adt

hash function: maps data of any size to a fixed size value

hashing: indexing hash table using hash function

## collision handling

| method            | characteristic                                                        | programming language            |
| ----------------- | --------------------------------------------------------------------- | ------------------------------- |
| separate chaining | origin of hash table, easy implementation, memory allocation overhead | C++, Java, Go                   |
| open addressing   | maximum: bucket size, clustering (sharp decline in performance)       | Python (load factor 0.66), Luby |

# graph

## traveling salesman problem

Eulerian trail: visit all edges once.

Hamiltonian trail: visit all vertices once. NP-complete.

Hamiltonian cycle: visit all vertices once, return to starting point. NP-complete.

travelling salesman problem (TSP): a Hamiltonian cycle with the least weight. NP-hard. $O(n^2 2^n)$ with dp.

-> decision version (where given L, decide whether the graph has a tour of at most L): NP-complete.

## graph representation

adjacency matrix

adjacency list

## graph traversal

dfs: mainly used for exploring all the possible cases. implemented by recursion, stack.

bfs: mainly used for shortest path problem. implemented by queue.

backtracking: check promising, pruning unnecessary parts. method of exploring in a way such as dfs.

constraint satisfaction problem (CSP): problem of finding states that satisfy constraints. optimized by backtracking.
