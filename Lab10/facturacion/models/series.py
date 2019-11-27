
from odoo import models,fields,api

class Series(models.Model):
	_name = 'facturacion.series'
	_description = 'Series de documentos'

	name = fields.Char(string='Nombre de la serie')
	prefix = fields.Char(string='Prefijo de la serie')
	document_type = fields.Selection([('01','Factura'),
		('03','Boleta'),
		('04','Nota de Crédito'),
		('05','Nota de Débito')
	])
	active = fields.Boolean(string='Estado de la serie', default=True)
