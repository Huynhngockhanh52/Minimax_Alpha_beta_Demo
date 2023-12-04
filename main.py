# ===================== Chương trình trò chơi NIM ========================
# Thư viện sử dụng
import numpy
from alphabeta_solution import alphabetaFunction

class Board(object):
    """
    Lớp Board là lớp chương trình chính, bao gồm các phương thức khởi tạo, phương thức cập nhật trạng thái tiếp theo và phương thức tính toán của máy.

    Args:
        object: Dữ liệu đầu vào cần truyền vào để khởi tạo
    """
    
    # Phương thức khởi tạo
    def __init__(self, board):
        self.board = board

    # Cập nhật lại trạng thái sau mỗi lượt chơi
    def update(self, piles, num):
        self.board[piles] -= num

    # Phương thức tính toán của người chơi là máy tính
    def computerUpdate(self):
        self.board = alphabetaFunction(self.board, -float('inf'), float('inf'), True)[1][1]

def isValid(remove, board):
    """
    Phương thức isValid xác định dữ liệu đầu vào cho mỗi lượt đi có chính xác hay không.

    Args:
        remove: Dữ liệu đầu vào cho mỗi lượt chơi
        board: Dữ liệu về số lượng sỏi hiện tại

    Returns:
        True or False: True nếu dữ liệu phù hợp, ngược lại là False
    """
    if not remove or len(remove) != 2: return False
    if remove[0] > 0 and remove[1] > 0 and remove[1] <= len(board) and remove[0] <= board[int(remove[1]-1)]:
        return True
    return False

# Phương thức main, xử lý chính trò chơi:
if __name__ == "__main__":
    print("======================== Starting Nim Game with AI! ========================")

    # Khởi tạo dữ liệu đầu vào
    ele = int(input("Số lượng đống sỏi: "))
    lis = []

    print("Số lượng sỏi có trong mỗi đống (sử dụng ENTER để ngăn cách mỗi giá trị):")
    for _ in range(ele):
        lis.append(int(input()))

    game = Board(lis)
    print("***CHÚ Ý:***")
    print("Nhập số lượng sỏi cần loại bỏ, tiếp theo mới nhập vị trí của đống để loại bỏ: ")
    print("Người chơi loại bỏ viên sỏi cuối cùng sẽ thua cuộc --> LOSE!")
    print("Example: Loại bỏ 3 viên sỏi từ đống thứ 2 --> 3 2, ENTER")

    player_win = True
    while True:
       
        print("Lượng sỏi hiện tại: %s" %(game.board))

        # player's turn
        user = str(input("Lượt người chơi: "))
        player_remove = [int(i) for i in user.strip().split(' ')]

        while not isValid(player_remove, game.board):
            print("ERROR! Giá trị đầu vào không chính xác!\nNhập lại dữ liệu!")
            user = str(input("Lượt người chơi: "))
            player_remove = [int(i) for i in user.split(' ')]
        print(f"Bạn đã thực hiện loại bỏ {player_remove[0]} viên sỏi tại đống thứ {player_remove[1]}!")
        
        game.update(int(player_remove[1] - 1), player_remove[0])

        if sum(game.board) == 0:
            player_win = False
            break
        elif sum(game.board) == 1:
            break
        
        print("Lượng sỏi hiện tại: %s" %(game.board))
        print("Lượt người máy AI!...")
        pre_state = game.board[:]
        game.computerUpdate()
        for index, value in enumerate(pre_state):
            if (value != game.board[index]):
                aiplayer = [int(value-game.board[index]), index+1]
        print(f"Người máy đã thực hiện loại bỏ {aiplayer[0]} viên sỏi tại đống thứ {aiplayer[1]}!")

        if sum(game.board) == 0:
            break
        elif sum(game.board) == 1:
            player_win = False
            break

    if player_win:
        print(game.board)
        print("Bạn đã thắng --> VICTORY!!!")
    else:
        print(game.board)
        print("Bạn thua cuộc --> LOSE!!!")

