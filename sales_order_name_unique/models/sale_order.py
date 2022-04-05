from odoo import fields,models, _


class SalesNameUnique(models.Model):
    _inherit = "sale.order"
    _sql_constraints = [
                     ('name', 
                      'unique(name)',
                      'Choose another name - it has to be unique!')
                    ]
