# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 575 (printed ٥٧٤)."""

PAGE_NUMBER = 575
PRINTED_PAGE = "٥٧٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: غير مستعملة إلا معها، يعني:» at the foot of PDF p. 574.
    {"type": "matn",
     "ar": "إذا عطف شيء على آخر بـ«إما» يلزم أن يصدر المعطوف عليه أولا بـ«إما» ثم عطف عليه المعطوف بـ«إما» نحو: «جاءني إما زيد وإما عمرو»؛",
     "en": "…when one thing is coordinated with another by “immā”, the term coordinated upon must first be headed by “immā”, and then the coordinated term is coordinated with it by “immā”, as in “there came to me either Zayd or ʿAmr”,"},
    {"type": "matn",
     "ar": "ليعلم من أول الأمر أن الكلام مبني على الشك،",
     "en": "so that it is known from the outset that the statement is built on doubt;"},
    {"type": "matn",
     "ar": "(جائزة مع «أو») يعني: إذا عطف شيء على آخر بـ«أو» يجوز أن يصدر[[١]] المعطوف عليه بـ«إما» نحو: «جاءني إما زيد أو عمرو»، لكن لا يجب نحو: «جاءني زيد أو عمرو».",
     "en": "(it is permissible with “aw”), that is, when one thing is coordinated with another by “aw”, the term coordinated upon may be headed by “immā”, as in “there came to me either Zayd or ʿAmr” [with aw], but this is not obligatory, as in “Zayd or ʿAmr came to me”."},
    {"type": "matn",
     "ar": "وذهب بعض النحاة إلى أن «إما» ليست من الحروف العاطفة، وإلا لم تقع قبل المعطوف عليه،",
     "en": "Some grammarians held that “immā” is not one of the coordinating particles; otherwise it would not occur before the term coordinated upon;"},
    {"type": "matn",
     "ar": "وأيضا يدخل عليها الواو العاطفة، فلو كانت هي أيضا للعطف يلزم إيراد عاطفين معا، ويكون أحدهما لغوا.",
     "en": "moreover, the coordinating wāw enters upon it, so if it too were for coordination, two coordinators would be brought together, and one of them would be redundant."},
    {"type": "matn",
     "ar": "والجواب عن الأول: أن «إما» السابقة على المعطوف عليه ليست للعطف، بل للتنبيه على الشك في أول الكلام، كما عرفت.",
     "en": "The answer to the first is that the “immā” preceding the term coordinated upon is not for coordination, but to signal doubt at the beginning of the statement, as you have learned."},
    {"type": "matn",
     "ar": "وعن الثاني: أن الواو الداخلة على «إما» الثانية[[٢]] لعطفها على «إما» الأولى، و«إما» الثانية لعطف ما بعدها على ما بعد «إما» الأولى، فلكل منهما فائدة أخرى، فلا لغو.",
     "en": "And to the second: the wāw entering upon the second “immā” coordinates it with the first “immā”, while the second “immā” coordinates what follows it with what follows the first “immā”; so each of them has a distinct function, and there is no redundancy."},

    {"type": "matn",
     "ar": "(و«لا، وبل، ولكن») هذه الحروف الثلاثة (لأحدهما معينا) أي: لنسبة الحكم إلى أحد من الأمرين المعطوف والمعطوف عليه على التعيين،",
     "en": "(And “lā”, “bal” and “lākin”): these three particles are (for one of the two, specified), that is, for attributing the judgment to one of the two things, the coordinated term and the term coordinated upon, specifically."},
    {"type": "matn",
     "ar": "فكلمة «لا» لنفي الحكم الثابت للمعطوف عليه عن المعطوف، فالحكم ههنا للمعطوف عليه لا للمعطوف[[٣]]،",
     "en": "The word “lā” is for negating of the coordinated term the judgment established for the term coordinated upon; so here the judgment belongs to the term coordinated upon, not to the coordinated term,"},
    {"type": "matn",
     "ar": "نحو: «جاءني زيد لا عمرو» فحكم المجيء فيه لزيد لا لعمرو.",
     "en": "as in “Zayd came to me, not ʿAmr”; the judgment of coming in it belongs to Zayd, not to ʿAmr."},
    {"type": "matn",
     "ar": "وكلمة «بل» بعد الإثبات لصرف الحكم عن المعطوف عليه إلى المعطوف نحو: «جاءني زيد بل عمرو» أي: بل جاءني عمرو،",
     "en": "The word “bal”, after an affirmation, is for diverting the judgment from the term coordinated upon to the coordinated term, as in “Zayd came to me, rather ʿAmr”, that is, rather ʿAmr came to me;"},
    {"type": "matn",
     "ar": "فحكم المجيء فيه للمعطوف دون المعطوف عليه على عكس «لا».",
     "en": "the judgment of coming in it belongs to the coordinated term and not to the term coordinated upon, the reverse of “lā”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فمعنى الكلام أحد الشيئين.",
     "en": "So the sense of the statement is one of the two things."},
    {"type": "pair",
     "ar": "وأما مع أو، فإن تقدم إما فهو كذلك، وإن لم يتقدم جاز أن يعرض للمتكلم الشك أو الإبهام بعد ذلك المعطوف عليه.",
     "en": "As for [coordination] with “aw”: if “immā” precedes, it is likewise; and if it does not precede, it is possible that doubt or vagueness occurs to the speaker after that term coordinated upon."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هذا من مخترعات الشارح أخذه من قول الأندلسي حيث قال: العاطفة كلتاهما، والواو لعطف إحداهما على الأخرى لتجعلهما كحرف واحد يعطف به ما بعد الثانية على ما بعد الأولى.",
     "en": "This is one of the commentator’s own devisings, which he took from the statement of al-Andalusī, where he said: both are coordinating, and the wāw coordinates one of them with the other so as to make them like a single particle by which what follows the second is coordinated with what follows the first."},
    {"type": "pair",
     "ar": "ويتجه على الشارح أنه لما لم يكن إما الأولى للعطف كيف يصح عطف الثانية عليها بحرف الجمع المفيد شركة المعطوف والمعطوف عليه في حكم التركيب،",
     "en": "Against the commentator it may be objected that, since the first “immā” is not for coordination, how can the second be coordinated with it by the particle of conjunction, which conveys the participation of the coordinated term and the term coordinated upon in the syntactic status?"},
    {"type": "pair",
     "ar": "والمشهور أن الواو زائدة لتأكيد العطف، ورفع الالتباس بغير العاطف حتى قيل: إلزامها فيها دون لكن للزومها مصاحبة غير عاطفة بخلاف لكن.",
     "en": "The well-known view is that the wāw is redundant (zāʾida), for emphasizing the coordination and removing confusion with the non-coordinating [immā]; so much so that it was said: it is made obligatory with it, and not with “lākin”, because it [immā] is necessarily accompanied by a non-coordinating [immā], unlike “lākin”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بل للمعطوف نفيا على خلاف لكن العاطفة على المنفي،",
     "en": "Rather, [it is] for the coordinated term negatively, unlike “lākin” coordinating upon a negated [term];"},
    {"type": "pair",
     "ar": "فإن الحكم الثابت لما قبل إلا لا يثبت له بذكر لا حتى يكون لا للمعطوف عليها، بل بذكر لا ينفى عما بعد لا، فيكون لا لما بعدها.",
     "en": "for the judgment established for what precedes “illā” is not established for it by mentioning “lā”, such that “lā” would be for the term coordinated upon; rather, by mentioning “lā” it is negated of what follows “lā”, so “lā” is for what follows it."},
    # REVIEW: printed «لما قبل إلا» (expected perhaps «لما قبل لا») and «للمعطوف عليها»; transcribed as printed.
]
