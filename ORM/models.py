from __init__ import db
from datetime import datetime


print('enter models.py')
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Participant
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class User(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key = True)
    games = db.relationship('Game', secondary = 'players_games', back_populates = 'players')
    participants = db.relationship('Participant')

    name = db.Column(db.Text)
    region = db.Column(db.Text)
    subregion = db.Column(db.Integer)

    def __repr__(self):
        return '<User (name = ' + self.name + ') >'

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Participant
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Participant(db.Model):
    __tablename__ = 'participants'

    id = db.Column(db.Integer, primary_key = True)

    game = db.relationship('Game')
    user = db.relationship('User')

    name = db.Column(db.Text)
    league = db.Column(db.Text)
    scaled_rating = db.Column(db.Integer)
    playrace = db.Column(db.Text)
    avg_apm = db.Column(db.Float)
    winner = db.Column(db.Boolean)

    events_PSE = db.relationship('PlayerStatsEvent', back_populates = 'game')
    events_UBE = db.relationship('UnitBornEvent', back_populates = 'game')
    events_UTCE = db.relationship('UnitTypeChangeEvent', back_populates = 'game')
    events_UCE = db.relationship('UpgradeCompleteEvent', back_populates = 'game')
    events_UIE = db.relationship('UnitInitEvent', back_populates = 'game')
    events_UDE = db.relationship('UnitDoneEvent', back_populates = 'game')
    events_BCE = db.relationship('BasicCommandEvent', back_populates = 'game')
    events_TPE = db.relationship('TargetPointEvent', back_populates = 'game')
    events_UDiE = db.relationship('UnitDiedEvent', back_populates = 'game')
    events_UDiE_player = db.relationship('UnitDiedEvent', secondary = 'players_ude', back_populates = 'player')
    events_UDiE_killing_player = db.relationship('UnitDiedEvent', secondary = 'players_ude', back_populates = 'killing_player')

    def __repr__(self):
        return '<Participant (name = ' + self.name + ') >'

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Game
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key = True)
    players = db.relationship('Player',  secondary = 'players_games', back_populates = 'games')

    name = db.Column(db.Text)
    map = db.Column(db.Text)
    game_winner = db.Column(db.Text)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    category = db.Column(db.Text)
    expansion = db.Column(db.Text)
    time_zone = db.Column(db.Float)

    def __repr__(self):
        return '<Game (map = ' + self.map + ', matchup = ' + self.playerOne_playrace + ' v. ' + self.playerTwo_playrace + ') >'

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Events
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

class PlayerStatsEvent(db.Model):
    __tablename__ = 'playerstatsevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_PSE')
    #game = db.relationship('Game', back_populates = 'events_PSE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    minerals_current = db.Column(db.Float)
    vespene_current = db.Column(db.Float)
    minerals_collection_rate = db.Column(db.Float)
    vespene_collection_rate = db.Column(db.Float)
    workers_active_count = db.Column(db.Float)
    minerals_used_in_progress_army = db.Column(db.Float)
    minerals_used_in_progress_economy = db.Column(db.Float)
    minerals_used_in_progress_technology = db.Column(db.Float)
    minerals_used_in_progress = db.Column(db.Float)
    vespene_used_in_progress_army = db.Column(db.Float)
    vespene_used_in_progress_economy = db.Column(db.Float)
    vespene_used_in_progress_technology = db.Column(db.Float)
    vespene_used_in_progress = db.Column(db.Float)
    resources_used_in_progress = db.Column(db.Float)
    minerals_used_current_army = db.Column(db.Float)
    minerals_used_current_economy = db.Column(db.Float)
    minerals_used_current_technology = db.Column(db.Float)
    minerals_used_current = db.Column(db.Float)
    vespene_used_current_army = db.Column(db.Float)
    vespene_used_current_economy = db.Column(db.Float)
    vespene_used_current_technology = db.Column(db.Float)
    vespene_used_current = db.Column(db.Float)
    resources_used_current = db.Column(db.Float)
    minerals_lost_army = db.Column(db.Float)
    minerals_lost_economy = db.Column(db.Float)
    minerals_lost_technology = db.Column(db.Float)
    minerals_lost = db.Column(db.Float)
    vespene_lost_army = db.Column(db.Float)
    vespene_lost_economy = db.Column(db.Float)
    vespene_lost_technology = db.Column(db.Float)
    vespene_lost = db.Column(db.Float)
    resources_lost = db.Column(db.Float)
    minerals_killed_army = db.Column(db.Float)
    minerals_killed_economy = db.Column(db.Float)
    minerals_killed_technology = db.Column(db.Float)
    minerals_killed = db.Column(db.Float)
    vespene_killed_army = db.Column(db.Float)
    vespene_killed_economy = db.Column(db.Float)
    vespene_killed_technology = db.Column(db.Float)
    vespene_killed = db.Column(db.Float)
    resources_killed = db.Column(db.Float)
    food_used = db.Column(db.Float)
    food_made = db.Column(db.Float)
    minerals_used_active_forces = db.Column(db.Float)
    vespene_used_active_forces = db.Column(db.Float)
    ff_minerals_lost_army = db.Column(db.Float)
    ff_minerals_lost_economy = db.Column(db.Float)
    ff_minerals_lost_technology = db.Column(db.Float)
    ff_vespene_lost_army = db.Column(db.Float)
    ff_vespene_lost_economy = db.Column(db.Float)
    ff_vespene_lost_technology = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

class UnitBornEvent(db.Model):
    __tablename__ = 'unitbornevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_UBE')
    #game = db.relationship('Game', back_populates = 'events_UBE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit_type_name = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

#Take a closer look at this
class UnitDiedEvent(db.Model):
    __tablename__ = 'unitdiedevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    player = db.relationship('Participant', secondary = 'players_ude', back_populates = 'events_UDiE_player')
    killing_player = db.relationship('Participant', secondary = 'players_ude', back_populates = 'events_UDiE_killing_player')
    #game = db.relationship('Game', back_populates = 'events_UDiE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    killing_unit = db.Column(db.Text)
    unit = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player[0].name + ', killing_player = ' + self.killing_player[0].name + ') >'

class UnitTypeChangeEvent(db.Model):
    __tablename__ = 'unittypechangeevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_UTCE')
    #game = db.relationship('Game', back_populates = 'events_UTCE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit = db.Column(db.Text)
    unit_type_name = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

class UpgradeCompleteEvent(db.Model):
    __tablename__ = 'upgradecompleteevents'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_UCE')
    #game = db.relationship('Game', back_populates = 'events_UCE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    upgrade_type_name = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

class UnitInitEvent(db.Model):
    __tablename__ = 'unitinitevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participants', back_populates = 'events_UIE')
    #game = db.relationship('Game', back_populates = 'events_UIE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit_type_name = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

class UnitDoneEvent(db.Model):
    __tablename__ = 'unitdoneevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_UDE')
    #game = db.relationship('Game', back_populates = 'events_UDE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    unit = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

class BasicCommandEvent(db.Model):
    __tablename__ = 'basiccommandevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_BCE')
    #game = db.relationship('Game', back_populates = 'events_BCE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    ability_name = db.Column(db.Text)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

class TargetPointEvent(db.Model):
    __tablename__ = 'targetpointevent'

    id = db.Column(db.Integer, primary_key = True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participants.id'))
    #game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    participant = db.relationship('Participant', back_populates = 'events_TPE')
    #game = db.relationship('Game', back_populates = 'events_TPE')

    name = db.Column(db.Text)
    second = db.Column(db.Float)
    ability_name = db.Column(db.Text)
    loc_x = db.Column(db.Float)
    loc_y = db.Column(db.Float)

    def __repr__(self):
        return '<' + self.name + ' (player = ' + self.player.name + ') >'

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||Join
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

##Do we need these??

class Player_Games(db.Model):
    __tablename__ = 'players_games'

    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

class Player_UDiE(db.Model):
    __tablename__ = 'players_ude'

    id = db.Column(db.Integer, primary_key = True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    unitdiedevents_id = db.Column(db.Integer, db.ForeignKey('unitdiedevents.id'))

#db.create_all()

print('exit models.py')
