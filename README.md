# trees-xifu0847
trees-xifu0847 created by GitHub Classroom

## Usage

```sh
python insert_key_value_pairs.py --data_structure=${AVL|hash_table|binary_tree} --dataset={sorted.txt|random.txt} --data_number=${(0,10000]}
```

Example:
```sh
python insert_key_value_pairs.py --data_structure=hash_table --dataset=sorted.txt --data_number=10000
```

## Write benchmarking result to a txt

Example:
```sh
python insert_key_value_pairs.py --data_structure=hash_table --dataset=sorted.txt --data_number=10000 > /benchmarking_txt/sort_10000.txt
```

## Plot script

With time constraint, this plot.py doesn't fully automated by reading data and extract data from .txt file.\
It will need manually paste data in it. So the furture work will be automate this process.

Example:
```sh
# TODO: add argument to select plot data from command line
python plot.py 
```

## Figures and results

Note: The hash table and hash function selection in this experiment is ChainedHash and h_rolling

### Random 10000

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/trees-xifu0847/master/image/random_10000.png)

### Sort 10000

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/trees-xifu0847/master/image/sort_10000.png)

### Random 5000

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/trees-xifu0847/master/image/random_10000.png)

### Sort 5000

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/trees-xifu0847/master/image/sort_10000.png)

## Overall Summary

Apparently, the performance of hash table crashed the other two method AVL and binary_tree. It makes sense because the\
time complexity for inserting and searching is amortized O(1).

Compared to binary tree, AVL has a big overhead in inserting time. It is reasonable because there will be more operations\
for AVL to balance to tree. However, the search time of AVL is better because the more balance of a tree, the less operations\
will be taken for searching.

So if the data structure is constant(construct data structure once and won't change it), we should use AVL to accelerate the following search operations.
Otherwise, we should balance the performance of AVL and binary tree




