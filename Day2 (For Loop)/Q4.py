# Q4: Check whether a list is sorted in ascending order.

import logging

logging.basicConfig(
    filename="Q4.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_sorted(lst: list) -> bool:
    logging.info("Checking if list is sorted in ascending order")
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            logging.info("List is not sorted")
            return False
    logging.info("List is sorted")
    return True

print(is_sorted([1,2,3,4,5]))
