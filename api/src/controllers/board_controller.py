from flask import Blueprint, jsonify

from src.repositories.board_repository import get_board_repository

board_controller = Blueprint('board_controller', __name__, url_prefix='/board')


@board_controller.route('/<uuid:board_id>', methods=['GET'])
def get_board(board_id):
    board_repository = get_board_repository()
    return jsonify(board_repository.get_by_id(board_id).model_dump()), 200
