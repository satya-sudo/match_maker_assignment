from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from pydantic import EmailStr
from typing import List
import random
import faker

fake = faker.Faker()

def generate_random_users(n: int) -> List[dict]:
    users = []
    for _ in range(n):
        user = {
            "name": fake.name(),
            "age": random.randint(18, 60),
            "gender": random.choice(["Male", "Female"]),
            "email": fake.email(),
            "city": fake.city(),
            "interests": ", ".join(random.sample(["Reading", "Hiking", "Cooking", "Traveling", "Gaming", "Music", "Art"], 3))
        }
        users.append(user)
    return users

def add_users(users: List[dict]):
    db = SessionLocal()
    try:
        db_users = [User(**user) for user in users]
        db.add_all(db_users)
        db.commit()
        print(f"Successfully added {len(users)} users.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    users = generate_random_users(15)
    add_users(users)
