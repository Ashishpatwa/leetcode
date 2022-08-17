class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dictionary = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}

        set_words=set()
        for word in words:
            tmp_str=[]
            for element in word:
                tmp_str.append(dictionary[element])
            wrd="".join(tmp_str)
            if wrd not in set_words:
                set_words.add(wrd)
        return len(set_words)
                
        