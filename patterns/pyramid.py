n=5

for r in range(1,n+1):
  for s in range(n-r+1):
    print(" ",end=" ")
  for c in range((2*r)-1):
    print("*",end=" ")
  print()

  #         * 
  #       * * * 
  #     * * * * * 
  #   * * * * * * * 
  # * * * * * * * * * 

m=5

for r in range(1,m+1):
  for s in range(r-1):
    print(" ",end=" ")
  for c in range(2 * (m - r) + 1):
    print("*",end=" ")
  print()


# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 