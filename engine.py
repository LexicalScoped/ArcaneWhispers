from database_models import Player, Mob, Session
import threading
import time

class World():
    players_awake = []
    session = Session()
    def __init__(self):
        self.update_awake_players()

    def update_awake_players(self):
        try: 
            self.players_awake = self.session.query(Player).filter(Player.resting==False).all()
        except:
            print(f'Something went wrong initializing the world')    

    def Check_For_Player(self, pid):
        for player in self.players_awake:
            if player.player_id == pid:
                return True
        try:
            if self.session.query(Player).filter(Player.player_id==pid).first():
                return True
            else:
                return False
        except:
            print(f'Something went wrong with the DB character check')

    def Player_Awake(self, pid):
        # if we have issues with players being awake in DB and not synced in the world values, uncomment the options below for "quick fix"
        # self.update_awake_players()
        for player in self.players_awake:
            if player.player_id == pid:
                return player.resting
        return False

    def Player_Rest(self, pid):
        try:
            player = self.session.query(Player).filter(Player.player_id==pid).first()
            self.players_awake.remove(player)
            player.resting = True
            player.wakeable = False
            self.session.commit()
        except:
            print(f'Something went wrong with the DB query to set resting')
            return f'Something went wrong on attempting to rest for {player.player_name}'
        thread_rest_timer = threading.Thread(target=self.Thread_Rest, args=[pid])
        thread_rest_timer.start()
        # if we have issues with players being awake in DB and not synced in the world values, uncomment the options below for "quick fix"
        # self.update_awake_players()
        return f'{player.player_name} is now resting'

    def Thread_Rest(self, pid):
        time.sleep(30)
        pid = int(pid)
        try:
            player = self.session.query(Player).filter(Player.player_id==pid).first()
            player.wakeable = True
            player.current_health = player.maximum_health
            self.session.commit()
        except:
            print(f'Something went wrong with the timer to clear wakeable false on rest')

    def Player_Wake(self, pid):
        try:
            player = self.session.query(Player).filter(Player.player_id==pid).first()
            if not player.wakeable:
                return f'{player.player_name} is not elligible to awaken.'
            player.resting = False
            player.wakeable = False
            self.players_awake.append(player)
            self.session.commit()
        except:
            print(f'Something went wrong with the DB query to waken player')        
            return f'Something went wrong on attempting to wake for {player.player_name}'
        # if we have issues with players being awake in DB and not synced in the world values, uncomment the options below for "quick fix"
        # self.update_awake_players()
        return f'{player.player_name} has awoken'

    def Create_Player(self, pid, pname):
        try:
            player = Player(pid, pname)
            self.session.add(player)
            self.session.commit()
            return f'Registered new character for {pname}'
        except:
            print(f'Something went horribly wrong with character registration!')
            return f'Unable to Register character for {pname} - unknown err'