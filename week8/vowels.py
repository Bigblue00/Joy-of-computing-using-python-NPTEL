vowels = 'aeiou'
s=input();
i=0;
n=len(s);
while(i<n):
  print(s[i],end='');
  if(s[i] in vowels):
    while(i<n and s[i] in vowels):
      i+=1;
    continue;
  i+=1;