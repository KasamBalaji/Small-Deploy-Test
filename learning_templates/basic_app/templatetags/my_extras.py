from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out the arg from value
    We are assuming value to be of type string
    """
    return value.replace(arg,'')

# Register the filter cut by using the method filter

register.filter('cut',cut)
