class Scene():
    def enter(self):
        print('Didn\'t get any scene')
class Engine():
    def __init__(self, scene_map):
        self.map = scene_map
    def play(self):
        self.map.opening_scene()
        while True:
            cur_prompt = 'Choose if u want to kill him or not:'
            action = input(cur_prompt)
            if action == '1': 
                print('You\'ve slained the enemy. Now you can enter LaserWeaponArmory to get the bomb.')
                self.map.next_scene()
            else:
                Death().enter('Waited too long. Got shot by the alien.')
                break
            self.map.opening_scene()
            cur_prompt = 'Will you take the bomb?'
            action = input(cur_prompt)
            if action == '1': 
                print('You\'ve got the bomb. Now you can mine the spaceship.')
                self.map.next_scene()
            else:
                Death().enter('Waited too long. Bomb ran away')
                break
            self.map.opening_scene()
            cur_prompt = 'Will you place the bomb?'
            action = input(cur_prompt)
            if action == '1': 
                print('You\'ve got this ship on timer. Time to escape')
                self.map.next_scene()
            else:
                Death().enter('Waited too long. Bomb blew up')
                break
            self.map.opening_scene()
            cur_prompt = 'Will you escape?'
            action = input(cur_prompt)
            if action == '1': 
                print('You\'ve done great on this mission. Let\'s hope you will not land on planet similar to Earth')
                break
            else:
                Death().enter('The captain goes with his ship.')
                break
class Death(Scene):
    def enter(self, reason):
        print(f'You\'ve died because: {reason}')
class CentralCorridor(Scene):
    def enter(self):
        print('You\'re standing in the central corridor \nThere is an enemy in front of you')
class LaserWeaponArmory(Scene):
    def enter(self):
        print('You\'re now inside Armory. You can see a huge bomb.')
class TheBridge(Scene):
    def enter(self):
        print('you\'ve entered the Bridge')
class EscapePod(Scene):
    def enter(self):
        print('You are now in the room with one functioning escape pod.')
class Map():
    def __init__(self, start_scene):
        self.start = start_scene
    def next_scene(self):
        if isinstance(self.start, CentralCorridor):
            self.start = LaserWeaponArmory()
        elif isinstance(self.start, LaserWeaponArmory):
            self.start = TheBridge()
        elif isinstance(self.start, TheBridge):
            self.start = EscapePod()
    def opening_scene(self):
        if self.start == 'central_corridor':
            self.start = CentralCorridor()
            self.start.enter()
        else:
            self.start.enter()
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()