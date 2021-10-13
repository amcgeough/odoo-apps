from odoo import models, fields


class SimilarProductTemplate(models.Model):
    _inherit = 'product.template'

    similar_products = fields.One2many('similar.products', 'product_id', string='Similar Products', copy=True)

    def similar(self):
        """
        View similar products using Name field via pg base_fuzzy addon
        """

        # Clear previous results
        self.env['similar.products'].search([('product_id','=',self.id)]).unlink()

        # Set the fuzzy match threshold using config setting value
        threshold = self.env['ir.config_parameter'].sudo().get_param('similar_products.similarity_threshold') or 0.3
        threshold = 0 if float(threshold) < 0 else 1 if float(threshold) > 1 else threshold
        self.env.cr.execute(f"SELECT set_limit({threshold});")

        # base_search_fuzzy postgres search addon (OCA) - %
        similar_products = self.env['product.template'].search([('name', '%', self.name)])
        for record in similar_products:
            if self.id != record.id:
                self.env['similar.products'].create({'product_id': self.id, 'similar_id': record.id})
