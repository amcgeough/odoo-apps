# -*- coding:utf-8 -*-

{
	'name' : 'Similar Products',
	'version': '13.0.1',
    'author' : 'Andrew McGeough',
    'website' : 'wwww.mortimerapps.com',
	'category': 'Products',
	'summary':  'Display similar products via fuzzy search on product name',
	'description': 'Requires OCA addons base_search_fuzzy (provides Postgres fuzzy/trigram search)',
	'depends': ['product', 'base_search_fuzzy'],
	'data': [
		'views/product_template_views.xml',
        'security/ir.model.access.csv',
		'views/res_config_settings_views.xml'
	],
	'installable' : True,
	'application' : True,
	'auto_install' : False,
    'license': 'AGPL-3',
	'image': 'images/similar-products.png',
	'support': 'info@mortimerapps.com',
	# 'price': 100,
	# 'currency': 'EUR'
}
