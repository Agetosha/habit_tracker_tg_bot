import matplotlib.pyplot as plt #графики
import io #для буфера памяти
import pandas as pd #табличнык данные (DataFrame)

def generate_habit_chart(habit_title, logs):
    # создаем график прогресса по привычке
    if not logs:
        return None

    # формируем данные для графика
    data = {
        'Date': [log.date_logged.strftime('%Y-%m-%d') for log in logs],
        'Minutes': [log.minutes_spent for log in logs]
    }
    df = pd.DataFrame(data)
    # группируем по дате, суммируем минуты
    df = df.groupby('Date').sum().reset_index()

    # создаем столбчатую диаграмму
    plt.figure(figsize=(10, 6))
    plt.bar(df['Date'], df['Minutes'], color='skyblue', edgecolor='navy')
    plt.title(f'Прогресс по привычке: {habit_title}')
    plt.xlabel('Дата')
    plt.ylabel('Минуты')
    plt.xticks(rotation=45)  # поворачиваем подписи дат
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # сохраняем график в буфер памяти
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return buf