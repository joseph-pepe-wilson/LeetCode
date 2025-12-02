from collections import Counter


class Solution:
    def countTrapezoids(self, points) -> int:
        c=Counter([point[1] for point in points])
        y=[value for key, value in c.items()]
        s=set(y)
        c2=Counter(y)
        l=[[key, value] for key,value in c2.items()]
        d={}
        for key in s:
            d[key]=(key*(key-1))//2
        output=0
        for i in range(len(l)):
            for j in range(i,len(l)):
                if i==j:
                    count=d[l[i][0]]*d[l[i][0]]*(l[i][1]*(l[i][1]-1)//2)
                else:
                    count=d[l[i][0]]*d[l[j][0]]*l[i][1]*l[j][1]
                output+=count
        
        return output%(1000000000+7)