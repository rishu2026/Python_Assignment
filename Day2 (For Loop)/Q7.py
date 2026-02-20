# Q7: Find the missing number in a list containing numbers from 1 to N.

import logging

logging.basicConfig(
    filename="Q7.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_missing(lst: list) -> int:
    logging.info("Finding missing number in range 1 to N")
    n = len(lst) + 1
    total = n * (n + 1) // 2
    actual = 0
    for num in lst:
        actual += num
    missing = total - actual
    logging.info(f"Missing number found: {missing}")
    return missing

print(find_missing([1,2,4,5]))
