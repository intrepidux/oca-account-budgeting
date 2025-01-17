# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ExpenseBudgetMove(models.Model):
    _name = "expense.budget.move"
    _inherit = ["base.budget.move"]
    _description = "Expense Budget Moves"

    expense_id = fields.Many2one(
        comodel_name="hr.expense",
        readonly=True,
        index=True,
        help="Commit budget for this expense_id",
    )
    sheet_id = fields.Many2one(
        comodel_name="hr.expense.sheet",
        related="expense_id.sheet_id",
        readonly=True,
        store=True,
        index=True,
    )
    move_id = fields.Many2one(
        comodel_name="account.move",
        related="move_line_id.move_id",
        store=True,
    )
    move_line_id = fields.Many2one(
        comodel_name="account.move.line",
        readonly=True,
        index=True,
        help="Uncommit budget from this move_line_id",
    )

    @api.depends("sheet_id")
    def _compute_reference(self):
        for rec in self:
            rec.reference = (
                rec.reference if rec.reference else rec.sheet_id.display_name
            )
