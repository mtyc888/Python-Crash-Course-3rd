import requests

def get_repos_info():
    #Make an API call and check the response
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    #We define the headers for the API call that ask explicitly to use the 3rd version
    headers = {"Accept":"application/vnd.github.v3+json"}
    #Make the API call
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    return r

def show_repos_info(response_dict):
    """Show information about the returned repositories."""
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")

def get_response_dict(response):
    #Convert the response object to a dictionary
    response_dict = response.json()
    return response_dict

def get_repo_dicts(response_dict):
    #Explore information about the repositories
    repo_dicts = response_dict['items']
    return repo_dicts


#Examine the first repository
def show_repo_dicts_info(repo_dicts):
    print("\nSelected information about first repository:")
    for repo_dict in repo_dicts:
        print(f"Name: {repo_dict['name']}")
        print(f"Owner: {repo_dict['owner']['login']}")
        print(f"Stars: {repo_dict['stargazers_count']}")
        print(f"Repository {repo_dict['html_url']}")
        print(f"Created: {repo_dict['created_at']}")
        print(f"Updated: {repo_dict['updated_at']}")
        print(f"Description: {repo_dict['description']}")
        print("\n")

response = get_repos_info()
response_dict = get_response_dict(response)
show_repos_info(response_dict)
repo_dicts = get_repo_dicts(response_dict)
show_repo_dicts_info(repo_dicts)