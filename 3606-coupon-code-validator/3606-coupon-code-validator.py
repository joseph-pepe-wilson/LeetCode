import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_categories = ["electronics", "grocery", "pharmacy", "restaurant"]
        category_order = {cat: i for i, cat in enumerate(valid_categories)}
        
        valid_coupons = []
        
        for c, b, active in zip(code, businessLine, isActive):
            # Check code validity
            if not c or not re.match(r'^[A-Za-z0-9_]+$', c):
                continue
            # Check business line validity
            if b not in valid_categories:
                continue
            # Check active status
            if not active:
                continue
            
            valid_coupons.append((category_order[b], c))
        
        # Sort by category order, then lexicographically by code
        valid_coupons.sort(key=lambda x: (x[0], x[1]))
        
        # Extract only codes
        return [c for _, c in valid_coupons]