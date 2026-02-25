class Character():
    def __init__(self):
        self.inventory = []
        self.base_health = 10
        self.base_damage = 1
        self.equipment = {'Weapon': None, 'Armor': None}
        self.alive = 1
    def deal_damage(self):
        if self.equipment == None: return self.base_damage
        return self.base_damage + self.equipment['Weapon']
    def get_damage(self, damage):
        if self.equipment['Armor'] != None and self.equipment['Armor'] >= 0:
            self.equipment['Armor'] -= damage
        else:
            self.equipment['Armor'] = None
            self.base_health -= damage
        if self.base_health <= 0: self.death('Ran out of hp')
    def get_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)
    def death(self, quote):
        print(quote)
        return self.alive