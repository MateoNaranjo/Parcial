from flask import Blueprint

books_bp = Blueprint('books_bp', __name__)

@books_bp.route('/books', methods=['GET'])

@books_bp.route('/books/<int:band_id>', methods=['GET'])

@books_bp.route('/books', methods=['POST'])

@books_bp.route('/books/<int:band_id>', methods=['PUT'])

@books_bp.route('/books/<int:band_id>', methods=['DELETE'])
