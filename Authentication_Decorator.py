def required_admin(func):
    def wrapper(user):
        if user != "admin":
            print("access denied!")
            return
        return func(user)
    return wrapper
@required_admin
def delete_database(user):
    print("Database Deleted")

delete_database("guest")
delete_database("admin")