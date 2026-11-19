# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 57 (printed ٥٦)."""

PAGE_NUMBER = 57
PRINTED_PAGE = "٥٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "فبالصفة الأولى خرج الحرف عن حد الاسم، وبالثانية الفعل.",
     "en": "So by the first attribute the ḥarf (particle) is excluded from the definition of the ism, and by the second [attribute] the fiʿl (verb) [is excluded]."},
    {"type": "matn",
     "ar": "والمراد بعدم الاقتران[[١]]: أن يكون بحسب الوضع الأول.",
     "en": "What is meant by “non-conjunction” is that it be so with respect to the original coinage (al-waḍʿ al-awwal)."},
    {"type": "matn",
     "ar": "فدخل فيه[[٢]] أسماء الأفعال؛ لأن جميعها:",
     "en": "Hence the verbal nouns [functioning as verbs] (asmāʾ al-afʿāl) are included in it, because all of them are:"},
    {"type": "matn",
     "ar": "١- إما منقولة عن المصادر[[٣]] الأصلية، سواء كان النقل فيه صريحا[[٤]]، نحو: «رويد[[٥]]»، فإنه قد يستعمل مصدرا[[٦]] أيضا، أو غير صريح، نحو: «هيهات»، فإنه وإن لم يستعمل مصدرا، إلا أنه على وزن «قوقاة» مصدر «قوقى».",
     "en": "1. either transferred from the original verbal nouns (al-maṣādir) — whether the transfer therein is explicit (ṣarīḥ), as in “ruwayd” (for it is at times also used as a verbal noun), or non-explicit, as in “hayhāt” (for, even though it is not [actually] used as a verbal noun, it is nonetheless on the pattern of “qawqāt,” the verbal noun of “qawqā”);"},
    {"type": "matn",
     "ar": "٢- أو عن المصادر التي كانت في الأصل أصواتا، نحو: «صه».",
     "en": "2. or [transferred] from verbal nouns that were originally [mere] sounds, as in “ṣah” (hush);"},
    {"type": "matn",
     "ar": "٣- أو عن الظرف.",
     "en": "3. or from the adverb (al-ẓarf);"},
    {"type": "matn",
     "ar": "٤- أو عن الجار والمجرور، نحو: «أمامك زيدا»[[٧]]، و«عليك زيدا»[[٨]]، فليس لشيء منها الدلالة على أحد الأزمنة الثلاثة، بحسب الوضع الأول.",
     "en": "4. or from the preposition-and-genitive [phrase] (al-jārr wa-l-majrūr), as in “amāmaka Zaydan” (before you, [take] Zayd) and “ʿalayka Zaydan” (keep to Zayd); so none of them has any signification of one of the three times, with respect to the original coinage."},
    {"type": "matn",
     "ar": "وخرج عنه[[٩]] الأفعال المنسلخة عن الزمان[[١٠]]، نحو: «عسى وكاد» لاقتران معناهما به[[١١]] بحسب أصل الوضع.",
     "en": "And there are excluded from it the verbs stripped of tense (al-afʿāl al-munsalikha ʿan al-zamān), such as “ʿasā” and “kāda,” because their meaning is conjoined with it [i.e., time] according to the original coinage."},
    {"type": "matn",
     "ar": "وخرج عنه[[١٢]] المضارع[[١٣]] أيضا، فإنه على تقدير اشتراكه[[١٤]]…",
     "en": "And there is likewise excluded from it the imperfect verb (al-muḍāriʿ) as well, for it — on the supposition of its sharing…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: المراد بعدم اقتران المعنى المستقل أن يكون ذلك العدم بحسب الوضع.",
     "en": "That is: what is meant by the non-conjunction of the independent meaning [with time] is that this absence be with respect to the coinage (al-waḍʿ)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في حد الاسم.",
     "en": "That is: in the definition of the ism (noun)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن جميعها لا يخلو من أن يكون بعضها منقولة عن المصادر، وبعضها منقولة عن الظرف والجار والمجرور، فيكون من قبيل تقسيم الكل إلى الأجزاء. وقوله: «منقولة عن المصادر» معناه: أن الكل في الأصل مصادر موضوعة لمعنى مصدري نقل إلى معنى الفعل، وهذا المعنى متبادر من تلك العبارة من غير مسامحة.",
     "en": "He means: all of them do not fail to be [such that] some are transferred from verbal nouns and some transferred from the adverb and the preposition-and-genitive; so it is of the type of dividing a whole into its parts. And his words “transferred from the verbal nouns” mean that all of them are in origin verbal nouns coined for a verbal-noun meaning, [then] transferred to the meaning of the verb; and this meaning is what comes readily to mind from that expression without any laxity."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بأن يثبت استعماله في المعنى المصدري أولا، ثم ينقل.",
     "en": "By its being established that it is first used in the verbal-noun sense, and is then transferred."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: رويد.",
     "en": "That is: ruwayd (go gently)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: قليلا.",
     "en": "That is: [in the sense of] “a little” (qalīlan)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: تقدم.",
     "en": "That is: advance / go forward (taqaddam)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: الزم.",
     "en": "That is: hold fast / keep to (ilzam)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: عن حد الاسم.",
     "en": "That is: from the definition of the ism (noun)."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "معنى الأفعال المنسلخة عن الزمان.",
     "en": "[That is:] the meaning of “the verbs stripped of tense.”"},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: بالزمان.",
     "en": "That is: with time (bi-l-zamān)."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: عن حد الاسم الفعل.",
     "en": "That is: from the definition of the ism (noun) — [namely] the verb (al-fiʿl)."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أي: المضارع.",
     "en": "That is: the imperfect verb (al-muḍāriʿ)."},

    # ---------------- Footnote 14 ----------------
    {"type": "note", "num": "١٤"},
    {"type": "pair",
     "ar": "وهو الراجح على ما قيل من أنه للحال حقيقة، وللاستقبال مجازا أو بالعكس.",
     "en": "And this is the preponderant [view], as against what has been said — that it is [used] for the present in reality (ḥaqīqatan) and for the future figuratively (majāzan), or vice versa."},
]
