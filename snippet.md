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

## short-circuit evaluation

short-circuit operator `and`, `or` evaluates boolean conditions lazily

```python
1 and x # x
0 and x # 0 (x won't even be evaluated)
1 or x  # 1 (x won't even be evaluated)
0 or x  # x
```

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

## copy

```python
a = [1, 2, 3]

b = a[:]
b = a.copy()
```

nested list: deep copy

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(b)
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

## asterisk operator (`*`)

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

## comma operator (`,`)

if comma operator is used for `+=` operation of list, it makes the result of the operation to be a nested list instead of concatenation

```python
a = [1]
b = [2, 3] # tuple ([2, 3],)
a += b # [1, 2, 3] (concatenation)
a += b, # [1, [2, 3]] (nested list)
a += [b] # [1, [2, 3]] (nested list)
```

## Nested function

```python
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
```

## itertools

```python
import itertools

itertools.permutations([1, 2]) # ((1, 2), (2, 1))
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

## static method

```python
class Class:
    @staticmethod
    def static_method(...): # without 'self'
        pass

Class.static_method(...) # type: function
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

should be careful about the size change during iteration

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

| algorithm      | best       | average    | worst      | space     | stable | notes                                    |
| -------------- | ---------- | ---------- | ---------- | --------- | ------ | ---------------------------------------- |
| Bubble sort    | $O(n^2)$   | $O(n^2)$   | $O(n^2)$   | $O(1)$    | Yes    |                                          |
| Insertion sort | $O(n)$     | $O(n^2)$   | $O(n^2)$   | $O(1)$    | Yes    | efficient for small data sets            |
| Selection sort | $O(n^2)$   | $O(n^2)$   | $O(n^2)$   | $O(1)$    | No     |                                          |
| Quicksort      | $O(nlogn)$ | $O(nlogn)$ | $O(n^2)$   | $O(logn)$ | No     | fastest on average with $O(nlogn)$       |
| Merge sort     | $O(nlogn)$ | $O(nlogn)$ | $O(nlogn)$ | $O(n)$    | Yes    |                                          |
| Heapsort       | $O(nlogn)$ | $O(nlogn)$ | $O(nlogn)$ | $O(1)$    | No     |                                          |
| Timsort        | $O(n)$     | $O(nlogn)$ | $O(nlogn)$ | $O(n)$    | Yes    | Insertion + Merge heuristically          |
| Counting sort  | $O(n)$     | $O(n)$     | $O(n)$     | $O(n)$    | Yes    | efficient for data sets with duplication |
| Radix sort     | $O(n)$     | $O(n)$     | $O(n)$     | $O(n)$    | Yes    | efficient for large lists of numbers     |

```python
def bubblesort(data: List[int]) -> List[int]:
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def insertionsort(data: List[int]) -> List[int]:
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j - 1] > data[j]:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
    return data

def selectionsort(data: List[int]) -> List[int]:
    for i in range(len(data)):
        idx = i
        for j in range(i, len(data)):
            if data[j] < data[idx]:
                idx = j
        data[i], data[idx] = data[idx], data[i]
    return data

def quicksort(data: List[int]) -> List[int]:
    def partition(low: int, high: int) -> int:
        pivot = data[high]
        left = low
        for right in range(low, high):
            if data[right] < pivot:
                data[left], data[right] = data[right], data[left]
                left += 1
        data[left], data[high] = data[high], data[left]
        return left

    def sort(low: int, high: int):
        if low < high:
            pivot = partition(low, high)
            sort(low, pivot - 1)
            sort(pivot + 1, high)

    sort(0, len(data) - 1)
    return data

def mergesort(data: List[int]) -> List[int]:
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_list = data[:mid]
    right_list = data[mid:]

    left_list = mergesort(left_list)
    right_list = mergesort(right_list)

    result = []
    left_index = right_index = 0
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            result.append(left_list[left_index])
            left_index += 1
        else:
            result.append(right_list[right_index])
            right_index += 1
    result += left_list[left_index:]
    result += right_list[right_index:]

    return result

def heapsort(data: List[int]) -> List[int]:
    def heapify(data, index, size):
        largest = index
        left, right = 2 * index + 1, 2 * index + 2
        if left < size and data[left] > data[largest]:
            largest = left
        if right < size and data[right] > data[largest]:
            largest = right
        if largest != index:
            data[largest], data[index] = data[index], data[largest]
            heapify(data, largest, size)

    for i in range(len(data) // 2 - 1, -1, -1):
        heapify(data, i, len(data))

    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, 0, i)

    return data

def radixsort(data: List[int]) -> List[int]:
    buckets = [deque() for _ in range(10)]
    queue = deque(data)

    max_val = max(data)
    exponent = 0

    while max_val >= 10 ** exponent:
        while queue:
            num = queue.popleft()
            bucket = (num // 10 ** exponent) % 10
            buckets[bucket].append(num)
        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())
        exponent += 1

    return list(queue)
```

## python sorting

use Timsort algorithm

```python
sorted(iterable, key=lambda x: x, reverse=True) # iterable -> list

list.sort() # method of list, sort list itself
```

## sorting with custom comparator

```python
from functools import cmp_to_key

def cmp(a, b) -> int:
    return 1 if a > b else 0 if a == b else -1

data.sort(key=cmp_to_key(self.cmp))
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

# kth largest
heapq.nlargest(k, data)[-1]
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

- adjacency matrix

- adjacency list

## graph traversal

- dfs: mainly used for exploring all the possible cases. implemented by recursion, stack.

- bfs: mainly used for shortest path problem. implemented by queue.

- backtracking: check promising, pruning unnecessary parts. method of exploring in a way such as dfs.

- constraint satisfaction problem (CSP): problem of finding states that satisfy constraints. optimized by backtracking.

## shortest path problem

### Dijkstra algorithm

single-source shortest paths of directed graphs with nonnegative weights

time complexity: $O(V^2)$ with list, $O((V+E)log(V))$ with priority queue

```python
def dijkstra(graph: Dict[int, List[Tuple[int, int]]],
             start: int) -> Dict[int, int]:
    dists: Dict[int, int] = {u: sys.maxsize for u in graph}
    dists[start] = 0

    pq: List[Tuple[int, int]] = []
    heapq.heappush(pq, (dists[k], k))

    while pq:
        dist, node = heapq.heappop(pq)

        if dist > dists[node]:
            continue

        for target, weight in graph[node]:
            if dist + weight < dists[target]:
                dists[target] = dist + weight
                heapq.heappush(pq, (dists[target], target))

    return dists
```

## topological sort

a linear ordering of vertices such that for every directed edge from u to v, u comes before v in the ordering

possible if and only if the graph is directed acyclic graph (DAG)

linear time `O(V+E)` with adjacency list

```python
def bfsTopologicalSort(graph: Dict[int, Set[int]]) -> List[int]:
    degrees: Dict[int, int] = {n: 0 for n in graph.keys()}
    for adjs in graph.values():
        for adj in adjs:
            degrees[adj] += 1

    q = deque([n for n, d in degrees.items() if not d])
    topological = []

    while q:
        n = q.popleft()
        topological.append(n)

        for adj in graph[n]:
            if degrees[adj]:
                degrees[adj] -= 1
                if not degrees[adj]:
                    q.append(adj)

    return topological
```

# tree

- tree: abstract data type that represents a hierarchical tree structure

  - one root node without parent exists, all other child node has exactly one parent node (!= mathematical terminology)

  - recursively defined, self-referential: each child can be treated like the root node of its own subtree

  - special form of graph: one type of directed asyclic graph (whose undirected version is also asyclic)

- terminology

  - degree: for a given node, its number of children. a leaf has necessarily degree zero

  - depth: the length of the unique path to the root node

  - height: the length of the longest downward path to a leaf node

  - level: a set of nodes with a specific depth when using zero-based counting

  - width: the number of nodes in a level

  - size: the number of all child nodes, including itself

- trie (prefix tree): a type of k-ary search tree; a tree used for locating specific keys from within a set

  - the keys are most often strings, with links between nodes defined by individual characters

## binary tree

- binary tree: m-ary tree when m = 2. each node has less than 2 children (degree <= 2).

  - full binary tree: a tree every node has either 0 or 2 children

  - complete binary tree: a binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible

  - perfect binary tree: a binary tree in which all interior nodes have two children and all leaves have the same depth or same level

- binary search tree (BST): sorted binary tree. value of each node is greater than the node values of the left subtree and less than node values of the right subtree

  - allows binary search for fast lookup, addition, and removal: average $O(log n)$, worst $O(n)$

  - self-balancing BST: BST that automatically keeps its height small in the face of arbitrary item insertions and deletions

  - height-balanced BST: BST that the height is defined to be logarithmic $O(log n)$ (i.e. AVL trees, red-black tree)

- order of binary tree traversal in depth-first search

  - pre-order traversal: NLR(node-left-right)

  - in-order traversal: LNR(left-node-right)

  - post-order traversal: LRN(left-right-node)

## heap

- heap: tree-based data structure which is a complete tree that satisfies the heap property

  - heap property: in a max (min) heap, for any given node, then the value of parent node is greater (less) than or equal to the value of that node

  - the highest (lowest) priority element is always stored at the root; efficient implementation of priority queue ADT

  - heap is not a sorted structure; partially ordered only for the hierarchial relationship

- binary heap: heap data structure that takes the form of a binary tree. introduced for heapsort algorithm. commonly implemented with an array
