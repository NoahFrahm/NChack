from abc import abstractmethod
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import csv
import itertools


def main() -> None:
    urls: List[str] = set_up()
    data: Dict[str,List[str]] = crawl(urls)
    csv_builder(data)


def csv_builder(data: Dict[str,List[str]]) -> None:
    with open("data111.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data.keys())
        writer.writerows(itertools.zip_longest(*data.values()))


def filtered(urls: List[str]) -> List[str]:
    """Filters the urls list to contain only course urls."""
    while urls[-1] != 'https://catalog.unc.edu/courses/maya/':
        urls.pop(-1)
    urls.pop(-1)
    while urls[-1] != 'https://catalog.unc.edu/courses/maya/':
        urls.pop(-1)

    while urls[0] != 'https://catalog.unc.edu/courses/aero/':
        urls.pop(0)
    return urls


def set_up() -> List[str]:
    URL = 'https://catalog.unc.edu/courses/'
    page = requests.get(URL)

    links_list: List[str] = []

    soup = BeautifulSoup(page.content, 'html.parser')
    # links = soup.select('ul > li > a')
    links = soup.select('div#atozindex > ul > li > a') # 'h.letternav-head > 
    #print(links)
    for link in links:
        url: str = 'https://catalog.unc.edu' + str(link['href'])
        links_list.append(url)

    return links_list


def crawl(links: List[str]) -> Dict[str,List[str]]:
    courses: Dict[str,List[int]] = {}

    for link in links: # in range(0,4):
        data: Dict[str,List[str]] = department_courses(link)
        for key in data:
            courses[key] = data[key]
    return courses


def department_courses(link: str) -> Dict[str, List[int]]:
    courses: List[str] = []
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    department = soup.select('h1.page-title')[0].get_text()
    drop: bool = False

    blocks = soup.select('p.courseblocktitle > strong') #changed here
    
    for course in blocks:
        cname: str = course.get_text()
        p = cname[0:9]
        # try to implement sort here
        try:
            courses.append(int(p[5:8]))
        except:
            try:
                courses.append(int(p[5:7]))
            except:
                try:
                    courses.append(int(p[6:9]))
                except:
                    print(department)
    start: int = len(department) - 5
    stop: int = len(department) - 1
    abreviation: str = department[start:stop]
    department = department[0:(start - 1)].strip()
    if '(' in abreviation:
        abreviation = abreviation[1:4]

    # implement search by abreviation vs department, two dicts
    return {abreviation: courses}


# courses: List[str] = []
# page = requests.get('https://catalog.unc.edu/courses/bcb/')
# soup = BeautifulSoup(page.content, 'html.parser')
# department = soup.select('h1.page-title')[0].get_text()
# drop: bool = False

if __name__ == '__main__':
    main()

main()