n=5

for r in range(1,n+1):
  for c in range(r):
    print("*",end=" ")
  print()
for r in range(1,n+1):
  for c in range(n-r):
    print("*",end=" ")
  print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
