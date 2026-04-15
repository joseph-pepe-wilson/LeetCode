class Solution:
    def closestTarget(self, words: List[str], target: str, start: int) -> int:
        return -1  if  not target in (ww := words*3)  else min(
            w1.index(target)  if  target in (w1 := ww[(ss := start + len(words)):])  else inf,
            w2.index(target)  if  target in (w2 := ww[:ss + 1][::-1])  else inf,
        )
        