from operator import itemgetter
import requests
import plotly.express as px
#Make an API call and check the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

#Process infomation about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids [:20]:
    #Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} status:{r.status_code}")
    response_dict = r.json()
    try:

        #Build a dictionary for each article
        submission_dict = {
            'title':response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments':response_dict['descendants']
        }


    except ValueError:
        continue
    else:

        submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, 
    key=itemgetter('comments'), 
    reverse=True
)

#Process the data for plotting
#we need the title, discussion links, article link, comment count
article_links, comment_counts, hover_texts = [],[],[]
for submission_dict in submission_dicts:
    #shorten long article titles
    title = submission_dict['title'][:30]
    discussion_link = submission_dict['hn_link']
    article_link = f"<a href='{discussion_link}'>{title}</a>"
    comment_count = submission_dict['comments']

    article_links.append(article_link)
    comment_counts.append(comment_count)
    #Show the full title on hover
    hover_texts.append(submission_dict['title'])

#Make the visualization
title = "Most active discussions on Hacker News"
labels = {'x':'Article', 'y':'comments'}
fig = px.bar(x=article_links, y=comment_counts, hover_name=hover_texts)

fig.write_html('comments.html', auto_open=True)

