import argparse
import json
import requests
from difflib import get_close_matches
import os

def load_countries():
    with open("countries.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_iso_code(input_name, countries):
    input_name = input_name.lower()
    for name, code in countries.items():
        if input_name == name.lower() or input_name == code.lower():
            return code.lower()
    closest_match = get_close_matches(input_name, [name.lower() for name in countries.keys()], n=1)
    if closest_match:
        for name, code in countries.items():
            if closest_match[0] == name.lower():
                return code.lower()
    return None

def fetch_country_data(iso_code):
    api_url = f"https://www.apicountries.com/alpha/{iso_code}"
    response = requests.get(api_url)
    if response.status_code == 200:
        country_data = response.json()
        flag_url = f"https://flagcdn.com/{iso_code}.svg"
        flag_file = f"{iso_code}.svg"

        os.system(f"wget -q {flag_url} -O {flag_file}")

        print("\nCountry Information:")
        print("--------------------")
        os.system(f"terminal_images -w 40 {flag_file}")
        print(f"Name: {country_data['name']}")
        print(f"Capital: {country_data['capital']}")
        print(f"Alt Spellings: {', '.join(country_data['altSpellings'])}")
        print(f"Region: {country_data['region']}")
        print(f"Demonym: {country_data['demonym']}")
        print(f"Native Name: {country_data['nativeName']}")
        print("Languages:")
        for language in country_data["languages"]:
            print(f"  - {language['name']} ({language['nativeName']})")
        print(f"CIOC: {country_data['cioc']}")

        os.remove(flag_file)
    else:
        print(f"Error: Unable to fetch data for ISO code '{iso_code}'. HTTP Status: {response.status_code}")

def display_help():
    help_text = """
Usage: countryfetch [COUNTRY_NAME_OR_ISO]

Options:
  COUNTRY_NAME_OR_ISO   The name or ISO Alpha-2 code of the country you want to fetch data for.

Examples:
  countryfetch IL             Fetch data for Israel using ISO Alpha-2 code.
  countryfetch israel         Fetch data for Israel using the country name (case-insensitive).
  countryfetch romani         Fetch data for Romania (auto-detected from closest match).
"""
    print(help_text)

def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("input", nargs="?", help="The name or ISO Alpha-2 code of the country.")
    args = parser.parse_args()

    if not args.input:
        display_help()
    else:
        countries = load_countries()
        iso_code = get_iso_code(args.input, countries)
        if iso_code:
            fetch_country_data(iso_code)
        else:
            print(f"Error: '{args.input}' is not a valid country or ISO Alpha-2 code.")

if __name__ == "__main__":
    main()
