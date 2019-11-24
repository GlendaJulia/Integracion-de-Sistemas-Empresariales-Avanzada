from odoo import models,fields,api

class FacturacionDocuments(models.Model):
	_name = 'facturacion.documentos'
	_description = 'Documentos de Facturacion'

	code = fields.Char(string='Codigo')
	description = fields.Char(string='Descripcion')