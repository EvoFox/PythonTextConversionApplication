import re
from random import choice

#Array to store the additions that will follow punctuation
owo_faces = ["OwO", "Owo", "owO", "ÓwÓ", "ÕwÕ", "@w@", "ØwØ", "øwø", "uwu", "☆w☆", "✧w✧", "♥w♥", "゜w゜", "◕w◕", "ᅌwᅌ", "◔w◔", "ʘwʘ", "⓪w⓪", "︠ʘw ︠ʘ", "(owo)", "𝕠𝕨𝕠", "𝕆𝕨𝕆", "𝔬𝔴𝔬", "𝖔𝖜𝖔", "𝓞𝔀𝓞", "𝒪𝓌𝒪", "𝐨𝐰𝐨", "𝐎𝐰𝐎", "𝘰𝘸𝘰", "𝙤𝙬𝙤", "𝙊𝙬𝙊", "𝚘𝚠𝚘", "σωσ", "OɯO", "oʍo", "oᗯo", "๏w๏", "o̲wo̲", "ᎧᏇᎧ", "օաօ", "(。O ω O。)", "(。O⁄ ⁄ω⁄ ⁄ O。)", "(O ᵕ O)", "(O꒳O)", "ღ(O꒳Oღ)", "♥(。ᅌ ω ᅌ。)", "(ʘωʘ)", "( ʘ ྌ ʘ )", "(⁄ʘ⁄ ⁄ ω⁄ ⁄ ʘ⁄)♡", "( ͡o ω ͡o )", "( ͡o ᵕ ͡o )", "( ͡o ꒳ ͡o )", "( o͡ ꒳ o͡ )", "( °꒳° )", "( °ᵕ° )", "( °﹏° ) ( °ω° ) (ဝ့ ྌ ဝ့) (ဝ့ ྌྏྏྏྏྏྏྏ ဝ့)", "（ ゜ω 。）", "（ 。ω ゜）", "OwO *𝘸𝘩𝘢𝘵’𝘴 𝘵𝘩𝘪𝘴*", "OwO *𝘯𝘰𝘵𝘪𝘤𝘦𝘴 𝘣𝘶𝘭𝘨𝘦*", "𝐎𝐰𝐎 *𝘸𝘩𝘢𝘵’𝘴 𝘵𝘩𝘪𝘴*", "๏w๏ *𝘯𝘰𝘵𝘪𝘤𝘦𝘴 𝘣𝘶𝘭𝘨𝘦*", "( ͡o ꒳ ͡o )*𝔫𝔬𝔱𝔦𝔠𝔢𝔰 𝔟𝔲𝔩𝔤𝔢*", "*𝓌𝒶𝓉𝓈 𝒹𝒾𝓈?*ღ(O꒳Oღ)", "*𝓃𝓊𝓏𝓏𝓁𝑒𝓈 𝓎𝑜𝓊*(。O⁄ ⁄ω⁄ ⁄ O。)", "(𝐎𝐰𝐎)<𝕣𝕒𝕨𝕣𝕣𝕣)~", "‿︵*𝓇𝒶𝓌𝓇*‿︵ ʘwʘ", "✼ ҉ (O꒳O) ҉ ✼", "✼ ҉♡ (。O⁄ ⁄ω⁄ ⁄ O。) ҉♡ ✼", "✧･ﾟ: *✧･ﾟ:*(OwO )*:･ﾟ✧*:･ﾟ✧‏"]

#Dictionary to store match patterns
pattern = {
    #n_vowel: Matches anything that begins with an N, and is followed by a vowel (case insensitive)
    "n_vowel" : r"([nN])([aeiouAEIOU])",
    #rl_w: Matches any R or L (case insensitive)
    "rl_w" : r"([RrLl])",
    #ove: Matches any instance of OVE (case insensitive)
    "ove" : r"([Oo][Vv][Ee])",
    #punctuation: Matches any !, ? or .
    "punctuation" : r"([!?\.])"
}

#Dictionary to store replacement strings
replace = {
    #n_vowel: Utilises the capture groups in pattern["n_vowel"] to insert a character in between the capture groups
    "n_vowel" : "\\1y\\2",
    #rl_w: Blanket replaces anything caught by pattern["rl_w"] with a lower case W
    "rl_w" : "w",
    #ove: Blanket replaces anything caught by pattern["ove"] with a lower case uv
    "ove" : "uv",
    #punctuation: Utilises the capture group in pattern["punctuation"] to add a string to each instance.
    "punctuation" : f"\\1{choice(owo_faces)}"
}

def owoify(str_input):
    #Stage 1 Processing: Take the initial input, and replave any instances of an N followed by a vowel, by itself, seperated by a Y
    processed = re.sub(pattern["n_vowel"], replace["n_vowel"], str_input)
    #Stage 2 Processing: Take the Stage 1 Processed string, and replace any R with W
    processed = re.sub(pattern["rl_w"], replace["rl_w"], processed)
    #Stage 3 Processing: Take the Stage 2 Processed string, and replace any instance of ove with uv
    processed = re.sub(pattern["ove"], replace["ove"], processed)
    #Stage 4 Processing: Take the Stage 3 Processed string, and add a preselected string following any !, ? or .
    processed = re.sub(pattern["punctuation"], replace["punctuation"] , processed)

    #Return the processed string to where this function was called.
    return processed
    