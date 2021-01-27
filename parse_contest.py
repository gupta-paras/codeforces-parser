import os
import shutil
import requests
from bs4 import BeautifulSoup
import threading
import sys
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# step-1 get contest details

contest_id = str(sys.argv[1])
base_url = 'https://codeforces.com'

def requests_get(endpoint):
    return requests.get(base_url + endpoint)

logger.info("Getting Contest Problem links...")

contest_page = requests_get("/contest/{}".format(contest_id))

soup = BeautifulSoup(contest_page.content, 'html.parser')
datatable_ = soup.find_all('div', class_='datatable')
datatable = BeautifulSoup(str(datatable_), 'html.parser')
problem_endpoints = {e['href'] for e in datatable.find_all('a') if 'problem' in e['href']}

logger.info("Getting Contest links completed!")

# step-2 get parsed problems

logger.info("parsing problems...")

parsed_problems = {}

def parse_problem_page(endpoint):
    resp = requests_get(endpoint)
    c_soup = BeautifulSoup(resp.content, 'html.parser')
    all_inputs = c_soup.find_all('div', class_ = 'input')
    all_inputs_text = [e.find_all('pre')[0].get_text() for e in all_inputs]

    c_soup = BeautifulSoup(resp.content, 'html.parser')
    all_outputs = c_soup.find_all('div', class_ = 'output')
    all_outputs_text = [e.find_all('pre')[0].get_text() for e in all_outputs]
    
    parsed_problems[endpoint[-1]] = {
        "inputs": all_inputs_text, 
        "outputs": all_outputs_text
    }

threads = [threading.Thread(target=parse_problem_page, args = (e,)) for e in problem_endpoints]
for t in threads:
    t.start()
for t in threads:
    t.join()

logger.info("parsing problems completed!")

# step-3 write files

ref_cpp_file = "ref/ref.cpp"
with open(ref_cpp_file) as f:
    ref_cpp = f.read()


logger.info("creating directory structure...")

pretest_folder = '{}/pretests'.format(contest_id)
code_folder = '{}'.format(contest_id)

shutil.rmtree(pretest_folder, ignore_errors=True)
os.makedirs(pretest_folder, exist_ok=True)

for key in parsed_problems:
    os.makedirs(os.path.join(pretest_folder, key), exist_ok=True)
    inputs = parsed_problems[key]['inputs']
    outputs = parsed_problems[key]['outputs']
    for idx, data in enumerate(inputs):
        file_path = os.path.join(pretest_folder, key, 'input_{}.txt'.format(idx))
        with open(file_path, 'w') as f:
            f.write(data.strip())
            
    for idx, data in enumerate(outputs):
        file_path = os.path.join(pretest_folder, key, 'output_{}.txt'.format(idx))
        with open(file_path, 'w') as f:
            f.write(data.strip())
    
    file_path = os.path.join(code_folder, '{}.cpp'.format(key))
    with open(file_path, 'w') as f:
        f.write(ref_cpp)

logger.info("creating directory Completed!")