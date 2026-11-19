# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 553 (printed ٥٥٢)."""

PAGE_NUMBER = 553
PRINTED_PAGE = "٥٥٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(ويختص) أي: الكاف (بالظاهر) أي: بالاسم الظاهر عند الجمهور، فلا يقال: «كه» استغناء عنه بمثل ونحوه.",
     "en": "(And it is restricted), that is, the kāf, (to the explicit [noun]), that is, to the explicit noun, according to the majority; so one does not say “kahu” (like him), since “mithl” and the like make it unnecessary."},
    {"type": "matn",
     "ar": "وقد يدخل في السعة على المرفوع نحو: «ما أنا كأنت»، (خلافا للمبرد)، فإنه أجاز ذلك مطلقا، نظرا إلى ما جاء في بعض أشعارهم.",
     "en": "It sometimes enters, in free usage (saʿa), upon the nominative [pronoun], as in “mā anā ka-anta” (I am not like you); (contrary to al-Mubarrad), for he permitted that without restriction, in view of what occurs in some of their poetry."},

    {"type": "section", "ar": "[مذ ومنذ]",
     "en": "Mudh and Mundhu"},

    {"type": "matn",
     "ar": "(ومذ ومنذ):",
     "en": "(And mudh and mundhu [are]):"},
    {"type": "matn",
     "ar": "١-(للزمان) الماضي أو الحاضر، فهما (للابتداء في) الزمان (الماضي)",
     "en": "1. (for time), past or present; thus they are (for the beginning in) (past) time;"},
    {"type": "matn",
     "ar": "يعني: إذا أريد بهما الزمان الماضي، فالمراد أن مبدأ زمان الفعل المثبت أو المنفي هو ذلك الزمان الماضي الذي أريد بهما لا جميعه،",
     "en": "that is, when past time is meant by them, what is meant is that the beginning of the time of the affirmed or negated verb is that past time which is meant by them, not the whole of it;"},
    # REVIEW: «كا إذا قلت» printed thus; presumably «كما إذا قلت». Transcribed as printed.
    {"type": "matn",
     "ar": "كا إذا قلت: «سافرت من البلد مذ سنة كذا، أو ما رأيت فلانا مذ سنة كذا»، بشرط أن يكون هذه السنة ماضية، لا تكون أنت فيها،",
     "en": "as when you say “I travelled from the town since such-and-such a year” or “I have not seen so-and-so since such-and-such a year”, on condition that this year is past and you are not in it;"},
    {"type": "matn",
     "ar": "فإن معناه حينئذ: أن مبتدأ مسافرتي، أو عدم رؤيتي كان هذه السنة وامتد إلى الآن.",
     "en": "for its meaning then is that the beginning of my travelling, or of my not seeing, was that year, and it has extended until now."},
    {"type": "matn",
     "ar": "٢-(والظرفية) عطف على الابتداء أي: وهما للظرفية المحضة من غير[[١]] اعتبار معنى الابتداء (في) الزمان (الحاضر)",
     "en": "2. (and for adverbial containment (ẓarfiyya)) — coordinated with “beginning” — that is, they are for pure containment, without regard to the sense of beginning, (in present) time,"},
    {"type": "matn",
     "ar": "أي: الذي اعتبرته حاضرا وإن مضى بعضه،",
     "en": "that is, [time] that you regard as present even if part of it has passed;"},
    {"type": "matn",
     "ar": "يعني: إذا أريد بهما الزمان الذي اعتبر حاضرا، فالمراد أن جميع زمان الفعل هو ذلك الزمان الحاضر،",
     "en": "that is, when the time regarded as present is meant by them, what is meant is that the whole time of the verb is that present time,"},
    {"type": "matn",
     "ar": "(نحو: «ما رأيته مذ شهرنا، ومنذ يومنا») أي: جميع زمان انتفاء رؤيتنا هو هذا الشهر أو اليوم الحاضر عندنا؛",
     "en": "(as in “I have not seen him mudh this month of ours” and “mundhu this day of ours”), that is, the whole time of our not seeing [him] is this month or the day that is present to us,"},
    {"type": "matn",
     "ar": "لأنهما لم ينقضيا بعد، ولم يمتد زمان الفعل إلى ما ورائهما، فكيف يصح اعتبارهما مبدأ لزمان الفعل؟",
     "en": "because the two have not yet ended, and the time of the verb has not extended beyond them; so how could it be sound to regard them as the beginning of the time of the verb?"},
    {"type": "matn",
     "ar": "فالمثالان المذكوران كلاهما للظرفية،",
     "en": "So the two examples mentioned are both for containment."},
    {"type": "matn",
     "ar": "ويمكن أن يجعل الأول مثالا للابتداء، كما يتوهم بحسب الظاهر، لكن بتقدير مضاف، أي: «ما رأيته مذ دخول شهرنا».",
     "en": "The first may be made an example of beginning, as is imagined from the apparent sense, but by supposing an elided first term of annexation, that is, “I have not seen him since the start of this month of ours”."},

    {"type": "section", "ar": "[وحاشا وعدا وخلا]",
     "en": "Ḥāshā, ʿAdā and Khalā"},

    {"type": "matn",
     "ar": "(وحاشا، وعدا، وخلا: للاستثناء) أي: لاستثناء ما بعدها عما قبلها،",
     "en": "(And ḥāshā, ʿadā and khalā are for exception (istithnāʾ)), that is, for excepting what follows them from what precedes them."},
    {"type": "matn",
     "ar": "فإذا جررت بها ما بعدها تكون حروفا جارة، وبهذا الاعتبار ذكرت ههنا،",
     "en": "If you put what follows them in the genitive by them, they are prepositions, and in this respect they are mentioned here,"},
    {"type": "matn",
     "ar": "نحو: «جاءني القوم حاشا زيد، وعدا زيد، وخلا زيد».",
     "en": "as in “the people came to me, except Zayd” (ḥāshā Zaydin, ʿadā Zaydin, khalā Zaydin)."},
    {"type": "matn",
     "ar": "وإذا نصبت تكون أفعالا.",
     "en": "If you put it in the accusative, they are verbs."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "تفسير للمختصة، وإشارة إلى أنه إذا اعتبر معنى الابتداء، ففيه معنى الظرفية أيضا ضرورة وقوع الفعل في مدخوله.",
     "en": "An explanation of “pure”, and an indication that when the sense of beginning is regarded, the sense of containment is also in it, necessarily, since the verb occurs within what it governs."},
    # REVIEW: «تفسير للمختصة» printed thus; the matn word is «المحضة». Transcribed as printed.
]
