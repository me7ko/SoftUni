budget_for_actors = float(input())
flag = False
actor_name = input()
while actor_name != "ACTION":

    if len(actor_name) <= 15:
        reward = float(input())
        budget_for_actors -= reward
    else:
        budget_for_actors *= 0.8
    if budget_for_actors < 0:
        flag = True
        break
    actor_name = input()
if flag:
    print(f"We need {abs(budget_for_actors):.2f} leva for our actors.")
else:
    print(f"We are left with {budget_for_actors:.2f} leva.")