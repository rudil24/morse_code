from assets.itu_morse import itu_morse_dict


class MorseCodeTranslator:
    """
    A class to handle the translation of text to Morse code.
    """

    def __init__(self):
        """
        Initializes the Morse code dictionary.
        """
        self.morse_code_dict = itu_morse_dict

    def translate(self, text):
        """
        Translates the given text into Morse code.

        Args:
            text (str): The text to be translated.

        Returns:
            str: The Morse code translation of the text.
        """
        morse_code = ""
        for char in text.upper():
            if char != " ":
                if char in self.morse_code_dict:
                    morse_code += (
                        self.morse_code_dict[char] + "  "
                    )  # 2 spaces between letters
                else:
                    raise ValueError(
                        "ERROR: I'm only able to translate A-Z, 0-9, and limited punctuation, please try again."
                    )
            else:
                morse_code += "    "  # 4 spaces between words
        return morse_code.strip()


# Path: morse_code/translator.py
