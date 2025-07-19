class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Sort folders lexicographically
        result = []

        for f in folder:
            # Keep folder only if it's not a sub-folder of the last kept one
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)

        return result
