from operator import itemgetter
import requests

#Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids:
    #Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} status:{r.status_code}")
    response_dict = r.json()

    #Build a dictionary for each article
    submission_dict = {
        'title':response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comment':response_dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, 
    key=itemgetter('comments'), 
    reverse=True
)

for submission_dict in submission_dicts:
    print(f"Title: {submission_dict['title']}")
    print(f"Discussion Links: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")