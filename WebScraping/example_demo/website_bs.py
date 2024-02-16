from bs4 import BeautifulSoup

with open('./WebScraping/example_demo/website.html', 'r', encoding='utf-8') as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.getText(), "--->", tag.get('href'))

print()

main_list_items = soup.find('ul', id='main-list').find_all('li')
for item in main_list_items:
    print(item.getText())

print()

class_list_items = soup.find('ul', class_='list').find_all('li')
for item in class_list_items:
    print(item.getText())


print()

all_headings = soup.select('.subtitle')
for heading in all_headings:
    print(heading.getText())

print()

form_element = soup.find('form', action='/search/')
input_element = form_element.find('input', type='text')
maxlength_value = input_element.get('maxlength')
print(maxlength_value)
