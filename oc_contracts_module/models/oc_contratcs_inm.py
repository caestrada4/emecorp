from odoo import models, fields

class ContractInmueble(models.Model):
    _name = 'oc.contractc.inm'
    _description = 'Contrato de Inmueble'

    numero_contrato = fields.Char(string='Número de Contrato')
    objeto = fields.Char(string='Objeto')
    company_id = fields.Many2one('res.company', string='Compañía')
    fecha_solicitud = fields.Date(string='Fecha de Solicitud')
    fecha_creacion = fields.Date(string='Fecha de Creación')
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], string='Estado')
    razon_social = fields.Char(string='Razón Social')
    fecha_vencimiento = fields.Date(string='Fecha de Vencimiento')
    nombre_arrendadora = fields.Char(string='Nombre de la arrendadora o concedente')
    precio_venta_inmueble = fields.Float(string='Precio de Venta del Inmueble')
    canon_arrendamiento = fields.Float(string='Canon de Arrendamiento')
    precio_contrato = fields.Float(string='Precio del contrato')
    bien_inmueble = fields.Char(string='Bien inmueble')

    # Campos secundarios
    vendedor = fields.Many2one('res.partner', string='Vendedor')
    corredor = fields.Many2one('res.partner', string='Corredor')
    proyecto_construccion = fields.Boolean(string='¿Es proyecto para construcción?')
    forma_pago = fields.Selection([
        ('efectivo', 'Efectivo'),
        ('cheque', 'Cheque'),
        ('tarjeta', 'Tarjeta de Crédito'),
    ], string='Forma de Pago')
    fecha_pago_financiar = fields.Date(string='Fecha de pago de valor a financiar')
    entidad_financiera = fields.Char(string='Entidad Financiera')
    valor_financiar = fields.Float(string='Valor a Financiar')
    plazo = fields.Integer(string='Plazo')
    unidad_medida = fields.Char(string='Unidad de Medida')
