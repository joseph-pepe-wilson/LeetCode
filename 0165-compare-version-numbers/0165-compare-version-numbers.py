class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings into revision lists
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')

        # Determine the maximum length to iterate over
        max_len = max(len(v1_parts), len(v2_parts))

        for i in range(max_len):
            # Convert each revision to integer, treating missing parts as 0
            rev1 = int(v1_parts[i]) if i < len(v1_parts) else 0
            rev2 = int(v2_parts[i]) if i < len(v2_parts) else 0

            # Compare revisions
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1

        # All revisions are equal
        return 0