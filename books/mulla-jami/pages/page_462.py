# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 462 (printed ٤٦١)."""

PAGE_NUMBER = 462
PRINTED_PAGE = "٤٦١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # REVIEW: a stray mark follows the colon in «أي:» on the first line; omitted here.
    {"type": "matn",
     "ar": "(فالرفع) في المعمول (على الفاعلية) أي: فاعليته للصفة.",
     "en": "(The nominative) in the governed term (is as agent), that is, its being the agent of the adjective."},
    {"type": "matn",
     "ar": "(والنصب على التشبيه) أي: تشبيه معمول الصفة[[١]] (بالمفعول في) المعمول (المعرفة، وعلى التمييز) أي: جعل معمول الصفة تمييزا (في) المعمول (النكرة). هذا عند البصريين.",
     "en": "(The accusative is by likening), that is, likening the governed term of the adjective, (to the object, in) the governed term (that is definite; and as specification), that is, making the governed term of the adjective a specification (tamyīz), (in) the governed term (that is indefinite). This is according to the Baṣrans."},
    {"type": "matn",
     "ar": "وقال الكوفيون: بل هو على التمييز في الجميع؛ لأنهم يجوزون تعريف المميز.",
     "en": "The Kūfans said: rather it is as specification in all cases, because they permit the specification to be definite."},
    {"type": "matn",
     "ar": "وقال بعض النحاة: على التشبيه بالمفعول في الجميع.",
     "en": "Some grammarians said: it is by likening to the object in all cases."},
    {"type": "matn",
     "ar": "وقال الشارح الرضي: والأولى التفصيل.",
     "en": "The commentator al-Raḍī said: the better view is the distinction [between the two]."},
    {"type": "matn",
     "ar": "(والجر) في المعمول (على الإضافة) أي: إضافة الصفة إليه.",
     "en": "(The genitive) in the governed term (is by annexation), that is, the annexation of the adjective to it."},
    {"type": "matn",
     "ar": "(وتفصيلها) أي: تفصيل هذه الأقسام في ضمن أمثلة جزئية، قولنا: (حسن وجهه) بتنوين الصفة، ورفع «وجهه» بالفاعلية، أو نصبه على التشبيه بالمفعول، أو بحذف التنوين وجر «وجهه» بالإضافة،",
     "en": "(Their detailed exposition), that is, the detailed exposition of these divisions through particular examples, is our saying: (“ḥasanun wajhuhu” (his face being good)), with tanwīn on the adjective and “wajhuhu” in the nominative as agent, or in the accusative by likening to the object; or with the tanwīn dropped and “wajhihi” in the genitive by annexation."},
    {"type": "matn",
     "ar": "فهذا التركيب[[٢]] (ثلاثة) أي: ثلاثة أمثلة من الأمثلة المقصودة، ذكرها لتوضيح الأقسام باعتبار اختلاف معمول الصفة رفعا ونصبا وجرا.",
     "en": "So this construction is (three), that is, three of the intended examples; he gave them to clarify the divisions with respect to the variation of the adjective’s governed term in the nominative, accusative and genitive."},
    {"type": "matn",
     "ar": "(وكذلك) أي: مثل هذا التركيب في كونه أمثلة ثلاثة (حسن الوجه) بالوجوه المذكورة (وحسن وجه) عطف على «حسن الوجه» أي: هو أيضا بالوجوه المذكورة أمثلة ثلاثة",
     "en": "(Likewise), that is, like this construction in being three examples, are (“ḥasanu l-wajh”) in the ways mentioned, (and “ḥasanu wajhin”), coordinated with “ḥasanu l-wajh”, that is, it too, in the ways mentioned, is three examples;"},
    {"type": "matn",
     "ar": "(الحسن وجهه) بإدخال اللام على الصفة، ورفع «وجهه» بالفاعلية، أو نصبه بالتشبيه بالمفعول، أو جره بالإضافة،",
     "en": "(“al-ḥasanu wajhuhu”), with the lām put on the adjective and “wajhuhu” in the nominative as agent, or in the accusative by likening to the object, or in the genitive by annexation."},
    {"type": "matn",
     "ar": "وإنما غير الأسلوب بترك العاطف، إشارة إلى أنه شروع في قسم آخر من الصفة المشبهة؛ لأن الأمثلة السابقة كانت للصفة المجردة عن اللام، وهذه الصفة ذات اللام",
     "en": "He changed the style by leaving out the conjunction only to indicate that it is the beginning of another division of the resembling adjective; for the preceding examples were of the adjective devoid of the lām, while this adjective has the lām;"},
    {"type": "matn",
     "ar": "(الحسن الوجه) بالوجوه الثلاثة (الحسن وجه)",
     "en": "(“al-ḥasanu l-wajh”) in the three ways, (“al-ḥasanu wajhin”)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وجه تشبيهه به أنهم لما قصدوا التخفيف في الصفة بالإضافة، ولا يمكن إضافتها إلى الفاعل؛ لأنه يلزم إضافة الشيء إلى نفسه؛ لأن الصفة عين الفاعل",
     "en": "The ground of likening it to it is that when they sought lightening in the adjective through annexation, and its annexation to the agent was impossible, since that would entail annexing a thing to itself, because the adjective is identical with the agent,"},
    {"type": "pair",
     "ar": "شبهوا مرفوعا بالمفعول، فنصبوه لتصح الإضافة إليه؛ لأن المفعول غير الصفة،",
     "en": "they likened [the term] in the nominative to the object and put it in the accusative, so that annexation to it would be valid, because the object is other than the adjective;"},
    {"type": "pair",
     "ar": "وجعلوا الصفة في اللفظ لغيره، وأضمروا فيها الضمير إذا كانت في اللفظ جارية على غير المعمول خبرا أو نعتا أو حالا، وفي المعنى دلالة على صفة له في نفسه",
     "en": "and they made the adjective in wording belong to something else, and placed a pronoun in it when it is in wording applied to other than the governed term as predicate, qualifier or circumstantial state, and in meaning indicates a quality of that [other] in itself,"},
    {"type": "pair",
     "ar": "سواء كانت هي الصفة المذكورة نحو: زيد حسن الوجه، فإنه يحسن بحسن وجهه أو لا نحو: زيد غليظ الساقين، أي: قبيح،",
     "en": "whether it is the quality mentioned, as in “Zayd is good of face”, for he is good through the goodness of his face, or not, as in “Zayd is thick of shanks”, that is, ugly."},
    {"type": "pair",
     "ar": "فإن لم تجر في اللفظ عليه نحو: زيد وجهه حسن، أو جرت عليه لكنها لم تدل على صفة له في نفسه لم يجز استتار الضمير فيها، فيقبح زيد أبيض الثوب.",
     "en": "If it is not applied to it in wording, as in “Zayd, his face is good”, or is applied to it but does not indicate a quality of it in itself, the pronoun may not be concealed in it; so “Zayd is white of garment” is unacceptable."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن ثلاثة وقع خبرا لحسن وجهه بتأويل هذا التركيب مع قطع النظر عن إعراب وجهه، وإلا فهو مثال واحد،",
     "en": "He means that “three” stands as the predicate of “ḥasan wajhuhu”, by construing it as “this construction”, disregarding the inflection of “wajhuhu”; otherwise it would be a single example."},
    {"type": "pair",
     "ar": "وليس مراده أن ثلاثة خبر مبتدأ محذوف، كما قاله الفاضل الهندي؛ لأنه لا يصلح أن يكون حسن وجهه مقول القول لكونه مفردا.",
     "en": "His meaning is not that “three” is the predicate of an omitted subject, as al-Fāḍil al-Hindī said, because “ḥasan wajhuhu” cannot be the object of “saying” (maqūl al-qawl), since it is a single word [not a sentence]."},
]
