# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 510 (printed ٥٠٩)."""

PAGE_NUMBER = 510
PRINTED_PAGE = "٥٠٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «تعلق لكل واحد من الزمان والمكان والغاية» at the foot of PDF p. 509 (mid-sentence).
    {"type": "matn",
     "ar": "وهيئة الفاعل[[١]]، لكن فهمه مع الغفلة عن هذه المتعلقات جائز.",
     "en": "…and the state of the agent, yet understanding it while disregarding these connected things is possible."},
    {"type": "matn",
     "ar": "وغير المتعدي يصير متعديا: إما بالهمزة نحو: «أذهبت زيدا» أو بتضعيف العين نحو: «فرحت زيدا»، أو بألف المفاعلة نحو: «ماشيته»، أو بسين الاستفعال نحو: «استخرجته»، أو بحرف الجر نحو: «ذهبت بزيد».",
     "en": "The intransitive becomes transitive either by the hamza, as in “adhhabtu Zaydan” (I made Zayd go), or by doubling the ʿayn, as in “farraḥtu Zaydan” (I gladdened Zayd), or by the alif of mufāʿala, as in “māshaytuhu” (I walked with him), or by the sīn of istifʿāl, as in “istakhrajtuhu” (I extracted it), or by a preposition, as in “dhahabtu bi-Zaydin” (I went off with Zayd)."},
    {"type": "matn",
     "ar": "(والمتعدي قد يكون) متعديا:",
     "en": "(And the transitive may be) transitive:"},
    {"type": "matn",
     "ar": "١-(إلى مفعول واحد: كـ«ضرب») وهذا في الكلام كثير.",
     "en": "1. (to one object, like “ḍaraba” (he struck)); and this is frequent in speech;"},
    {"type": "matn",
     "ar": "٢-(وإلى اثنين) ثانيهما غير الأول (كـ«أعطى») وإلى اثنين، ثانيهما عين الأول فيما صدق عليه نحو: (علم).",
     "en": "2. (and to two), the second of which is other than the first, (like “aʿṭā” (he gave)); and to two, the second of which is identical with the first in what it is true of, as in (“ʿalima” (he knew));"},
    {"type": "matn",
     "ar": "٣-(وإلى) مفاعيل (ثلاثة: كـ«أعلم»، و«أرى») بمعنى: «أعلم»، وهما أصلان في هذا القسم،",
     "en": "3. (and to three) objects, (like “aʿlama” (he informed) and “arā”) in the sense of “aʿlama”. These two are the basic members of this division,"},
    {"type": "matn",
     "ar": "فإنهما كانا قبل إدخال الهمزة متعديين إلى مفعولين، فلما أدخلت عليهما الهمزة زاد مفعول آخر يقال له: المفعول الأول.",
     "en": "for before the hamza was introduced they were transitive to two objects; and when the hamza was introduced into them, another object was added, which is called the first object."},
    {"type": "matn",
     "ar": "وأما الأفعال الأخر (و) هي: (و«أنبأ»، و«نبأ»، و«خبر»، و«أخبر»، و«حدث») فليست أصلا في التعدية إلى ثلاثة، بل تعديتها إليها إنما هي بواسطة اشتمالها على معنى الإعلام.",
     "en": "As for the other verbs, (and) they are: (“anbaʾa”, “nabbaʾa”, “khabbara”, “akhbara” and “ḥaddatha”) (to inform, tell), they are not basic in being transitive to three; rather, their transitivity to them is only by virtue of their containing the sense of informing (iʿlām)."},
    {"type": "matn",
     "ar": "(وهذه) الأفعال المتعدية إلى ثلاثة مفاعيل (مفعولها الأول كمفعول باب: أعطيت) في جواز الاقتصار عليه كقولك: «أعلمت زيدا»، والاستغناء عنه كقولك: «أعلمت عمرا منطلقا»",
     "en": "(And these) verbs transitive to three objects: (their first object is like the object of the class of “aʿṭaytu”) in that it is permitted to restrict oneself to it, as in your saying “aʿlamtu Zaydan” (I informed Zayd), and to dispense with it, as in your saying “aʿlamtu ʿAmran munṭaliqan” (I made known ʿAmr as departing);"},
    {"type": "matn",
     "ar": "(والثاني والثالث) من مفعوليها (كمفعولي «علمت») في وجوب ذكر أحدهما عند ذكر الآخر وجواز تركهما معا.",
     "en": "(and the second and the third) of its objects (are like the two objects of “ʿalimtu”), in that mentioning one of them is obligatory when the other is mentioned, and leaving out both together is permitted."},

    {"type": "section", "ar": "[أفعال القلوب]",
     "en": "Verbs of the Heart (Afʿāl al-Qulūb)"},

    {"type": "matn",
     "ar": "(أفعال القلوب) وتسمى أفعال الشك واليقين أيضا، وكأنهم أرادوا بالشك الظن،",
     "en": "(The verbs of the heart): they are also called the verbs of doubt and certainty; it is as though by “doubt” they meant supposition (ẓann);"},
    {"type": "matn",
     "ar": "وإلا فلا شيء من هذه الأفعال بمعنى الشك المقتضي تساوي الطرفين[[٢]]، (وهي:",
     "en": "otherwise none of these verbs has the sense of doubt, which entails the equality of the two alternatives. (They are:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «كالمعتدي» (letters transposed), apparently a misprint for «كالمتعدي»; transcribed as printed, translated as «كالمتعدي».
    {"type": "pair",
     "ar": "قد حقق أن المفعول الذي يبين الحال هيئة أعم من المفعول به، فلا وجه لترك هيئة المفعول في هذا المقام، فإن اللازم كالمعتدي له تعلق بهيئة الفاعل والمفعول.",
     "en": "It has been established that the object whose state the ḥāl clarifies is more general than the direct object; so there is no reason to leave out the state of the object in this place, for the intransitive, like the transitive, has a connection with the state of the agent and of the object."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: وقوع الخبر وعدم وقوعه.",
     "en": "That is, the occurrence of the predicate and its non-occurrence."},
]
