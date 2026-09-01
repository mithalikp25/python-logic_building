n=5

for r in range(1,n+1):
  for c in range(r):
    if r==n or c==0 or c==r-1:
      print("*", end=" ")
    else:
      print(" ", end=" ")
  print()

# * 
# * * 
# *   * 
# *     * 
# * * * * * 