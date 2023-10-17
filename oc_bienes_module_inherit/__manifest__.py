# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Módulo de Bienes Inmuebles - OctupusTech',
    'version': '16.0.1.6.24',
    'license': 'LGPL-3',
    'category': 'OctupusTech',
    'author': 'OctupusTech',
    "company": 'OctupusTech',
    'website': 'https://www.octupustech.com/',
    'summary': 'Módulo de operaciones para Bienes Inmuebles',
    'description': """
Bienes Inmuebles  Module
==================
    """,
    'depends': ['base'],
    'data': [
        #
        'views/oc_bienes_inm.xml',
        'views/oc_alicuotas.xml',
        'views/oc_convenios.xml',
        'views/oc_llaves.xml',
        'views/oc_entrega.xml',

        #

        #

        #

        #

        #

        #

        #
        'views/ir_ui_menu.xml',
        #
        'security/ir.model.access.csv',


        #
    ],
    "qweb": [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
