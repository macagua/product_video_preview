# -*- coding: utf-8 -*-
{
    'name': 'Product Video Preview',
    'version': '13.0.1.0.1',
    'author': 'Leonardo Caballero <leonardo@pidela.cl>',
    'license': 'AGPL-3',
    'maintainer': 'Leonardo Caballero <leonardo@pidela.cl>',
    'support': 'soporte@pidela.cl',
    'category': 'Hidden',
    'description': """
Product Video Preview
=====================

This module enable a field to enter the URL for a Product video preview. On giving the URL the video can be previewed.

""",
    'depends': [
        'base',
        'web',
        'product'
    ],
    'website': 'https://github.com/macagua/product_video_preview/',
    'data': [
        'views/template.xml',
        'views/product_template.xml'
    ],
    "qweb": [
        'static/src/xml/product_video.xml'
    ],
    'demo': [],
    'images': [
        'static/description/icon.png'
    ],
    'installable': True
}

