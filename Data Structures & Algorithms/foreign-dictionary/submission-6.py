class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}
        ind=defaultdict(int)
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        ind[w2[j]] += 1
                    break
        print(ind)
        que=deque()
        vis=set()
        for c in adj:
            if ind[c] == 0:
                que.append(c)
        res=""
        while que:
            node=que.popleft()
            vis.add(node)
            res+=node
            for nei in adj[node]:
                if nei not in vis:
                    ind[nei]-=1
                    if ind[nei]==0:
                        que.append(nei)
        if len(res) != len(adj):
            return ""
        return res
