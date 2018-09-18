from django import template

register=template.Library()

@register.filter(name='chait')
def cut(value,arg):
	"""this cut out all value of arg from a string"""
	return value.replace(arg,'')



def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


# register.filter('chait',cut)
register.filter('small',lower)