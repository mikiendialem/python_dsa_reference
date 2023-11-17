def validparenthesis(s):
  stack=[]
  mapp={')': '(', '}': '{', ']': '['}
  for i in s:
    if i in mapp:
      if not stack or stack[-1] != mapp[i]:
        return False
      stack.pop()
    else: 
      stack.append(i)
  return len(stack)==0

s='(]'
print(validparenthesis(s))
        
      