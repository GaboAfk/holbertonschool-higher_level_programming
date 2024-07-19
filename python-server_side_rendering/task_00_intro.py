import os

def generate_invitations(template, attendees):

    try:
        if not template:
            raise TypeError("Template is empty, no output files generated.")

        if not  isinstance(template, str):
            raise TypeError("template is not a string")
        
        if not attendees:
            raise TypeError("No data provided, no output files generated.")

        if not isinstance(attendees, list) or\
           not all(isinstance(att, dict) for att in attendees):
            raise TypeError("attendees is not a list of dictionaries")

        to_replace_name = "{name}"
        to_replace_title = "{event_title}"
        to_replace_date = "{event_date}"
        to_replace_location = "{event_location}"

        index = 0

        for att in attendees:
            index += 1
            new_att_name = att.get("name") or "N/A"
            new_att_title = att.get("event_title") or "N/A"
            new_att_date = att.get("event_date") or "N/A"
            new_att_location = att.get("event_location") or "N/A"

            new_invitation = template.replace(to_replace_name, new_att_name)\
                                    .replace(to_replace_title, new_att_title)\
                                    .replace(to_replace_date, new_att_date)\
                                    .replace(to_replace_location, new_att_location)

            file = f"output_{index}.txt"
            if os.path.exists(f"./{file}"):
                print(file, "already exists")
                continue

            with open(f"output_{index}.txt", "w") as wfile:
                wfile.write(new_invitation)
    
    except Exception as e:
        print(f"{e}")
        return