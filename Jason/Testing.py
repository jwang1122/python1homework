def pattern(n):
      k = 2 * n - 2
      for i in range(1,n):
           for j in range(2,k):
               print(end=" 4")
           k = k - 1
           for j in range(0, i+1):
                print("1", end=" 4")
           print("1")
 
pattern(4)