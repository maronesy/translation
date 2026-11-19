# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 414 (printed ٤١٣)."""

PAGE_NUMBER = 414
PRINTED_PAGE = "٤١٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «وإنما بنيتا لموافقتهما «مذ ومنذ» الحرفين.» at the foot of PDF p. 413 (new sentence).
    {"type": "matn",
     "ar": "وتكونان تارة (بمعنى: «أول المدة») أي: أول مدة زمان الفعل[[١]] المتقدم عليهما،",
     "en": "They are sometimes (in the sense of “the beginning of the period”), that is, the beginning of the period of the time of the verb that precedes them,"},
    {"type": "matn",
     "ar": "نحو: «ما رأيته مذ -أو منذ- يوم الجمعة» أي: أول مدة زمان عدم رؤيته يوم الجمعة",
     "en": "as in “mā raʾaytuhu mudh—or mundhu—yawmi l-jumuʿa” (I have not seen him since Friday), that is, the beginning of the period of the time of not seeing him is Friday;"},
    {"type": "matn",
     "ar": "(فيليهما) أي: يقع بعدهما، أي: بعد «مذ ومنذ» (المفرد) أي: الاسم المفرد[[٢]]، لا المثنى والمجموع",
     "en": "(so there follows them), that is, there occurs after them, that is, after “mudh” and “mundhu”, (the singular), that is, the singular noun, not the dual or the plural,"},
    {"type": "matn",
     "ar": "حقيقة كالمثال المتقدم، أو حكما نحو: «ما رأيته مذ اليومان اللذان صاحبنا فيهما» أي: أول مدة عدم رؤيته هذان اليومان،",
     "en": "whether in reality, as in the preceding example, or in status, as in “mā raʾaytuhu mudh al-yawmāni lladhāni ṣāḥabnā fīhimā” (I have not seen him since the two days in which we kept company), that is, the beginning of the period of not seeing him is these two days."},
    {"type": "matn",
     "ar": "فما دام لا يلاحظ «هذان اليومان» أمرا واحدا[[٣]] لا يحكم عليهما بأولية المدة؛",
     "en": "So long as “these two days” are not regarded as a single thing, they are not judged to be the beginning of the period,"},
    {"type": "matn",
     "ar": "لأن أول المدة إنما يكون أمرا واحدا لا شيئين أو أشياء، فالمثنى والمجموع إذا وقعا أول المدة يكونان في حكم المفرد",
     "en": "because the beginning of the period can only be a single thing, not two things or several; so the dual and the plural, when they occur as the beginning of the period, have the status of the singular;"},
    {"type": "matn",
     "ar": "(المعرفة) حقيقة كالمثال المتقدم، أو حكما نحو: «ما رأيته مذ يوم لقيتني فيه» لحصول التعيين المقصود من كونه معرفة،",
     "en": "(and definite), whether in reality, as in the preceding example, or in status, as in “mā raʾaytuhu mudh yawmun laqītanī fīhi” (I have not seen him since a day on which you met me), since the specification intended by its being definite is achieved."},
    {"type": "matn",
     "ar": "وإنما كان التعيين مقصودا؛ لأنه لا فائدة في جعل الوقت المجهول أول مدة فعل؛ لأن أولية وقت ما لزمان مدة الفعل معلوم بالضرورة.",
     "en": "Specification is intended only because there is no benefit in making an unknown time the beginning of the period of an action, since that some time or other is the beginning of the time of the action’s period is known necessarily."},
    {"type": "matn",
     "ar": "(و) تارة تكونان (بمعنى: «جميع المدة») أي: جميع مدة زمان الفعل (فيليهما) أي: «مذ ومنذ» (المقصود) أي: الزمان الذي[[٤]] قصد بيانه",
     "en": "(And) sometimes they are (in the sense of “the whole period”), that is, the whole period of the time of the verb; (so there follows them), that is, “mudh” and “mundhu”, (what is intended), that is, the time whose statement is intended,"},
    {"type": "matn",
     "ar": "حال كونه متلبسا (بالعدد[[٥]]) أي: بعدده المستغرق جميع أجزائه بحيث لا يشذ منه شيء،",
     "en": "while it is accompanied (by number), that is, by its number, which takes in all its parts so that nothing of it is left out,"},
    {"type": "matn",
     "ar": "نحو: «ما رأيته مذ يومان» أي: جميع أجزاء مدة زمان عدم رؤيته يومان؛ لا أزيد ولا أنقص.",
     "en": "as in “mā raʾaytuhu mudh yawmāni” (I have not seen him for two days), that is, all the parts of the period of the time of not seeing him are two days, no more and no less."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فاللام في المدة للعهد أو عوض عن المضاف إليه.",
     "en": "So the definite article in “al-mudda” is for prior reference (ʿahd), or a substitute for the second term of the genitive construction."},
    {"type": "pair",
     "ar": "وما قيل: إن معناه أول المدة مطلقا، وتعين كونها بأول مدة الفعل المتقدم عليها مستفاد من سبق ذكر الفعل، فلا حاجة إلى التأويلين،",
     "en": "As for what has been said—that its meaning is the beginning of a period absolutely, and that its being specified as the beginning of the period of the preceding verb is drawn from the prior mention of the verb, so that neither interpretation is needed—"},
    {"type": "pair",
     "ar": "فإنما يصح لو ثبت استعمالهما في أول المدة مطلقا، وليس كذلك، فإنهما لا يستعملان إلا في أول مدة الفعل المتقدم،",
     "en": "this would be valid only if their use for the beginning of a period absolutely were established; but it is not so, for they are used only for the beginning of the period of the preceding verb,"},
    {"type": "pair",
     "ar": "والوضع إنما يوجد من الاستعمال لا من مجرد الاحتمال.",
     "en": "and coinage (waḍʿ) is known only from usage, not from mere possibility."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الدال على الوحدة لا المثنى، والمجموع وما في حكمهما مما يدل على التعدد،",
     "en": "[That is,] the one that denotes oneness, not the dual, the plural, or what has their status among the things that denote multiplicity."},
    {"type": "pair",
     "ar": "فلا يرد «ما رأيته مذ ثلاثة أيام»؛ لأنه في حكم المجموع.",
     "en": "So “mā raʾaytuhu mudh thalāthati ayyāmin” (I have not seen him for three days) is no objection, since it has the status of the plural."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بجهة من جهات الوحدة كالمصاحبة في المثال المذكور، ولظهوره لم يتعرض لبيان جهة الوحدة.",
     "en": "[That is,] in one of the respects of oneness, such as keeping company in the example mentioned; because this is evident, he did not undertake to state the respect of oneness."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أن الباء ليست صلة المقصود، وإلا لكان الواجب المقصود به العدد؛",
     "en": "He means that the bāʾ is not the complement of “al-maqṣūd” (what is intended); otherwise it would have had to be “what is intended by it is number”,"},
    {"type": "pair",
     "ar": "لأنك قصدت بقولك: يومان عدد اثنين لا أنك قصدت بالعدد يومين.",
     "en": "because by your saying “yawmāni” you intended the number two, not that you intended two days by the number."},
    # REVIEW: «فيأبى عنه لفظة» printed so (لفظة with tāʾ marbūṭa); transcribed as printed.
    {"type": "pair",
     "ar": "وما قيل: إن المعنى الذي قصد باسم العدد فيأبى عنه لفظة، فيليهما لأنه لا يليهما المعنى المقصود باسم العدد إلا تجوزا.",
     "en": "As for what has been said—that [it means] the meaning intended by the number-noun—the wording “fa-yalīhimā” rejects it, because the meaning intended by the number-noun does not follow them except by figurative extension."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "جعل الباء في قوله: بالعدد للمصاحبة، وقطعه عن المقصود الذي يطلب صلة الباء لما قاله الرضي:",
     "en": "He made the bāʾ in his words “bi-l-ʿadad” one of accompaniment, and detached it from “al-maqṣūd”, which calls for the bāʾ as its complement, because of what al-Raḍī said:"},
    {"type": "pair",
     "ar": "إنه لو لم يؤول بهذا الكلام لكان العبارة، فيليهما المقصود به العدد.",
     "en": "that if it were not interpreted in this way, the wording would have had to be “so there follows them what is intended by it is number”."},
    {"type": "pair",
     "ar": "قلت: المراد بالعدد اسم العدد بقرينة جعله مقصودا به، والكون مقصودا به شأن اللفظ، وإنما شأن المعنى كونه مقصودا.",
     "en": "I say: what is meant by “number” is the number-noun, as indicated by its being made what is intended by it; being that by which something is intended belongs to the wording, whereas what belongs to the meaning is its being intended."},
    {"type": "pair",
     "ar": "واختار المقصود بالعدد على العدد ليشمل المثنى والمجموع والمفرد المقيد بالوحدة، نحو: «ما رأيته منذ يوم، ومذ يومان، ومذ أيام»؛",
     "en": "He chose “what is intended with number” over “number” so as to include the dual, the plural and the singular restricted to oneness, as in “mā raʾaytuhu mundhu yawmin, wa-mudh yawmāni, wa-mudh ayyāmin” (I have not seen him for a day, for two days, for days),"},
    {"type": "pair",
     "ar": "لأنها ليست أعدادا، لكنها تفيد المقصود بالعدد من تعيين الآحاد.",
     "en": "for these are not numbers, but they convey what is intended by number, namely the specification of the units."},
]
