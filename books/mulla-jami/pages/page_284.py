# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 284 (printed ٢٨٣)."""

PAGE_NUMBER = 284
PRINTED_PAGE = "٢٨٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ليس إلا بظهور قرينة دالة على بعض» from the foot of PDF p. 283.
    {"type": "matn",
     "ar": "معين من المستثنى منه مقطوع دخوله فيه في الأول وعدم ظهورها في الثاني،",
     "en": "…specific part of the mustathnā minhu in which its inclusion is certain, in the first, and the absence of such [an indication] in the second."},
    {"type": "matn",
     "ar": "فلو قام في الثاني أيضا قرينة ظاهرة الدلالة على بعض معين كما إذا قيل: «من ضربك من القوم؟» أي: القوم الداخل فيهم زيد فقلت: «ضربني إلا زيد»، فالظاهر أن ذلك أيضا مما يستقيم فيه المعنى،",
     "en": "So if in the second too there were an indication clearly pointing to a specific part—as when it is asked “Who of the people struck you?”, that is, the people among whom Zayd is included, and you say “There struck me except Zayd”—then it appears that this too is a case in which the meaning holds;"},
    {"type": "matn",
     "ar": "لكن الغالب عدم وجدان قرينة كذلك في الموجب، فالغالب فيه عدم استقامة المعنى.",
     "en": "but what predominates is that no such indication is found in affirmative speech, so what predominates in it is that the meaning does not hold."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل أن المفرغ لا يكون في الموجب إلا أن يستقيم المعنى (لم يجز) مثل: («ما زال زيد إلا عالما»)؛",
     "en": "(Hence), that is, because the emptied [exception] does not occur in affirmative speech unless the meaning holds, (it is not permitted [to say]) such as (“Zayd did not cease [to be anything] except learned”);"},
    {"type": "matn",
     "ar": "إذ معنى «ما زال»: ثبت[[١]]؛ لأن نفي النفي إثبات[[٢]]، فيكون المعنى: «ثبت زيد دائما[[٣]] على جميع الصفات إلا على صفة العلم»، فلا يستقيم المعنى.",
     "en": "since the meaning of “mā zāla” is “he remained,” because the negation of a negation is an affirmation; so the meaning becomes: “Zayd remained always in all attributes except the attribute of knowledge,” and the meaning does not hold."},
    {"type": "matn",
     "ar": "وقال الشارح الرضي: يمكن أن يحمل الصفات على ما يمكن أن يكون زيد عليها مما لا يتناقض، ويستثنى من جملتها العلم،",
     "en": "The commentator al-Raḍī said: “the attributes” may be taken to mean those, among non-contradictory [attributes], that Zayd can possibly have, with knowledge excepted from their totality;"},
    {"type": "matn",
     "ar": "أو يحمل ذلك على المبالغة في نفي صفة العلم[[٤]] كأنك قلت: أمكن أن يحصل فيه جميع الصفات إلا صفة العلم، وعلى التقديرين يندرج في صورة الاستقامة.",
     "en": "or that may be taken as hyperbole in denying the attribute of knowledge, as if you said: all attributes could be found in him except the attribute of knowledge. On either supposition it falls under the case where [the meaning] holds."},
    {"type": "matn",
     "ar": "ولا يخفى على الفطن أنه يمكن بمثل هذه التأويلات إرجاع جميع المواد الإيجابية عند الاستثناء إلى صورة الاستقامة،",
     "en": "It is not hidden from the discerning that by such interpretations all affirmative instances of exception could be brought back to the case where [the meaning] holds;"},
    {"type": "matn",
     "ar": "كما يقال مثلا في قولك: «ضربني إلا زيد»: المراد كل من يتصور منه الضرب من معارفك أو المقصود منه المبالغة في غلو المجتمعين على ضربك.",
     "en": "as it might be said, for example, of your saying “There struck me except Zayd”: what is meant is everyone of your acquaintances from whom striking is conceivable; or what is intended is hyperbole about the excess of those who gathered to strike you."},
    {"type": "matn",
     "ar": "(وإذا تعذر[[٥]] البدل) من حيث حمله (على اللفظ) أي: لفظ المستثنى منه (فعلى الموضع) أي: يحمل على موضع المستثنى منه لا على لفظه عملا بالمختار على",
     "en": "(And when the substitute is impossible) as regards construing it (on the wording), that is, the wording of the mustathnā minhu, (then [it is construed] on the position), that is, it is construed on the syntactic position of the mustathnā minhu, not on its wording, acting on the preferred [view] as far as…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأظهر أن يقال: ثبت دائما، لكن الدليل لا يفيد إلا أن يقال: إن نفي النفي يفيد دوام الإثبات، وفي إفادته بحث.",
     "en": "It would be clearer to say “he remained always”; but the proof does not yield this unless it is said that the negation of a negation conveys the permanence of the affirmation, and whether it conveys that is open to discussion."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: مستلزم للإثبات، لا أنه عينه، فإن تصور نفي النفي يتوقف على تصور النفي، وتصور الإثبات لا يتوقف عليه، فهو ليس عينه.",
     "en": "That is, it entails affirmation, not that it is identical with it; for conceiving the negation of a negation depends on conceiving negation, while conceiving affirmation does not depend on it; so it is not identical with it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ليس المعنى الدوام المطلق بل في الماضي مذ قبله.",
     "en": "The meaning is not absolute permanence, but [permanence] in the past, since before it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «وأي:» (with a prefixed wāw) at the start of the footnote; transcribed as printed.
    {"type": "pair",
     "ar": "وأي: مبالغة فوق أن يقال: أمكن فيه جميع الصفات المتقابلة إلا العلم، فجعل العلم أحق بالانتقال من عدة متقابلات.",
     "en": "That is, what hyperbole is greater than saying: all mutually opposed attributes could be in him except knowledge? Thus knowledge is made more deserving of being taken away (intiqāl) than a number of opposed [attributes]."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: print has a question mark after «المختار»; transcribed as printed.
    {"type": "pair",
     "ar": "أي: إذا امتنع البدل المختار؟ فاللام للعهد الخارجي.",
     "en": "That is, when the preferred substitute is impossible; so the definite article denotes external definite reference (al-ʿahd al-khārijī)."},
]
