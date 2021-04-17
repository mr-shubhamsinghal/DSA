
"""
LADDU
"""

T = int(input())
for _ in range(T):
    n, nationality = input().split()

    laddu = 0
    for i in range(int(n)):

        action_type = input().split()
        if action_type[0] == 'CONTEST_WON':
            rank = int(action_type[1])
            laddu += 300
            if rank < 20:
                laddu += 20 - rank
        elif action_type[0] == 'TOP_CONTRIBUTOR':
            laddu += 300
        elif action_type[0] == 'BUG_FOUND':
            severity = int(action_type[1])
            laddu += severity
        elif action_type[0] == 'CONTEST_HOSTED':
            laddu += 50
    
    months = 0
    if nationality == 'INDIAN':
        months = laddu//200
    else:
        months = laddu//400

    print(months)
