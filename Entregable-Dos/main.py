from Lexer import Lexer
from Lexer import print_table
from Lexer import format_table
from formatCode import format_code
from getInputFile import get_input_files_strings

if __name__ == "__main__":
    input_files = get_input_files_strings()

    for filename, input_string in input_files:
        lexer = Lexer(input_string)
        tokens = lexer.tokenize()

        # Convert list of tokens to list of tuples
        token_tuples = [(token.type, token.lexeme) for token in tokens]

        # Print the inputted text
        print(f"Processing file: {filename}")
        print(f"Input text:\n{input_string}")

        # Print lexer analysis
        print("Lexer analysis:")
        print_table(token_tuples)

        # Generate HTML table
        table_html = format_table(token_tuples)

        # Generate HTML representation of input code
        input_html = format_code(input_string)

        # Write HTML of table and input code to file
        output_filename = f"{filename}.html"
        with open(output_filename, "w") as output_file:
            # Add HTML head with link to external CSS file
            output_file.write(
                f"<html><head><link rel='stylesheet' type='text/css' href='styles.css'></head><body>"
                f"<h1 id='filename'>File Analyzed: {filename}</h1>"
                f"<h2 id='author'>Author: Armando Arredondo Valle</h2>"
            )

            # Write HTML representation of input code and table to file
            output_file.write(input_html)
            output_file.write(table_html)

            # Close HTML body and file
            output_file.write("</body></html>")

        print(f"HTML report generated: {output_filename}")
