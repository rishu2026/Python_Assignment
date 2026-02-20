# Q3: Find the second largest element in a list using a for loop.

import logging

logging.basicConfig(
    filename="Q3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(lst: list) -> int:
    logging.info("Finding second largest element")
    large = float('-inf')
    slarge = float('-inf')
    for num in lst:
        if num > large:
            slarge = large
            large = num
        elif num < large and num > slarge:
            slarge = num
    logging.info(f"Second largest found: {slarge}")
    return slarge

print(second_largest([1,5,2,6,9]))
