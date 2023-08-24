class Solution:
    @staticmethod
    def leftRightJustify(words: List[str], maxlineLength: int) -> str:
        if len(words) == 1:
            return words[0]+(" "*(maxlineLength -len(words[0])))

        numSpaces = (len(words)-1)
        wordsLength = sum(len(word) for word in words)
        spaceLength = maxlineLength - wordsLength
        base = spaceLength // numSpaces
        spaces = [base] * numSpaces
        remainder = spaceLength % numSpaces

        for index in range(remainder):
            spaces[index] += 1

        res = []
        if len(words) > 0:
            res.append(words[0])
            for index in range(numSpaces):
                res.append(" "*spaces[index])
                res.append(words[index+1])

        return "".join(res)
    
    @staticmethod
    def leftJustify(words: List[str], maxlineLength: int) -> str:
        spaceJoinedWords = " ".join(words)
        rightSpaces = " " * (maxlineLength - len(spaceJoinedWords))
        return spaceJoinedWords + rightSpaces

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        wordLst = []
        currWordsLength = 0
        for word in words:
            wordsLength = currWordsLength + len(word)
            singleSpacesLength = len(wordLst)

            if wordsLength + singleSpacesLength <= maxWidth:
                wordLst.append(word)
                currWordsLength += len(word)
            else:
                lines.append(wordLst.copy())
                currWordsLength = len(word)
                wordLst = [word]

        if wordLst:
            lines.append(wordLst.copy())

        res = []
        for index in range(len(lines)-1):
            res.append(Solution.leftRightJustify(lines[index], maxWidth))
        if lines:
            res.append(Solution.leftJustify(lines[-1], maxWidth))

        return res