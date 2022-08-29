# Ninja Training
# 2D DP

tasks = [[2, 1, 3],
         [3, 4, 6],
         [10, 1, 6],
         [8, 3, 7]]

dp = [[-1 for i in range(4)] for j in range(len(tasks))]


def total_points(day, last):
    if day == 0:
        maxi = 0
        for i in range(3):
            if i != last:
                maxi = max(maxi, tasks[0][i])
        return maxi

    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for i in range(3):
        if i != last:
            points = tasks[day][i] + total_points(day - 1, i)
            maxi = max(maxi, points)

    dp[day][last] = maxi

    return dp[day][last]


print(total_points(len(tasks) - 1, 3))
