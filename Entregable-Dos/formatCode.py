from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


def format_code(code):
    lexer = PythonLexer()
    formatter = HtmlFormatter()
    highlighted_code = highlight(code, lexer, formatter)
    css = formatter.get_style_defs('.highlight')
    return f'<style>{css}</style>\n{highlighted_code}'
