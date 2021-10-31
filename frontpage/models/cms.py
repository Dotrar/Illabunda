from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

# Create your models here.


class HomePage(Page):
    # https://docs.wagtail.io/en/stable/reference/streamfield/blocks.html#streamfield-block-reference
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("subheading", blocks.CharBlock(form_classname="sub title")),
            ("paragraph", blocks.RichTextBlock()),
            ("image", ImageChooserBlock()),
        ]
    )

    content_panels = Page.content_panels + [StreamFieldPanel("body")]
