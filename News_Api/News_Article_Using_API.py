import requests
import json

key = '39a47b048e284247930d15c61de3a2b2'

#####################################         STEP 1         #########################################################

url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-17&sortBy=publishedAt&apiKey='+key
# print(url)

#sending a get requests to the url
response = requests.get(url)                
# print(response, response.text, type(response.text))


#To convert string type into dictionary type using json function (json.loads)
j_response = json.loads(response.text)
# print(j_response, type(j_response))

z = []
for i in range(len(j_response['articles'])):    
    z.append(j_response['articles'][i]['description'])


#####################################         STEP 2         #########################################################

source = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey='+key
# print(source)

# sending a get requests to the url
res = requests.get(source)                
# print(res, res.text, type(res.text))


# #To convert string type into dictionary type using json function (json.loads)
j_res = json.loads(res.text)
# print(j_res, type(j_res))

x = list()
for i in range(len(j_res['articles'])):
    x.append(j_res['articles'][i]['description'])

#####################################         STEP 3         #########################################################

n = input('Option:')
if n == '1':
    print(z)
if n == '2':
    print(x)