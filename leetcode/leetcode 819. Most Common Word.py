[Input] paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
[Output] "ball"

import re
import collections
from typing import List
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    #가장흔하게등장하는 단어의 첫번째 인덱스를 리턴
    return counts.most_common(1)[0][0]


mostCommonWord(paragraph,banned)