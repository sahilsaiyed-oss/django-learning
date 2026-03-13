from django import template

register = template.Library()

@register.filter(name='upper_case')
def upper_case(value):
    """
    Converts a string to uppercase.
    Example usage in template:
    {{ name|upper_case }}
    """
    if isinstance(value, str):
        return value.upper()
    return value


@register.filter(name='word_count')
def word_count(value):
    """
    Counts number of words in a string.
    Example usage:
    {{ text|word_count }}
    """
    if isinstance(value, str):
        return len(value.split())
    return 0
