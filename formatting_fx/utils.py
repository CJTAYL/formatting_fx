# formatting_fx/utils.py

import string
import numpy as np


def remove_currency_format(value):
    """
    Remove commas and dollar signs from value.
    
    Args:
        value (str): Value formated in USD as string.
    
    Returns:
        new_value (float): Value without USD formatting.
    """
    new_value = value.replace('$', '').replace(',', '')
    new_value_float = float(new_value)
    
    return new_value_float


def remove_extra_spaces(text):
    """
    Remove extra spaces from a text element. 
    
    Args:
        text (string): Text that requires cleaning.
        
    Returns:
        string: Text without extra spaces.
    """
    words = text.split()
    return " ".join(words)


def remove_punctuation(text):
  """
  Removes punctuation from a string.
  
  Args:
    text(string): Text with punctuation.
  
  Returns:
    string: Contents of text wihtout punctuation.
  
  """
  text = str(text)
  return ''.join([char for char in text if char not in string.punctuation])

