from wagtail.core.blocks import ChoiceBlock, StructBlock, StructValue

from .choices import fontawesome


class FontAwesomeBlockValue(StructValue):
    @property
    def css_classes(self):
        return self["icon_name"] + " " + self["icon_size"]


class FontAwesomeBlock(StructBlock):
    icon_name = ChoiceBlock(choices=fontawesome.ICONS)
    icon_size = ChoiceBlock(choices=fontawesome.SIZES)

    class Meta:
        template = "wagtailiconify/icon_block.html"
        value_class = FontAwesomeBlockValue
        icon = "italic"
