print("Name:Lata.S.B",
      "USN:1AY24AI060",
      "Section:'O'")
def main():
    # Number of coin flips
    num_flips = 1000
    
    # Simulate coin flips
    flips = [flip_coin() for _ in range(num_flips)]
    
    # Find the longest streak
    max_streak = count_streaks(flips)
    
    # Display results
    print(f"Coin flipped {num_flips} times.")
    print(f"Longest streak of heads or tails: {max_streak}")

if _name_ == "_main_":
    main()
