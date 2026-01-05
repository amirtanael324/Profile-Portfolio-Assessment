european_countries = {
    "France": "paris",
    "Italy": "rome",
    "Germany": "berlin",
    "Spain": "madrid",
    "Poland": "warsaw",
    "Portugal": "lisbon",
    "Bulgaria": "sofia",
    "Greece": "athens",
    "Netherlands": "amsterdam",
    "Belgium": "brussels"
}
for country, capital in european_countries.items():
    answer = input(f"What is the capital of {country}? ").lower()
    if answer == capital:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {capital}.")
