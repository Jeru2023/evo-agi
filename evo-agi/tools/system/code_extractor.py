import re

class CodeExtractor:
    def __init__(self, text):
        self.text = text

    def extract_code(self):
        code_pattern = re.compile(r'```python\n(.*?)```', re.DOTALL)
        code_blocks = code_pattern.findall(self.text)
        return '\n'.join(code_blocks)