from django import template

register = template.Library()

@register.filter(name='app')
def append_me(val,arg):

    return val + arg


#register.filter('app',append_me)