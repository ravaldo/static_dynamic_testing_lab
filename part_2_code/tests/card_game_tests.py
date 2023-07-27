import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
		
	def setUp(self):
	
		self.game = CardGame()		
		
		self.ace_of_clubs = Card("Clubs", 1)
		self.four_of_hearts = Card("Hearts", 4)
		self.seven_of_diamonds = Card("Diamonds", 7)
		self.king_of_spades = Card("Spades", 13)
		
		self.cards = [
			self.ace_of_clubs,
			self.four_of_hearts,
			self.seven_of_diamonds,
			self.king_of_spades		
		]
		
	def test_check_for_ace_pass(self):
		result = self.game.check_for_ace(self.ace_of_clubs)
		self.assertEqual(result, True)
	
	def test_check_for_ace_fail(self):
		result = self.game.check_for_ace(self.four_of_hearts)
		self.assertEqual(result, False) 
	
	def test_highest_card_pass(self):
		result = self.game.highest_card(self.four_of_hearts, self.seven_of_diamonds)
		self.assertEqual(result, self.seven_of_diamonds) 
	
	def test_highest_card_fail(self):
		result = self.game.highest_card(self.four_of_hearts, self.seven_of_diamonds)
		self.assertNotEqual(result, self.four_of_hearts) 

	def test_cards_total(self):
		result = self.game.cards_total(self.cards)
		self.assertEqual(result, "You have a total of 25")