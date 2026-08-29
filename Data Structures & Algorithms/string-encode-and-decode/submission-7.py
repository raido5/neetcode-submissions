class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str(len(word)) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Chercher le #
            while s[j] != "#":
                j += 1

            # Tout ce qui est entre i et j est la longueur
            length = int(s[i:j])

            # Le mot commence juste après #
            word_start = j + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])

            i = word_end

        return result