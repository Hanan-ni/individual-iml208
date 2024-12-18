# Global variables to store user's selections
user_data = {
    "movie": None,
    "screen": None,
    "time": None,
    "tickets": 0
}

def t_movie():
    global user_data
    print("Which movie do you want to watch?")
    print("1. Angry Birds")
    print("2. Moana")
    print("3. Encanto")
    print("4. Back")
    print("5. Delete Existing Data")  # Option to delete data
    movie = int(input("Choose your movie: "))
    if movie == 4:
        center()
        return
    elif movie == 5:
        delete_data()
        return
    else:
        user_data["movie"] = movie  # Store selected movie
        if user_data["movie"]:
            theater()

def delete_data():
    global user_data
    print("Are you sure you want to delete your existing selections? (y/n)")
    choice = input().lower()
    if choice == 'y':
        user_data = {
            "movie": None,
            "screen": None,
            "time": None,
            "tickets": 0
        }
        print("All data has been deleted!")
    else:
        print("Data not deleted.")

def theater():
    global user_data
    print("Which screen do you want to watch the movie?")
    print("1. SCREEN 1")
    print("2. SCREEN 2")
    print("3. SCREEN 3")
    a = int(input("Choose your screen: "))
    if a not in [1, 2, 3]:
        print("Invalid choice! Try again.")
        return theater()
    user_data["screen"] = a  # Store selected screen
    ticket = int(input("Number of tickets you want?: "))
    user_data["tickets"] = ticket  # Store number of tickets
    timing(a)

def timing(a):
    global user_data
    time1 = {
        "1": "9.00-11.00", "2": "12.10-2.10", "3": "3.20-5.20", "4": "7.30-9.30"
    }
    time2 = {
        "1": "10.15-1.15", "2": "1.25-4.25", "3": "4.35-7.35", "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30", "2": "1.40-4.40", "3": "4.50-7.50", "4": "8.00-10.45"
    }

    times = {1: time1, 2: time2, 3: time3}
    print("Choose your time:")
    print(times[a])
    t = input("Select your time:")
    if t not in times[a]:
        print("Invalid time! Try again.")
        return timing(a)
    user_data["time"] = times[a][t]  # Store selected time
    print(f"Successful! Enjoy the movie at {user_data['time']}")

def movie(theater):
    if theater in [1, 2, 3]:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Wrong choice")

def center():
    print("Which is your eligibility category price?")
    print("1. Adult price")
    print("2. Student price")
    print("3. Senior price")
    print("4. Back")
    print("5. Delete Existing Data")  # Option to delete data
    a = int(input("Choose your option: "))
    if a == 5:
        delete_data()
        return
    movie(a)

def city():
    print("Hello everyone!! Welcome to the movie ticket booking:")
    print("Where do you want to watch the movie?")
    print("1. Kuala Lumpur")
    print("2. Kuala Selangor")
    print("3. Sungai Petani")
    print("4. Delete Existing Data")  # Option to delete data
    place = int(input("Choose your option: "))
    if place == 4:
        delete_data()
        return
    if place in [1, 2, 3]:
        center()
    else:
        print("Wrong choice! Try again.")
        city()

# To start the booking system
city()
