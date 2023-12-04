# ===================== Giải thuật Minimax sử dụng phương pháp cắt tỉa Alpha-Beta ==========================

def alphabetaFunction(state, alpha, beta, maxTurn):
    """
    Phương thức alphabetaFunction thực hiện xác định lượng giá cho một trạng thái "state" hiện tại.

    Tham số:
        state: Trạng thái cần xác định lượng giá
        alpha: Giá trị alpha cho mức MAX
        beta : Giá trị beta cho mức MIN
        maxTurn: Lớp đang xét hiện tại của trạng thái đã cho

    Returns:
        res_max:
    """
    # Nếu đây là trạng thái của node lá hoặc là node gốc và các trường hợp tổng số lượng token xác định bằng 0 hoặc 1 thì đưa ra kết quả
    if (sum(state) == 1 and maxTurn) or (sum(state) == 0 and not maxTurn): return (-1, [state])
    if (sum(state) == 1 and not maxTurn) or (sum(state) == 0 and maxTurn): return (1, [state])
    
    # Trường hợp với lớp MAX
    if maxTurn:
        res_max = -float('inf')
        res = None
        for i in findNodeChild(state):
            val, temp = alphabetaFunction(i, alpha, beta, not maxTurn)
            if val > res_max:
                res_max = val
                res = temp
            # Cập nhật lại giá trị alpha
            alpha = max(alpha, val)
            # Cắt tỉa
            if alpha >= beta:
                break
        return res_max, [state] + res
    # Thực hiện với mức MIN
    else: 
        res_min = float('inf')
        res = None
        for i in findNodeChild(state):
            val, temp = alphabetaFunction(i, alpha, beta, not maxTurn)
            if val < res_min:
                res_min = val
                res = temp
            beta = min(beta, val)
            if alpha >= beta:
                break
        return res_min, [state] + res
    
def findNodeChild(state):
    """
    Phương thức findNodeChild tìm tất cả các trạng thái con (trạng thái tiếp theo) của trạng thái hiện tại. 

    Args:
        state: Trạng thái hiện tại cần xác định

    Returns:
        res: Một mảng các trạng thái con của trạng thái cho trước.
    """
    visited = set()
    res = []
    
    for i in range(len(state)):
        for m in range(1, state[i] + 1):
            temp = list(state[:])
            temp[i] -= m
            # Nếu trạng thái đó đã tồn tại thì bỏ qua, ngược lại thêm vào res
            rearranged = tuple(sorted(temp))
            if rearranged not in visited:
                res.append(temp)
                visited.add(rearranged)
    return res