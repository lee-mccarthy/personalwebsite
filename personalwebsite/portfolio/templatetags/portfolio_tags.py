from django.template import Library

register = Library()

# found here: https://benjaminbaka.wordpress.com/2016/01/23/add-class-attribute-to-django-form-fields/
@register.filter(name='addclass')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr})
