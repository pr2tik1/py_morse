# py_morse

`py_morse` is a simple Python library for converting between text and Morse code. This library includes two primary functions:

- `text_to_morse(message)`: Converts plain text to Morse code.
- `morse_to_text(code)`: Converts Morse code back to plain text.

## Installation
Not on PyPI hence -

```bash
pip install py_morse-0.1.tar.gz
```

# Usage
## Converting Text to Morse Code
To convert a plain text message to Morse code, use the text_to_morse function:

```python
from py_morse import text_to_morse

message = "Hello World"
morse_code = text_to_morse(message)
print("Morse Code:", morse_code)
```


## Converting Morse Code to Text
To convert Morse code back to plain text, use the morse_to_text function:

```python
from py_morse import morse_to_text

code = "... --- ..."
decoded_message = morse_to_text(code)
print("Decoded Text:", decoded_message)
```


## From terminal

```python
python3 py_morse/main.py
```