# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 449 (printed ٤٤٨)."""

PAGE_NUMBER = 449
PRINTED_PAGE = "٤٤٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(مستويا فيه) أي: في» at the foot of PDF p. 448 (mid-sentence).
    {"type": "matn",
     "ar": "هذه الصفة بتأويل الوصف (مع المؤنث مثل: «جريح وصبور») يقال: «رجل جريح وصبور»، و«امرأة جريح وصبور»،",
     "en": "…this adjective, construed as “the qualifier”, (with the feminine, as in “jarīḥ” (wounded) and “ṣabūr” (patient)); one says “a wounded, patient man” and “a wounded, patient woman”."},
    {"type": "matn",
     "ar": "فلا يجمع بالواو والنون، ولا بالألف والتاء، فإنه لما لم يختص بالمذكر ولا بالمؤنث لم يحسن أن يجمع جمعا مخصوصا بأحدهما،",
     "en": "So it is pluralized neither with the wāw and nūn nor with the alif and tāʾ; for since it is not specific to the masculine or to the feminine, it is not fitting to give it a plural specific to one of them;"},
    {"type": "matn",
     "ar": "بل المناسب أن يجمع جمعا يستويان فيه مثل: «جرحى وصبر».",
     "en": "rather, what is fitting is to give it a plural in which both share equally, as in “jarḥā” and “ṣubur”."},
    {"type": "matn",
     "ar": "(و) الشرط الخامس: (ألا يكون) الاسم المذكور مذكرا متلبسا (بتاء التأنيث مثل: «علامة»[[١]]) كراهة اجتماع صيغة جمع المذكر وتاء التأنيث، ولو حذفت التاء لزم اللبس[[٢]].",
     "en": "(And) the fifth condition: (that) the noun mentioned, being masculine, (not be) accompanied (by the tāʾ of the feminine, as in “ʿallāma”) (a very learned man), out of aversion to the coming together of the masculine plural form and the tāʾ of the feminine; and were the tāʾ dropped, ambiguity would follow."},
    {"type": "matn",
     "ar": "(ويحذف نونه) أي: نون الجمع (بالإضافة) لما مر في التثنية",
     "en": "(And its nūn is dropped), that is, the nūn of the plural, (in annexation), for the reason given under the dual."},
    {"type": "matn",
     "ar": "(وقد شذ نحو: «سنين») بكسر السين[[٣]]، جمع «سنة» بفتحها (و«أرضين») بفتح الراء[[٤]]، وقد جاء إسكانها، جمع «أرض» بسكونها،",
     "en": "(Anomalous is the like of “sinīn”), with a kasra on the sīn, the plural of “sana” (year) with a fatḥa on it, (and “araḍīn”), with a fatḥa on the rāʾ (its quiescence also occurs), the plural of “arḍ” (earth) with a quiescent [rāʾ];"},
    {"type": "matn",
     "ar": "وإنما حكم بشذوذهما لانتفاء التذكير والعقل، وعدم كونهما علما أو صفة.",
     "en": "he judged them anomalous only because masculinity and rationality are absent, and they are neither proper names nor adjectives."},
    {"type": "matn",
     "ar": "وقد أدرج صاحب اللباب بعض هذه الأسماء تحت قاعدة كلية أخرجتها من الشذوذ، منها «سنين» وأمثاله، وأبقى بعضها على الشذوذ منها «أرضين» وأمثاله، فمن أراد تفصيل ذلك، فليراجع إليه.",
     "en": "The author of al-Lubāb brought some of these nouns under a universal rule that removed them from anomaly, among them “sinīn” and its like, and left some of them anomalous, among them “araḍīn” and its like. Whoever wants the details of this should consult it."},
    {"type": "matn",
     "ar": "(المؤنث) أي: الجمع الصحيح المؤنث (ما لحق) أي: جمع لحق (آخره) أي: آخر مفرده (ألف وتاء[[٥]]).",
     "en": "(The feminine), that is, the sound feminine plural, (is that at whose end), that is, a plural at the end of whose singular, (an alif and a tāʾ are attached)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «يستوي فيه المذكر المؤنث» without the conjunction «و»; transcribed as printed, translated as «المذكر والمؤنث».
    {"type": "pair",
     "ar": "وما قيل: إن نحو علامة خارج بقوله: ولا مستويا فيه مع المؤنث؛ لأن فعالة يستوي فيه المذكر المؤنث، فليس بشيء؛",
     "en": "What has been said, that the like of “ʿallāma” is excluded by his words “nor shared equally in it with the feminine”, because in “faʿʿāla” the masculine and the feminine share equally, is of no weight;"},
    {"type": "pair",
     "ar": "لأنه ليس مذكرا مستويا مع المؤنث، بل مؤنثا مستويا مع المذكر.",
     "en": "for it is not a masculine shared equally with the feminine, but a feminine shared equally with the masculine."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بين جمعه حال التجرد عن التاء وجمعه حال التلبس بها.",
     "en": "Between its plural when free of the tāʾ and its plural when accompanied by it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "تنبيها على أنه ليس بجمع سلامة في الحقيقة. وقد جاء سنون بضمها، وهو قليل.",
     "en": "As a pointer that it is not really a sound plural. “Sunūn”, with a ḍamma on it, also occurs, but rarely."},
    {"type": "pair",
     "ar": "ولمثل هذا التنبيه كسروا عين عشرين.",
     "en": "For a pointer of the same kind they gave a kasra to the ʿayn of “ʿishrīn” (twenty)."},
    {"type": "pair",
     "ar": "وقد جاء في بعض ما هو مضموم الفاء الكسر، نحو: قلون وثبون وليس بمطرد.",
     "en": "The kasra has occurred in some of what has a ḍamma on the fāʾ [of the singular], as in “qilūn” and “thibūn”, but it is not regular."},
    # REVIEW: printed «ولعل ذلك الاعتدال الكسر»; «لاعتدال» (“because of the balance”) seems intended; transcribed as printed.
    {"type": "pair",
     "ar": "وأما مكسور الفاء، فلم يسمع فيه التغيير كعضين ومئين وفئين. ولعل ذلك الاعتدال الكسر بين الضم والفتح.",
     "en": "As for what has a kasra on the fāʾ, no change is attested in it, as in “ʿiḍīn”, “miʾīn” and “fiʾīn”. Perhaps that is because the kasra is balanced between the ḍamma and the fatḥa."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "للتنبيه على أنه ليس بجمع سلامة حقيقة، ولأن الواو والنون في مقام الألف والتاء كأنه قيل: أرضات.",
     "en": "To point out that it is not really a sound plural; and because the wāw and nūn stand in the place of the alif and tāʾ, as though “araḍāt” had been said."},
    # REVIEW: printed «كجقة» (two dots above the third letter); probably a misprint (e.g. for «جفنة»); transcribed as printed, left untransliterated in the English.
    {"type": "pair",
     "ar": "وكل مؤنث على وزن فعل سواء كانت التاء فيه مقدرة كدعد أو ظاهرة كجقة",
     "en": "Every feminine on the measure “faʿl”, whether the tāʾ in it is implied, as in “Daʿd”, or apparent, as in [the word printed “jqh”],"},
    # REVIEW: printed «كسعة» as the example of an adjective on faʿl; «سعة» is not an obvious adjective of that measure; transcribed as printed.
    {"type": "pair",
     "ar": "إن كانت صفة كسعة أو مضاعفا كمدة، أو معتل العين كجوزة وبيضة وجب إسكان العين في الجمع بالألف والتاء.",
     "en": "if it is an adjective, as in “saʿa”, or doubled, as in “madda”, or has a weak ʿayn, as in “jawza” (walnut) and “bayḍa” (egg), the ʿayn must be quiescent in the plural with the alif and tāʾ."},
    {"type": "pair",
     "ar": "وإن خلا من هذه الأشياء وجب فتح عينه كثمرات ووعدات.",
     "en": "If it is free of these things, its ʿayn must take a fatḥa, as in “thamarāt” and “waʿadāt”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما خص الزيادة بالألف والتاء؛ لأنه عرض فيه الجمعية والتأنيث الغير الحقيقي،",
     "en": "He restricted the addition to the alif and tāʾ only because plurality and non-real femininity occur in it;"},
    {"type": "pair",
     "ar": "وكل واحد من الحرفين قد يدل على واحد من المعنيين كما في رجال وسلمى والجمالة والضاربة، كذا في الرضي.",
     "en": "and each of the two letters may indicate one of the two meanings, as in “rijāl”, “Salmā”, “al-jimāla” and “al-ḍāriba”; so in al-Raḍī."},
]
