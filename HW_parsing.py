import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

def parse_vacancies(url, params):
    ua = UserAgent()
    headers = {"user-agent": ua.random}

    response = requests.get(url, headers=headers, params=params)
    print("Server response status code:", response.status_code)
    print("Server response content:")
    print(response.text)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        vacancies = []

        vacancy_items = soup.find_all('a', {'data-qa': 'serp-item__title'})
        print("Number of vacancy items found:", len(vacancy_items))

        for vacancy_item in vacancy_items:
            vacancy_title = vacancy_item.text
            vacancy_link = vacancy_item.get('href')
            
            company_element = vacancy_item.find_next('a', {'data-qa': 'vacancy-serp__vacancy-employer'})
            company_name = company_element.text if company_element else ""
            
            address_element = vacancy_item.find_next('div', {'data-qa': 'vacancy-serp__vacancy-address'})
            address_text = address_element.text if address_element else ""
            city, metros = extract_city_and_metro(address_text, soup)
            
            salary_element = vacancy_item.find_next('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
            salary = salary_element.text.strip() if salary_element else ""

            if 'Python' in vacancy_title and ('Django' in vacancy_title or 'Flask' in vacancy_title):
                vacancies.append({
                    'title': vacancy_title,
                    'link': vacancy_link,
                    'company': company_name,
                    'city': city,
                    'metros': metros,
                    'salary': salary
                })

        return vacancies
    else:
        print("Failed to get data from the page.")
        return []

def extract_city_and_metro(address_text, soup):
    city = ""
    metros = []

    address_parts = address_text.split(',')
    if len(address_parts) >= 1:
        city = address_parts[0].strip()

    metro_elements = soup.select('span.metro-station')
    for metro_element in metro_elements:
        metro_name = metro_element.text.strip()
        metros.append(metro_name)

    return city, metros

if __name__ == "__main__":
    url = "https://spb.hh.ru/search/vacancy"
    params = {
        "text": "python",
        "area": [1, 2]
    }

    vacancies = parse_vacancies(url, params)

    print("Parsed vacancies:", vacancies)  

    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies, file, indent=2, ensure_ascii=False)

    print("Vacancies have been successfully parsed and saved to vacancies.json.")


    print("Vacancies have been successfully parsed and saved to vacancies.json.")


