

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1+score_2
time_avg = (team1_time+team2_time)/tasks_total

print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %d и %d" %(team1_num, team2_num))

print( "Команда Волшебники данных решила задач: {}!".format(score_2))
print( "Волшебники данных решили задачи за {time} c".format(time=team1_num))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Результат битвы: победа команды Мастера кода со счетом {score_1} за {team1_time} c!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Результат битвы: победа команды Волшебнники Данных со счетом {score} за {time} c!'.format(score=score_2, time=team2_time))
else:
    print("Ничья")

