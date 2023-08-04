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

        vacancy_items = soup.find_all('div', {'class': 'vacancy-serp-item'})
        print("Number of vacancy items found:", len(vacancy_items))

        for vacancy_item in vacancy_items:
            vacancy_title = vacancy_item.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).text
            vacancy_link = vacancy_item.find('a', {'data-qa': 'vacancy-serp__vacancy-title'}).get('href')
            company_name = vacancy_item.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).text
            city = vacancy_item.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
            salary_element = vacancy_item.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
            salary = salary_element.text.strip() if salary_element else ""

            if 'Python' in vacancy_title and ('Django' in vacancy_title or 'Flask' in vacancy_title):
                vacancies.append({
                    'title': vacancy_title,
                    'link': vacancy_link,
                    'company': company_name,
                    'city': city,
                    'salary': salary
                })

        return vacancies
    else:
        print("Failed to get data from the page.")
        return []

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
