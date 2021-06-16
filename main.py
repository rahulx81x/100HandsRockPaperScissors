from computer import computer
import logic
import time
consent = 'y'
while consent == 'y':
    print("\nWELCOME TO 100 HANDS ROCK PAPER SCISSOR")
    time.sleep(1)
    player_sign = input('ENTER YOUR HAND SIGN \n\nr=rock,p=paper, and s=scissor:  ')
    win_count = logic.winner(player_sign, computer)
    if win_count == 0:
        print("\nWoaah, where did you spend all your luck. You Got 0 wins")
    if 0 < win_count < 33:
        print('\nStill Impressive. Your win count is: ', end="")
        print(win_count)
    if 33 <= win_count < 50:
        print('\nMajestic,. You score ', end="")
        print(win_count, end=" ")
        print('wins')
    if 50 <= win_count < 100:
        print('\nHow did you do that?. Your win count is: ', end="")
        print(win_count)
    if win_count == 100:
        print('\nNo Mercy! ABSOLUTE DOMINATION. YOU SCORED A CENTURY')
    consent = input('\n\nWANNA PLAY AGAIN!??? \n input y for yes , anything else for No ')

print('\nWe hope to see you again!')
print('-rahulx81x')
time.sleep(3)
#rahulx81x