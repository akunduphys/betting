import random
import numpy as np
import matplotlib.pyplot as plt


def kelly_criterion(bankroll, odds_g, odds_l, prob_g):
    kelly_fraction = prob_g/odds_l - (1-prob_g)/odds_g #(odds * probability - 1) / odds
    return kelly_fraction * bankroll

def simulate_betting(bankroll, num_bets):
	win = False
	for _ in range(num_bets):
		# Simulate random odds and probability
		odds = random.uniform(1.0, 2.0)  # Example odds between 1.5 and 10.0
		probability = random.uniform(0.7, 0.9)  # Example probability between 0.1 and 0.9
	
		# Calculate Kelly Criterion bet size
		bet_size = kelly_criterion(bankroll, odds,1, probability)
		
		#anti-martingle
		if(win and bet_size*1.33<bankroll):
			bet_size = bet_size*1.33
		# Simulate the bet outcome (win or loss)
		
		#print("Bet",bet_size)
		#print probability
		
		win = np.random.choice([True, False],p=[probability,1-probability])
		#print(odds)
		#bankroll -= bet_size
		if win:
			bankroll += bet_size*odds
			#print "Win! Bankroll: $%.2f" % bankroll
		else:
			bankroll -= bet_size

			#print "Bankroll: $%.2f" % bankroll

	
	return bankroll

def main():
	
	hist_ret = []
	initial_bankroll = 5000  # Example initial bankroll
	num_bets = 3  # Number of simulated bets
	
	NMC=1000
	
	for i in range(NMC):
		final_bankroll = simulate_betting(initial_bankroll, num_bets)
		hist_ret.append(final_bankroll)
	
	edges,bins = np.histogram(np.asarray(hist_ret),normed=True)
	plt.plot(bins[1:],edges)
	print("average return", np.average(hist_ret))
	plt.show()
	print "\nFinal Bankroll after %d bets: $%.2f" % (num_bets, final_bankroll)

if __name__ == "__main__":
    main()
