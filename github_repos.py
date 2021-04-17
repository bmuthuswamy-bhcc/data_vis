import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Below, we define headers for our API call that explicitly ask to use github's V3 API
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: { r.status_code}")
response_dict = r.json()

print(f"Total repositories: { response_dict['total_count']}")

# Explore information about the repos
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repo
repo_dict = repo_dicts[0]
print(f"\nKeys : {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
	print(key)