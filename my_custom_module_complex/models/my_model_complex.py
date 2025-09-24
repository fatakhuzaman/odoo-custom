from odoo import models, fields, api

class MyModelComplex(models.Model):
    _name = "my.model.complex"
    _description = "Model Utama"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")

    submodel_ids = fields.One2many('my.submodel.complex', 'parent_id', string="Submodels")

    total_submodels = fields.Integer(string="Total Submodels", compute="_compute_total_submodels")
    fix_total_submodels = fields.Integer(string="Fix Total Submodels")

    total_value = fields.Float(string="Total Value", compute="_compute_total_value")

    @api.depends('submodel_ids')
    def _compute_total_submodels(self):
        for record in self:
            record.total_submodels = len(record.submodel_ids) * 2

    def button_count_submodels(self):
        for record in self:
            record.fix_total_submodels = len(record.submodel_ids)

    @api.depends('submodel_ids.value')
    def _compute_total_value(self):
        for record in self:
            record.total_value = sum(record.submodel_ids.mapped('value'))