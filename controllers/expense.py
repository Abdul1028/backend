from flask import Blueprint, request, jsonify
from models import Expense

expense_blueprint = Blueprint('expense', __name__)

@expense_blueprint.route('/add-expense', methods=['POST'])
def add_expense():
    try:
        data = request.get_json()
        title = data.get('title')
        amount = data.get('amount')
        category = data.get('category')
        description = data.get('description')
        date = data.get('date')

        income = Expense(
            title=title,
            amount=amount,
            category=category,
            description=description,
            date=date
        )

        # Validations
        if not all([title, category, description, date]):
            return jsonify({'message': 'All fields are required!'}), 400

        if amount <= 0 or not isinstance(amount, (int, float)):
            return jsonify({'message': 'Amount must be a positive number!'}), 400

        income.save()
        return jsonify({'message': 'Expense Added'}), 200

    except Exception as e:
        return jsonify({'message': 'Server Error'}), 500

@expense_blueprint.route('/get-expenses', methods=['GET'])
def get_expenses():
    try:
        incomes = Expense.objects().order_by('-createdAt')
        return jsonify(incomes), 200

    except Exception as e:
        return jsonify({'message': 'Server Error'}), 500

@expense_blueprint.route('/delete-expense/<id>', methods=['DELETE'])
def delete_expense(id):
    try:
        expense = Expense.objects.get(id=id)
        expense.delete()
        return jsonify({'message': 'Expense Deleted'}), 200

    except Exception as e:
        return jsonify({'message': 'Server Error'}), 500
