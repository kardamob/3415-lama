# ДИСКЛЕЙМЕР
ЯВЛЯЕТСЯ СТУДЕНЧЕСКИМ ПРОЕКТОМ ДЛЯ ОБРАЗОВАТЕЛЬНЫХ ЦЕЛЕЙ 
# 3415-lama
Реализация игры L.L.A.M.A.
## Правила игры
### Цель игры
Иметь наименьшее число очков, когда счет одного игрока достигнет 40 очков или более.
### Содержание
- 56 карт (8 со значением 1-6 & 8 лам) 
- 70 маркеров (20 черных 10s, 50 белых 1s)
### Создание игры
1. Перемешивайте все карты и раздавайте 6 карт каждому игроку
2. Разместите остальные карты в центр стол, чтобы сформировать колоду лицом вниз
3. Переверните верхнюю карту из колоды вытаскивания, чтобы начать колоду сброса
4. Разместите все маркеры на стол
5. Игра проводится в раундах — самый молодой игрок начинает первый раунд
6. Право хода передается справа налево
### Как играть?
На твой ход ты должен сделать одно из трех действий:
- Сыграть карту из своей руки на колоду сброса
- Вытащить карту, чтобы добавить в руку
- Уйти из раунда
      
#### 1. Сыграть карту
Верхняя карта на колоде сброса устанавливает какую карту вы можете сыграть:
- Вы можете сыграть карту с теми же значениями, что и верхняя карта или другой картой со значением плюс один
- Вы можете сыграть лады на верх 6 или на другие ламы
- Также вы можете сыграть 1s на верх лам
#### 2. Вытащить карту
Вытащить 1 карту из колоды. Вы не можете сыграть карту на том же ходе как вы вытащили одну, итак, игра переходит игроку слева от тебя
Если колода закончилась, нельзя создавать новую. С этого момента вы не можете выбирать это действие 
#### 3. Уйти с раунда
Если вы не можете сыграть карту (или не хотите) и не выбирать вытащить карту, мы обязаны пропустить настоящий раунд. Поместите карты перед собой лицевой стороной вниз
### Конец раунда
Раунд заканчивается когда:
- один игрок играет его/её последней картой или
- все игроки вышли из раунда
Если все игроки кроме одного покинули раунд, то этот игрок продолжит играть, но больше не может вытаскивать карты.

#### 4. Счёт
Каждая карта которую ты не сыграл дает тебе отрицательные очки, будь то в вашей руке или лицом вниз перед вами, потому что вы бросили раунд. Каждая карты стоит своему значению в очках. Ламы стоят 10 очков. Однако вы считаете каждую карточную ценность только единожды за раунд, итак, если вы имеете две 4s, например, вы получить только 4 очка и все ламы дают только 10 очков.
##### Взятие маркеров
Складываются все твои отрицательные очки и берутся это число маркеров. Белые маркеры стоят 1 очко и черные маркеры стоят 10 очков. Вы можете поменять 10 белых маркеров на 1 черный (или 1 черный на 10 белых) в любое время
##### Возвращение маркеров
Если вам удалось разыграть все ваши карты и вы имеете маркеры с предыдущего раунда, вы можете вернуть один из ваших маркеров или 1-очковый маркер, или 10-очковый маркер, ваш выбор.
После того как все игроки закончили набивать очки, пришло время начать новый раунд. Перемешать все карты и раздавать 6 каждому игроку. Начать новую колоду сброски с верхней карты из колоды вытаскивания. Последний игрок, который сыграл карту в предыдущем раунде, начинает новый раунд

### Конец игры
Продолжайте играть до тех пор, пока один из вас соберет 40 или более очков. Игрок с наименьшим количеством очков побеждает. Если у нескольких игроков очков одинаковое количество, то они разделяют победу.

## Пример текстового интерфейса игры 
```
Бито: 2
Миша: 3 5 4 1 Л
Миша: введите какую карту играем из руки: 8
Миша: такой карты нет в руке
Миша: введите какую карту играем из руки: 3
Миша: играет 3
-----
Бито: 3
Вася: 6 2 8 5 Л
Вася: берёт карту
Вася : 6 2 8 5 Л 4
Вася: Играет 4
----
Бито: 4
Миша: 5 4 1 Л
Миша: играет 5
----
Бито: 5
Вася: 6 2 8 5 Л
Вася: играет 6
---
Бито: 6
Миша: 4 1 Л
....
----
Миша WIN!
``` 

## Пример save-файла 
Начало игры.
```json
{
"top": "2",
"deck": "7 3 1 8 4",
"current_player_index": 0,
"players": [
{
"name": "Alex",
"hand": "5 6 4 2",
"is_human": true
},
{
"name": "Bob",
"hand": "6 2 4",
"is_human": false
}
]
}
```
