import requests
from bs4 import BeautifulSoup
import os

Raw_data_dir = "../data/raw"

def scrape(url,filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    text = soup.get_text(separator="\n", strip=True)

    os.makedirs(Raw_data_dir, exist_ok=True)
    filepath = os.path.join(Raw_data_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f'[+] Saved{filename} with {len(text)} characters.')

if __name__ == "__main__":
    scrape("https://www.gram.edu/academics/calendar/", "academic_calender.txt")
    scrape("https://www.gram.edu/student-life/residential-life/", "residency.txt")
    scrape("https://www.gram.edu/offices/registrar/facts/","registrar.txt")
    scrape("https://www.gram.edu/offices/registrar/procedures/", "reg_procedure.txt")
