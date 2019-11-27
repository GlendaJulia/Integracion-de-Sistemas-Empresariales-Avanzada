from odoo import models,fields,api

class FacturacionDocuments(models.Model):
	_name = 'facturacion.documentos'
	_description = 'Documentos de Facturacion'

	name = fields.Char(string='Nombre del documento')
	code = fields.Char(string='Codigo')