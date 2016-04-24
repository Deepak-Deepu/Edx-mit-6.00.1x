count =0
for i in range(1,len(s)):
        if s[i-1:i+2] == 'bob':
                count += 1
print count


