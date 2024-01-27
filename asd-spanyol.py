import random

spanish_words = {
    'hola': 'hello',
    'gracias': 'thank you',
    'adiós': 'goodbye',
    'por favor': 'please',
    'sí': 'yes',
    'no': 'no',
    '¿Cómo estás?': 'How are you?',
    'buenos días': 'good morning',
    'buenas noches': 'good night',
    'casa': 'house',
    'gato': 'cat',
    # Bővítheted a szótárat további szavakkal és kifejezésekkel
}

def practice_spanish():
    print("Spanyol nyelv gyakorlása!")
    print("Írja be a megfelelő fordítást. Kilépéshez írja be: 'exit'\n")

    words = list(spanish_words.keys())

    while True:
        word = random.choice(words)
        correct_translation = spanish_words[word]

        user_translation = input(f"{word}: ")

        if user_translation.lower() == 'exit':
            break

        if user_translation.lower() == correct_translation.lower():
            print("Helyes!\n")
        else:
            print(f"Nem helyes. A helyes fordítás: '{correct_translation}'\n")

if __name__ == "_main_":
    practice_spanish()

def main():
    practice_spanish()

main()