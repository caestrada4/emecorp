from odoo import models, fields

class Entrega(models.Model):
    _name = 'oc.entrega'
    _description = 'Entrega'

    numero = fields.Char(string='Número')
    tipo = fields.Selection([
        ('entrega', 'Acta de Entrega'),
        ('recepcion', 'Acta de Recepción'),
    ], string='Tipo')
    company_id = fields.Many2one('res.company', string='Compañía')
    bien_inmueble_id = fields.Many2one('oc.bien.inm', string='Bien Inmueble')
    fecha_entrega = fields.Date(string='Fecha de Entrega o Recepción')
    cliente = fields.Many2one('res.partner', string='Cliente')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('completo', 'Completo'),
    ], string='Estado')
    solicitante = fields.Many2one('res.partner', string='Solicitante')
    asignado_a = fields.Many2one('res.partner', string='Asignado a')
