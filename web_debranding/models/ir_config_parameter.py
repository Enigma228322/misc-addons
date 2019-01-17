# Copyright 2015-2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2016 Stanislav Krotov <https://it-projects.info/team/ufaks>
# Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
# Copyright 2017 Ilmir Karamov <https://it-projects.info/team/ilmir-k>
# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, api
from odoo.tools.translate import _

PARAMS = [
    ('web_debranding.new_name', _('Software')),
    ('web_debranding.new_title', _('Software')),
    ('web_debranding.new_website', 'example.com'),
    ('web_debranding.new_documentation_website', ''),
    ('web_debranding.favicon_url', ''),
    ('web_debranding.send_publisher_warranty_url', '0'),
    ('web_debranding.planner_footer', ''),
    ('web_debranding.icon_url', ''),
    ('web_debranding.apple_touch_icon_url', ''),

]


def get_debranding_parameters_env(env):
    res = {}
    for param, default in PARAMS:
        value = env['ir.config_parameter'].sudo().get_param(param, default)
        res[param] = value.strip()
    return res

class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def get_debranding_parameters(self):
        return get_debranding_parameters_env(self.env)

    @api.model
    def create_debranding_parameters(self):
        for param, default in PARAMS:
            if not self.env['ir.config_parameter'].sudo().get_param(param):
                self.env['ir.config_parameter'].sudo().set_param(param, default or ' ')
