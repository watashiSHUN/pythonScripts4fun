 #! /usr/bin/env python3
class node:
    def __init__(self,zero,one):
        self.zero = zero
        self.one = one

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        highestOrder = len(bin(max(nums)))-2
        orBuffer = 2**highestOrder
        newNums = [bin(x|orBuffer)[3:] for x in nums]#'0b1.......'
        returnV = 0
        # building trie
        T = node(None,None)
        for x in newNums:
            currentNode = T
            for i in range(highestOrder):
                if x[i] == '0':
                    if not currentNode.zero:
                        currentNode.zero = node(None,None)
                    currentNode = currentNode.zero
                    # move to the left
                else:
                    if not currentNode.one:
                        currentNode.one =  node(None,None)
                    currentNode = currentNode.one
                    # move to the right
        for x in newNums:
            currentMaxXor = []
            currentNode = T
            for i in range(highestOrder):
                if x[i] == '0':
                    # if we can move to right, add 1
                    if currentNode.one:
                        currentMaxXor.append('1')
                        currentNode = currentNode.one
                    else:# always exists, since there was a binary string
                    #share the same prefix, at least 1 line goes to the
                    # bottom
                        currentMaxXor.append('0')
                        currentNode = currentNode.zero
                else:
                    if currentNode.zero:
                        currentMaxXor.append('1')
                        currentNode = currentNode.zero
                    else:
                        currentMaxXor.append('0')
                        currentNode = currentNode.one
            temp = int(''.join(currentMaxXor),2)
            if temp > returnV:
                returnV = temp
        return returnV

print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))
