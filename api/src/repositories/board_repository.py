from src.entities.board_entity import BoardEntity
from src.models.board import Board


class BoardRepository:
    def get_by_id(self, board_id):
        board = Board.query.filter_by(id=board_id).first()
        if board is None:
            raise ValueError(f'Board with id {board_id} not found')  # noqa: TRY003
        return BoardEntity(id=board.id, name=board.name)


def get_board_repository():
    return BoardRepository()
