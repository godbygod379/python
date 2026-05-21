#!/usr/bin/env python3
import random

def color_of(n):
	if n == 0:
		return 'zelená'
	# Standard European roulette coloring for 1-36
	red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
	return 'červená' if n in red else 'čierna'

def spin():
	return random.randint(0,36)

def ask_money():
	while True:
		try:
			amt = float(input('Koľko peňazí máš? '))
			if amt > 0:
				return amt
		except:
			pass
		print('Zadaj kladné číslo.')

def ask_bet(balance):
	print(f'Máš: {balance:.2f} €')
	print('Typy stávok: cislo, farba, parne, desiatka, vsetko(koniec)')
	t = input('Zadaj typ stávky: ').strip().lower()
	if t == 'koniec' or t == 'vsetko':
		return None
	if t == 'cislo':
		n = input('Na ktoré číslo (0-36)? ')
		try:
			n = int(n)
			if not (0 <= n <=36): raise ValueError
		except:
			print('Neplatné číslo.')
			return ask_bet(balance)
		amt = ask_amount(balance)
		return ('cislo', n, amt)
	if t == 'farba':
		c = input('farba (cervena/cerna): ').strip().lower()
		if c.startswith('cerv'):
			c = 'červená'
		elif c.startswith('cer'):
			c = 'čierna'
		else:
			print('Neplatná farba.')
			return ask_bet(balance)
		amt = ask_amount(balance)
		return ('farba', c, amt)
	if t == 'parne':
		p = input('parne alebo neparne? (parne/neparne): ').strip().lower()
		if p not in ('parne','neparne'):
			print('Neplatné.')
			return ask_bet(balance)
		amt = ask_amount(balance)
		return ('parne', p, amt)
	if t == 'desiatka':
		d = input('Ktorá desiatka? (1:1-12, 2:13-24, 3:25-36): ').strip()
		if d not in ('1','2','3'):
			print('Neplatné.')
			return ask_bet(balance)
		amt = ask_amount(balance)
		return ('desiatka', int(d), amt)
	print('Neznámy typ.')
	return ask_bet(balance)

def ask_amount(balance):
	while True:
		try:
			a = float(input('Suma stávky: '))
			if 0 < a <= balance:
				return a
		except:
			pass
		print('Neplatná suma.')

def resolve(bet, result):
	num = result
	col = color_of(num)
	typ = bet[0]
	amt = bet[2]
	if typ == 'cislo':
		if num == bet[1]:
			return amt * 35
		return -amt
	if typ == 'farba':
		if num != 0 and col == bet[1]:
			return amt
		return -amt
	if typ == 'parne':
		if num == 0:
			return -amt
		if (num %2 ==0 and bet[1]=='parne') or (num%2==1 and bet[1]=='neparne'):
			return amt
		return -amt
	if typ == 'desiatka':
		d = bet[1]
		ranges = {1: range(1,13), 2: range(13,25), 3: range(25,37)}
		if num in ranges[d]:
			return amt * 2
		return -amt
	return -amt

def main():
	bal = ask_money()
	while bal > 0:
		bet = ask_bet(bal)
		if bet is None:
			print(f'Odchádzaš s {bal:.2f} €')
			break
		bal -= bet[2]
		res = spin()
		col = color_of(res)
		print(f'Padlo: {res} ({col})')
		change = resolve(bet, res)
		if change > 0:
			print(f'Vyhral si {change:.2f} €')
		else:
			print(f'Prehral si {abs(change):.2f} €')
		bal += max(0, change) + (0 if change>0 and bet[0]=='cislo' else 0)
		# Note: for number win we already returned 35*amt, but we subtracted stake earlier so add full change
		# For even-money wins change==amt which is net profit; we added stake back by not doing anything special.
		# Simpler: recompute balance precisely:
		# Implement precise balance update instead:
		# Recompute
		# Undo previous and do accurate update:
		# For clarity, recalc:
		bal = bal  # already adjusted
		# To avoid complicated logic above, recompute from scratch:
		# But keep it simple: after subtracting stake, just add stake if win plus payout
		# We'll implement direct: (we subtracted stake) so add payout outcome if positive
		if change > 0:
			bal += change
		print(f'Aktuálny zostatok: {bal:.2f} €')
		if bal <= 0:
			print('Skončil si bez peňazí.')
			break
	print('Ďakujeme za hranie.')

if __name__ == '__main__':
	main()
