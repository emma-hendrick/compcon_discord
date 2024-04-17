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

    # CSS
    css = """
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                    margin: 0;
                    padding: 20px;
                }

                header {
                    margin-bottom: 20px;
                }

                header h1 {
                    color: #333;
                }

                header h2 {
                    margin-top: 5px;
                }

                h2 {
                    color: #a01717;
                }

                p {
                    color: #999;
                }

                /* Style for character details */
                .character-details {
                    margin-bottom: 20px;
                }

                .character-details h2 {
                    font-size: 18px;
                }

                .character-details p {
                    font-size: 16px;
                    margin: 5px 0;
                }

                /* Style for character history */
                .character-history {
                    margin-bottom: 20px;
                }

                .character-history h2 {
                    font-size: 18px;
                }

                .character-history p {
                    font-size: 16px;
                    line-height: 1.5;
                }

                /* Style for character skills and talents */
                .character-skills-talents {
                    margin-bottom: 20px;
                }

                .character-skills-talents h2 {
                    font-size: 18px;
                }

                .character-skills-talents h3 {
                    font-size: 16px;
                    color: #666;
                }

                .character-skills-talents ul {
                    padding-left: 20px;
                }

                ul {
                    list-style: none;
                }
            """
    css_html = f"<style>{css}</style>"

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
        {css_html}
    </head>
    """

    # Body elements
    charname = f"<h1>{charname_line}</h1>"
    subheader = f"<h2>Level {level} - {hp_line} - {character['background']}</h2>"
    stati = f"<p>Status: {character['status']} <br>Dead: {character['dead']}</p>"
    description_html = f"<h2>Description</h2><p>{description}</p>"   
    notes = f"<h2>Notes</h2><p>{character['notes']}</p>"
    history = f"<h2>History</h2>{character['history']}"

    # Header
    header = f"<header>{charname}{subheader}</header>"

    # Character details
    character_details = f"<section class='character-details'>{stati}{description_html}{notes}</section>"

    # History Block
    history_block = f"<section class='character-history'>{history}</section>"

    # Skills
    skills = character["skills"]
    skill_content = ""
    for skill in skills:
        skill_content += f"<li>{skill['id']} {skill['rank']}</li>"
    skill_html = f"<h3>Skills</h3><ul>{skill_content}</ul>"

    # Talents
    talents = character["talents"]
    talent_content = ""
    for talent in talents:
        talent_content += f"<li>{talent['id']} {talent['rank']}</li>"
    talent_html = f"<h3>Talents</h3><ul>{talent_content}</ul>"

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
        mech_skill_content += f"<li>{mech_skill_names[index]}: {mech_skill}</li>"
    mech_skill_html = f"<h3>Mech Skills</h3><ul>{mech_skill_content}</ul>"

    # Skills and talents block
    skills_talent_block = f"<section class='character-skills-talents'><h2>Skills and Talents</h2>{skill_html}{talent_html}{mech_skill_html}</section>"

    # Amalgamate the body
    body = f"""
    <body>
        {header}
        {character_details}
        {history_block}

        {skills_talent_block}
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
