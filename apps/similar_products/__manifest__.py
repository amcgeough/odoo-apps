# -*- coding:utf-8 -*-

{
	'name' : 'Similar Products',
	'version': '1.0',
    'author' : 'Andrew McGeough',
    'website' : 'wwww.google.com',
    'license': 'Other proprietary',
	'category': 'Product',
	'summary':  """Display similar products via fuzzy search on product name""",
	'description': """
	Requires OCA addons base_search_fuzzy (provides Postgres fuzzy/trigram search) and web_widget_numeric_step
	""",
	'depends': ['product', 'base_search_fuzzy', 'web_widget_numeric_step'],
	'data': [
		'views/product_template_views.xml',
        'security/ir.model.access.csv',
		'views/res_config_settings_views.xml'
	],
	'installable' : True,
	'application' : True,
	'auto_install' : False,
}




