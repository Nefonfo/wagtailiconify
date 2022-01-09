# WAGTAIL ICONIFY
---
![Wagtail](/wagtail.svg)

##### Library developed for **Wagtail CMS**, its purpose is to provide icon blocks from various libraries

### **INSTALATION**

1. **// TODO: CREATE PIP PACKAGE MODULE**
2. Add to INSTALLED_APPS in settings/base.py
    ```python
    INSTALLED_APPS = [
        ... ,
        'wagtailiconify',
        ...
    ```

### **USE EXAMPLE**

```python
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtailiconify.blocks import FontAwesomeBlock

class HomePage(Page):
    body = StreamField([
        ('icon', FontAwesomeBlock())
    ], null = True, blank = False)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
```

### **CONTRIBUTIONS**

All support for the library is well accepted, in fact I would appreciate it very much since I am the only one who is giving support

Any questions, comments or suggestions can be made known to me with an "Issue" notification or make a contribution with a pull request.

Any closer attention can write to me at: victorarmenta30@gmail.com

### **TODO WORK**
- **Setuptools installation... build failing, scss not copied and npm not running**
- **Pip package installation**
- Admin icons support (Fontawesome have troubleshoots with Wagtail svg icons )
- Support for FeatherIcons
- More docs for developers
- A niceeeee logo for this little library... **Why not?**