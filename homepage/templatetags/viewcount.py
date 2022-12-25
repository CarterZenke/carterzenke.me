from django import template

register = template.Library()


@register.filter(name='viewcount')
def viewcount(value):
    """Format viewcounts."""
    return f"{value:,.0f}"