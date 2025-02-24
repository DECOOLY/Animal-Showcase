import webbrowser
import os
from tkinter import Tk, Toplevel, Label, Button, StringVar, Radiobutton, Frame, CENTER, DISABLED, NORMAL, PhotoImage

def create_info_window(title, content, quiz_command, link_url):
    window.withdraw()  # Hide main window
    info_win = Toplevel(window)
    info_win.title(title)
    info_win.geometry("1920x1080")
    
    # Ensure that if the info window is closed, the main window reappears
    info_win.protocol("WM_DELETE_WINDOW", lambda: [info_win.destroy(), window.deiconify()])
    
    Label(info_win, text=content, wraplength=1000, justify=CENTER,
          font=("Comic Sans MS", 14), padx=50, pady=50).pack(pady=20)
    
    # Hyperlink label for more information
    link_label = Label(info_win, text="Learn more", font=("Comic Sans MS", 12), fg="blue", cursor="hand2")
    link_label.pack(pady=10)
    link_label.bind("<Button-1>", lambda e: webbrowser.open(link_url))
    
    Button(info_win, text="Take Quiz", font=("Comic Sans MS", 30, "bold"),
           command=lambda: [info_win.destroy(), quiz_command()]).pack(pady=50)

def lion_info_win():
    content = """Lions: The Majestic Kings of the Savannah

Lions, often referred to as the "kings of the jungle," are among the most iconic and majestic animals in the world. Known for their strength, social structure, and cultural significance, lions symbolize power and pride. These big cats, native to Africa and parts of Asia, have fascinated humans for centuries and continue to be a subject of admiration and study.

Lions are the second largest members of the cat family, following tigers. Male lions are easily recognized by their impressive manes, which vary in color from light blond to dark brown and serve as a sign of maturity and strength. Lions are unique among big cats because they live in social groups called prides.

Unfortunately, lions face numerous threats, including habitat loss, human-wildlife conflict, and poaching. Preserving lions and their environments requires global efforts and a commitment to coexistence.

As we marvel at the majesty of lions, we must also recognize our responsibility to ensure their continued existence. By protecting lions, we honor not only their legacy but also the ecological balance they help maintain."""
    
    create_info_window(
        title="Information on the Lion 🦁", 
        content=content, 
        quiz_command=lambda: launch_quiz("Lion"), 
        link_url="https://en.wikipedia.org/wiki/Lion"
    )

quiz_data = {
    "Lion": {
        "emoji": "🦁",
        "link": "https://en.wikipedia.org/wiki/Lion",
        "questions": [
            ("What is the lion often called?", 
             ["King of the Jungle", "Prince of the Forest", "Guardian of the Wild", "Lord of the Cats"], 
             "King of the Jungle"),
            ("What is unique about lions compared to other big cats?", 
             ["They are the biggest cats", "They live in social groups", "They are herbivores", "They can fly"], 
             "They live in social groups"),
            ("What is the main threat to lions?", 
             ["Too many prey", "Habitat loss and poaching", "Climate change", "Lack of water"], 
             "Habitat loss and poaching")
        ],
        "next": "Tiger"
    },
    "Tiger": {
        "emoji": "🐯",
        "link": "https://en.wikipedia.org/wiki/Tiger",
        "questions": [
            ("What is the tiger's primary habitat?", 
             ["Rainforests", "Savannas", "Tundra", "Deserts"], 
             "Rainforests"),
            ("What is unique about tigers compared to other cats?", 
             ["They are the largest cats", "They can fly", "They are herbivores", "They live in groups"], 
             "They are the largest cats"),
            ("What is the tiger's main diet?", 
             ["Vegetation", "Small mammals", "Large herbivores", "Fish and aquatic plants"], 
             "Large herbivores")
        ],
        "next": "Elephant"
    },
    "Elephant": {
        "emoji": "🐘",
        "link": "https://en.wikipedia.org/wiki/Elephant",
        "questions": [
            ("What is the primary threat to elephants?", 
             ["Poaching", "Habitat destruction", "Climate change", "None of the above"], 
             "Poaching"),
            ("What is a characteristic feature of elephants?", 
             ["Trunk", "Tusks", "Large ears", "All of the above"], 
             "All of the above"),
            ("Where do elephants live?", 
             ["Asia only", "Africa only", "Both Africa and Asia", "America"], 
             "Both Africa and Asia")
        ],
        "next": "Giraffe"
    },
    "Giraffe": {
        "emoji": "🦒",
        "link": "https://en.wikipedia.org/wiki/Giraffe",
        "questions": [
            ("What is the giraffe's most distinguishing feature?", 
             ["Long neck", "Large ears", "Big feet", "Short tail"], 
             "Long neck"),
            ("What do giraffes primarily eat?", 
             ["Leaves from tall trees", "Grass", "Bushes", "Insects"], 
             "Leaves from tall trees"),
            ("Where do giraffes primarily live?", 
             ["South America", "Africa", "Asia", "Australia"], 
             "Africa")
        ],
        "next": None
    }
}

def launch_quiz(animal):
    data = quiz_data[animal]
    quiz_win = Toplevel(window)
    quiz_win.title(f"{animal} Quiz {data['emoji']}")
    quiz_win.geometry("1920x1080")
    
    Label(quiz_win, text=f"{animal} Quiz", font=("Comic Sans MS", 20, "bold")).pack(pady=20)
    
    # Add a clickable link for more information about the animal
    link_label = Label(quiz_win, text=f"Learn more about {animal}", font=("Comic Sans MS", 12), fg="blue", cursor="hand2")
    link_label.pack(pady=10)
    link_label.bind("<Button-1>", lambda e: webbrowser.open(data["link"]))
    
    user_answers = []
    for question, options, correct in data["questions"]:
        frame = Frame(quiz_win)
        frame.pack(pady=10, padx=20)
        Label(frame, text=question, font=("Comic Sans MS", 14)).pack(anchor="w")
        
        selected = StringVar()
        for option in options:
            Radiobutton(frame, text=option, variable=selected, 
                        value=option, font=("Comic Sans MS", 12)).pack(anchor="w")
        user_answers.append((selected, correct))
    
    result_label = Label(quiz_win, text="", font=("Comic Sans MS", 14, "bold"))
    result_label.pack(pady=20)
    
    next_button = None
    if data["next"]:
        next_button = Button(
            quiz_win, 
            text=f"Next: {data['next']} Quiz", 
            font=("Comic Sans MS", 14), 
            state=DISABLED,
            command=lambda: [quiz_win.destroy(), launch_quiz(data['next'])]
        )
        next_button.pack(pady=20)
    
    def check_answers():
        score = sum(1 for (var, correct) in user_answers if var.get() == correct)
        result_label.config(
            text=f"Score: {score}/{len(data['questions'])}", 
            fg="green" if score == len(data['questions']) else "red"
        )
        if next_button and score == len(data['questions']):
            next_button.config(state=NORMAL)
    
    Button(quiz_win, text="Submit Answers", font=("Comic Sans MS", 14), command=check_answers).pack(pady=20)

# Main window setup
window = Tk()
window.title("Animal Info and Quizzes")
window.geometry("1920x1080")

# Create a text button for starting the quiz
start_button = Button(window, text="Start with Lion", font=("Comic Sans MS", 30, "bold"), command=lion_info_win)
start_button.pack(pady=20)

# Place the desired image below the button (ensure 'start.png' is in the same directory)
if os.path.exists("start.png"):
    start_img = PhotoImage(file="start.png")
    start_img_label = Label(window, image=start_img)
    start_img_label.image = start_img  # Keep a reference
    start_img_label.pack(pady=20)
else:
    Label(window, text="(Image not found: start.png)", font=("Comic Sans MS", 16, "bold")).pack(pady=20)

# Add a label at the bottom with your prompt
Label(
    window, 
    text="Are you ready to quiz yourself on the greatest animals?",
    font=("Comic Sans MS", 16, "bold")
).pack(pady=20)

window.mainloop()
