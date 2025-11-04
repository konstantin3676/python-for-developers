import requests

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        posts = response.json()

        for i, post in enumerate(posts[:5], start=1):
            print(f"Пост {i}:")
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    fetch_and_print_posts()