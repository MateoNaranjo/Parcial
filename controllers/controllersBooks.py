from flask import Blueprint

books_bp = Blueprint('band_bp', __name__)

@books_bp.route('/bands', methods=['GET'])

@books_bp.route('/bands/<int:band_id>', methods=['GET'])

@books_bp.route('/bands', methods=['POST'])

@books_bp.route('/bands/<int:band_id>', methods=['PUT'])

@books_bp.route('/bands/<int:band_id>', methods=['DELETE'])