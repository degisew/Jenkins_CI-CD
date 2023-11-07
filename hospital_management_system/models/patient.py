from odoo import models, fields


class Patient(models.Model):
    _name = 'patient'
    _description = "A model that stores the patients data"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string='Is_child?')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')