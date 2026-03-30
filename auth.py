import json
import os
import hashlib

USER_FILE = "users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists(USER_FILE):
        return []
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)


def register():
    users = load_users()

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("❌ Empty fields not allowed!")
        return None

    for u in users:
        if u["username"] == username:
            print("❌ User already exists!")
            return None

    users.append({
        "username": username,
        "password": hash_password(password)
    })

    save_users(users)
    print("✅ Registered successfully!")
    return username


def login():
    users = load_users()

    username = input("Username: ").strip()
    password = hash_password(input("Password: ").strip())

    for u in users:
        if u["username"] == username and u["password"] == password:
            print("✅ Login successful!")
            return username

    print("❌ Invalid credentials")
    return None