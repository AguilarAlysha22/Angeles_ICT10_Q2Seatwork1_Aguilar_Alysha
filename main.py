from pyscript import document

club_members = ["Alysha Aguilar", "Mica Frigillana", "Raji Santos", "Megan Tan", "Damien Tanglao"]

def check_name(e):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()
    full_name = first + " " + last

    output = document.getElementById("output")

    if not first or not last:
        output.innerHTML = "Please enter your first and last name."
    else:
        result = full_name.lower() in [name.lower() for name in club_members]

        if result:
            output.innerHTML = f"Congratulations {full_name}! You are now part of the Glee Club."
        else:
            output.innerHTML = f"Sorry {full_name}, your name is not on the list."