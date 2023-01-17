from bs4 import BeautifulSoup
import requests
import os


def available_seats(course, sec):
    html_txt = requests.get('https://usis.bracu.ac.bd/academia/admissionRequirement/getAvailableSeatStatus').text
    soup = BeautifulSoup(html_txt, 'html.parser')
    #print(soup.find('h1').text.split('(')[-1].split(')')[0])
    job = soup.find_all('tr')
    for i in job:
        s = i.find_all('td')[1:]
        if str(s[0].text) == course.upper():
            if int(s[4].text) == sec:
                return [s[-1].text, soup.find('h1').text.split('(')[-1].split(')')[0]]
    return "Not Found"

def examScheduleCse(course):
    pwd = os.path.dirname(__file__)
    with open(pwd+'/advising_PlusPlus_bracU/main/CentralExamDates.html', 'r') as f:
        html_txt = f.read()
    soup = BeautifulSoup(html_txt, 'lxml')
    job = soup.find_all('tr')[3:]
    for i in job:
        s = i.find_all('td')
        if str(s[0].text) == course.upper():
            return s[1].text + ' ' + s[2].text + ' ' + s[3].text
    return "Invalid course code"



def course_time_table(course, sec):
    with open('/advising_PlusPlus_bracU/main/Tabular.html', 'r') as f:
        html_txt = f.read()
    soup = BeautifulSoup(html_txt, 'lxml')
    job = soup.find_all('tr')[4:]
    for i in job:
        s = i.find_all('td')
        a, b = s[0].text.split('-')

        if a == course.upper() and int(b) == sec:
            return f"Theory: {s[4].text} {s[5].text} {s[6].text} Lab: {s[7].text} {s[8].text} {s[9].text}"
    return "Invalid course code"

def main(Course, Section):
    print("Available seats: ", available_seats(Course, Section))
    print("Exam Schedule: ", examScheduleCse(Course))
    print("Time Table: ", course_time_table(Course, Section))




        





