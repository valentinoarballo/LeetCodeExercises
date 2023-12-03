class Solution(object):
    def summatory(self, word, chars):
        """
        :type word: str
        :type chars: str
        :rtype: int
        """
        counter = 0 
        old_length = len(chars)      
        for char in word:
            if char in chars:
                counter += 1
                chars = chars.replace(char, "", 1)
                if len(chars) == 0:
                    if old_length == counter:
                        break
                    else:
                        counter = 0
                        break
        if counter == len(word):
            return counter
        else:
            return 0
        

    def countCharacters (self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        acum = 0
        for word in words:
            result = self.summatory(word, chars)
            acum += result
        return acum

instance = Solution()

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

instance.summatory(words, chars)
