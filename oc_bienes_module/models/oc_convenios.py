from odoo import models, fields

class Convenios(models.Model):
    _name = 'oc.convenios'
    _description = 'Convenios'

    company_id = fields.Many2one('res.company', string='Compañía')
    organizacion = fields.Char(string='Organización')
    fecha_primer_pago = fields.Date(string='Fecha del Primer Pago')
    valor_convenio = fields.Float(string='Valor del Convenio')
    numero_cuotas = fields.Integer(string='Número de Cuotas')