from typing import List
from Board import Board


class User:
    def __init__(self, username, boards={}, tasks={}, sections={}):
        self.__username = username
        self.__boards = boards
        self.__tasks = tasks
        self.__sections = sections
    
    def getUsername(self):
        return self.__username
    
    def addBoard(self, board):
        self.__boards[board.getId()] = board
        
        board.addMemberUsername(self.__username)

    def createBoard(self, boardTitle: str, boardId):
        board = Board(boardTitle, boardId)
        
        self.__addBoard(board)

    def deleteBoard(self, boardId):
        self.__boards.pop(boardId, None)
