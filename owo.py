import re
from random import choice
owo_faces = ["OwO", "Owo", "owO", "ÓwÓ", "ÕwÕ", "@w@", "ØwØ", "øwø", "uwu", "☆w☆", "✧w✧", "♥w♥", "゜w゜", "◕w◕", "ᅌwᅌ", "◔w◔", "ʘwʘ", "⓪w⓪", "︠ʘw ︠ʘ", "(owo)", "𝕠𝕨𝕠", "𝕆𝕨𝕆", "𝔬𝔴𝔬", "𝖔𝖜𝖔", "𝓞𝔀𝓞", "𝒪𝓌𝒪", "𝐨𝐰𝐨", "𝐎𝐰𝐎", "𝘰𝘸𝘰", "𝙤𝙬𝙤", "𝙊𝙬𝙊", "𝚘𝚠𝚘", "σωσ", "OɯO", "oʍo", "oᗯo", "๏w๏", "o̲wo̲", "ᎧᏇᎧ", "օաօ", "(。O ω O。)", "(。O⁄ ⁄ω⁄ ⁄ O。)", "(O ᵕ O)", "(O꒳O)", "ღ(O꒳Oღ)", "♥(。ᅌ ω ᅌ。)", "(ʘωʘ)", "( ʘ ྌ ʘ )", "(⁄ʘ⁄ ⁄ ω⁄ ⁄ ʘ⁄)♡", "( ͡o ω ͡o )", "( ͡o ᵕ ͡o )", "( ͡o ꒳ ͡o )", "( o͡ ꒳ o͡ )", "( °꒳° )", "( °ᵕ° )", "( °﹏° ) ( °ω° ) (ဝ့ ྌ ဝ့) (ဝ့ ྌྏྏྏྏྏྏྏ ဝ့)", "（ ゜ω 。）", "（ 。ω ゜）", "OwO *𝘸𝘩𝘢𝘵’𝘴 𝘵𝘩𝘪𝘴*", "OwO *𝘯𝘰𝘵𝘪𝘤𝘦𝘴 𝘣𝘶𝘭𝘨𝘦*", "𝐎𝐰𝐎 *𝘸𝘩𝘢𝘵’𝘴 𝘵𝘩𝘪𝘴*", "๏w๏ *𝘯𝘰𝘵𝘪𝘤𝘦𝘴 𝘣𝘶𝘭𝘨𝘦*", "( ͡o ꒳ ͡o )*𝔫𝔬𝔱𝔦𝔠𝔢𝔰 𝔟𝔲𝔩𝔤𝔢*", "*𝓌𝒶𝓉𝓈 𝒹𝒾𝓈?*ღ(O꒳Oღ)", "*𝓃𝓊𝓏𝓏𝓁𝑒𝓈 𝓎𝑜𝓊*(。O⁄ ⁄ω⁄ ⁄ O。)", "(𝐎𝐰𝐎)<𝕣𝕒𝕨𝕣𝕣𝕣)~", "‿︵*𝓇𝒶𝓌𝓇*‿︵ ʘwʘ", "✼ ҉ (O꒳O) ҉ ✼", "✼ ҉♡ (。O⁄ ⁄ω⁄ ⁄ O。) ҉♡ ✼", "✧･ﾟ: *✧･ﾟ:*(OwO )*:･ﾟ✧*:･ﾟ✧‏"]

#Dictionary to store match patterns
pattern = {
    "n_vowel" : r"([nN])([aeiouAEIOU])",
    "rl_w" : r"([RrLl])",
    "ove" : r"([Oo][Vv][Ee])",
    "punctuation" : r"([!?\.])"
}

#Dictionary to store replacement strings
replace = {
    "n_vowel" : "\\1y\\2",
    "rl_w" : "w",
    "ove" : "uv",
    "punctuation" : f"\\1{choice(owo_faces)}"
}

def owoify(str_input):
    processed = re.sub(pattern["n_vowel"], replace["n_vowel"], str_input)
    processed = re.sub(pattern["rl_w"], replace["rl_w"], processed)
    processed = re.sub(pattern["rl_w"], replace["rl_w"], processed)
    owo = choice(owo_faces)
    processed = re.sub(pattern["punctuation"], replace["punctuation"] , processed)
    return processed
    