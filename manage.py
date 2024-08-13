from app import db, User

def reset_db():
    db.drop_all()
    db.create_all()
    print("Database reset successfully!")

def populate_db():
    users = [
        User(username='user1', password='password1'),
        User(username='user2', password='password2'),
        User(username='user3', password='password3')
    ]
    for user in users:
        db.session.add(user)
    db.session.commit()
    print("Database populated with initial users!")

if __name__ == '__main__':
    reset_db()
    populate_db()
