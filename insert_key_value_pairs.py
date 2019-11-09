import binary_tree
import os
import sys
import argparse
import time
sys.path.append('hash_table_xifu0847')
from hash_functions import *
from hash_tables import *
sys.path.append('avl_tree')
from avl import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='analyze binary search tree')

    parser.add_argument('--data_structure', type=str, default='',
                        help='AVL, hash_table or binary_tree')
    parser.add_argument('--dataset', type=str, default='',
                        help='random.txt or sorted.txt')
    parser.add_argument('--data_number', type=int, default='',
                        help='data_number > 0 and data_number <= 10000')
   
    args = parser.parse_args()
    
    if args.data_structure not in ['AVL', 'hash_table', 'binary_tree']:
        raise ValueError(
            'data_structure should be AVL, hash_table or binary_tree')

    if args.dataset not in ['random.txt', 'sorted.txt']:
        raise ValueError('dataset should be random.txt or sorted.txt')

    if not os.path.exists(args.dataset):
        raise FileNotFoundError('dataset not exist')

    if args.data_number <= 0 or args.data_number > 10000:
        raise ValueError('data_number should be in range (0, 10000]')

    with open(args.dataset) as file:
        data = [next(file) for x in range(args.data_number)]
    
    print('Using {}'.format(args.data_structure))
    if args.data_structure == 'AVL':
        tree = AVL()

        insert_start_time = time.time()
        for word in data:
            tree.insert(word)
        insert_end_time = time.time()
        
        search_start_time = time.time()
        for word in data:
            tree.find(word)
        search_end_time = time.time()
        
        search_not_exist_start_time = time.time()
        for word in data:
            tree.find(word + '__bad')
        search_not_exist_end_time = time.time()
        
        print('Insert time: {} secs'.format(
            insert_end_time - insert_start_time))
        print('Search existed key time: {} secs'.format(
            search_end_time - search_start_time))
        print('Search not existed key time: {} secs'.format(
            search_not_exist_end_time - search_not_exist_start_time))
        
    elif args.data_structure == 'hash_table':
        table = ChainedHash(10000, h_rolling)

        insert_start_time = time.time()
        for word in data:
            table.add(word, None)
        insert_end_time = time.time()
        
        search_start_time = time.time()
        for word in data:
            table.search(word)
        search_end_time = time.time()
        
        search_not_exist_start_time = time.time()
        for word in data:
            table.search(word + '__bad')
        search_not_exist_end_time = time.time()

        print('Insert time: {} secs'.format(
            insert_end_time - insert_start_time))
        print('Search existed key time: {} secs'.format(
            search_end_time - search_start_time))
        print('Search not existed key time: {} secs'.format(
            search_not_exist_end_time - search_not_exist_start_time))
    else:
        # Do something
        pass
