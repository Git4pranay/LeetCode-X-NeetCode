Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

# EASY

class Solution:
    def longestPalindrome(self, s):
        reslen=0
        res=""
        for i in range(len(s)):
            l=i
            r=i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1)>reslen:
                    reslen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            l=i;r=i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1)>reslen:
                    reslen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res

# beats 50%
o(n^2)