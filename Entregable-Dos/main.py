from Lexer import Lexer
from Lexer import print_table
from Lexer import format_table
from formatCode import format_code
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
        print("Outputted text from the txt:\n", input_string)

        # Print pretty table
        print("Lexer analysis:")
        print_table(token_tuples)
        # Generate HTML table
        table_html = format_table(token_tuples)
        # Generate inputted text
        input_html = format_code(input_string)

        # Write HTML of table and inputted text to file
        with open(f"{filename}.html", "w") as output_file:
            # Add HTML head with link to external CSS file
            output_file.write(
                f"<html><head><link rel='stylesheet' type='text/css' href='styles.css'></head><body><h1 id='fileName'>File analyzed: {filename}</h1><h2 id='madeby'>Armando Arredondo Valle</h2>"
            )

            # Write input HTML and table HTML to file
            output_file.write(input_html)
            output_file.write(table_html)

            # Close HTML body and file
            output_file.write("</body></html>")
