print("Name:Lata.S.B","USN:1AY24AI060","Section:'O'")
def collatz(n):
    while n != 1:
        print(n, end=' → ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)  # Final number in the sequence

def main():
    try:
        num = int(input("Enter a positive integer: "))
        if num <= 0:
            print("Please enter a number greater than 0.")
        else:
            print("Collatz sequence:")
            collatz(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

main()
