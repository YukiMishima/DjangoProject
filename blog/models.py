from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # text = models.TextField()
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください. ')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def text_to_markdown(self):
        return markdownify(self.text)

    def __str__(self):
        return self.title
