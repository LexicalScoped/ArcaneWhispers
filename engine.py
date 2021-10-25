from database_models import Player, Mob, Session

def Check_For_Player(pid):
    try:
        session = Session()
        if session.query(Player).filter(Player.player_id==pid).first():
            session.close()
            return True
        else:
            session.close()
            return False
    except:
        print(f'Something went wrong with the character check')

def Create_Player(pid, pname):
    try:
        session = Session()
        player = Player(pid, pname)
        session.add(player)
        session.commit()
        session.close()
        return f'Registered new character for {pname}'
    except:
        print(f'Something went horribly wrong with character registration!')
        return f'Unable to Register character for {pname} - unknown err'