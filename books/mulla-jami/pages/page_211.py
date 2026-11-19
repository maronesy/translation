# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 211 (printed ٢١٠)."""

PAGE_NUMBER = 211
PRINTED_PAGE = "٢١٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "آلتي التعريف بلا فاصلة",
     "en": "…of the two instruments of definiteness without a separator;"},
    {"type": "matn",
     "ar": "(و«يا هذا الرجل»[[١]]) بتوسيط «هذا»[[٢]] (و«يا أيهذا الرجل») بتوسيط الأمرين معا.",
     "en": "(and “yā hādhā al-rajulu”—O this man) by interposing “hādhā,” (and “yā ayyuhādhā al-rajulu”) by interposing both together."},
    {"type": "matn",
     "ar": "(والتزموا[[٣]]) يعني: العرب (رفع «الرجل»[[٤]]) مثلا وإن كان صفة، وحقها جواز الوجهين: «الرفع والنصب» كما مر",
     "en": "(And they made obligatory)—meaning the Arabs—(the nominative of “al-rajul”), for example, even though it is a qualifier, whose due is that both forms be allowed, the nominative and the accusative, as has passed,"},
    {"type": "matn",
     "ar": "(لأنه) أي: «الرجل» مثلا (هو المقصود بالنداء[[٥]]) فالتزموا رفعه؛",
     "en": "(because it)—that is, “al-rajul,” for example—(is what is intended by the vocation); so they made its nominative obligatory,"},
    {"type": "matn",
     "ar": "لتكون حركته الإعرابية موافقة للحركة البنائية التي هي علامة المنادى، فيدل على أنه هو المقصود بالنداء،",
     "en": "so that its inflectional vowel matches the indeclinable vowel that is the mark of the vocative, and thus indicates that it is what is intended by the vocation."},
    {"type": "matn",
     "ar": "وهذا بمنزلة المستثنى عن قاعدة جواز الوجهين في صفة المنادى، ولهذا لم يذكر هناك ما يخرج صفة الاسم المبهم[[٦]] عن تلك القاعدة.",
     "en": "This is in the position of an exception to the rule allowing both forms in the qualifier of the vocative; for this reason he did not mention there what excludes the qualifier of the vague noun (al-ism al-mubham) from that rule."},
    {"type": "matn",
     "ar": "(وتوابعه) بالجر عطف على «الرجل» أي: والتزموا رفع توابع الرجل مضافة أو مفردة،",
     "en": "(And its appositives), in the genitive, coordinated with “al-rajul”; that is, they made obligatory the nominative of the appositives of “al-rajul,” whether annexed or singular,"},
    {"type": "matn",
     "ar": "نحو: «يا أيها الرجل الظريف، ويا أيها الرجل ذو المال»؛",
     "en": "as in: “O you witty man” (yā ayyuhā al-rajulu al-ẓarīfu) and “O you man of wealth” (yā ayyuhā al-rajulu dhū al-māli);"},
    {"type": "matn",
     "ar": "(لأنها توابع) منادى (معرب[[٧]]) وجواز الوجهين إنما يكون في توابع المنادى المبني.",
     "en": "(because they are appositives) of a (declinable) vocative, and the permissibility of both forms applies only to the appositives of an indeclinable vocative."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "والفرق بين «أيها» و«هذا» أن «أيها» لا يكون مقصودا بالنداء أصلا. وهذا يحتمل الأمرين،",
     "en": "The difference between “ayyuhā” and “hādhā” is that “ayyuhā” is never intended by the vocation at all, whereas “hādhā” admits both possibilities:"},
    {"type": "pair",
     "ar": "وإذا كان هذا مقصودا بالنداء، فالرجل مقصود بالصفة. فيجوز رفعه ونصبه،",
     "en": "when “hādhā” is intended by the vocation, “al-rajul” is intended as a qualifier, so both its nominative and accusative are allowed;"},
    {"type": "pair",
     "ar": "«هذا» إذا كان أي موصوفة. وأما إذا كان موصولة كما هو رأي الأخفش، فيجوز كونه مقصودا بالنداء مثل هذا، فتأمل.",
     "en": "this is when “ayy” is a qualified noun. But when it is a relative, as is al-Akhfash’s view, it may be intended by the vocation, like “hādhā”; so reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ليس نصا في الوصلة، فإنه قد يقصد نداؤه بخلاف أي، فإنه نص فيها،",
     "en": "[Hādhā] is not explicitly a link (wuṣla), for its vocation may itself be intended, unlike “ayy,” which is explicitly a link;"},
    {"type": "pair",
     "ar": "ولذلك قد يقتصر على هذا، ويؤتى بتابعه كما يؤتى بتابع تابعه،",
     "en": "for this reason one may confine oneself to “hādhā,” and its appositive may be brought just as the appositive of its appositive is brought;"},
    {"type": "pair",
     "ar": "فيقال: يا هذا الرجل وعبد الله معطوفا على هذا، ولا يجوز عطفه على الرجل؛ لأن المعطوف في حكم المعطوف عليه،",
     "en": "so one says “yā hādhā al-rajulu wa-ʿAbda llāhi,” coordinated with “hādhā”; its coordination with “al-rajul” is not allowed, because the coordinated noun has the rule of what it is coordinated with,"},
    {"type": "pair",
     "ar": "ويمتنع وصف باب هذا إلا بذي اللام،",
     "en": "and the class of “hādhā” cannot be qualified except by what bears the lām."},
    {"type": "pair",
     "ar": "ولا يجوز الاقتصار على أيها، ولا يؤتى بتابعه، بل يؤتى بتابع تابعه،",
     "en": "One may not confine oneself to “ayyuhā,” nor is its [own] appositive brought, but the appositive of its appositive;"},
    {"type": "pair",
     "ar": "فلا يصح يا أيها الرجل وعبد الله لامتناع وصف أيها إلا بذي اللام.",
     "en": "so “yā ayyuhā al-rajulu wa-ʿAbda llāhi” is not valid, since “ayyuhā” cannot be qualified except by what bears the lām."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه رد على الأخفش حيث جعل \"أي\" موصولة؛ لأنه على هذا التقدير لا حاجة إلى نكتة التزام الرفع.",
     "en": "In this is a rebuttal of al-Akhfash, who made “ayy” a relative; for on that supposition there is no need for a subtle reason for making the nominative obligatory."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يفهم من هذا القول أنه لم يختر مذهب الأخفش؛ لأنه على مذهبه لا حاجة إلى نكتة التزام رفع الرجل؛",
     "en": "It is understood from this statement that he did not adopt al-Akhfash’s position, because on his position there is no need for a subtle reason for making the nominative of “al-rajul” obligatory,"},
    {"type": "pair",
     "ar": "لأنه على مذهبه خبر مبتدأ، فيكون مرفوعا لا محالة.",
     "en": "since on his position it is the predicate of a mubtadaʾ, and so is necessarily nominative."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بحسب الواقع لا بحسب اللفظ، فإنه ذكر ليدل على معنى في المتبوع.",
     "en": "In fact, not in wording; for it is mentioned to indicate a meaning in the antecedent."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الذي جعل وسيلة إلى نداء المعرف باللام، وإلا فلا يجوز إخراج صفة الاسم المبهم مطلقا،",
     "en": "[That is, the vague noun] which is made a means to calling the noun made definite by the lām; otherwise excluding the qualifier of the vague noun unrestrictedly is not allowed,"},
    {"type": "pair",
     "ar": "فإن الاسم المبهم الذي كان مقصودا بالنداء، فصفته ترفع وتنصب، فلا وجه لإخراجه عن تلك القاعدة.",
     "en": "for when the vague noun is itself intended by the vocation, its qualifier takes the nominative and the accusative; so there is no ground for excluding it from that rule."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    # REVIEW: print reads «بالرفع والنصف»; evidently «والنصب»; transcribed as printed.
    {"type": "pair",
     "ar": "اندفع بتقدير المنادى ما يقال من أن تابع المعرب قد يجوز فيه الوجهان، نحو: إن زيدا قائم وعمرو بالرفع والنصف.",
     "en": "By supplying “vocative” is repelled what is said, that the appositive of a declinable noun sometimes admits both forms, as in “inna Zaydan qāʾimun wa-ʿAmrun,” with the nominative and the accusative."},
    {"type": "pair",
     "ar": "وقد يدفع أيضا بأن التنوين في معرب للوحدة، فلا ينتقض الحكم بالمثال المذكور؛",
     "en": "It is also repelled by [noting] that the tanwīn in “muʿrab” denotes oneness, so the rule is not broken by the said example,"},
    {"type": "pair",
     "ar": "لأن «عمرا» في المثال المذكور ليس تابعا لمعرب واحد، فإن «زيدا» باعتبار تعدد إعرابه معربان لا معرب واحد.",
     "en": "because “ʿAmr” in that example is not the appositive of one declinable noun; for “Zayd,” in view of its multiple inflections, is two declinables, not one."},
    {"type": "pair",
     "ar": "وفيه أن للمعرف باللام أيضا إعرابين. أما الرفع فظاهر. وأما النصب فلأنه منادى معنى، فيكون منصوب المحل.",
     "en": "Against this: the noun made definite by the lām also has two inflections. The nominative is evident; the accusative is because it is a vocative in meaning, and so accusative in position."},
]
