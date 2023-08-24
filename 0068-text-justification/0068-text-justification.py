class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(words :List[str]) -> str:
            if len(words) == 1:
                return words[0]+(" "*(maxWidth -len(words[0])))

            numSpaces = (len(words)-1)
            wordsLength = sum(len(word) for word in words)
            spaceLength = maxWidth - wordsLength
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

        def justifyLeft(wordLst: List[str]) -> str:
            spaceJoinedWords =" ".join(wordLst)
            rightSpaces = " " * (maxWidth - len(spaceJoinedWords))
            return spaceJoinedWords + rightSpaces

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
            res.append(justify(lines[index]))

        if lines:
            res.append(justifyLeft(lines[-1]))

        return res