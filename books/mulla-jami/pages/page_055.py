# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 55 (printed ٥٤)."""

PAGE_NUMBER = 55
PRINTED_PAGE = "٥٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "بينه وبين غيره، بل تلك الجزئيات لا تتعقل إلا بذكر متعلقاتها، لتكون آلات لملاحظة أحوالها[[١]] بقولهم[[٢]]: إن الحرف تدل على معنى في غيرها.",
     "en": "…between it and something else; rather, those particulars cannot be conceived except through the mention of the things related to them, so that they may serve as instruments for observing their states, according to their statement: “the ḥarf (particle) signifies a meaning in [something] other than itself.”"},
    {"type": "matn",
     "ar": "وإذا عرفت هذا علمت[[٣]] أن المراد بكينونة المعنى في نفسه: استقلاله بالمفهومية، وبكينونة المعنى في نفس الكلمة: دلالتها[[٤]] عليه من غير حاجة إلى ضم كلمة أخرى إليها، لاستقلاله[[٥]] بالمفهومية.",
     "en": "Once you have grasped this, you know that what is meant by “the meaning’s being in itself” is its independence in conceivability (istiqlāl bi-l-mafhūmiyya); and [what is meant] by “the meaning’s being in the word itself” is its [the word’s] signifying it without need to adjoin another word to it, on account of its [the meaning’s] independence in conceivability."},
    {"type": "matn",
     "ar": "فمرجع كينونة المعنى[[٦]] في نفسه، وكينونته في نفس الكلمة الدالة عليه إلى أمر واحد، وهو استقلاله[[٧]] بالمفهومية.",
     "en": "So the reference-point of the meaning’s being in itself, and its being in the word that signifies it, comes back to a single matter — namely, its independence in conceivability."},
    {"type": "matn",
     "ar": "ففي هذا الكتاب[[٨]] الضمير المجرور في «نفسه»:",
     "en": "So in this book, the pronoun in the genitive in “[fī] nafsihi” (in itself):"},
    {"type": "matn",
     "ar": "١- يحتمل أن يرجع إلى «ما» الموصولة، التي هي عبارة عن الكلمة، وهذا هو الظاهر، ليكون على طبق ما سبق[[٩]] في وجه الحصر من كينونة المعنى في نفس الكلمة.",
     "en": "1. It may refer back to the relative “mā,” which stands for “the word” — and this is the more apparent [reading] — so that it conforms to what preceded regarding the ground of the restriction, [namely] the meaning’s being in the word itself."},
    {"type": "matn",
     "ar": "٢- ويحتمل أن يرجع إلى المعنى تنبيها على صحة إرادة كلا المعنيين[[١٠]]، ولكن عبارة «المفصل» ظاهرة في المعنى الأخير[[١١]]، وإرجاع الضمير إلى المعنى[[١٢]]، لعدم مسبوقيتها[[١٣]]…",
     "en": "2. Or it may refer back to “the meaning,” by way of drawing attention to the soundness of intending both meanings; yet the wording of al-Mufaṣṣal is apparent in [favoring] the latter meaning and the referral of the pronoun to “the meaning,” since it is not preceded…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: أحوال المتعلقات.",
     "en": "That is: the states of the correlated terms (al-mutaʿallaqāt)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: بقول النحاة.",
     "en": "That is: according to the statement of the grammarians (al-nuḥāt)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وعلمت أيضا أن كينونة المعنى في غيره من المعاني أو في كلمة أخرى عدم الاستقلال بالمفهومية.",
     "en": "You also come to know that the meaning’s being in something else — [whether] in [another of] the meanings or in another word — is [its] lack of independence in conceivability."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الكلمة.",
     "en": "That is: the word (al-kalima)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: المعنى.",
     "en": "That is: the meaning (al-maʿnā)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "مبتدأ خبره قوله: إلى أمر واحد، وهو مصدر ميمي بقرينة ذكر «إلى»، أي: فرجوعهما إليه. وفي بعض النسخ لم يوجد كلمة «إلى»، فالمرجع حينئذ اسم مكان.",
     "en": "[Marjiʿ, “reference,” is] a subject (mubtadaʾ) whose predicate is his words “to a single matter”; it is a mīmī verbal noun (maṣdar mīmī), by the indication of the mention of “ilā” (to) — that is: “their returning to it.” In some copies the word “ilā” does not occur, in which case marjiʿ is a noun of place (ism makān)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: المعنى.",
     "en": "That is: the meaning."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "جواب شرط مقدر أي: إذا كان رجوع الكينونتين إلى أمر واحد، ففي هذا الكتاب أعني: الكافية الضمير المجرور إلى آخره.",
     "en": "[This is] the apodosis of an implied conditional; that is: “Since the two modes of being return to a single matter, then in this book” — I mean al-Kāfiya — “the genitive pronoun…,” and so on."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "وليوافق بالضمير الذي قبله، وهو ضمير «دل»، ولأنه لا يحتاج حينئذ إلى صرف كلمة «في» عن معناها الحقيقي، فتأمل.",
     "en": "And so that it may agree with the pronoun preceding it — namely the pronoun in “dalla” (it signified) — and because in that case there is no need to divert the word “fī” (in) from its literal sense; so reflect."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أحدهما: أن يكون في نفس ما دل. والثاني: أن يكون في نفس المعنى.",
     "en": "One of the two: that it be in the very [word] that signifies. The second: that it be in the meaning itself."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: كون المعنى ملحوظا في نفسه. وذلك لقرب المرجع ورد العبارة إلى ما هو المشهور، وحملها على ما هو ملاك امتياز الحرف عن أخويه.",
     "en": "That is: the meaning’s being regarded in itself. This is on account of the nearness of the referent, the restoring of the wording to what is well-known, and construing it in accordance with what constitutes the criterion distinguishing the ḥarf from its two sisters [the ism and the fiʿl]."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: لم يصرف عن الظاهر بإرجاع الضمير إلى «ما»، كما في عبارة هذا الكتاب لعدم مسبوقيتها إلى آخره.",
     "en": "That is: it is not diverted from the apparent [sense] by referring the pronoun to “mā,” as in the wording of this book, on account of its not being preceded [by a prior mention], and so on."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أشار إلى أن الظاهر من نفس العبارة المعنى الأخير، ولا يصار إلى المعنى الأول إلا لداع، وكان وجه قرب مرجع الضمير وشيوع المعنى الأخير. قال ابن مالك في التسهيل: إذا دار الضمير بين الأقرب والأبعد فهو للأقرب.",
     "en": "He indicated that the apparent [reading] from the wording itself is the latter meaning, and one does not resort to the first meaning save for a [compelling] motive; the aspect [here] being the nearness of the pronoun’s referent and the prevalence of the latter meaning. Ibn Mālik said in al-Tashīl: when a pronoun hovers between the nearer and the farther [candidate], it belongs to the nearer."},
]
