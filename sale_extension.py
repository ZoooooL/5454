
from odoo import models, fields

class ZoolAIDashboard(models.Model):
    _name = "zool.ai.dashboard"
    _description = "Zool AI Dashboard"

    name = fields.Char(default="AI Overview")
    total_sales = fields.Float(string="Total Sales")
    total_invoices = fields.Float(string="Total Invoices")
    ai_comment = fields.Text(string="AI Insight")
