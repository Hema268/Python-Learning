#User function Template for python3

class Solution:
    def rotate(self, arr):
        if len(arr) == 0:
            return arr
        last_ele = arr.pop()
        arr.insert(0,last_ele)
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
