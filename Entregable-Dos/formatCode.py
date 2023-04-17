from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

def format_code(code):
    lexer = PythonLexer()
    monokai_style = get_style_by_name('monokai')
    formatter = HtmlFormatter(style=monokai_style)
    highlighted_code = highlight(code, lexer, formatter)
    css = formatter.get_style_defs('.highlight')
    return f'<style>{css}</style>\n{highlighted_code}'
