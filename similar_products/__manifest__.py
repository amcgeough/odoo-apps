# -*- coding:utf-8 -*-

{
	'name' : 'Similar Products',
	'version': '15.0.2',
    'author' : 'Andrew McG',
	'category': 'Products',
	'summary':  'Display similar products via fuzzy search on product name',
	'description': 'Requires OCA addons base_search_fuzzy (provides Postgres fuzzy/trigram search)',
	'depends': [
				'sale_management',
				'base_search_fuzzy'
				],
	'data': [
		'views/product_template_views.xml',
        'security/ir.model.access.csv',
		'views/res_config_settings_views.xml'
	],
	'installable' : True,
	'application' : True,
	'auto_install' : False,
    'license': 'AGPL-3',
	'images':[
        'static/description/thumbnail.png'
	],
    'post_init_hook': 'install_pg_trgm',
}
