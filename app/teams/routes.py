from flask import Blueprint, Request, render_template, request, url_for, request_started, request_finished, redirect, flash
from flask_login import current_user, login_required
from app.teams.forms import TeamRegistry
from app.models import Team, User
import requests

team = Blueprint('team', __name__, template_folder='team_templates')

@team.route('/teamregistry', methods=['GET', 'POST'])
def tregister():
    form = TeamRegistry()
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            tclass = form.tclass.data
            level = form.level.data
            my_id = current_user.id
            challenge_score = 0
            if tclass == 'fighter':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.6)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.55)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.5)
            elif tclass == 'barbarian':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.6)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.7)
            elif tclass == 'warlock':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.5)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.6)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.6)
            elif tclass == 'ranger':
                if level >= 1 and level <= 5:
                    challenge_score = (level * 1.5)
                elif level >= 6 and level <= 10:
                    challenge_score = (level * 1.4)
                elif level >= 11 and level <=15:
                    challenge_score = (level * 1.5)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.45)
            elif tclass == 'paladin':
                if level >= 1 and level <= 5:
                    challenge_score = (level * 1.6)
                elif level >= 6 and level <= 10:
                    challenge_score = (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score = (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.8)
            elif tclass == 'battle dancer':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.3)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.4)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.5)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.5)
            elif tclass == 'wizard':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.3)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 2)
            elif tclass == 'rogue':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.7)
            elif tclass == 'bard':
                if level >= 1 and level <= 5:
                    challenge_score = (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score = (level * 1.8)
                elif level >= 11 and level <=15:
                    challenge_score = (level * 1.8)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.8)
            elif tclass == 'cleric':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.8)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.8)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.9)

            print(name, tclass, level, challenge_score)

            team = Team(name, tclass, level, challenge_score, current_user.id)

            team.save_to_db()
            return redirect(url_for('team.viewteam', my_id = current_user.id))
            
    return render_template('registry.html', form=form)       


@team.route('/team/view/<my_id>')
def viewteam(my_id):
    boxes = Team.query.filter_by(user_id = my_id)
    print(boxes)
    tchallenge_score = 0
    for box in boxes:
        tchallenge_score += box.challenge_score
    tchallenge_score = tchallenge_score / 4
    tchallenge_score = round(tchallenge_score, 2)
    
    

        
    return render_template('teamview.html', boxes=boxes[::-1], tchallenge_score=tchallenge_score)

@team.route('/team/delete/<int:team_id>')
def delete_player(team_id):
    post = Team.query.get( team_id )
    post.delete_from_db()
    my_id = current_user.id
    return redirect(url_for('team.viewteam', my_id = current_user.id))

@team.route('/team/update/<int:team_id>', methods=['GET', 'POST'])
def update_player(team_id):
    form = TeamRegistry()
    team = Team.query.get(team_id)
    
    if request.method == 'POST':
        if form.validate():
            name = form.name.data
            tclass = form.tclass.data
            level = form.level.data
            challenge_score = 0
            if tclass == 'fighter':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.6)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.55)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.5)
            elif tclass == 'barbarian':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.6)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.7)
            elif tclass == 'warlock':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.5)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.6)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.6)
            elif tclass == 'ranger':
                if level >= 1 and level <= 5:
                    challenge_score = (level * 1.5)
                elif level >= 6 and level <= 10:
                    challenge_score = (level * 1.4)
                elif level >= 11 and level <=15:
                    challenge_score = (level * 1.5)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.45)
            elif tclass == 'paladin':
                if level >= 1 and level <= 5:
                    challenge_score = (level * 1.6)
                elif level >= 6 and level <= 10:
                    challenge_score = (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score = (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.8)
            elif tclass == 'battle dancer':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.3)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.4)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.5)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.5)
            elif tclass == 'wizard':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.3)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 2)
            elif tclass == 'rogue':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.7)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.7)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.7)
            elif tclass == 'bard':
                if level >= 1 and level <= 5:
                    challenge_score = (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score = (level * 1.8)
                elif level >= 11 and level <=15:
                    challenge_score = (level * 1.8)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.8)
            elif tclass == 'cleric':
                if level >= 1 and level <= 5:
                    challenge_score += (level * 1.8)
                elif level >= 6 and level <= 10:
                    challenge_score += (level * 1.8)
                elif level >= 11 and level <=15:
                    challenge_score += (level * 1.8)
                elif level >= 16 and level <= 20:
                    challenge_score += (level * 1.9)

            print(name, tclass, level, challenge_score)

            team.name = name
            team.tclass = tclass
            team.level = level
            team.challenge_score = challenge_score

            team.update_db()

            return redirect(url_for('team.viewteam', my_id = current_user.id))
        

    return render_template('update.html', form=form, team=team)
