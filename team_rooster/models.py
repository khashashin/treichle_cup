from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.blocks import StructBlock, CharBlock, ChoiceBlock, IntegerBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailblocks_cards.blocks import CardsBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from .constanten import POSITIONS, POSITIONS_SP


# Create your models here.
class Teams(Page):
    parent_page_types = ['home.HomePage']

class Staff(StructBlock):
    photo = ImageChooserBlock(required=False)
    name = CharBlock(required=True)
    vorname = CharBlock(required=True)
    position = ChoiceBlock(choices=POSITIONS, icon='cup')

    class Meta:
        icon = 'plus'

class Spieler(StructBlock):
    photo = ImageChooserBlock(required=False)
    nummer = IntegerBlock(required=True)
    name = CharBlock(required=True)
    vorname = CharBlock(required=True)
    position = ChoiceBlock(choices=POSITIONS_SP, icon='cup')
    jahrgang = IntegerBlock(required=True)

    class Meta:
        icon = 'user'

class TeamRooster(models.Model):
    team_name = models.CharField(max_length=100, default="")
    team_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    staff = StreamField([
        ('staff', CardsBlock(Staff(), icon="plus")),
    ], blank=True)
    spieler = StreamField([
        ('spieler', CardsBlock(Spieler(), icon="user")),
    ], blank=True)

    parent_page_types = ['team_rooster.Teams']

    content_panels = [
        FieldPanel('title'),
        FieldPanel('team_name', classname="col12"),
        ImageChooserPanel('team_logo'),
        StreamFieldPanel('staff'),
        StreamFieldPanel('spieler'),
    ]

    def __str__(self):
        return self.team_name
