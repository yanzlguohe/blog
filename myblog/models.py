from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField('生成时间', auto_now_add=True)
    title = models.CharField('标题', max_length=100, blank=True, default='')
    code = models.TextField('代码', )
    linenos = models.BooleanField(default=False)
    language = models.CharField('语言', choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField('风格', choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
        verbose_name = '测试'
        verbose_name_plural = '测试'

