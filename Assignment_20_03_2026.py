
messy_sentences = [
    "yo wat's up m8, hows ur day goin? 🔥",
    "i cnt blieve its alrdy friday!!! 😂😂",
    "ngl this is awesum lol xD",
    "ur killin it fam 💯 no cap",
    "wtf did u just say?? thats not kool bro 😤",
    "omg ima lose my mind rn fr fr 🤦",
    "she be like 'nah fam' nd i was like bruh 💀",
    "lowkey this code is trash lmaooo 🗑️",
    "bet u cant do it, sis 👀✨",
    "srsly tho, u need to chill tf out",
    "its been cray cray lately ngl 😭",
    "aint no way jose, thats cap af 🧢",
    "im dead 💀💀 ur so funny g",
    "highkey struggling w/ dis assignmnt tbh",
    "yo this slaps fr, no joke 🎵🔊",
    "ur telling me ur rly gonna do that? sus 🤨",
    "bestie ur looks r fire af periodt 💅",
    "cant even, this is 2 much 4 me rn",
    "nah im goood, ill pass thanks 🙅",
    "literally shook rn, this is insane 😱😱"
]

print("=" * 60)
print("MESSY TEXT PREPROCESSING ANALYSIS")
print("=" * 60)

for i, sentence in enumerate(messy_sentences, 1):
    print(f"\n{i}. {sentence}")

print("\n" + "=" * 60)
print("PREPROCESSING NEEDED:")
print("=" * 60)
print("""
1. SLANG REMOVAL:
   - 'wat's up' → 'what is up'
   - 'm8' → 'mate'
   - 'ngl' → 'not gonna lie'
   - 'lol', 'lmao', 'xD' → remove or replace
   - 'fr fr', 'fr', 'fam', 'bro', 'sis' → standard terms
   - 'cap', 'sus', 'fire', 'slaps' → context-based replacement

2. EMOJI REMOVAL:
   - Remove all emoji characters (🔥😂💯😤🤦💀🗑️👀✨😭🧢🎵🔊🤨💅😱)
   - Consider if sentiment analysis needed before removal

3. TYPOS & ABBREVIATIONS:
   - 'cnt' → 'can't'
   - 'blieve' → 'believe'
   - 'alrdy' → 'already'
   - 'ur' → 'your'/'you are'
   - 'goin' → 'going'
   - 'kool' → 'cool'
   - 'nd' → 'and'
   - 'u' → 'you'
   - 'rly' → 'really'
   - 'w/' → 'with'
   - 'af' → remove intensifier
   - 'u' → 'you'
   - 'dis' → 'this'
   - 'assignmnt' → 'assignment'
   - 'tbh' → expand or remove

4. CONTRACTIONS:
   - Expand: "aint" → "am not", "cant" → "cannot"

5. EXTRA PUNCTUATION:
   - Multiple '!!!' → '!'
   - Multiple '???' → '?'
   - Remove excess capitalization

6. STANDARDIZATION:
   - Lowercase all text
   - Remove multiple spaces
   - Trim whitespace
""")