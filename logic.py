def winner(player, comp):
    win_count = 0
    for i in range(len(comp)):
        if (player == 'r' and comp[i][0] == 's') or (player == 's' and comp[i][0] == 'p') or (player == 'p' and comp[i][0] == 'r'):
            win_count += 1
    print(comp)
    return win_count
