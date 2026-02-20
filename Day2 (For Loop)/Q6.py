# Q6: Remove duplicate elements from a list while preserving order.

import logging

logging.basicConfig(
    filename="Q6.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicates(lst: list) -> list:
    logging.info("Removing duplicates while preserving order")
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    logging.info(f"Updated list: {result}")
    return result

print(remove_duplicates([1,2,2,3,4,4,5]))
