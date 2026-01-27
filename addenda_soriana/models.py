from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    # Campo para guardar el numero de proveedor (Ej. 325746)
    soriana_proveedor_id = fields.Char(string='ID Proveedor Soriana')

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Campos que cambian en cada factura
    soriana_folio_entrada = fields.Char(string='Folio Nota de Entrada Soriana')
    soriana_numero_tienda = fields.Char(string='Número de Tienda Soriana', default='992')
