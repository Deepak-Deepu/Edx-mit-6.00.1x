def nfruits(dic,x):

        for i in x[:-1]:
                if i in dic.keys():
                        for j in dic.keys():
                                dic[j]+=1
                dic[i] -=2
#       return dic      
        if x[-1] in dic.keys():
                dic[x[-1]] -= 1
        return max(dic.values())
      

