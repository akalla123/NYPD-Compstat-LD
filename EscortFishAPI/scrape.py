def scrape(n):
  import requests
  from bs4 import BeautifulSoup
  import re

  def find_by_label(soup, label):
      return soup.find("span", text=re.compile(label)).next_sibling

  link_items = []
  get = 'https://escortfish.ch/manhattan/'
  for i in range(1,n):

    get_this = str(get) + str(i) + '/'
    page = requests.get(str(get_this))
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a', href=True):
      if link['href'].split('/')[-1].isdigit():
        link_items.append(link['href'])
  ad_text = []
  time = []
  date = []
  age = []
  location = []
  phone = []    
       
  phone_d = {}
  age_d = {}
  location_d = {}
  ad_text_d = {}
  time_d = {}
  date_d = {}
  for item in link_items:
    page = requests.get(item)
    soup = BeautifulSoup(page.content,'html.parser')
    for link in soup.find_all('a',class_='tel-num', href=True):
      a = (link['href'])
      a = a.split(':')[-1]
      phone.append(a)
      
    spans = soup.find_all('span', {'class' : 'location-text'})
    for span in spans:
      location.append(span.get_text())
    
    spans = find_by_label(soup, "Age:").strip()
    age.append(spans)
    
    a = (soup.select('.post-details > .description > p'))
    ad = []
    for item in a:
      ad.append(item.get_text())
    ad_text.append(ad)

    for i in soup.findAll('time'):
      if i.has_attr('datetime'):
        time.append((i['datetime']).split(' ')[-1])
        date.append((i['datetime']).split(' ')[-2])
  final_array = []
  for i in range(0,len(phone)):
    keys = ['phone','age','location','ad_text','time','date','ad_url']
    values = [phone[i],age[i],location[i],ad_text[i],time[i],date[i],link_items[i]]
  
    dictionary = dict(zip(keys, values))
    final_array.append(dictionary)
  return final_array[0]


