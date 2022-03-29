from odoo import models, fields


class SimilarProductsMixIn(models.AbstractModel):
    _name = 'similar.products.mixin'

    def similar(self):
        """
        View similar products using Name field via pg base_fuzzy addon
        """

        # Set the fuzzy match threshold using config setting value
        threshold = self.env['ir.config_parameter'].sudo().get_param('similar_products.similarity_threshold') or 0.3
        threshold = 0 if float(threshold) < 0 else 1 if float(threshold) > 1 else threshold
        self.env.cr.execute(f"SELECT set_limit({threshold});")

        # base_search_fuzzy postgres search addon (OCA) - %
        similar_products = self.env['product.template'].search([('name', '%', self.name)])
        
        # Clear previous results and add new ones
        for product_template in similar_products:
            product_product = self.env['product.product'].search([('product_tmpl_id','=',product_template.id)], limit=1)
            
            if self._name == 'product.template' and self.id != product_template.id:
                self.env['similar.products'].search([('product_template_id','=',self.id)]).unlink()
                self.env['similar.products'].create({'product_template_id': self.id, 'similar_id': product_template.id})

            elif self._name == 'product.product' and self.id != product_product.id:
                self.env['similar.products'].search([('product_product_id','=',self.id)]).unlink()
                self.env['similar.products'].create({'product_product_id': self.id, 'similar_id': product_template.id})

            else:
                pass