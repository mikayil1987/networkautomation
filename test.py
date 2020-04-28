#! /usr/bin/env python3

import multiprocessing as mp
import time

def print_name_and_time(name):
    print('Hello', name, ' current timestamp is ', time.time())
    process_list = list()
    for i in range(10):
        process = mp.Process(target=print_name_and_time, args=(name)
        process_list.append(process)
        for p in process_list:
            p.start()





print_name_and_time('Mikayil')


# if __name__ == '__main__':
#     process_list = list()
#
#     for i in range(10):
#         process = mp.Process(target=print_name_and_time, args=('Mikayil',))
#         process_list.append(process)
#
#     for p in process_list:
#         p.start()

    # for p in process_list:
    #     p.join()

print('End of Script')
