#imports
from random import randint

hello = ['Доброго времени суток', "Приветствую","Привет","Здравствуй","Приветик"]
mood = ["Как у помощника","Неплохо, спасибо","Лучше не бывает","Прекрасно"]
bye = ["Удачи","До встречи","Пока","До свидания","Всего хорошего"]
leagues = ["Приятной игры","Так Точно"]

def get_hello():
	return hello[randint(0, len(hello) - 1)]

def get_mood():
	return mood[randint(0, len(mood) - 1)]

def get_bye():
	return bye[randint(0, len(bye) - 1)]

def get_league():
	return leagues[randint(0, len(leagues) - 1)]