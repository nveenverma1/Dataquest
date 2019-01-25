## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)
#print(response.json())
json_response = response.json()
python_top_articles = json_response["data"]["children"]

most_upvoted = ""
most_upvotes = 0

for article in python_top_articles:
    data = article["data"]
    #print(type(data['ups']))
    if data['ups'] >= most_upvotes:
        most_upvoted = data["id"]
        most_upvotes = data['ups']
  

#most_upvoted = python_top_articles[0]["data"]["id"]


## 4. Getting Post Comments ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = {"t":"day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)
#print(response.json())

json_response = response.json()
python_top_articles = json_response["data"]["children"]
most_upvoted = python_top_articles[0]["data"]["id"]

response_comments = requests.get("https://oauth.reddit.com/r/python/comments/{}".format(most_upvoted), headers=headers)
comments = response_comments.json()
print(comments)

## 5. Getting the Most Upvoted Comment ##

#print(comments[1]["data"]["children"])
comments_list = comments[1]["data"]["children"]
#print(comments_list)

most_upvoted_comment = ''
most_upvotes_comment = 0

for row in comments_list:
    data = row["data"]
    if data['ups'] >= most_upvotes_comment:
        most_upvotes_comment = data['ups']
        most_upvoted_comment = data['id']


## 6. Upvoting a Comment ##

payload = {"dir":1, "id":"d16y4ry"}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.post("https://oauth.reddit.com/api/vote", headers=headers, json=payload)
status = response.status_code