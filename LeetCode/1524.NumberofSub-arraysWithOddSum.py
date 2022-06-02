class Solution:
    def numOfSubarrays(self, arr) -> int:
        result=-100000
        for i in range(len(arr)+1):
            sm=0;
            arr1=[]
            for j in range(i):
                sm=sum(arr[j:i])
                print(arr[j:i])
                print(sm)
                # result=max(result,sm)
                # if(sm%2!=0):
                #  result+=1
        # print(result)

solve=Solution();
solve.numOfSubarrays([2,-5,-3])