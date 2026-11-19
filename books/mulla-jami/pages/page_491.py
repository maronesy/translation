# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 491 (printed ٤٩٠)."""

PAGE_NUMBER = 491
PRINTED_PAGE = "٤٩٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(و) كلمة «أن» (التي تقع بعد العلم) … (هي) «أن»» at the foot of PDF p. 490 (mid-sentence).
    {"type": "matn",
     "ar": "(المخففة[[١]] من المثقلة)؛ لأن المخففة للتحقيق، فتناسب العلم، بخلاف الناصبة، فإنها للرجاء والطمع، فلا تناسبه[[٢]].",
     "en": "…(lightened from the heavy [anna]), because the lightened one is for affirmation, and so suits knowledge; unlike the accusative-governing one, which is for hope and expectation, and so does not suit it."},
    {"type": "matn",
     "ar": "(وليست) أي: «أن» الواقعة بعد العلم (هذه) أي: «أن» الناصبة (نحو: «علمت أن سيقوم، وألا يقوم»)",
     "en": "(And it is not), that is, the “an” occurring after knowledge, (this one), that is, the accusative-governing “an”, (as in “I knew that he will stand” and “that he does not stand”)."},
    {"type": "matn",
     "ar": "(و) «أن» (التي تقع بعد الظن، ففيها الوجهان)؛",
     "en": "(And) the “an” (that occurs after supposition admits both treatments),"},
    {"type": "matn",
     "ar": "لأن الظن باعتبار دلالته على غلبة الوقوع[[٣]] يلائم «أن» المخففة الدالة على التحقيق، وباعتبار عدم التيقن يلائم «أن» المصدرية، فيصح وقوع كليهما، فيجري في «أن» التي بعده الوجهان.",
     "en": "because supposition, in respect of its indicating the preponderance of occurrence, befits the lightened “an”, which indicates affirmation, and in respect of the absence of certainty befits the infinitival “an”; so the occurrence of both is valid, and both treatments apply to the “an” that follows it."},
    {"type": "matn",
     "ar": "(و«لن» مثل: «لن أبرح»، ومعناها) أي: معنى «لن» (نفي المستقبل) نفيا مؤكدا لا مؤبدا[[٤]]،",
     "en": "(And “lan”, as in “lan abraḥa” (I shall not leave); its meaning), that is, the meaning of “lan”, (is the negation of the future), an emphatic negation, not a perpetual one;"},
    {"type": "matn",
     "ar": "وإلا يلزم أن يكون في قوله تعالى: ﴿فلن أبرح الأرض حتى يأذن لي أبي﴾[[٥]] تناقض؛ لأن «لن» تقتضي التأبيد، و«حتى» تقتضي الانتهاء.",
     "en": "otherwise it would follow that there is a contradiction in His words, the Exalted, “So I will never leave this land until my father permits me”, because “lan” would require perpetuity while “ḥattā” requires termination."},
    {"type": "matn",
     "ar": "(و«إذن») التي ينتصب بها المضارع (إذا لم يعتمد ما بعدها على ما قبلها) أي: لم يكن ما بعدها معمولا لما قبلها،",
     "en": "(And “idhan”), by which the muḍāriʿ is put in the accusative, (when what follows it does not lean upon what precedes it), that is, what follows it is not governed by what precedes it;"},
    {"type": "matn",
     "ar": "فإنه إذا اعتمد[[٦]] ما بعدها على ما قبلها لا ينتصب؛ لأنها لضعفها لا تقدر أن تعمل فيما اعتمد على ما قبلها، فصار كأنه سبقها حكما",
     "en": "for when what follows it leans upon what precedes it, it is not put in the accusative, because, owing to its weakness, it cannot govern what leans upon what precedes it, so it became as if it preceded it in status;"},
    {"type": "matn",
     "ar": "(وكان) عطف على «لم يعتمد» أي: ينتصب بها المضارع إذا لم يعتمد ما بعدها على ما قبلها، وإذا كان (الفعل) المذكور بعدها[[٧]] (مستقبلا)",
     "en": "(and is), coordinated with “does not lean”; that is, the muḍāriʿ is put in the accusative by it when what follows it does not lean upon what precedes it, and when (the verb) mentioned after it (is future),"},
    {"type": "matn",
     "ar": "لكونها[[٨]] جوابا وجزاء، وهما لا يمكنان إلا في الاستقبال، فإن فقد أحد الشرطين، نحو: «أنا إذن أحسن إليك»،",
     "en": "because it is a reply and a requital, and these two are possible only in the future. If one of the two conditions is missing, as in “anā idhan uḥsinu ilayka” (I, then, will do good to you),…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "صيغة الفصل ههنا للحصر أي: هي المخففة لا غير، وبه صار مقابلا لقوله: والتي تقع بعد الظن،",
     "en": "The separating form (ṣīghat al-faṣl) here is for restriction, that is, it is the lightened one and nothing else; and by this it is set against his words “and the one that occurs after supposition”."},
    {"type": "pair",
     "ar": "وقوله: من المثقلة متعلق بالأخذ، أي: المخففة المأخوذة من المثقلة.",
     "en": "His words “from the heavy” are attached to [the notion of] taking, that is, the lightened one taken from the heavy one."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فكذا الداخل على الماضي.",
     "en": "So likewise the one that enters upon the past."},
    {"type": "pair",
     "ar": "ولا يبعد أن يقال: هي الناصبة ألغيت لخروجها عن مقتضى وضعها، وهي أخف من المخففة الموجبة لحذف ضمير الشأن.",
     "en": "It is not far-fetched to say: it is the accusative-governing one, cancelled because it has left what its coining requires; and this is lighter than the lightened one, which requires the omission of the pronoun of the matter (ḍamīr al-shaʾn)."},
    {"type": "pair",
     "ar": "وقوله: وليست هذه تأكيد للحصر.",
     "en": "His words “and it is not this one” are an emphasis of the restriction."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: كون جانب الوقوع غالبا على عدمه، وليس المراد بغلبة الوقوع كثرته، كما هو المتبادر.",
     "en": "That is, the side of occurrence preponderating over its non-occurrence; by preponderance of occurrence its frequency is not meant, as first comes to mind."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مطلقا كما قيل: ولا مؤبدا في الدنيا كما قيل: هو الحق.",
     "en": "[Not perpetual] absolutely, as has been said, nor perpetual in this world, as has been said; this is the truth."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة يوسف: ٨٠.",
     "en": "Qurʾān, Sūrat Yūsuf 12:80."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "حاصله: أن «إذن» لكونه حرفا ضعيف العمل لا يعمل فيما هو مقدم عليه حكما،",
     "en": "Its gist: “idhan”, being a particle of weak government, does not govern what precedes it in status."},
    {"type": "pair",
     "ar": "وترك الدليل المشهور الذي ذكره من فسر الاعتماد بكونه معمولا، وهو أنه يلزم توارد العاملين، أعني: إذن وما قبلها؛",
     "en": "He left aside the well-known proof mentioned by those who explained “leaning” as being governed, namely that it would entail two governors converging [on one term], that is, idhan and what precedes it;"},
    {"type": "pair",
     "ar": "لأن توارد العاملين جائز إذا كان عمل أحدهما لفظيا، وعمل الآخر محليا، نحو: إن زيدا قائم وعمرو.",
     "en": "because the convergence of two governors is permissible when the government of one is overt and that of the other is positional (maḥallī), as in “inna Zaydan qāʾimun wa-ʿAmrun”."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: متصلا كما هو المتبادر، ففيه إشارة إلى اشتراط الاتصال أيضا،",
     "en": "That is, adjacent, as first comes to mind; so there is in it an indication that adjacency is also a condition,"},
    {"type": "pair",
     "ar": "فإنها لا تعمل بالفصل إلا إذا كان بالقسم أو بلا النافية، نص عليه في المغني.",
     "en": "for it does not govern with a separation unless [the separation] is by an oath or by the negating lā; this is stated explicitly in al-Mughnī."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: في الأصل باعتبار مدخولها جوابا لكلام مقدم صدر عن ذلك المتكلم نحو: إن جئتني إذن أكرمك، أو من متكلم آخر كما في مثال المتن، وجزاء لشرط مذكور أو مقدر.",
     "en": "That is, originally, in respect of what it enters upon being a reply to a preceding utterance, issued by that same speaker, as in “in jiʾtanī idhan ukrimaka” (if you come to me, then I will honour you), or by another speaker, as in the example of the text; and a requital of a condition, stated or supposed."},
]
