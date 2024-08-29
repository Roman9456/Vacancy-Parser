# Vacancy Parser

This script parses job vacancies from the hh.ru website based on search parameters and saves the results to a JSON file.

## Usage

1. Import the parse_vacancies function from the script.
2. Provide the search parameters as a dictionary, for example:

params = {
    "text": "python",
    "area": [1, 2]
}

3. Call the parse_vacancies function with the URL and parameters:

vacancies = parse_vacancies(url, params)

4. The parsed vacancies are returned as a list of dictionaries, which can be saved to a JSON file:

with open('vacancies.json', 'w', encoding='utf-8') as file:
    json.dump(vacancies, file, indent=2, ensure_ascii=False)

## Requirements

- Python 3.x
- The following Python libraries:
  - requests
  - BeautifulSoup4
  - fake_useragent
  - json

## License

This project is licensed under the [MIT License](LICENSE).

README.md (Russian)

# Парсер вакансий

Этот скрипт парсит вакансии с сайта hh.ru на основе заданных параметров поиска и сохраняет результаты в файл в формате JSON.

## Использование

1. Импортируйте функцию parse_vacancies из скрипта.
2. Предоставьте параметры поиска в виде словаря, например:

params = {
    "text": "python",
    "area": [1, 2]
}

3. Вызовите функцию parse_vacancies с URL и параметрами:

vacancies = parse_vacancies(url, params)

4. Распарсенные вакансии возвращаются в виде списка словарей, которые можно сохранить в файл JSON:

with open('vacancies.json', 'w', encoding='utf-8') as file:
    json.dump(vacancies, file, indent=2, ensure_ascii=False)

## Требования

- Python 3.x
- Следующие библиотеки Python:
  - requests
  - BeautifulSoup4
  - fake_useragent
  - json

## Лицензия

Этот проект распространяется под [Лицензией MIT](LICENSE).
