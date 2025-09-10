from collections import defaultdict
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Convert each user's language list to a set for fast lookup
        user_langs = [set(langs) for langs in languages]
        
        # Identify all friendship pairs that cannot currently communicate
        need_teaching = set()
        for u, v in friendships:
            u -= 1  # Convert to 0-based index
            v -= 1
            if user_langs[u].intersection(user_langs[v]):
                continue  # They can already communicate
            need_teaching.add(u)
            need_teaching.add(v)

        # If all friends can already communicate
        if not need_teaching:
            return 0

        # Count how many of the users needing teaching know each language
        lang_count = [0] * (n + 1)  # 1-based indexing for languages
        for user in need_teaching:
            for lang in user_langs[user]:
                lang_count[lang] += 1

        # Choose the language that is already known by the most users in need
        max_known = max(lang_count)
        
        # Minimum users to teach = total needing teaching - already knowing chosen language
        return len(need_teaching) - max_known
