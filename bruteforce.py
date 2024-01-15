import itertools
import string
import time

def common_guess(word: str) -> str | None:
    with open("bruteforcedata.txt", "r") as words:
        words_list: list[str] = words.read().splitlines()
    
    for i, match in enumerate(words_list, start=1):
        if match == word:
            return f'common match: {match} (#{i})'

def brute_force(word: str, length: int, digits: bool = False, symbols: bool = False) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0 
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess_str: str = "".join(guess)

        if guess_str == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'
        
        print(guess_str, attempts)

def main():
    print("searching>>>>>>")
    password: str = "carrot"

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=4, digits=True, symbols=True):
            print(cracked)
        else:
            print("There was no match....")
        
    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), "s")

if __name__ == '__main__':
    main()
