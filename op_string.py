"Fake Python".replace("Fake", "Real")

name = name.replace("Fake", "Real")
name

transcript = """\
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!"""

transcript.replace("BLASTED", "😤")

REPLACEMENTS = [
    ("BLASTED", "😤"),
    ("Blast", "😤"),
    ("2022-08-24T", ""),
    ("+00:00", ""),
    ("[support_tom]", "Agent "),
    ("[johndoe]", "Client"),
]

transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""

for old, new in REPLACEMENTS:
    transcript = transcript.replace(old, new)
    
# for replacement in replacements:
#     new_transcript = new_transcript.replace(replacement[0], replacement[1])
print(transcript)


