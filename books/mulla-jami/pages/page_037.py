# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 37 (printed ٣٦)."""

PAGE_NUMBER = 37
PRINTED_PAGE = "٣٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "قيل: يخرج عنه[[١]] وضع الحرف، حيث لا يفهم معناه[[٢]] متى أطلق، بل إذا أطلق مع ضم ضميمة[[٣]]؟",
     "en": "It has been said: the positing (waḍʿ) of the particle (ḥarf) falls outside it, since its meaning is not understood when it is uttered [alone], but only when it is uttered together with the addition of an adjunct (ḍamīma)?"},
    {"type": "matn",
     "ar": "وأجيب عنه: بأن المراد متى أطلق إطلاقا صحيحا[[٤]]، وإطلاق الحرف بلا ضم ضميمة غير صحيح.",
     "en": "The reply to it is: what is intended is “when it is uttered in a sound utterance,” and the uttering of the particle without the addition of an adjunct is not sound."},
    {"type": "matn",
     "ar": "ولا يبعد أن يقال[[٥]]: إن المراد بإطلاق الألفاظ أن يستعملها[[٦]] أهل اللسان في محاوراتهم وبيان مقاصدهم، فلا حاجة إلى اعتبار قيد زائد.",
     "en": "It is not far-fetched to say: what is meant by the uttering of the expressions is that the speakers of the language employ them in their discourse and in expressing their aims; so there is no need to include any additional qualification."},
    {"type": "matn",
     "ar": "(لمعنى) المعنى: ما يقصد بشيء[[٧]].",
     "en": "His words “li-maʿnā” (for a meaning): the meaning (al-maʿnā) is that which is intended by a thing."},
    {"type": "matn",
     "ar": "فهو: ١- إما مفعل اسم مكان[[٨]]، بمعنى المقصد.",
     "en": "So it [the word maʿnā] is: (1) either mafʿal, a noun of place, in the sense of the object aimed at (al-maqṣid);"},
    {"type": "matn",
     "ar": "٢- أو مصدر ميمي[[٩]]، بمعنى المفعول[[١٠]].",
     "en": "(2) or a mīmī verbal noun (maṣdar mīmī), in the sense of the passive participle (the thing meant);"},
    {"type": "matn",
     "ar": "٣- أو مخفف معني[[١١]] اسم مفعول، كمرمي.",
     "en": "(3) or a lightened form of maʿniyy, a passive participle, like marmiyy (thrown)."},
    {"type": "matn",
     "ar": "ولما كان المعنى مأخوذا في الوضع، فذكر المعنى بعده[[١٢]] مبني على تجريده[[١٣]] عنه[[١٤]]،",
     "en": "Since “meaning” is already included within [the definition of] positing (waḍʿ), the mention of “meaning” after it is based upon abstracting it from it;"},
    {"type": "matn",
     "ar": "فخرج به[[١٥]] المهملات، والألفاظ الدالة بالطبع[[١٦]]؛ إذ لم يتعلق بها[[١٧]] وضع",
     "en": "so by it there are excluded the meaningless utterances (al-muhmalāt) and the expressions that signify by nature, since no positing attaches to them"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: عن تعريفه.",
     "en": "That is: from its definition."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: معنى الحرف.",
     "en": "That is: the meaning of the particle."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى: بل متى أطلق مع ضميمة.",
     "en": "The better [wording] is: “but only when it is uttered together with an adjunct.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولذا لم يكتف بـ«أحس». وكذا الحال في الوجه الثاني.",
     "en": "And that is why he was not content with [merely] “perceived” (aḥassa). Likewise is the case with the second aspect."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: أنه لا حاجة إلى التقييد، فإن المتبادر من الإطلاق الاستعمال في المقاصد، والاستعمال فيها لا يكون بدون الضميمة.",
     "en": "That is: there is no need for the qualification, for what comes readily to mind from “utterance” is [its] employment for [conveying] aims, and its employment for them does not occur without the adjunct."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: يستعمل تلك الألفاظ.",
     "en": "That is: [he] employs those expressions."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: اصطلاحا. وقد يكتفى فيه بصحة القصد.",
     "en": "That is: in technical usage. Sometimes the mere soundness of the intention suffices for it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "من مصدر المعلوم، أو المجهول.",
     "en": "[Derived] from the verbal noun of the active, or of the passive."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "للمعلوم والمجهول.",
     "en": "For [both] the active and the passive."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "يجوز ألا يعتبر نقله إليه، فيرتفع مؤنة النقل.",
     "en": "It is permissible not to regard it as having been transferred to it, so that the burden of [establishing] a transference (naql) is removed."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "تخفيفا غير قياسي. والذي جرأه على هذا الاحتمال مع بعده لفظا الميل إلى جانب المعنى، واستعمال المشدد بمعنى المخفف، فيقال: معنى الكلام ومعنيته واحد.",
     "en": "[This is] a non-standard lightening (takhfīf ghayr qiyāsī). What emboldened him to this possibility, despite its remoteness as regards wording, is the inclination toward the side of meaning, and the use of the geminated form in the sense of the lightened form; so one says: “the meaning (maʿnā) of speech and its being-meant (maʿniyya) are one.”"},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: بعد ذكر الوضع.",
     "en": "That is: after the mention of positing (waḍʿ)."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أي: على انتزاع المعنى.",
     "en": "That is: upon the abstraction of the meaning."},

    # ---------------- Footnote 14 ----------------
    {"type": "note", "num": "١٤"},
    {"type": "pair",
     "ar": "أي: عن الوضع.",
     "en": "That is: from positing."},

    # ---------------- Footnote 15 ----------------
    {"type": "note", "num": "١٥"},
    {"type": "pair",
     "ar": "أي: بقيد الوضع.",
     "en": "That is: by the restriction “positing.”"},

    # ---------------- Footnote 16 ----------------
    {"type": "note", "num": "١٦"},
    {"type": "pair",
     "ar": "وكذا الألفاظ الدالة بالعقل فقط، كما يدل عليه الدليل. ولك أن تجعل الطبع في مقابلة الوضع.",
     "en": "Likewise the expressions that signify by reason alone, as the proof indicates. You may [also] set [signification by] nature in opposition to positing."},

    # ---------------- Footnote 17 ----------------
    {"type": "note", "num": "١٧"},
    {"type": "pair",
     "ar": "أي: بالمهملات والألفاظ الدالة.",
     "en": "That is: to the meaningless utterances and the [naturally] signifying expressions."},
]
