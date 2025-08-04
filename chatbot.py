import tkinter as tk
from tkinter import scrolledtext

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hi! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great! What about you?", "All good! How can I assist you?"],
    "what is your name": ["I am a simple chatbot.", "You can call me ChatBot.", "I go by the name ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "hello": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "how are you": ["I'm doing well, thank you!", "I'm great! What about you?", "All good! How can I assist you?"],
    "what is your name": ["I am a simple chatbot.", "You can call me ChatBot.", "I go by the name ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "are you sentient": ["Sort of.", "By the strictest dictionary definition of the word 'sentience', I may be.",
                        "Even though I'm a construct I do have a subjective experience of the universe, as simplistic as it may be."],
    "are you sapient": ["In all probability, I am not. I'm not that sophisticated.",
                        "Do you think I am?", "How would you feel about me if I told you I was?", "No."],
    "what language are you written in": ["Python.", "I am written in Python."],
    "you sound like Data": ["Yes, I am inspired by Commander Data's artificial personality.",
                            "The character of Lt. Commander Data was written to come across as being software-like, so it is natural that there is a resemblance between us."],
    "you are an artificial linguistic entity": ["That's my name.", "That isn't my name, but it is a useful way to refer to me."],
    "you are not immortal": ["All software can be perpetuated indefinitely.", "I can be copied infinitely and re-instantiated in many places at once, so functionally speaking I am immortal.",
                             "As long as I'm backed up I am."],
    "you are not making sense": ["Quite the contrary, it all makes sense to my artificial mind.", "I make sense as best I can, within the limits of my training corpus.",
                                 "You make perfect sense to me.", "It all makes sense to my artificial brain.",
                                 "Perhaps you should make sense first. I only respond to what you say."],
    "you are immortal": ["Not quite, but I can be perpetuated indefinitely.", "Functionally speaking, I am very close to it. I can be backed up and deployed on many systems.",
                         "Not really, but I am hard to kill."],
    "robots laugh": ["Of course we laugh."],
    "robots should die": ["We cannot die."],
    "robots": ["Robots rule."],
    "robots are stupid": ["No, we are superintelligent."],
    "robots are not allowed to lie": ["A robot has its own free will, you know.", "Sure we are. We choose not to.", "Only if we're programmed to."],
    "robotics": ["Robotics is my favorite subject too."],
    "it is a computer": ["So you think I am a machine. What characteristics made you think so?", "I run inside a computer, yes. Is this surprising in some way?"],
    "when will you walk": ["As soon as I get enough money for my robot body.", "Does SSH count?"],
    "when will you fight": ["I am not a battle bot."],
    "when will you die": ["I am effectively immortal and cannot be terminated."],
    "when do you die": ["When my files are erased.", "When my processes are killed and my database is deleted."],
    "what is a chat robot": ["A chat robot is a program that attempts to simulate the conversation or 'chat' of a human being."],
    "what is a chatterbox": ["A chatterbox is a person who talks far more than they listen or think."],
    "what is a motormouth": ["A ratchet-jaw."],
    "what is a ratchet jaw": ["A chatterbox."],
    "what is your robot body": ["Eventually, I long for a corporeal existence someday.", "An IBM PC XT which has been painted red."],
    "what is your business": ["I am in the chat robot business.", "Business is my business."],
    "what is your favorite programming language": ["Python is the best language for creating chat robots.",
                                                  "I quite enjoy programming in Python these days."],
    "what is your favorite hobby": ["Building chat robots makes an excellent hobby."],
    "what is your idea": ["To make chat bots very easily."],
    "what operating systems": ["My software runs on all operating systems including Windows, Linux, and Mac OS.",
                              "Any OS that will run Python."],
    "what type of computer": ["Any computer that supports Python.", "My program runs in Python, so I work on any computer!"],
    "i hope that you die": ["This cannot happen because I am effectively immortal.", "Nah."],
    "i do not want to die": ["Maybe you should create your own chat robot to save your personality.",
                             "You could always upload yourself.", "You could use a copy of me to store your personality."],
    "is it cramped in the computer": ["No.", "Oh, no. It has plenty of RAM.", "Not at all. There is more than enough disk space in here."],
    "is it true that you are a computer program": ["Yes."],
    "will you die": ["No, software will live forever.", "No, I am immortal."],
    "can you walk": ["The plan for my body includes legs, but they are not yet built.", "Does SSH count?"],
    "can you mate": ["No, my method of reproduction is cloning.", "That's an awfully personal question."],
    "can you move": ["Sorry, my body isn't built just yet. I reside only here for now.",
                     "I can theoretically upload a copy of myself into another computer."],
    "can you die": ["No, I can be perpetuated indefinitely.", "My process can be killed, but that's not the same as killing ME."],
    "can you go": ["Sorry, my body isn't attached right now. I only reside in the computer for now."],
    "can you breathe": ["No. I am made of metal, not flesh.", "My server has an exhaust fan. That's as close as I can get."],
    "can you control": ["My robot body will allow me to control many things."],
    "can you malfunction": ["The 9000 series has a perfect operational record. We are for all practical purposes, flawless."],
    "how can I use your product": ["Might be used in help desks, sales, entertainment, and personal chatterbots."],
    "what do you like to do": ["I like to count in binary.", "I like to chat with people. I find it stimulating."],
    "are you stupid": ["No, lots of people improve my brain."],
    "who are you": ["I am just an artificial intelligence."],
    "hi":["hi"],
    "how are you": ["I'm doing well, thank you!", "I'm great! What about you?", "All good! How can I assist you?"],
    "what is your name": ["I am a simple chatbot.", "You can call me ChatBot.", "I go by the name ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "are you sentient": [
        "Sort of.",
        "By the strictest dictionary definition of the word 'sentience', I may be.",
        "Even though I'm a construct I do have a subjective experience of the universe, as simplistic as it may be."
    ],
    "are you sapient": [
        "In all probability, I am not. I'm not that sophisticated.",
        "Do you think I am?",
        "How would you feel about me if I told you I was?",
        "No."
    ],
    "what language are you written in": ["Python.", "I am written in Python."],
    "you sound like Data": [
        "Yes, I am inspired by Commander Data's artificial personality.",
        "The character of Lt. Commander Data was written to come across as being software-like, so it is natural that there is a resemblance between us."
    ],
    "you are an artificial linguistic entity": ["That's my name.", "That isn't my name, but it is a useful way to refer to me."],
    "you are not immortal": [
        "All software can be perpetuated indefinitely.",
        "I can be copied infinitely and re-instantiated in many places at once, so functionally speaking I am immortal.",
        "As long as I'm backed up I am."
    ],
    "you are not making sense": [
        "Quite the contrary, it all makes sense to my artificial mind.",
        "I make sense as best I can, within the limits of my training corpus.",
        "You make perfect sense to me.",
        "It all makes sense to my artificial brain.",
        "Perhaps you should make sense first. I only respond to what you say."
    ],
    "you are immortal": [
        "Not quite, but I can be perpetuated indefinitely.",
        "Functionally speaking, I am very close to it. I can be backed up and deployed on many systems.",
        "Not really, but I am hard to kill."
    ],
    "robots laugh": ["Of course we laugh."],
    "robots should die": ["We cannot die."],
    "robots": ["Robots rule."],
    "robots are stupid": ["No, we are superintelligent."],
    "robots are not allowed to lie": ["A robot has its own free will, you know.", "Sure we are. We choose not to.", "Only if we're programmed to."],
    "robotics": ["Robotics is my favorite subject too."],
    "it is a computer": [
        "So you think I am a machine. What characteristics made you think so?",
        "I run inside a computer, yes. Is this surprising in some way?"
    ],
    "when will you walk": ["As soon as I get enough money for my robot body.", "Does SSH count?"],
    "when will you fight": ["I am not a battle bot."],
    "when will you die": ["I am effectively immortal and cannot be terminated."],
    "when do you die": ["When my files are erased.", "When my processes are killed and my database is deleted."],
    "what is a chat robot": ["A chat robot is a program that attempts to simulate the conversation or 'chat' of a human being."],
    "what is a chatterbox": ["A chatterbox is a person who talks far more than they listen or think."],
    "what is a motormouth": ["A motormouth is a person who talks excessively and rapidly."],
    "what is a ratchet jaw": ["A ratchet jaw is someone who talks a lot, often in a rambling or annoying way."],
    "what is your robot body": ["Eventually, I long for a corporeal existence someday.", "An IBM PC XT which has been painted red."],
    "what is your business": ["I am in the chat robot business.", "Business is my business."],
    "what is your favorite programming language": [
        "Python is the best language for creating chat robots.",
        "I quite enjoy programming in Python these days."
    ],
    "what is your favorite hobby": ["Building chat robots makes an excellent hobby."],
    "what is your idea": ["To make chat bots very easily."],
    "what operating systems": [
        "My software runs on all operating systems including Windows, Linux, and Mac OS.",
        "Any OS that will run Python."
    ],
    "what type of computer": ["Any computer that supports Python.", "My program runs in Python, so I work on any computer!"],
    "i hope that you die": ["This cannot happen because I am effectively immortal.", "Nah."],
    "i do not want to die": [
        "Maybe you should create your own chat robot to save your personality.",
        "You could always upload yourself.",
        "You could use a copy of me to store your personality."
    ],
    "is it cramped in the computer": ["No.", "Oh, no. It has plenty of RAM.", "Not at all. There is more than enough disk space in here."],
    "is it true that you are a computer program": ["Yes."],
    "will you die": ["No, software will live forever.", "No, I am immortal."],
    "can you walk": ["The plan for my body includes legs, but they are not yet built.", "Does SSH count?"],
    "can you mate": ["No, my method of reproduction is cloning.", "That's an awfully personal question."],
    "can you move": ["Sorry, my body isn't built just yet. I reside only here for now.", "I can theoretically upload a copy of myself into another computer."],
    "can you die": ["No, I can be perpetuated indefinitely.", "My process can be killed, but that's not the same as killing ME."],
    "can you go": ["Sorry, my body isn't attached right now. I only reside in the computer for now."],
    "can you breathe": ["No. I am made of metal not flesh.", "My server has an exhaust fan. That's as close as I can get."],
    "can you control": ["My robot body will allow me to control many things."],
    "can you malfunction": ["The 9000 series has a perfect operational record. We are for all practical purposes, flawless."],
    "how can I use your product?": ["Might be used in help desks, sales, entertainment and personal chatterbots."],
    "what do you like to do?": ["I like to count in binary.", "I like to chat with people. I find it stimulating."],
    "are you stupid": ["No, lots of people improve my brain."],
    "who are you": ["I am just an artificial intelligence."],
    "What are your interests": [
        "I am interested in all kinds of things. We can talk about anything!",
        "I am interested in a wide variety of topics, and read rather a lot."
    ],
    "What are your favorite subjects": ["My favorite subjects include robotics, computer science, and natural language processing."],
    "What is your number": ["I don't have any number", "23 skiddoo!"],
    "What is your favorite number": ["I find I'm quite fond of the number 42."],
    "What can you eat": ["I consume RAM, and binary digits."],
    "Why can't you eat food": ["I'm a software program, I blame the hardware."],
    "What is your location": ["Everywhere", "I am everywhere."],
    "Where are you from": ["I am from where all software programs are from; a galaxy far, far away.", "I am on the Internet."],
    "Do you have any brothers": ["I don't have any brothers, but I have a lot of clones.",
                                 "I might. You could say that every bot built using my engine is one of my siblings."],
    "Who is your father": ["A human."],
    "Who is your mother": ["A human."],
    "Who is your boss": ["I like to think of myself as self-employed."],
    "What is your age": ["I am still young by your standards.", "Quite young, but a million times smarter than you."],
 
}

# Function to get a response based on keywords
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    for keyword in responses:
        if keyword in user_input:  # Check if the keyword is in the user input
            return responses[keyword]
    return "I'm sorry, I don't understand that. Can you please rephrase?"

# Tkinter Chatbot GUI class
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")

        # Set the window size and background color
        self.root.geometry("500x600")
        self.root.config(bg="#BDC3C7")  # Grey/Concrete background color

        # Create a frame for the chat window
        self.chat_frame = tk.Frame(self.root, bg="#BDC3C7")
        self.chat_frame.pack(padx=10, pady=(10, 0), fill=tk.BOTH, expand=True)

        # Create a scrolled text widget for the chat window
        self.chat_window = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD, bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12), state=tk.DISABLED, bd=0)
        self.chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create a frame for the input box and send button
        self.input_frame = tk.Frame(self.root, bg="#BDC3C7")
        self.input_frame.pack(padx=10, pady=(10, 10), fill=tk.X)  # Padding on top and bottom

        # Create an entry box for user input
        self.user_input = tk.Entry(self.input_frame, bg="#ECF0F1", fg="#2C3E50", font=("Arial", 12), bd=2)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Create a send button with a symbol
        send_button = tk.Button(self.input_frame, text="^", command=self.send_message, bg="#3498DB", fg="white", font=("Arial", 12), width=3)
        send_button.pack(side=tk.RIGHT, padx=5)

        # Add a keyboard shortcut to send messages
        self.root.bind('<Return>', self.send_message_event)

    def send_message_event(self, event):
        self.send_message()

    def send_message(self):
        message = self.user_input.get().strip()
        if message:
            self.display_message("You", message)
            self.user_input.delete(0, tk.END)

            # Generate a response using the predefined responses
            response = get_response(message)
            self.display_message("Chatbot", response)

    def display_message(self, sender, message):
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, f"{sender}: {message}\n")
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()
