
class CardGame:

	def check_for_ace(self, card):
		return True if card.value == 1 else False
   
	def highest_card(self, card1, card2):
		if card1.value > card2.value:
			return card1
		else:
			return card2

	def cards_total(self, cards):
		total = 0
		for card in cards:
			total += card.value
		return f"You have a total of {total}"