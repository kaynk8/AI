if you = "":
    ca_brain = "I do not know what you're saying -_- \nTry again :>"
elif you = "hello":
    ca_brain = "hello my father"
elif you = "how are you":
    ca_brain = "I'm fine thank you and you"
elif you = "I'm fine too thank you":
    ca_brain = "yeah, it so good"
elif you = "today":
    today = date.today()
    ca_brain = today.strftime("%B %d, %Y")
else:
    ca_brain = "I do not know what you're saying -_- \nTry again :>"