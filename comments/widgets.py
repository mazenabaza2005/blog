from django.forms import Widget
from django.utils.safestring import mark_safe


class StarRatingWidget(Widget):
    template_name = 'comments/widgets/rating.html'

    def __init__(self, attrs=None, value=1, max_stars=5):
        self.max_stars = max_stars
        self.value = value
        super(StarRatingWidget, self).__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super(StarRatingWidget, self).get_context(name, value, attrs)
        context['value'] = value or 1
        context['choices'] = range(1, 6)
        return context
