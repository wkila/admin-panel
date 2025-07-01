from django import template
import re
register = template.Library()

@register.filter(name='find_form')
def find_form(form_dic, value):
    list_form = list(map(lambda x: x.do_name(), form_dic))
    indexed_el = list_form[list_form.index(value)]
    for form_el in form_dic:
        str_name = form_el.do_name()
        if indexed_el == str_name:
            return form_el
    return False
