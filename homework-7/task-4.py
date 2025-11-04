import requests

def main():
    url = "https://jsonplaceholder.typicode.com/posts"

    new_post = {
        "title": "Мой новый пост",
        "body": "Это содержимое нового поста, созданного через POST-запрос.",
        "userId": 1
    }

    try:
        response = requests.post(url, json=new_post, timeout=10)
        
        if response.status_code == 201:
            created_post = response.json()
            print("ID созданного поста:", created_post["id"])
            print("Содержимое поста:")
            print("Заголовок:", created_post["title"])
            print("Текст:", created_post["body"])
            
        elif response.status_code == 400:
            print("Ошибка 400: Неверный формат данных.")
            
        elif response.status_code == 404:
            print("Ошибка 404: Запрашиваемый эндпоинт не найден.")
            
        elif response.status_code == 500:
            print("Ошибка 500: Внутренняя ошибка сервера.")
            
        else:
            print(f"Неожиданный код состояния: {response.status_code}")
            print(f"Ответ сервера: {response.text}")

    except requests.exceptions.Timeout:
        print("Превышено время ожидания ответа от сервера.")
        
    except requests.exceptions.ConnectionError:
        print("Не удалось подключиться к серверу.")
        
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

if __name__ == "__main__":
    main()