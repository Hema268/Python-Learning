#User function Template for python3

class Solution:
    def rotate(self, arr):
        last_element = arr[-1]
        arr.pop(-1)
        arr.insert(0,last_element)
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        t -= 1

# } Driver Code Ends
