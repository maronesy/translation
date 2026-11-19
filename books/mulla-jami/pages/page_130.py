# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 130 (printed ١٢٩)."""

PAGE_NUMBER = 130
PRINTED_PAGE = "١٢٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "وكذا المراد في جميع حدود[[١]] المرفوعات والمنصوبات[[٢]] والمجرورات غير التوابع بقرينة ذكر التوابع بعدها[[٣]].",
     "en": "Likewise is [the qualifier of primacy] intended in all the definitions of the nominatives, the accusatives, and the genitives — exclusive of the dependents (al-tawābiʿ) — by the indication of mentioning the dependents after them."},
    {"type": "matn",
     "ar": "٢-(أو شبهه[[٤]]) أي: ما يشبهه في العمل[[٥]].",
     "en": "2. (Or what resembles it) — that is, what resembles it in governance (ʿamal)."},
    {"type": "matn",
     "ar": "وإنما قال ذلك؛ ليتناول فاعل «اسم الفاعل، والصفة المشبهة، والمصدر، واسم الفعل، وأفعل التفضيل، والظرف».",
     "en": "He said this only so that [the definition] might take in the agent of “the active participle (ism al-fāʿil), the assimilate epithet (al-ṣifa al-mushabbaha), the verbal noun (al-maṣdar), the verbal noun-of-command (ism al-fiʿl), the elative (afʿal al-tafḍīl), and the adverbial (al-ẓarf).”"},
    {"type": "matn",
     "ar": "(وقدم) أي: الفعل أو شبهه (عليه[[٦]]) أي: على ذلك الاسم.",
     "en": "(And is placed before) — that is, the verb or what resembles it — (it) — that is, before that noun."},
    {"type": "matn",
     "ar": "واحترز به عن نحو: «زيد» في «زيد ضرب»؛ لأنه مما أسند إليه الفعل[[٧]]؛ لأن الإسناد إلى ضمير شيء إسناد إليه في الحقيقة[[٨]]، لكنه مؤخر عنه.",
     "en": "By it he guards against the like of “Zayd” in “Zaydun ḍaraba” (Zayd, he struck); for it is something to which the verb has been predicated, since predication to a pronoun of a thing is in reality predication to that thing — but here it is postponed after it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: لا بد من اعتبار قيد الأصالة في تعريفات هذه الثلاثة لإخراج توابعها.",
     "en": "That is: the qualification of primacy (al-aṣāla) must be taken into account in the definitions of these three [cases] in order to exclude their dependents."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: لا بد من اعتبار الأصالة في تعريفات تلك المصطلحات لإخراج توابعها، فتأمل.",
     "en": "That is: primacy must be taken into account in the definitions of those technical terms in order to exclude their dependents — so reflect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا يخفى بعدها عن التعريف.",
     "en": "Their remoteness from the definition is not hidden."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "«أو» للتنويع لا للشك أو التشكيك.",
     "en": "“Or” is for classification (tanwīʿ), not for doubt or the casting of doubt."},
    {"type": "pair",
     "ar": "قال عصمت: «أو شبهه» لا يقال: ذكر «أو» التي للترديد، والشك لا يلائم في التعريف الذي هو للتعيين والتحقيق؛",
     "en": "ʿIṣmat said: regarding “or what resembles it,” one may not object that “or” — which serves for alternation — [is used], while doubt is unsuited to a definition, whose purpose is determination and verification;"},
    {"type": "pair",
     "ar": "لأنا نقول: كلمة «أو» ههنا للتنويع إشارة إلى أن الفاعل المعرف ههنا نوعان: يصدق على أحدهما ما أسند إليه الفعل، وعلى الآخر ما أسند إليه شبه الفعل.",
     "en": "because we say: the word “or” here is for classification, indicating that the agent being defined is here of two kinds: to the one applies “that to which the verb is predicated,” and to the other “that to which the verb-resembling word is predicated.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أو في الدلالة على الحدث، ولا يخرج فاعل الظرف؛ لأنه فاعل لعامله حقيقة.",
     "en": "Or [resemblance] in signifying the event (al-ḥadath); and the agent of the adverbial is not excluded, since it is really the agent of its governor."},
    {"type": "pair",
     "ar": "قال العصام: قوله: «أي: ما يشبهه في العمل» لم يقل: «في الاشتقاق» لئلا يخرج المصدر، ولا في الدلالة على الحدث لئلا يخرج الظرف.",
     "en": "Al-ʿIṣām said: his words “that is, what resembles it in governance” — he did not say “in derivation (ishtiqāq),” lest the verbal noun be excluded, nor “in signifying the event,” lest the adverbial be excluded."},
    {"type": "pair",
     "ar": "والأظهر أن إطلاق شبه الفعل على هذه الأمور قبل العمل؛ لأنهم يعللون عمل هذه الأمور بمشابهة الفعل، فالأولى أن يفسر بالمشابهة في الدلالة على الحدث،",
     "en": "The more evident view is that applying “resembling the verb” to these items precedes [their] governance; for they justify the governance of these items by resemblance to the verb, so it is preferable to interpret it as resemblance in signifying the event,"},
    {"type": "pair",
     "ar": "والظرف أيضا يدل على الحصول والثبوت، كأنه يشارك صيغة الحاصل في تلك، ولذا وجب حذف عامله.",
     "en": "and the adverbial too signifies occurrence and establishment, as though it shares in the form of “that which occurs” in that [respect] — and for this reason the deletion of its governor is obligatory."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "عطف على «أسند»، الجملة حالية بتقدير «قد»، والضمير فيه راجع إلى أحد الأمرين المستفاد من لفظة «أو».",
     "en": "It is conjoined to “predicated”; the clause is circumstantial (ḥāliyya) with an implicit “qad,” and the pronoun in it refers back to one of the two things understood from the word “or.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "رد على المصنف ومن يحذو حذوه في جعل قوله: «وقدم» لدفع توهم فاعلية «زيد» في المثال المذكور بناء على توهم إسناد «ضرب» إلى «زيد»، والغفلة عن الضمير المستتر.",
     "en": "A refutation of the author and those who follow his lead in taking his words “and is placed before” to be for repelling the illusion that “Zayd” is the agent in the cited example — an illusion based on supposing “ḍaraba” to be predicated of “Zayd,” and on heedlessness of the concealed pronoun."},
    {"type": "pair",
     "ar": "وإنما احتاجوا إلى هذا التكلف لحملهم الإسناد على الإسناد بحسب دلالة اللفظ كما هو الظاهر.",
     "en": "They needed this labored device only because they construed “predication” as predication according to the signification of the wording, as is apparent."},
    {"type": "pair",
     "ar": "واعلم أن تعريف الفاعل على رأي البصريين إنما يتميز عن تعريفه على رأي الكوفيين بهذا القيد، فإن «زيد» في المثال المذكور فاعل عند الكوفيين،",
     "en": "Know that the definition of the agent according to the view of the Baṣrans is distinguished from its definition according to the view of the Kūfans only by this qualifier; for “Zayd” in the cited example is an agent according to the Kūfans,"},
    {"type": "pair",
     "ar": "فلهم مزيد اهتمام بذكر هذا القيد احتيج إليه لتمام التعريف، كما ذهب إليه الشارح أولا كما ذهب إليه غيره.",
     "en": "so they have added concern for mentioning this qualifier, which is needed for the completeness of the definition — as the commentator held at first, and as others held too."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لأنه مقرر الإسناد، ولو أريد الإسناد بحسب الدلالة اللغوية لكان ذكر قوله: «قدم» لرفع توهم الدخول، وإليه مال المصنف في شرح الإيضاح.",
     "en": "Because it is what establishes the predication; and had predication according to linguistic signification been intended, then the mention of his words “is placed before” would have been for removing the illusion of [Zayd’s] inclusion — and to this the author inclined in his commentary on al-Īḍāḥ."},
]
