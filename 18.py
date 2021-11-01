def first_differ(s1,s2):
    if s1==s2:
        return -1
    if len(s1)>len(s2):
        for i in range(len(s2)):
            if s1[i]!=s2[i]:
                return i
        else:
            return i+1
    if len(s1)<len(s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                return i
        else:
            return i+1
s1=input()
s2=input()
print(first_differ(s1,s2))
            
            
            
    
