# Q1: Count how many vowels are present in a given string.

import logging

logging.basicConfig(
    filename="Q1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def count_vowels(s: str) -> int:
    logging.info("Counting vowels in the string")
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    logging.info(f"Vowel count calculated: {count}")
    return count

print(count_vowels("programming"))
