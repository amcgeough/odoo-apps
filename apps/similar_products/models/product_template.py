# -*- coding:utf-8 -*-

from odoo import models,fields


class SimilarProductTemplate(models.Model):
    _inherit = 'product.template'

    similar_products = fields.One2many('similar.products', 'product_id', string='Similar Products', copy=True)

    def similar(self):
        """
        View similar products using Name field via pg base_fuzzy addon
        """
        id = self.id
        self.env['similar.products'].search([('product_id','=',id)]).unlink()

        # set the fuzzy match threshold
        threshold = self.env['ir.config_parameter'].sudo().get_param('similar_products.similarity_threshold') or 0.3
        self.env.cr.execute(f"SELECT set_limit({threshold});")

        product_template = self.env['product.template'].search([('id','=',id),('active','in',[True,False])], limit=1)

        # base_search_fuzzy pg search addon
        similar_prods = self.env['product.template'].search([('name', '%', product_template.name)])
        for rec in similar_prods:
            if id != rec.id:
                product_id = self.env['product.template'].search([('id','=',rec.id)], limit=1).id
                sim = {'product_id': id,
                        'similar_id': product_id
                        }
                self.env['similar.products'].create(sim)
