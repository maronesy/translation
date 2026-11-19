# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 73 (printed ٧٢)."""

PAGE_NUMBER = 73
PRINTED_PAGE = "٧٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "«زيد»، فيجعل الرفع علامة لها[[١]]،",
     "en": "…“Zayd,” so rafʿ is made a mark for it;"},
    {"type": "matn",
     "ar": "وفي «رأيت زيدا»، «رأيت» عامل؛ إذ به حصل معنى المفعولية[[٢]] في «زيد»، فيجعل النصب علامة لها[[٣]]،",
     "en": "and in “I saw Zayd” (raʾaytu Zaydan), “I saw” (raʾaytu) is the governing agent, since through it the meaning of objecthood came about in “Zayd,” so naṣb is made a mark for it;"},
    {"type": "matn",
     "ar": "وفي «مررت بزيد»، «الباء» عامل[[٤]]؛ إذ به حصل معنى الإضافة في «زيد»، فيجعل الجر علامة لها[[٥]].",
     "en": "and in “I passed by Zayd” (marartu bi-Zaydin), “the bāʾ” is the governing agent, since through it the meaning of annexation came about in “Zayd,” so jarr is made a mark for it."},

    {"type": "section", "ar": "[ المعرب بالحركة ]",
     "en": "The Word Inflected by a Vowel (al-muʿrab bi-l-ḥaraka)"},

    {"type": "matn",
     "ar": "(فالمفرد[[٦]] المنصرف) أي: الاسم المفرد الذي لم يكن مثنى ولا مجموعا[[٧]]، ولا غير منصرف كـ«زيد» و«رجل».",
     "en": "“So the fully-declinable singular (al-mufrad al-munṣarif)” — that is, the singular noun that is neither dual nor plural, nor imperfectly declinable (ghayr munṣarif), such as “Zayd” and “rajul” (man)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: لمعنى الفاعلية.",
     "en": "That is: for the meaning of agenthood."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: بالفعل الذي في «رأيت»؛ لأن له استدعاء التعلق. قال الكوفيون: مجموع الفعل والفاعل عامل في المفعول؛ لأنه صار فضلة بمجموعهما.",
     "en": "That is: by the verb contained in “I saw,” because it entails the requirement of connection (taʿalluq). The Kūfans said: the verb and the agent together are the governing agent over the object, because it became a surplus element (faḍla) by the two of them together."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لمعنى المفعولية.",
     "en": "That is: for the meaning of objecthood."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: في لفظه. وأما في محله فالعامل هو الفعل، ومحله النصب. أما في «غلام زيد»، فالعامل عند بعض حرف الجر المقدر، وعند بعض المضاف النائب عن حرف الجر.",
     "en": "That is: with respect to its wording. As for its position (maḥall), the governing agent is the verb, and its position is naṣb. As for “Zayd’s servant” (ghulāmu Zaydin), the governing agent is, according to some, an implied preposition, and according to others, the muḍāf standing in place of the preposition."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لمعنى الإضافة.",
     "en": "That is: for the meaning of annexation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لما فرغ من بيان الإعراب والعامل والمعنى المقتضي أراد تفصيل اقتضاء المعنى المقتضي، فإنه تارة يقتضي الحركات الثلاث، وتارة ما سوى الفتحة، وتارة ما سوى الكسرة، وتارة يقتضي الحروف الثلاث، وتارة ما سوى الواو منها، وتارة ما سوى الألف، فهذه أقسام ستة.",
     "en": "When he had finished expounding iʿrāb, the governing agent, and the necessitating meaning, he intended to detail the necessitation of the necessitating meaning; for it sometimes necessitates the three vowels, sometimes all but the fatḥa, sometimes all but the kasra, sometimes it necessitates the three letters, sometimes all but the wāw among them, and sometimes all but the alif — so these are six categories."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "المفرد في المشهور يطلق على ما يقابل المركب، وعلى ما يقابل الجملة، وعلى ما يقابل المثنى والمجموع. والمراد هنا الأخير بقرينة المقابلة.",
     "en": "The term mufrad (singular), in the well-known usage, is applied to what is opposed to the compound (murakkab), to what is opposed to the sentence (jumla), and to what is opposed to the dual and the plural. What is intended here is the last [sense], by the indication of the [present] contrast."},
    {"type": "pair",
     "ar": "إن قيل: لا بد من تقييده بكونه غير الأسماء الستة، وما ألحق بالمثنى والمجموع؛ لأنها داخلة في المفرد خارجة عن الحكم، فلا يجاب بأنها غير داخلة فيما حكم عليه، بناء على أن القضية مهملة، أو أن الأسماء الستة وبعض ما ألحق بالمثنى غير خارجة؛ لأن شمول الحكم يستدعي شموله لجميع الأفراد لا شموله لجميع الأفراد في جميع الأحوال؛",
     "en": "If it be said: it must be restricted by its being other than the Six Nouns and what is annexed to the dual and the plural, because these fall under [the term] “singular” yet lie outside the ruling; and one cannot reply that they do not fall under that which is ruled upon — on the ground that the proposition is indeterminate (muhmala), or that the Six Nouns and some of what is annexed to the dual are not excluded — because the comprehensiveness of the ruling requires its comprehending all individuals, not its comprehending all individuals in all states;"},
    {"type": "pair",
     "ar": "لأن مقام الضبط يأباه مع أن ذكر المنصرف حينئذ لإخراج غير المنصرف الذي لم يضف ولم يعرف باللام أصلا لا لإخراج غير المنصرف مطلقا كما هو الظاهر، بل يجاب بأنها غير داخلة بواسطة ذكرها فيما بعد، وبيان إعرابها.",
     "en": "because the requirement of precise delimitation (ḍabṭ) refuses that [extension to all states], seeing that the mention of the fully-declinable (munṣarif) here serves [only] to exclude the imperfectly-declinable that is neither annexed nor made definite by the lām — not to exclude the imperfectly-declinable absolutely, as is evident. Rather, the reply is that they [the Six Nouns and the like] do not fall under it, by virtue of their being mentioned later, together with the exposition of their iʿrāb."},
    {"type": "pair",
     "ar": "إن قيل: قد بان فيما بعد إعراب غير المنصرف، فكان ينبغي أيضا أن يكتفى بذلك، ولا يصرح بقيد الانصراف هنا احترازا عنه؟",
     "en": "If it be said: the iʿrāb of the imperfectly-declinable [noun] has [also] been made clear later on, so it ought likewise to have sufficed with that, without stating the restriction of full declinability (inṣirāf) here in order to guard against it?"},
    {"type": "pair",
     "ar": "أجيب: بأن تلك الأسماء محصورة، وغير المنصرف لا يكاد ينحصر، فاحتيج في الاحتراز عنه لئلا يقع غلط في أمور كثيرة، واكتفي في الاحتراز عن المحصورة بأدنى شيء؛ إذ ليس الاعتناء بحالها كالاعتناء بما لا ينحصر مع أن الاختصار في العبارة مطلوب له جدا.",
     "en": "The reply is: those nouns are limited in number, whereas the imperfectly-declinable can scarcely be enumerated; so guarding against it was needed lest error occur in many instances, while guarding against the limited [category] was managed by the slightest means — since attention to its case is not like attention to what cannot be enumerated, especially as brevity of expression is something he greatly seeks."},
]
