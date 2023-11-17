def longestsubstring(s):
  n=len(s)
  str={}
  max_length=0
  start=0
  for i in range(n):
    if s[i] in str and start <= str[s[i]]:
      start=str[s[i]]+1

    else:
      max_length=max(max_length,i-start+1)
    str[s[i]]=i
  return max_length
  
print(longestsubstring("abcabcbb"))