import customtkinter as ctk


app = ctk.CTk()
app.title("Wörtre")

def styleApp():
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("system") 
    titelLabel = ctk.CTkLabel(app, text="WÖRTRE", fg_color="transparent", text_color="white", width=200, height=50, corner_radius=8, font=("Arial", 20, "bold"))
    titelLabel.pack(pady=20)

    startButton = ctk.CTkButton(app, text="Start", width=100, height=40, corner_radius=8, font=("Arial", 14), command=app.mainloop)
    startButton.pack(pady=10)   
    leaderboardButton = ctk.CTkButton(app, text="Leaderboard", width=100, height=40, corner_radius=8, font=("Arial", 14), command=app.mainloop)
    leaderboardButton.pack(pady=10)

def buildLevel(level):
    letterOne = ctk.CTkLabel(app, fg_color="gray", text_color="white", width=50, height=50, corner_radius=8, font=("Arial", 20, "bold"))
    letterTwo = ctk.CTkLabel(app, fg_color="gray", text_color="white", width=50, height=50, corner_radius=8, font=("Arial", 20, "bold"))
    letterThree = ctk.CTkLabel(app, fg_color="gray", text_color="white", width=50, height=50, corner_radius=8, font=("Arial", 20, "bold"))
    letterOne = ctk.CTkLabel(text="A")
    letterTwo = ctk.CTkLabel(text="B")
    letterThree = ctk.CTkLabel(text="C")
    
    letterOne.pack(pady=5)
    letterTwo.pack(pady=5)
    letterThree.pack(pady=5)


    if level == 1:
        level_length = 3
    elif level == 2:
        level_length = 4
    else:
        level_length = 5