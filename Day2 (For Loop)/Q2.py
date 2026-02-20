# Q2: Print the frequency of each character in a string.

import logging

logging.basicConfig(
    filename="Q2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def freq(s: str) -> dict:
    logging.info("Counting frequency of characters")
    dic = {}
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    logging.info(f"Frequency count calculated: {dic}")
    return dic

print(freq("aeioua"))
