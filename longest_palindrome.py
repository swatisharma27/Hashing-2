## Using HashMaps

class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        TC: O(n)
        AS: O(n)
        '''

        groups = {}
        count = 0
        flag = False

        if len(s) == 1:
            return 1

        for i in s:
            if i not in groups:
                groups[i] = 1
            else:
                groups[i] += 1

        for i, j in groups.items():
            if j%2 == 0:
                count += j
            else:
                count += (j//2 * 2)
                if not flag:
                    count += 1
                flag = True
        return count

x = Solution()
print(x.longestPalindrome("abb"))


## Using HashSets
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        TC: O(n)
        AS: O(n)
        '''

        tracker = set()
        count = 0

        for i in s:
            if i not in tracker:
                tracker.add(i)
            else:
                tracker.remove(i)
                count += 2
        
        if tracker:
            count += 1

        return count


x = Solution()
print(x.longestPalindrome("abb"))