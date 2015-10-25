from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from .models import MKCookies

class CMSCookiesPlugin(CMSPluginBase):
    model = MKCookies  # model where plugin data are saved
    name = _("Cookies Plugin")  # name of the plugin in the interface
    render_template = "privacy_policy.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
    
plugin_pool.register_plugin(CMSCookiesPlugin)  # register the plugin