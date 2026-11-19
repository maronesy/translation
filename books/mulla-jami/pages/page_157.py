# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 157 (printed ١٥٦)."""

PAGE_NUMBER = 157
PRINTED_PAGE = "١٥٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "على الخبر لفظا؛ لأن المبتدأ ذات، والخبر حال من أحوالها[[١]]، والذات متقدمة على أحوالها.",
     "en": "…over the khabar in wording; because the mubtadaʾ is an essence (dhāt), and the khabar is one of its states (aḥwāl), and the essence is prior to its states."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل أن الأصل في المبتدأ التقديم لفظا[[٢]] (جاز) قولهم: (في «داره زيد»[[٣]])",
     "en": "(And for that reason—wa-min thammata), that is: because the rule (aṣl) for the mubtadaʾ is precedence in wording, (it is permitted) [to say] their expression: (“In his house is Zayd”—fī dārihi Zaydun),"},
    {"type": "matn",
     "ar": "مع كون الضمير عائدا إلى «زيد» المتأخر لفظا لتقدمه رتبة؛ لأصالة التقديم.",
     "en": "although the pronoun refers back to “Zayd,” which comes later in wording, because it is prior in rank (rutba), precedence being its original [position]."},
    {"type": "matn",
     "ar": "(وامتنع) قولهم: («صاحبها في الدار») لعود الضمير إلى «الدار»، وهو في حيز الخبر الذي أصله التأخير،",
     "en": "(And there is excluded) their expression: (“Its owner is in the house”—ṣāḥibuhā fī al-dār), because the pronoun refers back to “the house” (al-dār), which lies within the domain of the khabar, whose original [position] is to come later;"},
    {"type": "matn",
     "ar": "فيلزم عود الضمير إلى المتأخر لفظا ورتبة، وهو غير جائز.",
     "en": "so it would entail the pronoun’s referring back to what comes later both in wording and in rank, and that is not permissible."},

    {"type": "section", "ar": "[ مسوغات الابتداء بالنكرة ]",
     "en": "What Permits an Indefinite Noun as Mubtadaʾ (Musawwighāt al-Ibtidāʾ bi-l-Nakira)"},

    {"type": "matn",
     "ar": "(وقد يكون المبتدأ نكرة[[٤]]) وإن كان الأصل فيه أن يكون معرفة؛",
     "en": "(The mubtadaʾ may be indefinite—nakira), even though the rule for it is that it be definite (maʿrifa);"},
    {"type": "matn",
     "ar": "لأن للمعرفة معنى معينا، والمطلوب المهم[[٥]] الكثير الوقوع في الكلام إنما هو الحكم على الأمور المعينة،",
     "en": "because the definite noun has a determinate meaning, and what is sought as important and frequently occurring in speech is only the judgment upon determinate things;"},
    {"type": "matn",
     "ar": "ولكنه لا يقع نكرة على الإطلاق، بل (إذا تخصصت[[٦]]) تلك النكرة (بوجه ما[[٧]]) من وجوه التخصيص؛",
     "en": "but it does not occur as an indefinite unrestrictedly; rather, (when) that indefinite noun (is specified in some way—idhā takhaṣṣaṣat bi-wajhin mā), among the ways of specification (takhṣīṣ);"},
    {"type": "matn",
     "ar": "إذ بالتخصيص يقل اشتراكها، فتقرب من المعرفة[[٨]].",
     "en": "for through specification its commonality (ishtirāk) is lessened, so it draws near to the definite noun."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "غالبا فلا يرد النقض بقولك: «المنطلق زيد».",
     "en": "[That is,] mostly; so no objection arises from your saying: “The one setting off is Zayd” (al-munṭaliqu Zaydun)."},
    {"type": "pair",
     "ar": "إن قيل: هذا الدليل جار في الفاعل، فينبغي أن يكون أصله التقديم؟",
     "en": "If it is said: this proof applies to the agent (fāʿil) [as well], so its rule ought to be precedence?"},
    {"type": "pair",
     "ar": "أجيب: بأن تقديم الحكم في الجملة الفعلية لكونه عاملا في المحكوم عليه، ومرتبة العامل قبل مرتبة المعمول.",
     "en": "It has been answered: the precedence of the predicate (ḥukm) in the verbal sentence is due to its being the governor (ʿāmil) of the subject of the judgment, and the rank of the governor is before the rank of the governed (maʿmūl)."},
    {"type": "pair",
     "ar": "وإنما اعتبر الأمر اللفظي دون الأمر المعنوي؛ لأن الأمر اللفظي طار، والاعتبار بالطاري دون المطرو عليه،",
     "en": "The verbal factor was taken into account rather than the semantic factor only because the verbal factor is supervening (ṭārin), and consideration goes to the supervening rather than to that upon which it supervenes;"},
    {"type": "pair",
     "ar": "وبأن الفعل محتاج إلى الاسم، والاسم مستغن عن الفعل، فأرادوا في الجملة المركبة منهما تتميم الناقص بالكامل.",
     "en": "and [it has been answered] that the verb needs the noun while the noun is independent of the verb, so in the sentence composed of the two they wished to complete the deficient by the complete."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وأما التقديم رتبة، فهو أمر لازم للمبتدأ لا ينفك عنه.",
     "en": "As for precedence in rank, it is a necessary attribute of the mubtadaʾ, never separated from it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "خلافا للكوفيين، فإن \"في داره\" عامل عندهم، ومرتبته التقدم على \"زيد\".",
     "en": "Contrary to the Kūfans; for “fī dārihi” is a governor according to them, and its rank is to precede “Zayd.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إنما لم يقدم عليه مواضع لزوم تقديم المبتدأ على الخبر وعكسه مع أنه المناسب للأصل الذي مهده آنفا",
     "en": "He did not place before it the cases in which the mubtadaʾ must precede the khabar, and the reverse, although that is what suits the rule he laid down just now,"},
    {"type": "pair",
     "ar": "لئلا يلزم الانتشار بينه وبين الأصلين الآخرين، وهما تعريف المبتدأ، وإفراد الخبر المفهومين من لفظة «قد» في قوله: «قد يكون المبتدأ نكرة»، وفي قوله: «والخبر قد يكون جملة»،",
     "en": "so that dispersion would not result between it and the two other rules—namely, the definiteness of the mubtadaʾ and the singleness (ifrād) of the khabar, both understood from the word “qad” in his saying “The mubtadaʾ may (qad) be indefinite” and in his saying “And the khabar may (qad) be a sentence”;"},
    {"type": "pair",
     "ar": "ولئلا يلزم تقديم ما يبتني ابتناء ما على المبتنى عليه، كما يظهر عند التفصيل.",
     "en": "and so that it would not result that what is in some way built upon [something] is placed before that upon which it is built, as will become apparent in the detailed exposition."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "القول بأن الحكم على الطبيعة المستفادة من المعرف بلام الجنس مهم دون الحكم عليها إذا كانت مستفادة من النكرة غير ظاهر.",
     "en": "The claim that the judgment upon the nature (ṭabīʿa) conveyed by [a noun] made definite with the generic lām (lām al-jins) is important, but not the judgment upon it when it is conveyed by an indefinite noun, is not evident."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: حقيقة أو حكما ليشمل نحو: \"ما أحد خير منك\"،",
     "en": "That is: actually or virtually (ḥukman), so as to include such as: “No one is better than you” (mā aḥadun khayrun minka);"},
    {"type": "pair",
     "ar": "فإنه وإن لم يحصل فيه تقليل الاشتراك، لكنه في حكم ما قل اشتراكه في التعين،",
     "en": "for although no lessening of commonality occurs in it, it is nonetheless in the status of that whose commonality has been lessened with respect to determinacy;"},
    {"type": "pair",
     "ar": "أو يقال: فيه اكتفاء، والمراد: إذا تخصصت أو تعينت.",
     "en": "or it may be said: there is an ellipsis by sufficiency (iktifāʾ) in it, and what is meant is: “when it is specified or made determinate.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لفظة «ما» زائدة أو صفة.",
     "en": "The word “mā” is redundant (zāʾida) or an adjective (ṣifa)."},
    {"type": "pair",
     "ar": "لما كان التخصيص منحصرا في أمثال الأمثلة المذكورة كان الأنسب أن يقول: إذا تخصصت بمثل \"ولعبد مؤمن\" إلى آخره؛",
     "en": "Since specification is confined to the likes of the examples mentioned, it would have been more fitting for him to say: “when it is specified by the like of ‘wa-la-ʿabdun muʾminun’ (and a believing slave…)” to the end;"},
    {"type": "pair",
     "ar": "لأن لفظة ما ينبئ عن عدم الانحصار.",
     "en": "because the word “mā” intimates non-confinement."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "التي هي منافية للشركة غالبا، فلا يرد أن مزية «ادخل السوق» على «ادخل سوقا» في قلة الشركة غير ظاهرة،",
     "en": "[The definite noun] which is, for the most part, incompatible with commonality (shirka); so the objection does not arise that the advantage of “Enter the market” (udkhul al-sūqa) over “Enter a market” (udkhul sūqan) in lessening commonality is not evident;"},
    {"type": "pair",
     "ar": "وكما أنه يقل الاشتراك بالتخصيص قد ينعدم إلا أنه خص بالذكر ما هو الغالب. ويكفي للوقوع مبتدأ.",
     "en": "and just as commonality is lessened through specification, it may also cease altogether; but he singled out for mention what is predominant. And [the lessening] suffices for [the noun’s] occurring as a mubtadaʾ."},
]
