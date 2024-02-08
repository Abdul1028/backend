import traceback

from flask import Blueprint, request, jsonify
from models import Income
income_blueprint = Blueprint('income', __name__)

@income_blueprint.route('/add-income', methods=['POST'])
def add_income():
    try:
        data = request.get_json()
        title = data.get('title')
        amount = data.get('amount')
        category = data.get('category')
        description = data.get('description')
        date = data.get('date')

        income = Income(
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
        return jsonify({'message': 'Income Added'}), 200

    except Exception as e:
        return jsonify({'message': 'Server Error'}), 500

@income_blueprint.route('/get-incomes', methods=['GET'])
def get_incomes():
    try:
        incomes = Income.objects().order_by('-createdAt')
        return jsonify(incomes), 200

    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()
        return jsonify({'message': e}), 500

@income_blueprint.route('/delete-income/<id>', methods=['DELETE'])
def delete_income(id):
    try:
        income = Income.objects.get(id=id)
        income.delete()
        return jsonify({'message': 'Income Deleted'}), 200

    except Exception as e:
        return jsonify({'message': 'Server Error'}), 500
