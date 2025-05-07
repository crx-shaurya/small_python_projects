import time
import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

easy = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yam", "zucchini", "apricot", "blackberry", "coconut", "dragonfruit", "eggplant", "fig",
    "guava", "huckleberry", "jackfruit", "kumquat", "lime", "mulberry", "nectar", "olive", "peach", "quinoa",
    "radish", "spinach", "tomato", "ugli", "violet", "walnut", "xanthan", "yam", "zebra", "zest"
]

normal = [
    "adventure", "balance", "capture", "dazzling", "eclipse", "fantasy", "genuine", "harmony", "imagine", "journey",
    "kingdom", "laughter", "mystery", "nature", "oceanic", "pinnacle", "quasar", "radiance", "serenity", "tranquil",
    "universe", "vibrant", "wanderer", "xylophone", "yearning", "zealous", "ambition", "bravery", "clarity", "destiny",
    "elegance", "freedom", "gratitude", "horizon", "inspire", "jovial", "kindness", "legacy", "momentum", "nurture",
    "optimism", "passion", "questing", "resilient", "symphony", "tenacity", "uplifting", "victory", "wholesome", "zenith"
]

hard = [
    "aberration", "belligerent", "cognizant", "deleterious", "ebullient", "facetious", "gregarious", "haphazard", "idiosyncratic", "juxtaposition",
    "kaleidoscope", "languorous", "magnanimous", "nefarious", "obfuscate", "paradigm", "quintessential", "recalcitrant", "sagacious", "tantamount",
    "ubiquitous", "vexatious", "whimsical", "xenophobia", "yesteryear", "zephyr", "ameliorate", "bombastic", "capricious", "diaphanous",
    "effervescent", "flabbergasted", "grandiloquent", "harbinger", "intransigent", "juxtapose", "kudos", "lugubrious", "mellifluous", "nonchalant",
    "ostentatious", "perspicacious", "quixotic", "reverberate", "serendipity", "transcendent", "unfathomable", "voracious", "wistful", "zealous"
]

mode = input(Fore.GREEN + "choose the mode, easy/normal/hard: ")
number_of_words = int(input(Fore.BLUE + "enter the number of words you want to practice: "))

if mode == "easy":
    random_words = random.sample(easy, number_of_words)
elif mode == "normal":
    random_words = random.sample(normal, number_of_words)
elif mode == "hard":
    random_words = random.sample(hard, number_of_words)
else:
    print(Fore.RED + "invalid input, please try again.")

b = input("press enter to start or exit to end this: ")

if b == "":
    try:
        start_time = time.time()
        right = 0
        wrong = 0
        for word in random_words:
            print(Fore.CYAN + word)
            a = input(Fore.LIGHTMAGENTA_EX + "type here: ")
            if a == word:
                print(Fore.GREEN + "great \n")
                right += 1
            else:
                print(Fore.RED + "wrong \n")
                wrong += 1
        
    finally:
        end_time = time.time()
        time_taken = (end_time - start_time)
        if time_taken > 60:
            time_ = f"{time_taken//60} min"
        else:
            time_ = f"{time_taken} sec"
        print(Fore.YELLOW + "right =", right)
        print(Fore.YELLOW + "wrong =", wrong)
        print(Fore.YELLOW + "time taken =", time_)
        wpm = int(right)/(time_taken/60)
        print(Fore.YELLOW + "wpm = ", wpm)
elif b == "exit":
    print("exitted")
    exit()
else:
    print("invalid input")
