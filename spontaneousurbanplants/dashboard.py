"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'spontaneousurbanplants.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        # append an model list module for Plants
        self.children.append(modules.Group(
            title="Content Admin",
            column=1,
            collapsible=False,
            children=[
                modules.ModelList(
                    title='Plant Catalog',
                    collapsible=False,
                    models=('apps.plants.models.Plant', 'apps.plants.models.Attribute'),
                ),
                modules.ModelList(
                    title='Instagram',
                    collapsible=False,
                    models=('apps.instamedia.models.*',),
                ),
            ]
        ))
        
        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            collapsible=False,
            column=2,
        ))

         # will only list the django.contrib apps
        self.children.append(modules.AppList(
            title='System Admin',
            column=3,
            collapsible=False,
            exclude=('apps.instamedia.models.*', 'apps.plants.models.*',)
        ))


