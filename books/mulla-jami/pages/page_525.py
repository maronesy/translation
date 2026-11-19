# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 525 (printed ٥٢٤)."""

PAGE_NUMBER = 525
PRINTED_PAGE = "٥٢٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(ويجوز تقديم أخبارها) … (كلها على أسمائها)؛ إذ» at the foot of PDF p. 524 (mid-sentence).
    {"type": "matn",
     "ar": "ليس فيها[[١]] إلا تقديم المنصوب على المرفوع فيما عامله فعل،",
     "en": "…there is in it nothing but placing the accusative before the nominative in what is governed by a verb."},
    {"type": "matn",
     "ar": "فإن أريد بجواز التقديم[[٢]] نفي الضرورة عن جانبي وجوده وعدمه، فينبغي أن يقيد[[٣]] بمثل قولنا: «ما لم يعرض ما يقتضي تقديمها عليها» نحو: «كم كان مالك؟»[[٤]]، أو تأخيرها عنها نحو: «صار عدوي صديقي»،",
     "en": "If by the permissibility of placing first is meant the negation of necessity on both sides, its occurrence and its non-occurrence, then it should be qualified by something like our saying “as long as nothing arises that requires placing them before them”, as in “kam kāna māluka?” (how much was your wealth?), “or placing them after them”, as in “ṣāra ʿaduwwī ṣadīqī” (my enemy became my friend);"},
    {"type": "matn",
     "ar": "وإن أريد به نفي الضرورة عن جانب العدم فقط، فينبغي أن يقيد بمثل قولنا: «إذا لم يمنع مانع من التقديم»، وحينئذ يجوز أن يكون واجبا كالمثال المذكور.",
     "en": "and if by it is meant the negation of necessity on the side of non-occurrence only, then it should be qualified by something like our saying “when no obstacle prevents placing first”; in that case it may be obligatory, as in the example mentioned."},
    {"type": "matn",
     "ar": "(وهي) أي: الأفعال الناقصة[[٥]] (في تقديمها) أي: تقديم أخبارها (عليها) أي: على تلك الأفعال واقعة (على ثلاثة أقسام):",
     "en": "(And they), that is, the incomplete verbs, (with respect to placing them), that is, their predicates, (before them), that is, before those verbs, fall (into three classes):"},
    {"type": "matn",
     "ar": "١-(قسم يجوز) تقديم أخبارها عليها (وهو من «كان» إلى «راح»[[٦]]) وهو أحد عشر فعلا؛ لكونها أفعالا، وجواز[[٧]] تقديم المنصوب على المرفوع في الأفعال لقوتها.",
     "en": "1. (A class in which) placing their predicates before them (is permissible; it is from “kāna” to “rāḥa”), eleven verbs, because they are verbs, and placing the accusative before the nominative is permissible with verbs because of their strength."},
    {"type": "matn",
     "ar": "٢-(وقسم لا يجوز) تقديم أخبارها عليها (وهو) أي: هذا القسم (ما في أوله) كلمة («ما») نافية كانت أو مصدرية.",
     "en": "2. (And a class in which) placing their predicates before them (is not permissible; it is), that is, this class, (what has at its beginning) the word (“mā”), whether negative or maṣdariyya."},
    {"type": "matn",
     "ar": "أما إذا كانت نافية فلامتناع تقديم «ما» في حيز النفي؛ لأنه يقتضي التصدر.",
     "en": "As for when it is negative, it is because placing what lies within the scope of negation before it is impossible, since [negation] requires the head position."},
    {"type": "matn",
     "ar": "وأما إذا كانت مصدرية فلامتناع تقديم معمول المصدر على نفس المصدر،",
     "en": "And as for when it is maṣdariyya, it is because placing what is governed by a verbal noun before the verbal noun itself is impossible."},
    {"type": "matn",
     "ar": "ويخالف هذا الحكم (خلافا) ثابتا (لابن كيسان[[٨]]) بأن يكون هذا الخلاف",
     "en": "This ruling is opposed, (contrary) [to the view] held (by Ibn Kaysān), in that this disagreement is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: في تقديم الأخبار، والتأنيث باعتبار المضاف إليه.",
     "en": "That is, in placing the predicates first; the feminine [pronoun] is in regard of the second term of the genitive construction."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يمكن أن يختار هذا الشق، ويراد أنه يجوز تقديم أخبارها على أسمائها بمعنى أنها لا تمنع من هذا التقديم،",
     "en": "One may choose this alternative and mean that placing their predicates before their nouns is permissible, in the sense that they do not prevent this placing first;"},
    {"type": "pair",
     "ar": "والموانع العارضة قد علم حكمها، فلا حاجة إلى التعرض لها هنا.",
     "en": "the ruling on accidental obstacles is already known, so there is no need to address them here."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "والتقييد إما بأن يكون الإطلاق قرينة التجريد عما سواه، أو باشتهار أن عدم المانع معتبر في حصول كل شيء.",
     "en": "The qualification [is supplied] either in that the unqualified statement is an indication of its being divested of everything else, or by its being well known that the absence of an obstacle is a condition for the occurrence of anything."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الظاهر أن هذا بمعزل عما هو فيه؛ إذ الكلام في تقديم الخبر على مجرد الاسم، وهذا المثال داخل في تقديم الخبر على نفس الفعل.",
     "en": "Apparently this is beside the point, since the discussion concerns placing the predicate before the noun alone, whereas this example falls under placing the predicate before the verb itself."},
    {"type": "pair",
     "ar": "نعم هذا يتجه على قوله: قسم يجوز.",
     "en": "Yes, this applies to his words “a class in which it is permissible”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    # REVIEW: printed «إلا أنه صرفة إلى الأفعال الناقصة» with tāʾ marbūṭa; «صرفه» (he directed it) seems intended. Transcribed as printed.
    {"type": "pair",
     "ar": "الأنسب لسياق الكلام أن هي راجعة إلى الأخبار إلا أنه صرفة إلى الأفعال الناقصة لاقتضاء ظاهر قوله: وهو من «كان» إلى «راح» وأخواته ذلك.",
     "en": "More fitting to the context is that “hiya” refers back to the predicates; but he directed it to the incomplete verbs because the apparent sense of his words “it is from ‘kāna’ to ‘rāḥa’” and its sisters requires that."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: في التركيب الذي ذكره المصنف. وغايته داخلة في المغيا بقرينة المقام.",
     "en": "That is, in the arrangement the author mentioned. Its end-point is included in what it bounds, by the indication of the context."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يعد اللام إشارة إلى أن المجموع دليل واحد، فالجزء الأول لإثبات أنه لا مانع من جانب العامل، والجزء الثاني لإثبات أنه لا مانع من جانب المرفوع",
     "en": "He did not repeat the lām, to indicate that the whole is a single proof: the first part establishes that there is no obstacle on the side of the governor, and the second part establishes that there is no obstacle on the side of the nominative."},
    {"type": "pair",
     "ar": "فمن قال: إنه سهو من طغيان القلم. والصواب: وجواز تقديم المنصوب على الأفعال، فقد سها.",
     "en": "So whoever said “it is an oversight, a slip of the pen, and the correct reading is ‘and the permissibility of placing the accusative before the verbs’” has himself erred."},

    # ---------------- Footnote 8 (runs on to the next page) ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: printed «لعدم قولهم بتقدير "ما"»; «بتصدير» (head position) seems intended by the sense. Transcribed as printed; the translation follows the apparent sense.
    {"type": "pair",
     "ar": "الخلاف في الأفعال الأربعة مختص بابن كيسان، والكوفيون يجوزون تقديم معمول ما في حيز ما مطلقا لعدم قولهم بتقدير \"ما\" على ما في شرح التسهيل ناقلا عن ابن مالك،",
     "en": "The disagreement concerning the four verbs is peculiar to Ibn Kaysān; the Kūfans permit placing first what is governed within the scope of “mā” without restriction, because they do not hold that “mā” is [given] the head position, according to what is in Sharḥ al-Tashīl, citing Ibn Mālik."},
    {"type": "pair",
     "ar": "فما قيل: الخلاف لا",
     "en": "So what has been said, “the disagreement is not…”"},
]
