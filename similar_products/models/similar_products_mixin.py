from odoo import models, fields, api
import logging


class SimilarProductsMixIn(models.AbstractModel):
    _name = 'similar.products.mixin'
    _description = 'Resuable abstract mixin class for similar products'

    name_fuzzy = fields.Char(
        string="Fuzzy Name",
        compute="_compute_name_fuzzy",
        store=True,
        index=True,
        help="Non-translatable name for fuzzy search"
    )

    @api.depends('name')
    def _compute_name_fuzzy(self):
        for rec in self:
            rec.name_fuzzy = rec.name


    def similar(self):
        """
        View similar products using Name field via pg base_fuzzy addon
        """

        # Clear previous results
        self.env['similar.products'].search([(f"{self._name.replace('.', '_')}_id",'=',self.id)]).unlink()

        # Set the fuzzy match threshold using config setting value
        threshold = self.env['ir.config_parameter'].sudo().get_param('similar_products.similarity_threshold') or 0.3
        threshold = 0 if float(threshold) < 0 else 1 if float(threshold) > 1 else threshold
        self.env.cr.execute(f"SELECT set_limit({threshold});")

        # base_search_fuzzy postgres search addon (OCA) - %
        logging.info(f"Searching '{self.name_fuzzy}' with id '{self.id}' for similar products with threshold '{threshold}'")
        similar_products = self.env['product.template'].search([('name_fuzzy', '%', self.name_fuzzy)])
        logging.info(f"Found {len(similar_products)} similar products")
        
        # Add new results
        for product_template in similar_products:
            product_product = self.env['product.product'].search([('product_tmpl_id','=',product_template.id)], limit=1)
            
            if self._name == 'product.template' and self.id != product_template.id:
                self.env['similar.products'].create({'product_template_id': self.id, 'similar_id': product_template.id})

            elif self._name == 'product.product' and self.id != product_product.id:
                self.env['similar.products'].create({'product_product_id': self.id, 'similar_id': product_template.id})

            else:
                pass
