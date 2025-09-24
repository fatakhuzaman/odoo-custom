from odoo import models, fields

class MySubModelComplex(models.Model):
    _name = "my.submodel.complex"
    _description = "Submodel dari Model Utama"

    name = fields.Char(string="Submodel Name", required=True)
    value = fields.Integer(string="Value")
    parent_id = fields.Many2one('my.model.complex', string="Parent Model", ondelete="cascade")