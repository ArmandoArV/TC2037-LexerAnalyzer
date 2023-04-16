def generate_html_table(token_tuples):
    table_html = "<table>\n"
    table_html += "<tr><th>Token Type</th><th>Lexeme</th></tr>\n"
    for row in token_tuples:
        table_html += "<tr>"
        for column in row:
            table_html += f"<td>{column}</td>"
        table_html += "</tr>\n"
    table_html += "</table>\n"
    return table_html
