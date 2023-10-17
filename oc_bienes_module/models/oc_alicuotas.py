from odoo import models, fields

class Alicuotas(models.Model):
    _name = 'oc.alicuotas'
    _description = 'Alicuotas'

    company_id = fields.Many2one('res.company', string='Compañía')
    bien_inmueble_id = fields.Many2one('oc.bien.inm', string='Bien Inmueble')
    fecha_pagos = fields.Date(string='Fecha de Pagos')
    valor = fields.Float(string='Valor')