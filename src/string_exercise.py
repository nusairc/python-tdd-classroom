class StringExercise:

    def reverse_string(self, input_str):

        #Reverses order of characters in string
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        vowels = "aeiouAEIOU"
        return character in vowels

    def find_longest_word(self, sentence):
        """
        Returns longest word in string sentence.
        In case there are several, return the first.
        """
        words = sentence.split()
        longest_word = max(words, key=len)
        return longest_word

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        words = text.split()
        word_lengths = [len(word) for word in words]
        return word_lengths
