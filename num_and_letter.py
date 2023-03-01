pattern = "?$??$**"
text = "a1bQ1po"
is_true = True

if len(pattern) != len(text):
    is_true = False
else:
    for i in range(len(pattern)):
        current_pattern = pattern[i]
        current_symbol = text[i]
        if current_pattern == '?' and not current_symbol.isalpha() and not 'o':
            is_true = False
        elif current_pattern == '$' and not current_symbol.isnumeric() and not 'o':
            is_true = False
        elif current_pattern == '*' and not current_symbol == 'o':
            is_true = False

print(is_true)
