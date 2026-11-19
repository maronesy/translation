# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 542 (printed ٥٤١)."""

PAGE_NUMBER = 542
PRINTED_PAGE = "٥٤١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: «وقد كان بعض» at the foot of PDF p. 541 (mid-sentence).
    {"type": "matn",
     "ar": "مطر، أو شيء من مطر»، أو هو وارد على الحكاية[[١]]، كأن قائلا قال: «هل كان من مطر؟»",
     "en": "…rain” or “something of rain”; or it occurs by way of quotation (ḥikāya), as though someone had said “hal kāna min maṭarin?” (has there been any rain?),"},
    {"type": "matn",
     "ar": "فأجاب: بأنه «قد كان من مطر».",
     "en": "and he answered that “qad kāna min maṭarin” (there has been rain)."},

    {"type": "section", "ar": "[إلى]",
     "en": "Ilā"},

    {"type": "matn",
     "ar": "١-(وإلى للانتهاء) أي: لانتهاء الغاية. فهي بهذا المعنى مقابلة لـ«من»[[٢]]",
     "en": "1. (And ilā is for termination), that is, for the termination of the extent (intihāʾ al-ghāya); in this sense it is the counterpart of “min”,"},
    {"type": "matn",
     "ar": "سواء كان في المكان، نحو: «خرجت إلى السوق» أو الزمان، نحو: ﴿أتموا الصيام إلى الليل﴾[[٣]]،",
     "en": "whether in place, as in “I went out to the market”, or in time, as in “Complete the fast until the night”,"},
    {"type": "matn",
     "ar": "أو غيرهما نحو: «قلبي إليك»؛ فإن قلب المخاطب[[٤]] منته إليه، باعتبار الشوق والميل.",
     "en": "or in something else, as in “qalbī ilayka” (my heart is towards you), for the heart of the addressee terminates at him, in respect of longing and inclination."},
    {"type": "matn",
     "ar": "٢-(وبمعنى مع قليلا) كقوله تعالى: ﴿ولا تأكلوا أموالهم إلى أموالكم﴾[[٥]]، أي: مع أموالكم.",
     "en": "2. (And in the sense of “maʿa” (with), rarely), as in His words, the Exalted: “and do not devour their property together with (ilā) your property”, that is, with your property."},

    {"type": "section", "ar": "[حتى]",
     "en": "Ḥattā"},

    {"type": "matn",
     "ar": "١-(وحتى كذلك) أي: مثل «إلى» في كونها لانتهاء الغاية.",
     "en": "1. (And ḥattā is likewise), that is, like “ilā” in being for the termination of the extent;"},
    {"type": "matn",
     "ar": "٢-(وبمعنى «مع» كثيرا) ولم يكتف في كونها بمعنى «مع» تشبيهها بـ«إلى» كما اكتفى في كونها لانتهاء الغاية به للتفاوت الواقع بينهما بالقلة والكثرة.",
     "en": "2. (and in the sense of “maʿa”, frequently). For its being in the sense of “maʿa” he was not content with likening it to “ilā”, as he was content with that for its being for the termination of the extent, because of the difference between the two in rarity and frequency."},
    {"type": "matn",
     "ar": "(وتختص) أي: «حتى»[[٦]] (بالظاهر) أي: بالاسم الظاهر، فلا يقال: «حتاه» كما",
     "en": "(And it is restricted), that is, “ḥattā”, (to the explicit [noun]), that is, to the explicit noun, so one does not say “ḥattāhu”, as…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فالمراد بكونه في كلام غير موجب: كونه فيه في الحال أو في الأصل.",
     "en": "So what is meant by its being in non-affirmative speech is its being in it either actually or originally."},
    {"type": "pair",
     "ar": "لما تقرر من أن المحكي يبقى على حاله.",
     "en": "This is because it is established that what is quoted remains in its [original] state."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في الجملة، فإن «من»:",
     "en": "That is, in general; for “min” is"},
    {"type": "pair",
     "ar": "إما للابتداء من المكان.",
     "en": "either for beginning from a place,"},
    {"type": "pair",
     "ar": "أو للابتداء من الزمان.",
     "en": "or for beginning from a time;"},
    {"type": "pair",
     "ar": "وإلى قد يكون للانتهاء في غيرهما.",
     "en": "whereas “ilā” is sometimes for termination in something other than these two."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة البقرة: ١٨٧.",
     "en": "Qurʾān, Sūrat al-Baqara 2:187."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر فإن قلب المتكلم منتهي إليه،",
     "en": "The obvious reading is “for the heart of the speaker terminates at him”;"},
    {"type": "pair",
     "ar": "وغاية التكلف أن يقرأ المخاطب على صيغة اسم الفاعل، وضمير الغيبة قائم مقام الخطاب.",
     "en": "and the utmost of strained interpretation is to read “al-mukhāṭib” in the form of the active participle (the one addressing), with the third-person pronoun standing in place of the second person."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة النساء: ٢.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:2."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: الجارة. أما إذا كانت عاطفة جاز دخولها على المضمر،",
     "en": "That is, the one that governs the genitive. When it is coordinating, it may enter upon a pronoun,"},
    {"type": "pair",
     "ar": "نحو: «جاءني القوم حتى أنت»، و«رأيت القوم حتى إياك»، و«مررت بالقوم حتى بك».",
     "en": "as in “the people came to me, even you”, “I saw the people, even you”, and “I passed by the people, even by you”."},
]
