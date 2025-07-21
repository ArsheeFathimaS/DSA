class Solution:
    def search(self,arr,key):
        for i in range(len(arr)):
            if arr[i]==key:
                return arr.index(arr[i])
        return -1