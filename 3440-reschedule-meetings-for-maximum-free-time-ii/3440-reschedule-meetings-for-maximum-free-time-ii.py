class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        diff = []
        prev=0
        for i,j in zip(startTime,endTime):
            diff.append(i-prev)
            diff.append(-(j-i))
            prev=j
        diff.append(eventTime-endTime[-1])

        c=Counter(i for i in diff if i>=0)
        k=sorted(list(set([abs(i) for i in diff])),reverse=True)
        for i in range(1,len(k)):
            c[k[i]]+=c[k[i-1]]

        ans=0
        for i in range(1,len(diff),2):
            candidate = diff[i-1]+diff[i+1]
            if c[-diff[i]]>int(diff[i-1]>=-diff[i])+int(diff[i+1]>=-diff[i]) and diff[i-1]-diff[i]+diff[i+1] > ans : 
                candidate -= diff[i]
            if candidate > ans : ans = candidate
        return ans