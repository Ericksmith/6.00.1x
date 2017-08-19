class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift = 0
        i = 0
        most_decoded = 0
        while i < 26:
            shifted_string = self.apply_shift(26 - i)
            decoded_count = 0
            for w in shifted_string.split(' '):
                if w in self.valid_words:
                    decoded_count += 1
            if decoded_count > most_decoded:
                most_decoded = decoded_count
                best_shift = i
            i += 1
        answer = (26 - best_shift, self.apply_shift(26 - best_shift))
        return tuple(answer)
