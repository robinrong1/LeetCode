class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
           
            max_length = max(max_length, (r-l)+1)
            char_set.add(s[r])
        return max_length


















        # charSet = set()
        # l = 0
        # max_len = 0
        # for r in range(len(s)):
        #     if s[r] in charSet:
        #         charSet.remove(s[l])
        #         max_len -= 1
            
        #     charSet.add(s[r])
        #     max_len = max(max_len, (r-l) + 1)
        # return max_len



















        # char_set = set()
        # l = 0
        # max_len = 0

        # for r in range(len(s)):
        #     while s[r] in char_set:
        #         char_set.remove(s[l])
        #         l += 1
        #     char_set.add(s[r])
        #     max_len = max(max_len, r-l+1)
        # return max_len
