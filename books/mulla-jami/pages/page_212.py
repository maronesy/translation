# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 212 (printed ٢١١)."""

PAGE_NUMBER = 212
PRINTED_PAGE = "٢١١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وقالوا) بناء على قاعدة تجويز اجتماع حرف النداء مع اللام، وهي اجتماع الأمرين:",
     "en": "(And they said), on the basis of the rule permitting the vocative particle to combine with the lām, which is the combination of two things:"},
    {"type": "matn",
     "ar": "أحدهما: كون اللام عوضا عن محذوف.",
     "en": "the first: the lām being a substitute for something elided;"},
    {"type": "matn",
     "ar": "وثانيهما: لزومها للكلمة (يا الله)؛",
     "en": "the second: its being inseparable from the word—(“yā Allāh,” O Allah);"},
    {"type": "matn",
     "ar": "لأن أصله «إله»، حذفت الهمزة، وعوضت اللام عنها[[١]] وأدغمت، ولزمت الكلمة،",
     "en": "because its origin is “ilāh”: the hamza was elided, the lām was substituted for it and assimilated, and it became inseparable from the word,"},
    {"type": "matn",
     "ar": "فلا يقال في سعة الكلام «لاة»[[٢]]،",
     "en": "so “lāh” is not said in ordinary unconstrained speech."},
    {"type": "matn",
     "ar": "ولما لم يجتمع هذان الأمران في موضع آخر اختص هذا الاسم بذلك الجواز، ولهذا قال: (خاصة[[٣]]).",
     "en": "Since these two things do not combine anywhere else, this name is singled out for that permission; hence he said: (exclusively)."},
    {"type": "matn",
     "ar": "وأما مثال: «النجم والصعق» وإن كانت اللام لازمة في مثلهما، لكن ليست عوضا عن محذوف.",
     "en": "As for examples such as “al-Najm” and “al-Ṣaʿiq,” although the lām is inseparable in their like, it is not a substitute for something elided."},
    # REVIEW: print reads «لازمة للكملة»; evidently «للكلمة»; transcribed as printed.
    {"type": "matn",
     "ar": "وأما «الناس» وإن كانت اللام فيه عوضا عن الهمزة؛ لأن أصله «الأناس» لكن ليست لازمة للكملة؛ لأنه يقال: «ناس» في سعة الكلام،",
     "en": "As for “al-nās” (the people), although the lām in it is a substitute for the hamza—its origin being “al-unās”—it is not inseparable from the word, since “nās” is said in unconstrained speech."},
    {"type": "matn",
     "ar": "فلا يجوز أن يقال: «يا النجم، ويا الناس»،",
     "en": "So one may not say “yā al-Najm” or “yā al-nās.”"},
    {"type": "matn",
     "ar": "ولعدم جريان هذه القاعدة في «التي» في قولهم:",
     "en": "And because this rule does not apply to “allatī” in their saying:"},
    {"type": "verse",
     "ar": "من أجلك يا التي تيمت قلبي          وأنت بخيلة بالوصل عني",
     "en": "For your sake, O you who have enslaved my heart, / while you are miserly with union toward me,"},
    {"type": "matn",
     "ar": "لأن لامها ليست عوضا عن محذوف، وإن كانت لازمة للكلمة حكموا عليه بالشذوذ،",
     "en": "since its lām is not a substitute for something elided, even though it is inseparable from the word, they judged it irregular (shādhdh);"},
    {"type": "matn",
     "ar": "وفي «الغلامان» في قولهم:",
     "en": "and in the case of “al-ghulāmān” in their saying:"},
    {"type": "verse",
     "ar": "فيا الغلامان اللذان فرا          ..................",
     "en": "So O you two lads who fled … (the second hemistich is not given)"},
    # REVIEW: matn prints «أشذ» (dhāl), while fn ٤ comments on the form «أشد» (dāl); transcribed as printed.
    {"type": "matn",
     "ar": "لانتفاء الأمرين كليهما حكموا بأنه أشذ شذوذا[[٤]].",
     "en": "since both things are absent, they judged it more irregular still."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولهذا لا يجمع بينهما إلا قليلا.",
     "en": "For this reason the two are combined only rarely."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قد يقال في غيرها نحو قوله: يسمعها لاهه الكبار بضم الكاف أي: الكبير.",
     "en": "It is sometimes said outside it, as in the poet’s words “yusmiʿuhā lāhuhu al-kubāru,” with ḍamma on the kāf, that is: “the Great.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا إشارة إلى ثلاثة أحكام للفظ \"الله\" في باب النداء:",
     "en": "This points to three rules of the word “Allāh” in the chapter of vocation:"},
    # REVIEW: print reads «بكملة يا»; evidently «بكلمة يا»; transcribed as printed.
    {"type": "pair",
     "ar": "قطع همزته واختصاص ندائه بكملة يا من بين حروف النداء كاختصاص نداء أيها وأيتها ذكره في مغني اللبيب، ونداؤه بلا توسط المبهم،",
     "en": "the disjunction of its hamza; the restriction of its vocation to the word “yā” among the vocative particles—like the restriction of the vocation of “ayyuhā” and “ayyatuhā”—mentioned in Mughnī al-labīb; and its vocation without the interposition of the vague noun."},
    {"type": "pair",
     "ar": "وتخصيصه بالحكم الأخير، وإن كان أشد تناسبا بالمقام، فمن ضيق الفطن الذي لا يليق بالكرام.",
     "en": "Restricting it to the last rule, though that is most suited to the context, comes from a narrowness of discernment unbefitting the noble."},
    {"type": "pair",
     "ar": "ولك أن تجعل معنى قوله: «خاصة» أنك تقول: يا الله خاصة من غير أن تقول: يا أيها الله مثلا في حين.",
     "en": "You may take the meaning of his word “exclusively” to be that you say “yā Allāh” only, without ever saying, for example, “yā ayyuhā Allāh.”"},
    {"type": "pair",
     "ar": "ومن خصائص هذا اللفظ أنه يحذف منه حرف النداء، ويعوض عنه الميم المشددة في آخره، فيجب حذفه، وهو مختص بالدعاء.",
     "en": "Among the peculiarities of this word is that the vocative particle is elided from it and the doubled mīm at its end is substituted for it, so its elision is then obligatory; and this is restricted to supplication (duʿāʾ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر أشذ، كأنهم توسلوا في التفضيل بصيغة «أشد»، ولم يبنوا من الشذوذ لجعل الشذوذ بمنزلة العيب.",
     "en": "The obvious [form] would be “ashadhdh”; it is as if they resorted, for the comparative, to the form “ashadd” and did not form it from shudhūdh, so as to treat irregularity as a defect."},
]
