# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 229 (printed ٢٢٨)."""

PAGE_NUMBER = 229
PRINTED_PAGE = "٢٢٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "فإنه مفسر بما يستلزمه أعني: «ضربت غلامه»، فإن ضرب الغلام يستلزم إهانة سيده",
     "en": "…for it is explained by what entails it, namely “ḍarabtu ghulāmahu” (I struck his servant), since striking the servant entails insulting his master;"},
    {"type": "matn",
     "ar": "(ولابست)، فإنه مفسر بما يستلزمه، أعني: «حبست عليه».",
     "en": "(and “lābastu”) (I was involved with), for it is explained by what entails it, namely “ḥabastu ʿalayhi.”"},
    {"type": "matn",
     "ar": "ثم إن الاسم الواقع في مظان الإضمار[[١]] على شريطة التفسير إما المختار أو الواجب فيه الرفع أو النصب أو يستوي فيه الأمران،",
     "en": "Further, the noun occurring in the places where suppression on condition of explanation (al-iḍmār ʿalā sharīṭat al-tafsīr) is presumed is one in which either the nominative or the accusative is preferred, or one of them is obligatory, or the two are equal;"},
    {"type": "matn",
     "ar": "وإلى هذه الصور الخمس أشار المصنف فقال: (ويختار) في الاسم المذكور (الرفع بالابتداء[[٢]]) أي: بكونه مبتدأ؛",
     "en": "and to these five cases the author pointed, saying: (And there is preferred) in the noun mentioned (the nominative by inchoation—bi-l-ibtidāʾ), that is, by its being a mubtadaʾ;"},
    {"type": "matn",
     "ar": "لأن تجرده عن العوامل اللفظية[[٣]] يصحح رفعه بالابتداء ويرجح",
     "en": "because its being free of verbal governors makes its nominative by inchoation valid and preponderant"},
    {"type": "matn",
     "ar": "(عند عدم قرينة خلافه) أي: قرينة ترجح خلاف الرفع[[٤]]، يعني: النصب؛",
     "en": "(when there is no indication (qarīna) for its opposite), that is, an indication giving preponderance to the opposite of the nominative, meaning the accusative;"},
    {"type": "matn",
     "ar": "لأن قرينتي الصحة[[٥]] فيهما متساويتان؛ لأن وجود ما له صلاحية التفسير قرينة مصححة للنصب،",
     "en": "because the two indications of validity are equal in them, since the presence of something fit to explain is an indication that makes the accusative valid;"},
    {"type": "matn",
     "ar": "فمتى لم يرجح النصب قرينة أخرى يرجح الرفع بسلامته عن الحذف[[٦]]، نحو: «زيد ضربته»",
     "en": "so whenever no further indication gives preponderance to the accusative, the nominative is preponderant through its being free of elision, as in “Zaydun ḍarabtuhu” (Zayd, I struck him)."},
    {"type": "matn",
     "ar": "(أو عند وجود القرينة) المرجحة من الجانبين، ولكن يكون القرينة المرجحة للرفع (أقوى منها) أي: من تلك القرينة المرجحة للنصب",
     "en": "(Or when there is an indication) giving preponderance on both sides, but the indication favouring the nominative is (stronger than it), that is, than that indication favouring the accusative,"},
    {"type": "matn",
     "ar": "(كـ«أما»[[٧]]) الداخلة على ذلك الاسم (مع غير الطلب[[٨]]) أي:",
     "en": "(such as “ammā”) entering on that noun (together with something other than a request), that is:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال في الحاشية: أي مواقع يظن في بادئ النظر أنه من قبيل الإضمار على شريطة التفسير وإن لم يكن منه في الواقع.",
     "en": "He said in the Ḥāshiya: that is, places of which it is thought at first glance that they belong to suppression on condition of explanation, even if in reality they do not."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يحتمل أمرين الابتداء الذي هو العامل في المبتدأ والخبر، وحينئذ لا يتعين بذكره كونه مبتدأ،",
     "en": "It admits two things: the inchoation that is the governor in the mubtadaʾ and the khabar, in which case its being a mubtadaʾ is not specified by mentioning it;"},
    {"type": "pair",
     "ar": "والثاني مصدر للمبتدأ الذي بمعنى كونه مبتدأ، وفيه رد لجعل رافعه فعلا مجهولا مقدرا؛ لأنه ارتكاب ما لا حاجة إليه،",
     "en": "and the second: a maṣdar of the mubtadaʾ in the sense of its being a mubtadaʾ. In it is a rejection of making its nominative-governor a supposed passive verb, because that is resorting to what is not needed;"},
    {"type": "pair",
     "ar": "وإشعار بجهة كون الرفع مختارا وهو الاستغناء من تكلف تقدير العامل.",
     "en": "and an intimation of the reason the nominative is preferred, namely dispensing with the strain of supposing a governor."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا بد له من قيد آخر، وهو الإسناد يعرف الداعي لتعريف الابتداء.",
     "en": "It needs a further qualification, namely predication (isnād), as one who considers the definition of inchoation knows."},
    {"type": "pair",
     "ar": "وفيه أن تجرده يوجب رفعه بالابتداء فكيف يصح قوله: يصحح إلا أن يقال المراد: صحة تجرده تصحح، فتدبر.",
     "en": "There is [an objection] in it: its being free necessitates its nominative by inchoation, so how is his saying “makes valid” correct? Unless it is said that what is meant is: the validity of its being free makes valid. Consider carefully."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أراد بترجيحه تقوية جانب النصب سواء كانت مع وجوبه أو اختياره على الرفع أو مساواته له.",
     "en": "By “giving it preponderance” he meant strengthening the side of the accusative, whether together with its being obligatory, or preferred over the nominative, or equal to it."},
    {"type": "pair",
     "ar": "وقيد القرينة بالمرجحة لأن القرينة المصححة للنصب موجودة في مثل «زيد ضربته»،",
     "en": "He qualified the indication as “giving preponderance” because the indication making the accusative valid is present in such as “Zaydun ḍarabtuhu,”"},
    {"type": "pair",
     "ar": "ولأن انتفاء القرينة المطلقة يستدعي وجوب الرفع لا اختياره،",
     "en": "and because the absence of any indication whatever calls for the nominative being obligatory, not preferred."},
    {"type": "pair",
     "ar": "نعم لو جعلت ضمير قوله: عند عدم قرينة خلافه راجعا إلى اختيار الرفع لم يحتج إلى هذا القيد، وفيه بعد.",
     "en": "Yes, if you made the pronoun in his words “when there is no indication for its opposite” refer to the preference for the nominative, this qualification would not be needed; but that is far-fetched."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "متعلق بـ«يختار» لا بتفسير قرينة خلاف الرفع بقرينة ترجح خلاف الرفع، كما توهم.",
     "en": "It is attached to “yukhtāru” (is preferred), not to the explanation of “an indication for the opposite of the nominative” as “an indication giving preponderance to the opposite of the nominative,” as has been imagined."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "يقال: يعارضه كون الخبر جملة على تقدير الرفع.",
     "en": "It may be said: this is opposed by the khabar being a sentence on the supposition of the nominative."},
    {"type": "pair",
     "ar": "ورد بأن السلامة عن الحذف أرجح، لكن حينئذ يكون «زيد ضربته» مما اختير فيه الرفع لوجود قرينة أقوى من قرينة خلاف الرفع لا لعدم القرينة المرجحة للنصب، والمشهور خلافه،",
     "en": "This was answered by [saying] that freedom from elision is more weighty; but then “Zaydun ḍarabtuhu” would be among those in which the nominative is preferred because of an indication stronger than the indication for the opposite of the nominative, not because of the absence of an indication favouring the accusative—and the well-known view is the contrary;"},
    {"type": "pair",
     "ar": "بل يلزم ألا يوجد ما يختار فيه الرفع لعدم قرينة خلافه.",
     "en": "rather, it would follow that there is nothing in which the nominative is preferred because of the absence of an indication for its opposite."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: قرينة الرفع التي تجامع قرينة النصب، وتكون أقوى منها شيئان فقط على ما ذكروه: أما وإذا للمفاجأة.",
     "en": "Shaykh al-Raḍī said: the indication for the nominative that coexists with the indication for the accusative and is stronger than it is only two things, according to what they mentioned: “ammā” and “idhā” of surprise (idhā al-mufājaʾa)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لم يقل: مع الخبر مع أنه أخصر للإشارة إلى انتفاء ما يوجب اختيار النصب،",
     "en": "He did not say “with a statement (khabar),” though it is shorter, so as to point to the absence of what necessitates preferring the accusative;"},
    {"type": "pair",
     "ar": "والأولى أن يقول أيضا: ومع عطف الجملة التي بعدها على فعلية، أو مع كونها جوابا لجملة استفهامية فعلية نحو: «أما زيد",
     "en": "and it would be better for him also to say: “and with the sentence after it being coordinated to a verbal one, or with its being the answer to an interrogative verbal sentence,” as in “As for Zayd…"},
]
