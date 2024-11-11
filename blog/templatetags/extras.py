from django import template

register=template.Library()

@register.filter(name='get_val') #from blogpost
def get_val(dict,key): #from blogpost
    return dict.get(key) #converts into dict