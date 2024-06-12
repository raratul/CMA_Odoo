from odoo import models, fields

class Collection(models.Model):
    _name = 'collections_import.collection'
    _description = 'Collection'

    owner = fields.Many2one('res.users', string='Owner', required=True)
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    number_of_items = fields.Integer(string='Number of Items')
    category = fields.Selection([
        ('Books', 'Books'),
        ('Signs', 'Signs'),
        ('Silverware', 'Silverware'),
        ('Other', 'Other')
    ], string='Category', required=True)
