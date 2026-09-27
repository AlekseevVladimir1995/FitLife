# Проект FitLife - MVP версия 1.0


WATER_30_ML = 30  # константа - коэфициент нормы воды
print('Здравствуйте! Давайте знакомиться, я - фитнес-трекер FitLife.')
user_name = input('Как вас зовут: ')
user_age = int(input('Сколько Вам лет: '))

user_weight = float(input('Ваш вес в килограммах: '))
user_height = input('И Ваш вост в метрах с точкой (например, 1.75): ')
user_height_clean = float(user_height.replace(',', '.'))  # страхуемся от ','

bmi = round((user_weight / (user_height_clean ** 2)), 1)

water_ml = user_weight * WATER_30_ML
water_needed = round((water_ml / 1000), 1)  # норму воды округлил до одного

print()  # пустая строка для удобства чтения
print(f'Отчет для пользователя: {user_name} ({user_age} л.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_needed}')
print()  # отделил пожелание пропуском
print('Расчет окончен. Будьте здоровы!')
