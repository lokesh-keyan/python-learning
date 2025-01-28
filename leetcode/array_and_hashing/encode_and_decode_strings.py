from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for word in strs:
            encoded_string.append(str(len(word))+'#'+ word)
        return ''.join(encoded_string)
        

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            curr_len = int(s[i:j])
            curr_word = s[j+1:j+1+curr_len]
            decoded_strings.append(curr_word)
            i = j + 1 + curr_len
        return decoded_strings