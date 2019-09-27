from django import template
register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})
#@register.filter(name='addcss')
#def addcss(field, css):
#    attrs = {}
#    definition = css.split(',')

 #   for d in definition:
 #       if ':' not in d:
 #           attrs['class'] = d
 #      else:
 #           key, val = d.split(':')
  #          attrs[key] = val

  #  return field.as_widget(attrs=attrs)