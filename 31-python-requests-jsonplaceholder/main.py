from api_client import APIClient

client = APIClient()

print("1 - Get All Posts")
print("2 - Get Post by ID")
print("3 - Create Post")
print("4 - Update Post (PUT)")
print("5 - Patch Post (PATCH)")
print("6 - Delete Post")

choice = input("Select: ")

if choice == "1":
    print(client.get_posts())

elif choice == "2":
    post_id = input("Post ID: ")
    print(client.get_post(post_id))

elif choice == "3":
    data = {
        "title": input("Title: "),
        "body": input("Body: "),
        "userId": 1
    }
    print(client.create_post(data))

elif choice == "4":
    post_id = input("Post ID: ")
    data = {
        "title": input("New Title: "),
        "body": input("New Body: "),
        "userId": 1
    }
    print(client.update_post(post_id, data))

elif choice == "5":
    post_id = input("Post ID: ")
    data = {
        "title": input("Updated Title: ")
    }
    print(client.patch_post(post_id, data))

elif choice == "6":
    post_id = input("Post ID: ")
    print("Status Code:", client.delete_post(post_id))