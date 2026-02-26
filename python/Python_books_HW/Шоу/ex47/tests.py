from ex47 import Room
import unittest

class TestRoom(unittest.TestCase):         
    def test_room(self):                    
        gold = Room('Gold room', 'This room has lots of gold that u can steal')
        self.assertEqual(gold.name, 'Gold room')
        self.assertEqual(gold.paths, {})
    def test_room_paths(self):
        center = Room('Cetner', 'Testing central room')
        north = Room('North', 'Testing north room')
        south = Room('South', 'Testing south room')
        center.add_paths({'north': north, 'south': south})
        self.assertEqual(center.go('north'), north)
        self.assertEqual(center.go('south'), south)
    def test_map(self):
        start = Room('Start', 'U can go west and fall into abyss')
        west = Room('Trees', 'Here u can see trees and u can go east')
        down = Room('Dungeon', 'Its dark here u can go up')
        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})
        self.assertEqual(start.go('west'), west)
        self.assertEqual(start.go('west').go('east'), start)
        self.assertEqual(start.go('down').go('up'), start)
if __name__ == '__main__':
    unittest.main()