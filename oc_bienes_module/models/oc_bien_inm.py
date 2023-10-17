from odoo import models, fields

class BienInmueble(models.Model):
    _name = 'oc.bien.inm'
    _description = 'Bien Inmueble'

    codigo_bien = fields.Char(string='Código del Bien Inmueble')
    tipo = fields.Char(string='Tipo')
    nombre = fields.Char(string='Nombre')
    ciudad = fields.Char(string='Ciudad')
    costo_recepcion = fields.Float(string='Costo de Recepción')
    costo_escritura = fields.Float(string='Costo Según Escritura')
    precio_lista = fields.Float(string='Precio de Lista')
    tipo_derecho = fields.Char(string='Tipo de Derecho')
    fecha_adquisicion = fields.Date(string='Fecha de Adquisición (Inscripción)')
    company_id = fields.Many2one('res.company', string='Compañía')
    fecha_efectiva_recepcion_material = fields.Date(string='Fecha Efectiva de Recepción Material')
    recibido_de = fields.Char(string='Recibido de')
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], string='Estado')
    subestado = fields.Char(string='Subestado')
    destino = fields.Char(string='Destino')

    # Campos secundarios
    fecha_pactada_recepcion_material = fields.Date(string='Fecha Pactada para la Recepción Material')
    fecha_pactada_recepcion_legal = fields.Date(string='Fecha Pactada para la Recepción Legal')
    area_solar_m2 = fields.Float(string='Área del Solar en m²')
    area_construccion_m2 = fields.Float(string='Área de Construcción en m²')
    bienes_accesorios = fields.Char(string='Bienes Accesorios')
    contrato_origen = fields.Char(string='Contrato de Origen')
    uso_suelo = fields.Char(string='Uso del Suelo')
    valor_alicuota = fields.Float(string='Valor de la Alícuota')
