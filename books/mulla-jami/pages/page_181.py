# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 181 (printed ١٨٠)."""

PAGE_NUMBER = 181
PRINTED_PAGE = "١٨٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "والخبر[[١]]، ولهذا يعملان عملها",
     "en": "…and the predicate; and for this reason they govern as it governs."},
    {"type": "matn",
     "ar": "(هو المسند إليه) هذا شامل للمبتدأ، ولكل مسند إليه",
     "en": "(Is that to which [something] is predicated [al-musnad ilayhi])—this covers the subject and every subject of predication—"},
    {"type": "matn",
     "ar": "(بعد دخولهما) خرج به غير اسم «ما ولا»، وبما عرفت من معنى الدخول لا يرد «أبوه» في «ما زيد أبوه قائم»",
     "en": "(after their entry): by this, whatever is not the noun of “mā” and “lā” is excluded; and, by what you have learned of the meaning of “entry,” “abūhu” in “Zayd—his father is not standing” (mā Zaydun abūhu qāʾimun) does not constitute an objection."},
    {"type": "matn",
     "ar": "(مثل: «ما زيد قائما»، و«لا رجل أفضل منك»).",
     "en": "(Such as: “Zayd is not standing,” mā Zaydun qāʾiman; and “No man is more excellent than you,” lā rajulun afḍala minka.)"},
    {"type": "matn",
     "ar": "وإنما أتى بالنكرة بعد «لا» لأن «لا» لا تعمل إلا في النكرة، بخلاف «ما»، فإنه يعمل في النكرة والمعرفة.",
     "en": "He brought an indefinite noun after “lā” only because “lā” governs only an indefinite noun, unlike “mā,” which governs both the indefinite and the definite."},
    {"type": "matn",
     "ar": "هذا لغة أهل الحجاز.",
     "en": "This is the dialect of the people of the Ḥijāz."},
    {"type": "matn",
     "ar": "وأما بنو تميم، فلا يثبتون لهما العمل، ويقولون: «الاسم والخبر بعد دخولهما مرفوعان بالابتداء كما كان قبل دخولهما»،",
     "en": "As for the Banū Tamīm, they do not grant them any governing, and they say: “The noun and the predicate after their entry are nominative by virtue of inchoation (ibtidāʾ), as they were before their entry.”"},
    {"type": "matn",
     "ar": "وعلى لغة أهل الحجاز ورد القرآن نحو: ﴿ما هذا بشرا﴾[[٢]].",
     "en": "The Qurʾān came in accordance with the dialect of the people of the Ḥijāz, as in: “This is not a human being” (mā hādhā basharan)."},
    {"type": "matn",
     "ar": "(وهو) أي: عمل «ليس»[[٣]] (في «لا») دون «ما» (شاذ) قليل[[٤]] لنقصان مشابهة «لا» بـ«ليس»؛",
     "en": "(And it)—that is, the governing [like that] of “laysa”—(in [the case of] “lā”), as opposed to “mā,” (is anomalous [shādhdh]), [i.e.] rare, because of the deficiency of the resemblance of “lā” to “laysa”;"},
    {"type": "matn",
     "ar": "لأن «ليس» لنفي الحال، و«لا» ليس كذلك، فإنه للنفي مطلقا، بخلاف «ما»، فإنه أيضا لنفي الحال،",
     "en": "because “laysa” is for negating the present, and “lā” is not so, for it is for negation absolutely—unlike “mā,” for it too is for negating the present."},
    {"type": "matn",
     "ar": "فيقتصر عمل «لا» على مورد السماع[[٥]] نحو قوله:",
     "en": "So the governing of “lā” is restricted to the instances where it is attested by transmission (samāʿ), as in the poet’s words:"},
    {"type": "verse",
     "ar": "من صد[[٦]] عن نيرانها          فأنا ابن قيس لا براح",
     "en": "Whoever turns away from its fires—I am the son of Qays: no leaving [for me]!"},
    {"type": "matn",
     "ar": "أي: لا براح لي، ولا يجوز أن يكون لنفي الجنس[[٧]]؛ لأنه إذا كان لنفي الجنس لا",
     "en": "That is: “there is no leaving for me”; and it cannot be [the “lā”] for negating the genus, because if it were for negating the genus, [it would] not…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وفيه أن كون مدخول «لا» مبتدأ قبل دخول «لا» مع كونه نكرة صرفة محل نظر، فتأمل.",
     "en": "There is [an issue] in this: that the noun “lā” enters upon being a subject before the entry of “lā,” while being a pure indefinite, is open to consideration; so reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة يوسف:٣١.",
     "en": "Qurʾān, Sūrat Yūsuf 12:31."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا مفهوم من إضافة الاسم إلى \"ما ولا\"،",
     "en": "This is understood from the annexation of “noun” to “mā and lā.”"},
    {"type": "pair",
     "ar": "لا تقول: المستفاد من إضافة عملهما لا عمل ليس. قلت: الحكم بالشذوذ على عملهما لا على عملهما عمل \"ليس\" حتى يتوهم كثرة عمل آخر.",
     "en": "Do not say: what is conveyed by the annexation is their governing [as such], not the governing of “laysa.” I say: the judgment of anomaly is upon their governing [as such], not upon their governing as “laysa” governs, such that the frequency of some other governing might be supposed."},
    {"type": "pair",
     "ar": "وإنما قال الشارح: أي: عمل \"ليس\" تعيينا لما هو الواقع.",
     "en": "The commentator said “that is, the governing of laysa” only to specify what is actually the case."},
    {"type": "pair",
     # REVIEW: «فقد يعد» as printed; the sense suggests «فقد بعد» ("has gone far [from the mark]"). Transcribed as printed.
     "ar": "ومن قال: العمل مستفاد من التشبيه بـ\"ليس\" فقد يعد.",
     "en": "Whoever said: “the governing is conveyed by the comparison with laysa” has gone far [from the mark]."},
    {"type": "pair",
     "ar": "وكذا تجويزه رجوع الضمير إلى التشبيه؛ لأن التشبيه واقع من غير الشذوذ.",
     "en": "Likewise his allowing the pronoun to refer back to the comparison; because the comparison occurs without anomaly."},
    {"type": "pair",
     "ar": "وإنما الشذوذ في نتيجة التشبيه؛ لأنه لا شذوذ في نفيه ودخوله على المبتدأ والخبر.",
     "en": "The anomaly lies only in the outcome of the comparison, since there is no anomaly in its negating or in its entering upon the subject and the predicate."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "حمله على الشذوذ في الاستعمال. والشذوذ بمعنى الخروج عن القياس.",
     "en": "He took it as anomaly in usage. Anomaly (shudhūdh) has the sense of departure from analogy (qiyās)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو النكرة. ومن قال: وهو الشعر، فبيانه مخل.",
     "en": "That is, the indefinite noun. Whoever said “that is, poetry,” his explanation is defective."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كتب في الحاشية: الصدود الإعراض، والبراح الزوال. والضمير في نيرانها للحرب،",
     "en": "He wrote in the gloss: “al-ṣudūd” is turning away, and “al-barāḥ” is departing. The pronoun in “nīrānihā” refers to war;"},
    {"type": "pair",
     "ar": "أي: من أعرض عن نيران الحرب، فلا زوال لي عنها.",
     "en": "that is: whoever turns away from the fires of war—there is no departing from them for me."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "رد على الشيخ الرضي حيث قال: إنه لنفي الجنس، ومنع وجوب تكرار المرفوع بعد «لا»، فإن التكرار إنما يجب مع الفصل بينها وبين معمولها.",
     "en": "[This is] a rejoinder to Shaykh al-Raḍī, where he said that it is for negating the genus, and denied that repeating the nominative after “lā” is obligatory, since repetition is obligatory only when there is separation between it and its governed element."},
    {"type": "pair",
     "ar": "بقي احتمال أن يكون لا براح من قبيل اللاشيء، فجعل الشاعر نفسه عدم المفارقة، كما يجعل الرجل عين العدل في رجل عدل،",
     "en": "There remains the possibility that “lā barāḥ” is of the type of “non-thing” (al-lā-shayʾ): the poet made himself [to be] non-departure itself, just as a man is made justice itself in “a man [who is] justice” (rajulun ʿadlun);"},
    {"type": "pair",
     "ar": "واحتمال ألا يكون \"لا\" عاملا لجواز أن يكون متعلق الظرف مرفوعا، فلا استشهاد في البيت على عمل \"لا\".",
     "en": "and the possibility that “lā” is not governing, since that to which the adverbial is attached (mutaʿallaq al-ẓarf) may be nominative; so there is no evidence in the verse for the governing of “lā.”"},
]
