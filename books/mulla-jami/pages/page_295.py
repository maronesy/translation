# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 295 (printed ٢٩٤)."""

PAGE_NUMBER = 295
PRINTED_PAGE = "٢٩٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «وهذا التعليل جار في المعرفة أيضا.» at the foot of PDF p. 294 (new sentence).
    {"type": "matn",
     "ar": "(ومثل: «قضية) أي: هذه قضية (ولا أبا حسن لها») أي: لهذه القضية.",
     "en": "(And such as “a case,” that is, “this is a case, (and there is no Abū Ḥasan for it”), that is, for this case."},
    {"type": "matn",
     "ar": "هذا جواب دخل مقدر على قوله: «وإن كان معرفة[[١]] وجب الرفع والتكرير»،",
     "en": "This is the answer to a supposed objection against his statement “If it is definite, the nominative and repetition are obligatory”:"},
    {"type": "matn",
     "ar": "فإن اسم «لا» فيه معرفة؛ لأن «أبا حسن» كنية علي رضي الله تعالى عنه ولا رفع فيه ولا تكرير، بل هو منصوب غير مكرر،",
     "en": "for the noun of “lā” in it is definite, since “Abū Ḥasan” is the kunya of ʿAlī, may Allah the Exalted be pleased with him; yet there is no nominative in it and no repetition—rather it is accusative and unrepeated."},
    {"type": "matn",
     "ar": "فأجاب عنه: بأنه (متأول) بالنكرة: إما بتقدير المثل أي: ولا مثل أبي حسن لها، فإن مثلا لتوغله في الإبهام لا يتعرف بالإضافة إلى المعرفة،",
     "en": "He answered it [by saying] that it is (interpreted) as indefinite: either by supposing “like,” that is, “and there is none like Abū Ḥasan for it”—for “mithl” (like), because of its deep vagueness, does not become definite by annexation to a definite noun—"},
    {"type": "matn",
     "ar": "أو بتأويله بفيصل[[٢]] بين الحق والباطل؛ لاشتهاره رضي الله تعالى عنه بهذه الصفة، فكأنه قيل: لا فيصل لها،",
     "en": "or by interpreting it as “a decisive judge (fayṣal) between truth and falsehood,” because he, may Allah the Exalted be pleased with him, was famed for this quality; so it is as if it were said, “there is no decisive judge for it.”"},
    {"type": "matn",
     "ar": "ويقوى هذا التأويل[[٣]] إيراد حسن بحذف اللام[[٤]]؛ لأن الظاهر أن تنوينه للتنكير.",
     "en": "This interpretation is strengthened by the citing of “Ḥasan” with the elision of the lām (al-Ḥasan), since the evident [reading] is that its nunation is for indefiniteness."},
    {"type": "matn",
     "ar": "(وفي مثل: «لا حول ولا قوة[[٥]] إلا بالله») أي: فيما كررت فيه «لا» على سبيل العطف وكان عقيب كل منهما نكرة بلا فصل،",
     "en": "(In such as “lā ḥawla wa-lā quwwata illā bi-llāh” [there is no power and no strength save through Allah]), that is, in what has “lā” repeated by way of conjunction, with an indefinite noun immediately after each of them, without separation,"},
    {"type": "matn",
     "ar": "يجوز (خمسة أوجه) بحسب اللفظ لا بحسب التوجيه، فإنها بحسب التوجيه تزيد[[٦]] عليها:",
     "en": "(five readings) are permitted with respect to wording, not with respect to grammatical analysis (tawjīh); for with respect to analysis they exceed that:"},
    {"type": "matn",
     "ar": "الأول: (فتحهما) أي: «لا حول ولا قوة إلا بالله» على أن يكون «لا» في كل منهما لنفي الجنس[[٧]]،",
     "en": "The first: (giving both the fatḥa), that is, “lā ḥawla wa-lā quwwata illā bi-llāh,” with the “lā” in each of them negating the genus;"},
    {"type": "matn",
     "ar": "و«لا قوة» عطف على «لا حول» عطف مفرد على مفرد، وخبرها محذوف[[٨]] أي: «لا حول ولا قوة موجود[[٩]] إلا بالله»،",
     "en": "and “lā quwwata” is conjoined to “lā ḥawla” as a single term conjoined to a single term, its predicate being elided, that is, “there is no power and no strength existent save through Allah”;"},
    {"type": "matn",
     "ar": "أو عطف جملة على جملة أي: «لا حول إلا بالله ولا قوة إلا بالله»، فحذف خبر الجملة الأولى استغناء عنه بخبر الجملة الثانية[[١٠]].",
     "en": "or it is a sentence conjoined to a sentence, that is, “there is no power save through Allah and no strength save through Allah,” the predicate of the first sentence being elided as dispensable given the predicate of the second sentence."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وعلى التعريف أيضا بأنه غير جامع.",
     "en": "And against the definition as well, [the objection] that it is not comprehensive (ghayr jāmiʿ)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "على وزن حيدر. هو القضاء بين الحق والباطل،",
     "en": "On the pattern of ḥaydar. It is judgment between truth and falsehood;"},
    {"type": "pair",
     "ar": "فإطلاق الفيصل من قبيل رجل عدل.",
     "en": "so applying “fayṣal” [to a person] is of the type of “a man [who is] justice” (rajul ʿadl)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اعلم أن نزع اللام واجب على التأويلين سواء كانت اللام في الاسم نفسه، أو فيما أضيف إليه",
     "en": "Know that removing the lām (the article) is obligatory on both interpretations, whether the lām is in the noun itself or in what it is annexed to,"},
    {"type": "pair",
     "ar": "إلا في عبد الله وفي عبد الرحمن؛ إذ الله والرحمن لا يطلقان على غيره تعالى حتى يقدر تنكيرهما.",
     "en": "except in “ʿAbd Allāh” and in “ʿAbd al-Raḥmān,” since “Allāh” and “al-Raḥmān” are not applied to other than Him, the Exalted, so that their indefiniteness could be supposed."},
    {"type": "pair",
     "ar": "أما النزع في الصورة الأولى: فلرعاية اللفظ وإصلاحه. وأما في الثانية: فالأمر واضح.",
     "en": "As for the removal in the first case, it is to observe and amend the wording; as for the second, the matter is clear."},
    {"type": "pair",
     "ar": "ولما كان النزع على التأويل الثاني واضحا كما يدل عليه قوله: لأن الظاهر أن تنوينه للتنكير جعله مقويا للتأويل الثاني.",
     "en": "Since the removal on the second interpretation is clear, as his words “since the evident [reading] is that its nunation is for indefiniteness” indicate, he made it a support for the second interpretation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يقال: حذف اللام من العلم القائم مقام المثل. والمؤول بالصفة المشتهر بها مسماها واجب",
     "en": "It may be said: eliding the lām from a proper name that stands in place of “mithl,” and from one interpreted as the quality for which its bearer is famed, is obligatory;"},
    {"type": "pair",
     "ar": "إلا أن تنوينه فيما إذا أول أوقع في مكانه من التنكير، فلذا جعل حذف اللام مقويا له.",
     "en": "but its nunation, when it is so interpreted, is better placed as [a mark of] indefiniteness; that is why he made the elision of the lām a support for it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لا حول عن المعصية، ولا قوة في الطاعة.",
     "en": "That is, there is no turning away from disobedience and no strength for obedience."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كما في أثناء تفصيل الوجوه تستفيد.",
     "en": "As you will learn in the course of the detailed account of the readings."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ويصح أن يكون في الثانية زائدة؛ لأنه جاز البناء مع الزائدة نظرا إلى لفظها.",
     "en": "It is also sound for [lā] in the second to be redundant, since indeclinability is permitted with a redundant [lā] in view of its form."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: print reads «يحكم المماثلة»; the sense suggests «بحكم المماثلة»; transcribed as printed.
    {"type": "pair",
     "ar": "واحدا مرفوع بلا الأولى والثانية. وإنما جاز ذلك مع أنهما عاملان؛ لأنهما يحكم المماثلة في حكم واحد كما في «إن زيدا وعمرا قائمان».",
     "en": "A single [predicate], put in the nominative by the first and the second lā. This is permitted although they are two governing words only because, by virtue of their likeness, they count as a single governor, as in “inna Zaydan wa-ʿAmran qāʾimān” (Zayd and ʿAmr are standing)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الأظهر موجودان.",
     "en": "The more evident [form] is “mawjūdān” (two existents)."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    # REVIEW: print reads «إن خبر» where «أن خبر» is expected after «يستفاد منه»; transcribed as printed.
    {"type": "pair",
     "ar": "يستفاد منه إن خبر الجملة الثانية مذكور. وقد سبق أنه موجود، فبينهما تنافر،",
     "en": "It is understood from this that the predicate of the second sentence is expressed, whereas it preceded that it is “mawjūd”; so there is an inconsistency between them."},
    {"type": "pair",
     "ar": "فالأولى أن يقول: سابقا، وخبرها بالله.",
     "en": "It would have been better for him to say earlier: “and its predicate is bi-llāh (through Allah).”"},
]
