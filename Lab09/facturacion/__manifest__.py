# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Facturacion",
    "summary": "Modulo basico para facturacion en Peru",
    "version": "1.0",
    "category": "Themes/Backend",
    "description": """
		Mecanismos para modulos de Contabilidad
    """,
    "depends": ['account'],
    "data": [
        'views/series_view.xml',
        'data/series.xml',
        'views/account_invoice_view.xml',
        'views/documentacion.xml',
        'data/documentacion.xml'
    ],
}

