import requests
from bs4 import BeautifulSoup

BASE_URL = "https://github.com"


def get_profile_info(username):
    url = f"{BASE_URL}/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Profile not found")

    soup = BeautifulSoup(response.text, "html.parser")

    name = soup.find("span", class_="p-name")
    bio = soup.find("div", class_="p-note")
    followers = soup.select_one('a[href$="?tab=followers"] span')
    following = soup.select_one('a[href$="?tab=following"] span')
    repositories = soup.select_one('a[href$="?tab=repositories"] span')

    return {
        "name": name.text.strip() if name else username,
        "bio": bio.text.strip() if bio else "No bio provided",
        "followers": followers.text.strip() if followers else "0",
        "following": following.text.strip() if following else "0",
        "repositories": repositories.text.strip() if repositories else "0",
    }


def get_top_repositories(username, limit=5):
    url = f"{BASE_URL}/{username}?tab=repositories"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    repo_items = soup.find_all("li", class_="public")

    repositories = []

    for repo in repo_items[:limit]:
        name = repo.find("a", itemprop="name codeRepository")
        language = repo.find("span", itemprop="programmingLanguage")
        stars = repo.find("a", href=lambda x: x and "stargazers" in x)

        repositories.append({
            "name": name.text.strip() if name else "Unknown",
            "language": language.text.strip() if language else "Not specified",
            "stars": stars.text.strip() if stars else "0"
        })

    return repositories


def print_profile_report(profile, repositories):
    print("\nGitHub Profile Summary\n")
    print(f"Name            : {profile['name']}")
    print(f"Bio             : {profile['bio']}")
    print(f"Public Repos    : {profile['repositories']}")
    print(f"Followers       : {profile['followers']}")
    print(f"Following       : {profile['following']}")

    print("\nTop Repositories:")
    for repo in repositories:
        print(
            f"- {repo['name']} | "
            f"Language: {repo['language']} | "
            f"Stars: {repo['stars']}"
        )


if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()

    profile_info = get_profile_info(username)
    top_repos = get_top_repositories(username)

    print_profile_report(profile_info, top_repos)
