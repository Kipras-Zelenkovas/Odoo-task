# -*- coding: utf-8 -*-

from odoo import models, fields

class Docs(models.Model):
    _name           = "docs"
    _description    = "Model for documents and books"

    name        = fields.Char(required=True)
    description = fields.Text(required=True)
    res_company = fields.Many2one('res.company', required=True)
 