import requests
import json

key = 'cyx1OR9P66yzvFUVcrbcCGE72wItuyKi'

#############################  For number of pages  ########################################
# url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Indigo&page=1&sort=oldest&api-key='+key
# print(url)

#############################  Year and Month  ########################################
url = 'https://api.nytimes.com/svc/archive/v1/2020/6.json?q=Indigo&api-key='+key
# print(url)


#############################  sending a get requests to the url  ####################################
response = requests.get(url)                
# print(response, response.text, type(response.text))


################   To convert string type into dictionary type using json function (json.loads)  ##############################
j_response = json.loads(response.text)
# print(j_response, type(j_response))
# print(j_response['response']['docs'][1]['web_url'])


z = []
for i in range(1, len(j_response['response']['docs'])):    
    z.append(j_response['response']['docs'][i]['web_url'])


a = len(j_response['response']['docs'])
# print(a)


for b, x in zip(range(1, a+1), z):
    print('URL '+str(b)+' = '+x, end='\n')