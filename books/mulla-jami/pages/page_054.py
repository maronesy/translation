# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 54 (printed ٥٣)."""

PAGE_NUMBER = 54
PRINTED_PAGE = "٥٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (continued from p. ٥٢) ----------------
    {"type": "matn",
     "ar": "لاحظه[[١]] العقل من حيث هو[[٢]] حالة بين السير والبصرة[[٣]] مثلا، وجعله آلة لتعرف حالهما[[٤]]، كان معنى غير مستقل بالمفهومية[[٥]]، لا يصلح أن يكون محكوما عليه وبه.",
     "en": "the intellect observes it[[١]] merely as it is[[٢]] — a state between the journey and Basra[[٣]], for example — and makes it an instrument for knowing the state of the two[[٤]], it is a meaning not independent in conceivability[[٥]], unfit to be predicated upon or by."},
    {"type": "matn",
     "ar": "ولا يمكن أن يتعقل[[٦]]، إلا بذكر متعلقه بخصوصه، ولا أن يدل عليه[[٧]]، إلا بضم كلمة دالة على متعلقه.",
     "en": "And it cannot be conceived[[٦]] except by mentioning its correlate specifically, nor can it be signified[[٧]] except by adjoining a word that signifies its correlate."},
    {"type": "matn",
     "ar": "والحاصل[[٨]]: أن لفظ «الابتداء» موضوع لمعنى كلي، ولفظة «من» موضوعة لكل واحد من جزئياته[[٩]] المخصوصة المتعلقة، من حيث إنها[[١٠]] حالات لمتعلقاتها[[١١]]، وآلات لتعرف أحوالها[[١٢]]،",
     "en": "In sum[[٨]]: the word «al-ibtidāʾ» is posited for a universal meaning, while the word «min» is posited for each one of its particular, specified, correlated instances[[٩]], inasmuch as they[[١٠]] are states pertaining to their correlates[[١١]] and instruments for knowing their conditions[[١٢]];"},
    {"type": "matn",
     "ar": "وذلك المعنى الكلي يمكن أن يتعقل قصدا، ويلاحظ في حد ذاته، فيستقل بالمفهومية، ويصلح أيضا أن يكون محكوما عليه وبه.",
     "en": "and that universal meaning can be conceived intentionally and observed in its own right, so that it is independent in conceivability and is also fit to be predicated upon and by."},
    {"type": "matn",
     "ar": "وأما تلك الجزئيات فلا تستقل بالمفهومية، ولا تصلح أن تكون محكوما عليها وبها؛ إذ لا بد في كل منهما[[١٣]] أن يكون ملحوظا قصدا، ليمكن أن تعتبر النسبة[[١٤]]",
     "en": "As for those particulars, they are not independent in conceivability, nor are they fit to be predicated upon or by; for each of the two[[١٣]] must be observed intentionally, so that the relation may be considered[[١٤]]"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: مفهوم لفظ الابتداء.",
     "en": "That is: the concept of the word «al-ibtidāʾ»."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: مفهوم لفظ الابتداء.",
     "en": "That is: the concept of the word «al-ibtidāʾ»."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهو معنى قائم بالسير بالقياس إلى البصرة.",
     "en": "It is a meaning subsisting in the journey (al-sayr) in relation to Basra."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: كون السير مبتدأ، وكون البصرة مبتدأ منه.",
     "en": "That is: the journey’s being a starting point, and Basra’s being that from which one starts."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: معنى متلبسا بالتبع.",
     "en": "That is: a meaning adhered to dependently."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: لا يمكن معرفة ذلك الابتداء المأخوذ على هذا الوجه إلا بذكر متعلقه المخصوص. ثم المتعلق إما المتكلم إن كان الذكر بالضم، أو السامع إن كان بالكسر.",
     "en": "That is: that inception, taken in this manner, cannot be known except by mentioning its specific correlate. Then the correlate is either the speaker — if «mention» (al-dhikr) is read with a ḍamma — or the hearer — if it is read with a kasra."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بصيغة المجهول. وفاعله المحذوف هو المتكلم، فالدلالة بمعنى الإرشاد.",
     "en": "In the passive form; its omitted agent is the speaker, so «signification» (al-dalāla) here has the sense of guidance (irshād)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: حاصل الفرق بين لفظ الابتداء وبين لفظ «من».",
     "en": "That is: the upshot of the difference between the word «al-ibtidāʾ» and the word «min»."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لأنه لا تستعمل إلا في الجزئيات، ويعلم الوضع بالاستعمال، والقول بأنه مجاز لا حقيقة له مما لا ضرورة فيه.",
     "en": "Because it is used only for the particulars, and the [manner of] positing is known through usage; and the claim that it is figurative with no literal sense to it is among that for which there is no necessity."},
    {"type": "pair",
     "ar": "ثم الظاهر أن تلك جزئيات إضافية كما قيل، لأنها حصص لمفهوم الابتداء لوحظت تبعا، وإثبات الأفراد له مما لا شاهد عليه. والظاهر أيضا أنه يجوز أن يلاحظ قصدا. والظاهر أيضا أنه يبقى حينئذ معنى حرفيا.",
     "en": "Then the apparent [view] is that those are relative particulars, as has been said, for they are portions of the concept of inception observed dependently; and affirming self-standing individuals for it has no evidence to support it. It is also apparent that it may be observed intentionally, and also that it then remains a particle-meaning."},
    {"type": "pair",
     "ar": "قيل: إن معنى «من» ليس من جزئيات الابتداء، بل الابتداء من لوازمه، وأنه في نفسه يأبى عن الالتفات إليه قصدا.",
     "en": "It has been said: the meaning of «min» is not one of the particulars of inception; rather inception is one of its concomitants, and it in itself refuses to be attended to intentionally."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: تلك الجزئيات.",
     "en": "That is: those particulars."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: لمتعلقات أنفسها.",
     "en": "That is: for their own correlates."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: أحوال المتعلقات.",
     "en": "That is: the conditions of the correlates."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أي: من المحكوم عليه ومن المحكوم به.",
     "en": "That is: of the subject (al-maḥkūm ʿalayhi) and the predicate (al-maḥkūm bihi)."},

    # ---------------- Footnote 14 ----------------
    {"type": "note", "num": "١٤"},
    {"type": "pair",
     "ar": "فيه منع، فإن كلا في «إنسان كاتب» آلة لملاحظة أفراده مع اعتبار النسبة بينه وبين غيره، فلا بد من التخصيص.",
     "en": "This is disputable, for each [term] in [the proposition] «a human being is a writer» is an instrument for observing its individuals together with considering the relation between it and another; so specification is unavoidable."},
]
