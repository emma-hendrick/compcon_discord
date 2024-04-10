import math

# Generate the html for the users character sheet
def generate_html(character):
    
    # Start building the html content
    charname_line = f"{character['callsign']} - {character['name']}"
    c_id = character["id"]
    p_name = character["player_name"]
    description = f"Page for character with id {c_id}, made by player {p_name}"
    level = character["level"]
    max_hp = 6 + math.ceil(int(level) / 2)
    current_hp = int(character["current_hp"])
    hp_line = f"{current_hp} / {max_hp} HP"

    # Head elements
    title = f"<title>{charname_line}</title>"
    
    # Meta tags
    description_tag = f"<meta name='description' content='{description}'>"
    author = f"<meta name='author' content='Emma Hendrick'>"
    meta = f"""
        {description_tag}
        {author}
    """

    # Amalgamate the head
    head = f"""
    <head>
        {title}
        {meta}
    </head>
    """

    # Body elements
    header = f"<h1>{charname_line}</h1>"
    background = f"<h4>{character['background']}</h4>"
    subheader = f"<h2>Level {level}</h2>"
    hp = f"<h4>{hp_line}</h4>"
    description_html = f"<p>{description}</p>"
    stati = f"<p>Status: {character['status']} <br>Dead: {character['dead']}</p>"
    notes = f"<p>Notes: {character['notes']}</p>"
    history = f"<h4>History</h4>{character['history']}"

    # Skills
    skills = character["skills"]
    skill_content = ""
    for skill in skills:
        skill_content += f"{skill['id']} {skill['rank']}<br>"
    skill_html = f"<h4>Skills</h4><p>{skill_content}</p>"

    # Talents
    talents = character["talents"]
    talent_content = ""
    for talent in talents:
        talent_content += f"{talent['id']} {talent['rank']}<br>"
    talent_html = f"<h4>Talents</h4><p>{talent_content}</p>"

    # Mech Skills
    mech_skills = character["mechSkills"]
    mech_skill_content = ""
    mech_skill_names = [
        "Hull", 
        "Agility", 
        "Systems", 
        "Engineering"
    ]
    for index, mech_skill in enumerate(mech_skills):
        mech_skill_content += f"{mech_skill_names[index]}: {mech_skill}<br>"
    mech_skill_html = f"<h4>Mech Skills</h4><p>{mech_skill_content}</p>"

    # Amalgamate the body
    body = f"""
    <body>
        {header}
        {background}
        {subheader}
        {hp}
        {description_html}
        {stati}
        {notes}
        {history}

        {skill_html}
        {talent_html}
        {mech_skill_html}
    </body>
    """

    # Document elements
    html = f"""
    <html>
        {head}
        {body}
    </html>
    """

    # Return the HTML
    return html
