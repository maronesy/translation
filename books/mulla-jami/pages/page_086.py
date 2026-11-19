# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 86 (printed ٨٥)."""

PAGE_NUMBER = 86
PRINTED_PAGE = "٨٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "والظرف متعلقا بالزيادة، وأريد بزيادة الألف قبل النون اشتراكهما في وصف الزيادة، وتقدم الألف عليها في هذا الوصف، لفهم زيادتهما جميعا.",
     "en": "And [were] the adverbial phrase connected to “the extra-ness” (al-ziyāda), and by “the extra-ness of the alif before the nūn” were intended their both sharing in the attribute of extra-ness, together with the precedence of the alif over it in this attribute — then the extra-ness of both together would be understood."},
    {"type": "matn",
     "ar": "وهذا كما إذا قلت: «جاءني زيد راكبا من قبله أخوه»، فإنه يدل على اشتراكهما في وصف الركوب، وتقدم أخيه عليه في هذا الوصف.",
     "en": "This is like when you say: “Zayd came to me riding, before him his brother [riding]” — for it indicates their both sharing in the attribute of riding, and the precedence of his brother over him in this attribute."},
    {"type": "matn",
     "ar": "وقوله: «وهذا القول تقريب»[[١]] يعني: أن ذكر العلل[[٢]] بصورة النظم تقريب لها إلى الحفظ[[٣]]؛ لأن حفظ النظم أسهل،",
     "en": "His words “and this statement is [only] an approximation” mean: that mentioning the causes in the form of verse is an approximation of them toward memorization, because memorizing verse is easier;"},
    {"type": "matn",
     "ar": "أو القول بأن كل واحد من الأمور التسعة علة، قول تقريبي لا تحقيقي؛ إذ العلة في الحقيقة اثنان منها لا واحدة،",
     "en": "or [it means that] the statement that each one of the nine matters is a cause is an approximate, not a precise, statement; for the cause is in reality two of them, not one;"},
    {"type": "matn",
     "ar": "أو القول بأنها تسع تقريب إلى الصواب؛ لأن في عددها خلافا:",
     "en": "or [it means that] the statement that they are nine is an approximation toward the correct view, because there is disagreement over their number:"},
    {"type": "matn",
     "ar": "فقال بعضهم[[٤]]: إنها تسعة.",
     "en": "Some said: they are nine."},
    {"type": "matn",
     "ar": "وقال بعضهم[[٥]]: إنها اثنتان.",
     "en": "Some said: they are two."},
    {"type": "matn",
     "ar": "وقال بعضهم[[٦]]: إنها إحدى عشرة.",
     "en": "And some said: they are eleven."},
    {"type": "matn",
     "ar": "ولكن القول بأنها تسع تقريب لها إلى ما هو الصواب من المذاهب الثلاثة.",
     "en": "But the statement that they are nine is an approximation of them toward what is correct among the three views."},
    {"type": "matn",
     "ar": "ثم إنه ذكر أمثلة العلل[[٧]] التسع المذكورة على ترتيب ذكرها في البيتين، فقال: (مثل: عمر) مثال للعدل[[٨]].",
     "en": "Then he mentioned examples of the nine aforementioned causes, in the order of their mention in the two verses, saying: (Like: “ʿUmar”) — an example of alteration (ʿadl)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ما ثبت في كلامهم الوجوه الثلاثة المذكورة. ولنا وجه رابع، وهو الاعتذار من مسامحات وقعت للناظم في هذه الأبيات لعدم مساعدة النظم بأن المقصود تقريب غير المنصرف، والعلل من الحفظ لا يتحقق القول فيها؛ إذ لا يساعده النظم.",
     "en": "What is established in their discourse is the three mentioned views. We, however, have a fourth view, which is the excusing of the loosenesses (musāmaḥāt) that befell the versifier in these verses on account of the metre’s not accommodating [precision]: namely, that the aim is the approximating of the diptote, while as for the causes — in the matter of memorization — no precise statement can be made about them, since the metre does not permit it."},
    {"type": "pair",
     "ar": "وقد عرفت بعض المسامحات في البيت الأول مما ذكرنا. ومنها إيهام العلل كما بين في تنكيرها، ومنها ما في قوله: «والنون زائدة» مما ذكره الشارح، ومما يذكر لك من أن السبب مجموع الألف والنون لا مجرد الألف.",
     "en": "You have already come to know some of the loosenesses in the first verse from what we mentioned. Among them is the ambiguity concerning the causes, as was made clear in [the poet’s] rendering them indefinite; and among them is what lies in his words “wa-l-nūn zāʾida,” [drawn] from what the commentator (al-Shāriḥ) mentioned, and from what is [further] pointed out to you: that the cause is the totality of the alif and the nūn, not the alif alone."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "من فسر التقريب بالأقرب، فلعله فهم من المبالغة المفهومة من حمل المصدر على صاحبه، أو من الصيغة، فإن باب التفعيل يجيء للتكثير، وفيه أنه إذا كان متعديا يجيء لتكثير المفعول لا لتكثير الفعل.",
     "en": "Whoever interpreted “taqrīb” as “the nearest” (al-aqrab) — perhaps he understood [it] from the hyperbole implied by predicating the verbal noun of its subject, or from the [morphological] form, for the tafʿīl pattern comes for intensification (takthīr); yet [the objection] is that when it is transitive it comes for the multiplying of the object, not the multiplying of the act."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: إلى حفظ المبتدئ وضبطه لا بمعنى الحفظ من العيوب.",
     "en": "That is: toward the beginner’s memorizing and mastering it — not in the sense of preserving [it] from defects."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كالزمخشري والمصنف والبيضاوي.",
     "en": "Such as al-Zamakhsharī, the author (al-Muṣannif), and al-Bayḍāwī."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو صدر الأفاضل والقاضي عضد ومن معهما.",
     "en": "Namely, Ṣadr al-Afāḍil, al-Qāḍī ʿAḍud, and those with them."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وهو صاحب اللباب ومن تبعه.",
     "en": "Namely, the author of al-Lubāb and those who followed him."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: أراد ذكرها توضيحا لها. وفيه مقابلة الجمع، فيصار إلى التوزيع.",
     "en": "That is: he intended to mention them by way of clarification. In it is the correspondence of plurals (muqābalat al-jamʿ), so one proceeds to distribution (tawzīʿ)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "يعني أنه غير منصرف تحقق فيه العدل المؤثر باجتماع العلة الأخرى، وهي العلمية، وهذا العدل هو كونه مخرجا عن صيغته الأصلية إلى هذه الصيغة المخصوصة، لا أن نفس هذا المثال عدل،",
     "en": "Meaning: it is a diptote in which the operative alteration (al-ʿadl al-muʾaththir) is realized by the concurrence (ijtimāʿ) of the other cause — namely, proper-name-hood (ʿalamiyya); and this alteration consists in its being diverted from its original form to this particular form — not that the example itself is [literally] “alteration”;"},
    {"type": "pair",
     "ar": "وكذا الحال في الأمثلة الباقية. فإن نفس الأسماء ليست علة، بل هي غير منصرف تحقق فيها العلل، فتأمل.",
     "en": "and the same holds for the remaining examples; for the nouns themselves are not the cause, but rather they are diptotes in which the causes are realized. So reflect (fa-taʾammal)."},
]
