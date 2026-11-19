# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 257 (printed ٢٥٦)."""

PAGE_NUMBER = 257
PRINTED_PAGE = "٢٥٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 256 ends with a complete sentence («طردا للباب.»); a new sentence begins here.
    {"type": "matn",
     "ar": "(ولا تتقدم) أي: الحال فيما عدا مثل: «زيد قائما كعمرو قاعدا»[[١]] (على العامل المعنوي[[٢]]).",
     "en": "(And it does not precede)—that is, the ḥāl (circumstantial qualifier), in cases other than such as “Zayd standing is like ʿAmr sitting”—(a governor of meaning [al-ʿāmil al-maʿnawī])."},
    {"type": "matn",
     "ar": "قد عرفت فيما قبل العامل المعنوي، وإنما هو مقدر بالفعل أو اسم الفاعل مثل الظرف وما يشبهه أعني: الجار والمجرور خارج عنه داخل في الفعل أو شبهه.",
     "en": "You have already learned earlier what the governor of meaning is: it is that which is construed as [implying] a verb or an active participle, such as the adverbial (ẓarf) and what resembles it, I mean the preposition and its object; it lies outside it [i.e., outside the verb], while [its meaning] is contained in the verb or what resembles it."},
    {"type": "matn",
     "ar": "فعلى هذا معنى الكلام[[٣]]: أن الحال لا يتقدم على العامل المعنوي اتفاقا[[٤]] (بخلاف الظرف) أي: بخلاف ما إذا كان العامل ظرفا أو شبهه، فإن فيه خلافا،",
     "en": "On this [reading], the meaning of the statement is: the ḥāl does not precede a governor of meaning, by agreement, (unlike the adverbial), that is, unlike the case where the governor is an adverbial or what resembles it, for in that there is disagreement:"},
    {"type": "matn",
     "ar": "فسيبويه لا يجوزه أصلا، نظرا إلى ضعف الظروف في العمل،",
     "en": "Sībawayh does not permit it at all, in view of the weakness of adverbials in governing;"},
    {"type": "matn",
     "ar": "وجوزه الأخفش بشرط تقدم المبتدأ على الحال نحو: «زيد قائما في الدار».",
     "en": "while al-Akhfash permits it on condition that the mubtadaʾ (subject) precedes the ḥāl, as in “Zayd, standing, is in the house.”"},
    {"type": "matn",
     "ar": "فأما مع تأخر المبتدأ عن الحال، فإنه وافق سيبويه في المنع، فلا يجوز «قائما زيد في الدار» ولا «قائما في الدار زيد» اتفاقا.",
     "en": "But where the mubtadaʾ comes after the ḥāl, he agrees with Sībawayh in forbidding it; so neither “standing, Zayd is in the house” nor “standing, in the house is Zayd” is permitted, by agreement."},
    {"type": "matn",
     "ar": "ويحتمل[[٥]] أن يكون معناه: أن الحال وإن كان مشابها للظرف لما فيه من معنى الظرفية، إلا أن الظرف يتقدم على عامله المعنوي، لتوسعهم في الظروف، والحال لا تتقدم عليه[[٦]].",
     "en": "It may also mean: although the ḥāl resembles the adverbial because of the sense of adverbiality (ẓarfiyya) in it, the adverbial may precede its governor of meaning, because of their latitude with adverbials, whereas the ḥāl may not precede it."},
    {"type": "matn",
     "ar": "هذا إذا لم يكن الظرف داخلا في العامل المعنوي. وأما",
     "en": "This is when the adverbial is not included in the governor of meaning. As for…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: فيما دل على حدثين غير متميزين بالعبارة مختلفين بالحال بأن يتعلق لكل منهما حال،",
     "en": "He means: in what denotes two events not distinguished in wording but differing in their ḥāl, in that a ḥāl attaches to each of them;"},
    {"type": "pair",
     "ar": "فإنه يجب أن يلي متعلق كل حدث صاحبه، وإن لزم التقدم على العامل الضعيف،",
     "en": "for what attaches to each event must follow its owner [ṣāḥib al-ḥāl], even if this entails preceding a weak governor."},
    {"type": "pair",
     "ar": "فإن التشبيه يدل على حدث قائم بالمشبه، وعلى حدث قائم بالمشبه به، وتعلق بما قام بالمشبه القيام، وبما قام بالمشبه به العقود.",
     "en": "For the comparison denotes an event subsisting in the thing compared and an event subsisting in that to which it is compared; “standing” attaches to what subsists in the thing compared, and “sitting” to what subsists in that to which it is compared."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولا على الفعل الغير المنصرف.",
     "en": "Nor [does it precede] an indeclinable (non-conjugating) verb."},
    {"type": "pair",
     "ar": "ولا على الفعل المصدر بما له صدر الكلام، ولا على المصدر بالحروف المصدرية، ولا على المصدر باللام الموصول، ولا على أفعل التفضيل فيما عدا هذا بسرا أطيب منه رطبا،",
     "en": "Nor a verb prefaced by something that takes the head of the sentence; nor one prefaced by the maṣdar particles; nor one prefaced by the relative lām; nor the elative (afʿal al-tafḍīl), except in [cases like] “this, as unripe dates, is better than it as ripe dates”;"},
    {"type": "pair",
     "ar": "فهو من قبيل زيدا قائما كعمرو قاعدا.",
     "en": "for that belongs to the same type as “Zayd standing is like ʿAmr sitting.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وحينئذ يكون قوله: بخلاف الظرف حالا عن قوله: على العامل المعنوي، كما أنه حال عن ضمير لا يتقدم على الاحتمال الثاني،",
     "en": "In that case his words “unlike the adverbial” are a ḥāl of his words “a governor of meaning,” just as on the second interpretation it is a ḥāl of the pronoun in “does not precede.”"},
    {"type": "pair",
     "ar": "ويحتمل أن يكون اعتراضية بتقدير المبتدأ.",
     "en": "It may also be parenthetical, with a mubtadaʾ understood."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كون مدار المخالفة بين العامل المعنوي والعامل الظرف، وكون أحدهما متفقا عليه، والآخر مختلفا فيه مما لا يفيده العبارة أصلا.",
     "en": "That the point of contrast lies between the governor of meaning and the adverbial governor, and that one is agreed upon and the other disputed, is something the wording does not convey at all."},
    {"type": "pair",
     "ar": "ولا يرضى به المتدرب في الاستفادة من دلالات الكلام،",
     "en": "Nor would one practised in drawing benefit from the significations of speech accept it."},
    {"type": "pair",
     "ar": "فالوجه أن يقال: المراد أنه لا يتقدم على العامل المعنوي أصلا بخلاف الظرف، فإنه يتقدم عليه في الجملة، وهو فيما تقدم المبتدأ على الحال، فيكون بناء الكلام على مذهب الأخفش،",
     "en": "The right approach is to say: what is meant is that it does not precede a governor of meaning at all, unlike the adverbial, for it does precede it in some cases, namely where the mubtadaʾ precedes the ḥāl; the statement is thus built on the doctrine of al-Akhfash."},
    {"type": "pair",
     "ar": "وبعد يتجه أن العامل المعنوي كما يخالف الظرف في عدم التقدم عليه أصلا بخلاف العامل الفعل والمشتق أيضا، فإن الحال يتقدم عليهما مطلقا،",
     "en": "Even so, it may be objected that the governor of meaning, just as it differs from the adverbial in that [the ḥāl] never precedes it, differs likewise from the verbal and the derived governor, for the ḥāl precedes these two without restriction;"},
    {"type": "pair",
     "ar": "فتخصيص المخالفة بالظرف مما لا بد له من وجه.",
     "en": "so restricting the contrast to the adverbial needs some justification."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فرق بين هذا الاحتمال والاحتمال السابق بأن قوله: بخلاف الظرف على هذا الاحتمال متعلق بضمير يتقدم، وعلى الاحتمال الأول بقوله: على العامل المعنوي حالا كان أو جملة معترضة.",
     "en": "The difference between this interpretation and the previous one is that his words “unlike the adverbial,” on this interpretation, attach to the pronoun in “precede,” and on the first interpretation to his words “a governor of meaning,” whether as a ḥāl or as a parenthetical clause."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه نظر؛ لأن الظرف لا يتقدم على العامل المعنوي الذي لم يكن ظرفا أو شبهه من الجار والمجرور،",
     "en": "This is open to question, because the adverbial does not precede a governor of meaning that is not an adverbial or something like it, a preposition and its object;"},
    {"type": "pair",
     "ar": "وإذا لم يدخل في العامل المعنوي لم يصح أن الظرف يتقدم على العامل المعنوي.",
     "en": "and if it is not included in the governor of meaning, it is not correct [to say] that the adverbial precedes the governor of meaning."},
]
