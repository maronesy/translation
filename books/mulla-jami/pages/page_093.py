# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 93 (printed ٩٢)."""

PAGE_NUMBER = 93
PRINTED_PAGE = "٩٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "وقع في الصورة فقط، فلا ينتقض بما حذف عنه بعض الحروف كالأسماء المحذوفة الأعجاز[[١]]، مثل: «يد ودم»، فإن المادة ليست باقية فيهما،",
     "en": "occurs in the form only; so it is not invalidated by that from which some letters have been elided, such as nouns whose final portions are elided, like “yad” (hand) and “dam” (blood), for the [full] material substance no longer remains in them;"},
    {"type": "matn",
     "ar": "وأن خروجه عن صيغته الأصلية يستلزم دخوله في صيغة أخرى، أي: مغايرة للأولى.",
     "en": "and that its departure from its original form entails its entry into another form — that is, one differing from the first."},
    {"type": "matn",
     "ar": "ولا يبعد أن يعتبر مغايرتها لها في كونها غير داخلة تحت أصل وقاعدة، كما كانت الأولى داخلة تحته، فخرجت عنه المغيرات القياسية[[٢]].",
     "en": "It is not far-fetched that its differing from it be regarded [as consisting] in its not falling under a principle and a rule, as the first did fall under it; thereby the analogical modifiers (al-mughayyirāt al-qiyāsiyya) are excluded from it."},
    {"type": "matn",
     "ar": "وأما المغيرات الشاذة[[٣]] فلا نسلم أنها مخرجة عن الصيغة الأصلية، فإن الظاهر أن مثل: «أقوس» و«أنيب» من الجموع الشاذة ليست مخرجة عما هو القياس فيهما، أعني: «أقواسا» و«أنيابا»،",
     "en": "As for the anomalous modifiers (al-mughayyirāt al-shādhdha), we do not concede that they take [a word] out of the original form; for the apparent case is that such [forms] as “aqwus” and “anyub” among the anomalous plurals are not taken out of what is the analogical [plural] in them — I mean “aqwās” and “anyāb” —"},
    {"type": "matn",
     "ar": "بل إنما جمع «القوس» و«الناب» ابتداء على «أقوس» و«أنيب»[[٤]] على خلاف القياس من غير أن يعتبر جمعهما أولا على «أقواس» و«أنياب» وإخراج «أقوس» و«أنيب» عنهما.",
     "en": "rather, “al-qaws” (bow) and “al-nāb” (canine tooth) are pluralized at the outset as “aqwus” and “anyub,” contrary to analogy, without their being first pluralized as “aqwās” and “anyāb” and then “aqwus” and “anyub” being derived out of these two."},
    {"type": "matn",
     "ar": "وقال بعض الشارحين: قد جوز بعضهم تعريف الشيء بما هو أعم منه إذا كان المقصود منه تمييزه عن بعض ما عداه،",
     "en": "One of the commentators said: Some have permitted defining a thing by what is more general than it when the intent behind [the definition] is to distinguish it from some of what lies outside it,"},
    {"type": "matn",
     "ar": "فيمكن أن يقال: المقصود ههنا تمييز العدل عن سائر العلل، لا عن كل ما عداه، فحيث[[٥]] حصل بتعريفه هذا التمييز لا بأس بكونه أعم",
     "en": "so it may be said: the intent here is to distinguish deviation (al-ʿadl) from the remaining causes [of inflectional impediment], not from everything besides it; hence, since this distinguishing is achieved by his definition, there is no harm in its being more general"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وكذا المحذوفة الأوائل مثل عدة، والمحذوفة الأواسط كمقول في وجه.",
     "en": "Likewise those whose initial [letters] are elided, such as “ʿida,” and those whose middle [letters] are elided, such as “maqūl” in one respect."},
    {"type": "pair",
     "ar": "ولا يبعد أن يقال: خرج عنه كل ما غير بإبدال حرف أصلي إلى حرف آخر كالمقام والإيلاء، فإن المادة ليست باقية فيها،",
     "en": "It is not far-fetched to say: excluded from it is everything altered by the substitution of an original letter for another, such as “al-maqām” and “al-īlāʾ,” for the [original] material substance no longer remains in them,"},
    {"type": "pair",
     "ar": "فلم يبق من المغيرات القياسية إلا المدغمات، فهي الخارجة باعتبار قيد المغايرة لا غير.",
     "en": "so that there remain of the analogical modifiers only the assimilated [forms] (al-mudghamāt); these are what are excluded by consideration of the restriction of differing, nothing else."},
    {"type": "pair",
     "ar": "هكذا ينبغي أن يحقق هذا المقام، فما قيل في بيان قوله: فخرجت عنه المغيرات القياسية كالمقام فبعيد عن المقام.",
     "en": "Thus should this point be investigated; and what has been said in explaining his statement “thereby the analogical modifiers are excluded from it” — such as “al-maqām” — is remote from the point at issue."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "كالمقام قيل: لم تدخل في الخروج؛ لأنها مخرجة لا خارجة، وفي دخول المعدولات حينئذ، تأمل.",
     "en": "Regarding [forms] like “al-maqām” it is said: it does not enter into the [category of] exclusion, because it is [something] taken out, not [something] going out [of itself]; and as to the entry of the deviated forms (al-maʿdūlāt) in that case — ponder it well."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كالجموع والمصغرات والمنسوبات الشاذة.",
     "en": "Such as the anomalous plurals, diminutives, and relative-adjective forms (al-mansūbāt)."},
    {"type": "pair",
     "ar": "وأما القلب كأيس في يئس فقيل: إنه ليس خارجا عن صورته؛ إذ لا مدخل لتقديم بعض الحروف على بعض في الوزن، فإنه أمر اعتباري.",
     "en": "As for metathesis (al-qalb), like “ayisa” for “yaʾisa,” it is said: it does not depart from its form, since the advancing of some letters over others has no bearing on the metrical pattern (al-wazn), for that is a purely notional matter."},
    {"type": "pair",
     "ar": "وأما نحو فخذ وعنق بسكون العين فقيل: إنه لم يخرج خروجا تاما؛ إذ يستعمل على الصيغة الأصلية أكثر من استعماله على الصيغة الفرعية.",
     "en": "As for such [forms] as “fakhdh” and “ʿunuq” with a quiescent middle radical, it is said: it does not depart completely, since it is used on the original form more than it is used on the derived form."},
    {"type": "pair",
     "ar": "واللفظ إذا أطلق انصرف إلى الكامل. ولا يخفى أن الاحتياج إلى هذا العذر على تقدير كون تغيره غير قياسي.",
     "en": "And a word, when used absolutely, directs itself to the complete [form]. It is not hidden that the need for this excuse is on the supposition that its alteration is non-analogical."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولهذا يضافان إليهما، فيقال: جمعهما ولو كانا مخرجين عن أقواس وأنياب لنسبا إليهما.",
     "en": "For this reason the two are ascribed to those two, so one says: they are the plural of the two; had they been derived out of “aqwās” and “anyāb,” they would have been attributed to those two [instead]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "كلمة «حيث» مكاني أو تعليلي.",
     "en": "The word “ḥaythu” [here] is [either] locative or causal."},
    {"type": "pair",
     "ar": "ويفهم من كلامه أن هذا التوجيه مرضي له مع أن الظاهر أن المقصود في هذا المقام تمييز غير المنصرف عن المنصرف لا مجرد تمييز بعض العلل عن بعض.",
     "en": "It is understood from his words that this orientation is acceptable to him, even though the apparent case is that the intent in this context is to distinguish the diptote (ghayr al-munṣarif) from the triptote (al-munṣarif), not merely to distinguish some of the causes from others."},
    {"type": "pair",
     "ar": "ولا شك أن هذا التعريف للعدل لا يتميز به غير المنصرف من المنصرف، فإنه إذا سمي بالجموع الشاذة مثلا شخص لم يعلم أنها منصرف أو غير منصرف،",
     "en": "There is no doubt that by this definition of deviation the diptote is not distinguished from the triptote; for if, say, a person is named with an anomalous plural, it is not known whether it is triptote or diptote,"},
    {"type": "pair",
     "ar": "بل يتوهم أنها غير منصرف لتحقق العلمية والعدل بهذا التعريف الأعم منها.",
     "en": "rather it is imagined to be diptote on account of the realization of proper-name status (al-ʿalamiyya) and of deviation by this definition, which is more general than it."},
]
