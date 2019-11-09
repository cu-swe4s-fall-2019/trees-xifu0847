#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_pystyle pycodestyle test_binary_tree.py
assert_no_stdout

run test_pystyle pycodestyle binary_tree.py
assert_no_stdout

run test_pystyle pycodestyle insert_key_value_pairs.py --ignore=E402
assert_no_stdout

run test_bad_data_structure python insert_key_value_pairs.py --data_structure=bad --dataset=sorted.txt --data_number=10000
assert_in_stderr 'data_structure should be AVL, hash_table or binary_tree'

run test_bad_dataset python insert_key_value_pairs.py --data_structure=AVL --dataset=bad.txt --data_number=10000
assert_in_stderr 'dataset should be random.txt or sorted.txt'

run test_bad_data_number python insert_key_value_pairs.py --data_structure=AVL --dataset=sorted.txt --data_number=10001
assert_in_stderr 'data_number should be in range (0, 10000]'

run test_good_usage python insert_key_value_pairs.py --data_structure=AVL --dataset=sorted.txt --data_number=10000
assert_no_stderr
