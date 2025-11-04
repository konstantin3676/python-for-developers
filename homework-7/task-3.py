import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "title": "Мой новый пост",
        "body": "Это содержимое нового поста, созданного через POST-запрос.",
        "userId": 1
    }

    response = requests.post(url, json=new_post)

    if response.status_code == 201:
        created_post = response.json()
        print("ID созданного поста:", created_post["id"])
        print("Содержимое поста:")
        print("Заголовок:", created_post["title"])
        print("Текст:", created_post["body"])
    else:
        print("Ошибка при создании поста:", response.status_code)

if __name__ == "__main__":
    main()