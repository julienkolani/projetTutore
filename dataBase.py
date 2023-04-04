import sqlite3

# Crée une connexion à la base de données
conn = sqlite3.connect('example.db')

# Crée une table 'users' avec les colonnes 'id', 'name' et 'email'
conn.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL);''')

# Crée une table 'posts' avec les colonnes 'id', 'user_id', 'title' et 'content'
conn.execute('''CREATE TABLE posts
             (id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             title TEXT NOT NULL,
             content TEXT NOT NULL,
             FOREIGN KEY (user_id) REFERENCES users(id));''')

# Fonction pour créer un nouvel utilisateur
def create_user(name, email):
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

# Fonction pour récupérer un utilisateur par son ID
def get_user_by_id(user_id):
    cursor = conn.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = cursor.fetchone()
    if row:
        return {
            'id': row[0],
            'name': row[1],
            'email': row[2]
        }
    else:
        return None

# Fonction pour mettre à jour un utilisateur
def update_user(user_id, name, email):
    conn.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, user_id))
    conn.commit()

# Fonction pour supprimer un utilisateur
def delete_user(user_id):
    conn.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()

# Fonction pour créer un nouveau post pour un utilisateur donné
def create_post(user_id, title, content):
    conn.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
    conn.commit()

# Fonction pour récupérer le dernier post créé par un utilisateur donné
def get_last_post_by_user(user_id):
    cursor = conn.execute("SELECT * FROM posts WHERE user_id=? ORDER BY id DESC LIMIT 1", (user_id,))
    row = cursor.fetchone()
    if row:
        return {
            'id': row[0],
            'user_id': row[1],
            'title': row[2],
            'content': row[3]
        }
    else:
        return None
