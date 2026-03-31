def fizzbuzz():
    """Print numbers 1-50 with Fizz/Buzz logic and count occurrences."""
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    
    for num in range(1, 51):
        if num % 15 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        elif num % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif num % 5 == 0:
            print("Buzz")
            buzz_count += 1
        else:
            print(num)
    
    print("\n--- Counts ---")
    print(f"Fizz: {fizz_count}")
    print(f"Buzz: {buzz_count}")
    print(f"FizzBuzz: {fizzbuzz_count}")

if __name__ == "__main__":
    fizzbuzz()