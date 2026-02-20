# Q5: Reverse a string using a for loop (no slicing).

import logging

logging.basicConfig(
    filename="Q5.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def reverse_string(s: str) -> str:
    logging.info("Reversing string using for loop")
    rev = ""
    for ch in s:
        rev = ch + rev
    logging.info(f"Reversed string: {rev}")
    return rev

print(reverse_string("Python"))
