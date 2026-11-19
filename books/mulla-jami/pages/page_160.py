# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 160 (printed ١٥٩)."""

PAGE_NUMBER = 160
PRINTED_PAGE = "١٥٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "«سلمت سلاما عليك»، فحذف الفعل وعدل إلى الرفع لقصد الدوام والاستمرار،",
     "en": "…“I give peace to you” (sallamtu salāman ʿalayka); then the verb was deleted and [the maṣdar] was shifted to the nominative to convey permanence and continuity;"},
    {"type": "matn",
     "ar": "فكأنه قال: «سلامي أي: سلام من قبلي عليك».",
     "en": "so it is as if he said: “My peace—that is, peace from my side—be upon you.”"},
    {"type": "matn",
     "ar": "هذا[[١]] هو المشهور فيما بين النحاة[[٢]]،",
     "en": "This is what is well known among the grammarians."},
    {"type": "matn",
     "ar": "وقال بعض المحققين[[٣]] منهم: مدار صحة الإخبار عن النكرة على الفائدة[[٤]]، لا على ما ذكروه من التخصيصات التي يحتاج في توجيهاتها إلى هذه التكلفات الركيكة الواهية الضعيفة،",
     "en": "But one of the verifying scholars (muḥaqqiqūn) among them said: the validity of predicating of an indefinite noun turns on informativeness (fāʾida), not on the specifications they mentioned, whose justification requires these feeble, flimsy and weak contrivances;"},
    {"type": "matn",
     "ar": "فعلى هذا يجوز أن يقال: «كوكب انقض الساعة» لحصول الفائدة، ولا يجوز أن يقال: «رجل قائم» لعدمه،",
     "en": "so on this [view] it is permissible to say “A star fell just now” (kawkabun inqaḍḍa al-sāʿata), since informativeness is attained, and it is not permissible to say “A man is standing” (rajulun qāʾimun), because it is lacking."},
    {"type": "matn",
     "ar": "وهذا القول أقرب إلى الصواب[[٥]].",
     "en": "This view is closer to what is correct."},

    {"type": "section", "ar": "[ الخبر يكون جملة ]",
     "en": "The Khabar as a Sentence"},

    {"type": "matn",
     "ar": "ولما كان الخبر المعرف فيما سبق مختصا بالمفرد[[٦]]، لكونه قسما من الاسم فلم تكن الجملة داخلة فيه",
     "en": "Since the khabar defined above was confined to the single [term] (mufrad), being a division of the noun, so that the sentence was not included in it,"},
    {"type": "matn",
     "ar": "أراد أن يشير إلى أن خبر المبتدأ قد يقع جملة أيضا، فقال:",
     "en": "he wished to indicate that the khabar of the mubtadaʾ may also occur as a sentence (jumla), and so he said:…"},

    {"type": "rule"},

    # ---------------- Continuation of footnote ٩ from the previous page (printed ١٥٨) ----------------
    # Unnumbered on this page; it does not correspond to a marker here.
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "السبب، فيكون التقدير دعائي الشر لك بعيد،",
     "en": "…the cause, so that the implied sense would be “my supplication for evil [be] to you,” is far-fetched."},
    {"type": "pair",
     "ar": "فالأولى أن يقال: تنكير سلام لرعاية أصله حين كان مصدرا منصوبا،",
     "en": "It is better, then, to say: “salām” is indefinite out of regard for its origin, when it was an accusative maṣdar;"},
    {"type": "pair",
     "ar": "وإنما أخر الجار والمجرور لتقديم الأهم، للمتبادر إلى المراد؛ إذ لو قدم الخبر لربما ذهب الوهم إلى اللعنة.",
     "en": "and the preposition with its object was placed last only to put first what is more important, [this being] what first comes to mind as the intended meaning; for had the khabar been placed first, the mind might have gone to [the sense of] a curse."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إشارة إلى اشتراط التخصيص بوجه ما في صحة وقوع النكرة مبتدأ.",
     "en": "A reference to the stipulation of specification in some way for the validity of an indefinite noun’s occurring as a mubtadaʾ."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إما إشارة إلى الحكم بأن النكرة يجب أن تتخصص حتى يقع مبتدأ، فحينئذ يكون قوله: وقال بعض المحققين منهم إلى آخره عديلا له،",
     "en": "It is either a reference to the ruling that the indefinite noun must be specified in order to occur as a mubtadaʾ—in which case his words “But one of the verifying scholars among them said…” to the end are its counterpart;"},
    {"type": "pair",
     "ar": "وإما إشارة إلى ما ذكره في تفسير سلام عليك، والمقصود منه الإشارة إلى ما فيه من المناقشة التي ذكرها الفاضل الهندي.",
     "en": "or it is a reference to what he mentioned in explaining “salāmun ʿalayka,” the purpose being to point to the dispute over it that the learned al-Hindī (al-Fāḍil al-Hindī) mentioned."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهو ابن الدهان بتشديد الهاء.",
     "en": "He is Ibn al-Dahhān, with a doubled hāʾ."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الضابط في تجويز الإخبار عن المبتدأ والفاعل سواء كانا معرفتين أو نكرتين جهل المخاطب بالنسبة،",
     "en": "The criterion for allowing predication of the mubtadaʾ and the agent, whether both are definite or both indefinite, is the addressee’s ignorance of the relation (nisba):"},
    {"type": "pair",
     "ar": "فإن كان جاهلا بها صح الإخبار وإن كان المخبر عنه نكرة، وإن كان عالما بها يصح الإخبار وإن كان المخبر عنه معرفة.",
     "en": "if he is ignorant of it, the predication is valid even if what is predicated of is indefinite; and if he knows it, the predication is valid even if what is predicated of is definite."},
    # REVIEW: the printed text reads «يصح» in the second clause where the sense calls for «لا يصح»; transcribed as printed.

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لظهور وجهه وورود الاستعمال عليه كقوله تعالى: ﴿وجوه يومئذ ناضرة﴾ (سورة القيامة:٢٢)، و﴿هل من مزيد﴾ (سورة ق:٣٠)،",
     "en": "Because its rationale is evident and usage accords with it, as in His words, the Exalted: “Faces on that day will be radiant” (Qurʾān, Sūrat al-Qiyāma 75:22), and “Are there any more?” (Qurʾān, Sūrat Qāf 50:30),"},
    {"type": "pair",
     "ar": "وقوله: فيوم علينا ويوم لنا إلى غير ذلك مما لا يعد،",
     "en": "and the poet’s words: “A day against us and a day for us,” and other [instances] beyond counting;"},
    {"type": "pair",
     "ar": "وإرجاعها إلى المخصصات المذكورة تكلف.",
     "en": "and to refer them back to the specifiers mentioned is a contrivance."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الباء داخل على المقصور عليه.",
     "en": "The bāʾ [of bi-l-mufrad] is attached to that to which [the khabar] is restricted."},
    {"type": "pair",
     "ar": "والمفرد بمعنى ما يقابل الجملة، فيشمل المثنى والمجموع والمركب بأقسامه.",
     "en": "“Single” (mufrad) has the sense of what stands opposite the sentence; so it includes the dual, the plural and the compound in all its kinds."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قد عرفت أن الخبر المعرف يجوز أن يكون مطلق الخبر كما هو الظاهر.",
     "en": "ʿAbd al-Ghafūr said: you have learned that the khabar [as] defined may be the khabar unrestrictedly, as is the apparent [sense]."},
    {"type": "pair",
     "ar": "فقوله: والخبر قد يكون جملة، للإشارة إلى تقسيمه، وكون أفراده أصلا.",
     "en": "So his statement “And the khabar may be a sentence” serves to indicate its division, and that its single [form] is the basic one."},
]
