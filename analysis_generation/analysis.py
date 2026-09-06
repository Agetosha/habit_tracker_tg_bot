import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('habit_market_research.csv')

plt.style.use('ggplot') 
fig = plt.figure(figsize=(18, 12))
fig.suptitle('Анализ актуальности проекта: "Трекер привычек с геймификацией"', fontsize=20)

ax1 = fig.add_subplot(2, 2, 1)
habit_counts = df['Habit_Type'].value_counts()
ax1.pie(habit_counts, labels=habit_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
ax1.set_title('Распределение интересов пользователей (Ниши)')

ax2 = fig.add_subplot(2, 2, 2)
avg_success = df.groupby('Tracking_Method')['Success_Rate_Percent'].mean().sort_values()
bars = ax2.bar(avg_success.index, avg_success.values, color=['gray', 'lightblue', 'orange', 'green'])
ax2.set_title('Средний % успеха выполнения привычки по методам')
ax2.set_ylabel('Успешность (%)')
ax2.set_xlabel('Метод отслеживания')
ax2.bar_label(bars, fmt='%.1f%%')

ax3 = fig.add_subplot(2, 2, 3)
dropped_data = df[df['Dropped_Early'] == True]['Days_Streak']
ax3.hist(dropped_data, bins=20, color='salmon', edgecolor='black', alpha=0.7)
ax3.set_title('Распределение дней отказа от привычки (Кто бросил)')
ax3.set_xlabel('На какой день бросили')
ax3.set_ylabel('Количество людей')
ax3.axvline(x=21, color='red', linestyle='--', linewidth=2, label='21 день (формирование)')
ax3.legend()

ax4 = fig.add_subplot(2, 2, 4)
methods_order = ['None', 'Paper', 'Simple App', 'Gamified App']
data_to_plot = [df[df['Tracking_Method'] == m]['Days_Streak'] for m in methods_order]
ax4.boxplot(data_to_plot, labels=methods_order, patch_artist=True)
ax4.set_title('Сравнение длительности непрерывных серий (Стриков)')
ax4.set_ylabel('Дней подряд')
ax4.set_xlabel('Метод')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

print("="*50)
print("обоснование полезности проекта (на основе данных):")
print("="*50)

top_habit = habit_counts.idxmax()
print(f"1. актуальность: самая популярная категория — '{top_habit}'. "
      f"люди активно ищут способы улучшить себя в спорте и обучении.")

drop_rate = len(df[df['Days_Streak'] < 21]) / len(df) * 100
print(f"2. проблема: {drop_rate:.1f}% пользователей бросают привычку до 21-го дня (этап формирования). "
      f"гистограмма показывает пик отказов в первые две недели.")

gamified_mean = df[df['Tracking_Method'] == 'Gamified App']['Success_Rate_Percent'].mean()
none_mean = df[df['Tracking_Method'] == 'None']['Success_Rate_Percent'].mean()
improvement = gamified_mean - none_mean
print(f"3. эффективность: использование геймифицированного приложения "
      f"повышает успешность на {improvement:.1f}% по сравнению с отсутствием контроля.")

print("\nвывод: разработка telegram-бота с системой стриков и ачивок оправдана, "
      "так как это решает проблему удержания привычки в критический период (до 21 дня) "
      "значительно эффективнее конкурентных методов.")