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

            print(name, tclass, level)

            team = Team(name, tclass, level, current_user.id)

            team.save_to_db()
            return redirect(url_for('team.viewteam', my_id = current_user.id))
            
    return render_template('registry.html', form=form)       


@team.route('/team/view/<my_id>')
def viewteam(my_id):
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

        
    return render_template('teamview.html', boxes=boxes[::-1], tchallenge_score=tchallenge_score)

@team.route('/team/delete/<int:team_id>')
def delete_poke(team_id):
    post = Team.query.get( team_id )
    post.delete_from_db()
    my_id = current_user.id
    return redirect(url_for('team.viewteam', my_id = current_user.id))