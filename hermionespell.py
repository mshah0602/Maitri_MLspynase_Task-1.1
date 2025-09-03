runes=["L","h","U","e","M","o","j","s","l"]
upper_runes=[rune.upper() for rune in runes]
#print(upper_runes)
required={"L":1,"U":1,"M":1,"O":1,"S":1}
collector={}
for i, rune in enumerate(upper_runes, start=1):
    collector[rune]=collector.get(rune,0)+1
spell_acheived=True
for letter in required:
    if collector.get(letter,0)<required[letter]:
        spell_acheived=False
        break
    if spell_acheived:
        print("LUMOS is achieved by Hermione at step",i)
        break
    else:
        print(-1)
print(collector)
