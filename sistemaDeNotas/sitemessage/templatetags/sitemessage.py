from django import template, VERSION
from django.template.base import FilterExpression
from django.template.loader import get_template
from django.conf import settings

from ..exceptions import SiteMessageConfigurationError


register = template.Library()


_CONTEXT_FLATTEN = VERSION >= (1, 11)


@register.tag
def sitemessage_prefs_table(parser, token):
    tokens = token.split_contents()
    use_template = detect_clause(parser, 'template', tokens)
    prefs_obj = detect_clause(parser, 'from', tokens)

    tokens_num = len(tokens)

    if tokens_num in (1, 3):
        return sitemessage_prefs_tableNode(prefs_obj, use_template)
    else:
        raise template.TemplateSyntaxError(
            '`sitemessage_prefs_table` tag expects the following notation: '
            '{% sitemessage_prefs_table from user_prefs template "sitemessage/my_pref_table.html" %}.')


class sitemessage_prefs_tableNode(template.Node):

    def __init__(self, prefs_obj, use_template):
        self.use_template = use_template
        self.prefs_obj = prefs_obj

    def render(self, context):
        resolve = lambda arg: arg.resolve(context) if isinstance(arg, FilterExpression) else arg

        prefs_obj = resolve(self.prefs_obj)
        if not isinstance(prefs_obj, tuple):
            if settings.DEBUG:
                raise SiteMessageConfigurationError(
                    '`sitemessage_prefs_table` template tag expects a tuple generated '
                    'by `get_user_preferences_for_ui` but `%s` is given.' % type(prefs_obj))
            return ''  # Silent fall.

        context.push()
        context['sitemessage_user_prefs'] = prefs_obj
        contents = get_template(
            resolve(self.use_template or 'sitemessage/user_prefs_table.html')
        ).render(context.flatten() if _CONTEXT_FLATTEN else context)
        context.pop()

        return contents


def detect_clause(parser, clause_name, tokens):
    """Helper function detects a certain clause in tag tokens list.
    Returns its value.

    """
    if clause_name in tokens:
        t_index = tokens.index(clause_name)
        clause_value = parser.compile_filter(tokens[t_index + 1])
        del tokens[t_index:t_index + 2]
    else:
        clause_value = None
    return clause_value
