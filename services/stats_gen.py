import matplotlib.pyplot as plt
import io
import pandas as pd

def generate_habit_chart(habit_title, logs):
    # logs - это список объектов HabitLog
    if not logs:
        return None

    data = {
        'Date': [log.date_logged.strftime('%Y-%m-%d') for log in logs],
        'Minutes': [log.minutes_spent for log in logs]
    }
    df = pd.DataFrame(data)
    # Группируем по дате, суммируем минуты
    df = df.groupby('Date').sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(df['Date'], df['Minutes'], color='skyblue', edgecolor='navy')
    plt.title(f'Прогресс по привычке: {habit_title}')
    plt.xlabel('Дата')
    plt.ylabel('Минуты')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Сохраняем в буфер (в память)
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return buf