from flask import Blueprint
from controllers.expense import expense_blueprint
from controllers.income import income_blueprint

transaction_blueprint = Blueprint('transaction', __name__)

transaction_blueprint.register_blueprint(expense_blueprint)
transaction_blueprint.register_blueprint(income_blueprint)
