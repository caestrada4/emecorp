from odoo import models, fields

class Llaves(models.Model):
    _name = 'oc.llaves'
    _description = 'Llaves'

    ubicacion = fields.Char(string='Ubicación')
    bienes_inmuebles_id = fields.Many2one('oc.bien.inm', string='Bienes Inmuebles')
    urbanizacion = fields.Char(string='Urbanización')
    casillero = fields.Char(string='Casillero')
    quien_recibe = fields.Many2one('res.partner', string='Quién Recibe')
    fecha_entrega = fields.Date(string='Fecha de Entrega')
    dia_visita = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ], string='Día de Visita')