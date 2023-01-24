from flask import Blueprint, Request, render_template, request, url_for, request_started, request_finished, redirect, flash
from flask_login import current_user, login_required
from app.models import Monsters, User, Team
import requests
import random

fight = Blueprint('fight', __name__, template_folder='fight_templates')

@fight.route('/fight/settings/<my_id>')
def settings(my_id):
    boxes = Team.query.filter_by(user_id = my_id)
    print(boxes)
    tchallenge_score = 0
    for box in boxes:
        if box.tclass == 'fighter':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1) 

        elif box.tclass == 'barbarian':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'warlock':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'ranger':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'paladin':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'battle dancer':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'wizard':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'bard':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'cleric':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)
        
        elif box.tclass == 'rogue':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)
    tchallenge_score = tchallenge_score / 4

    return render_template('fight_setting.html', boxes=boxes, tchallenge_score=tchallenge_score)
    

@fight.route('/fight/plans/<difficulty>/<my_id>')
def final_fight(my_id, difficulty):
    boxes = Team.query.filter_by(user_id = my_id)
    print(boxes)
    tchallenge_score = 0
    for box in boxes:
        if box.tclass == 'fighter':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1) 

        elif box.tclass == 'barbarian':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'warlock':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'ranger':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'paladin':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'battle dancer':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'wizard':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'bard':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)

        elif box.tclass == 'cleric':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)
        
        elif box.tclass == 'rogue':
            if box.level >= 1 and box.level <= 5:
                tchallenge_score += (box.level * 1)
            elif box.level >= 6 and box.level <= 10:
                tchallenge_score += (box.level * 1)
            elif box.level >= 11 and box.level <=15:
                tchallenge_score += (box.level * 1)
            elif box.level >= 16 and box.level <= 20:
                tchallenge_score += (box.level * 1)
    tchallenge_score = tchallenge_score / 4
    encounter = []
    match = 0
    monsters = Monsters.query.order_by(Monsters.challenge_rating).all()
    if difficulty == 'normal':
        while match <= (tchallenge_score - 3):
            monster = random.choice(monsters)
            rating = monster.challenge_rating
            if match + rating > tchallenge_score + 3:
                print('Fail')
            else:
                encounter.append(monster)
                match += rating
    elif difficulty == 'easy':
        while match <= (tchallenge_score - 5):
            monster = random.choice(monsters)
            rating = monster.challenge_rating
            if match + rating > tchallenge_score:
                print('Fail')
            else:
                encounter.append(monster)
                match += rating
    elif difficulty == 'hard':
        while match <= tchallenge_score:
            monster = random.choice(monsters)
            rating = monster.challenge_rating
            if  match + rating >= tchallenge_score + 7:
                print('Fail')
            else:
                print(monster)
                encounter.append(monster)
                match += rating


    print(encounter)
    print(monsters)
    return render_template('fight_complete.html', encounter=encounter, match=match, difficulty=difficulty) 
               