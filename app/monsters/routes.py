from flask import Blueprint, Request, render_template, request, url_for, request_started, request_finished, redirect, flash
from flask_login import current_user, login_required
from app.monsters.forms import ApiMonster, CustomMonster
from app.models import Monsters, User
import requests

monster = Blueprint('monster', __name__, template_folder='monster_templates')

@monster.route('/monster/entry', methods=['GET', 'POST'])
@login_required
def monst_entry():
    form = ApiMonster()
    if request.method == 'POST':
        if form.validate():

            entry = form.entry.data

            url = f'https://www.dnd5eapi.co/api/monsters/{entry}'
            response = requests.get(url)
            if response.ok == True:
                name = response.json()['name']
                challenge_rating = response.json()['challenge_rating']
                hit_points = response.json()['hit_points']
                armor_class = response.json()['armor_class']


                monster = Monsters(name, challenge_rating, hit_points, armor_class)

                monster.save_to_db()

                return redirect(url_for('monster.monview'))
        else: 
            flash('I am sorry this creature cannot be found')

    return render_template('monst_search.html', form=form)


@monster.route('/monster/view')
def monview():
    rolodex = Monsters.query.order_by(Monsters.name).all()
    print(rolodex)
    return render_template('monsters.html', rolodex=rolodex)