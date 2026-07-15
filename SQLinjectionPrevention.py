import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER, username TEXT, password TEXT)")
conn.execute("INSERT INTO users VALUES (1, 'admin', 'secret123')")

# - never do this
def unsafe_login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Running:", query)
    return conn.execute(query).fetchall()

#  - parameterized query
def safe_login(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    return conn.execute(query, (username, password)).fetchall()

# Try: unsafe_login("admin' --", "anything") to see the injection work
print(unsafe_login("admin' --", "anything"))
print(safe_login("admin' --", "anything"))  # returns nothing, as expected