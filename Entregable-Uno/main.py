from Lexer import Lexer
from Lexer import print_table
from getInputFile import get_input_files_strings

if __name__ == "__main__":

  input_files_strings = get_input_files_strings()

  for filename, input_string in input_files_strings:
    lexer = Lexer(input_string)
    tokens = lexer.tokenize()

    # Convert list of tokens to list of tuples
    token_tuples = [(token.type, token.lexeme) for token in tokens]

    # Print the inputted text
    print("Name of the file:", filename)
    print("Outputted text from the txt:", input_string)

    # Print pretty table
    print("Lexer analysis:")
    print_table(token_tuples)
