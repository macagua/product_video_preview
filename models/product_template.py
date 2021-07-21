# -*- coding: utf-8 -*-

# Odoo:
from odoo import _, api, fields, models  # noqa
from odoo.addons.website.tools import get_video_embed_code

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Video URL
    video_url = fields.Char(string='Video URL',
                            help='URL of a video for showcasing your product.')
    # Video Embed Code
    embed_code = fields.Char(compute="_compute_embed_code")

    @api.depends('video_url')
    def _compute_embed_code(self):
        for rec in self:
            rec.embed_code = get_video_embed_code(rec.video_url)

