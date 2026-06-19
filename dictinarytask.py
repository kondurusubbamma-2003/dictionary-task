# Empty dictionary to store user profiles
users = {}

print("Initial Dictionary:", users)


# Add a new user
def add_user(user_id, user_name):
    users[user_id] = user_name
    print("User Added")
    print(users)


# Retrieve user by ID
def get_user(user_id):
    if user_id in users:
        print("User Name:", users[user_id])
    else:
        print("User ID not found")


# Update user name
def update_user(user_id, new_name):
    if user_id in users:
        users[user_id] = new_name
        print("User Updated")
        print(users)
    else:
        print("User ID not found")


# Remove user
def remove_user(user_id):
    if user_id in users:
        del users[user_id]
        print("User Removed")
        print(users)
    else:
        print("User ID not found")


# Testing

add_user(101, "Subbu")
add_user(102, "Ravi")

get_user(101)

update_user(101, "Subhash")

remove_user(102)

get_user(102)