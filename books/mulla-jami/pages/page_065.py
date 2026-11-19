# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 65 (printed ٦٤)."""

PAGE_NUMBER = 65
PRINTED_PAGE = "٦٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "يعرف أحكامها بالسماع منهم[[١]]، فإن العارف بأحكامها كذلك[[٢]] مستغن عن النحو، ولا فائدة له[[٣]] معتد بها في معرفة اصطلاحاتهم.",
     "en": "…[nor] come to know its rulings by direct audition from them (al-samāʿ); for one who knows its rulings in that manner is dispensed from grammar, and there is no benefit worth reckoning for him in knowing their [technical] conventions."},

    {"type": "matn",
     "ar": "فالمقصود من معرفة المعرب مثلا أنه يعرف[[٤]] مما يختلف آخره في كلامهم، ليجعل آخره مختلفا، فيطابق كلامهم[[٥]]، فمعرفته[[٦]] متقدمة على معرفة أنه مما يختلف آخره.",
     "en": "The intent behind knowing the muʿrab, for instance, is that it be recognized as among that whose ending varies in their speech, so that one may render its ending variable and thereby conform to their speech. Hence knowing it [in essence] is prior to knowing that it is among that whose ending varies."},

    {"type": "matn",
     "ar": "فلو كان معرفة آخره[[٧]] المتقدمة حاصلة بمعرفة هذا الاختلاف، وتعريفه به، فوجب أن يعرف أولا[[٨]] بأنه[[٩]] مما يختلف آخره[[١٠]] في كلام العرب ليعرف أنه[[١١]] مما يختلف آخره، فيلزم تقدم الشيء على نفسه.",
     "en": "So were the aforementioned knowledge of it [the muʿrab] attained through knowledge of this variation and through defining it thereby, then it would be necessary first to know it as being among that whose ending varies in the speech of the Arabs, in order that it be known as among that whose ending varies — which would entail a thing’s being prior to itself."},

    {"type": "matn",
     "ar": "فينبغي أن يعرف أولا ما عرفه به الجمهور، ويجعل ما عرفوه به من جملة أحكامه، كما فعله المصنف.",
     "en": "Therefore one ought first to know that by which the majority defined it, and to make what they defined it by one of its rulings — just as the author has done."},

    {"type": "matn",
     "ar": "(وحكمه) أي: من جملة أحكام المعرب، وآثاره المترتبة عليه من حيث هو معرب (أن يختلف آخره) أي: آخر المعرب، بأن يتبدل حرف آخر بحرف آخر حقيقة أو حكما[[١٢]] إذا كان إعرابه[[١٣]] بالحروف، أو صفة[[١٤]] بأن يتبدل صفة بصفة أخرى حقيقة أو حكما إذا كان إعرابه بالحركة، (باختلاف",
     "en": "“And its ruling (wa-ḥukmuhu)” — that is, one of the rulings of the muʿrab and its effects consequent upon it inasmuch as it is muʿrab — “is that its ending varies (an yakhtalifa ākhiruhu)” — that is, the ending of the muʿrab — by one final letter’s being exchanged for another final letter, whether really or in effect (ḥaqīqatan aw ḥukman), when its inflection is by letters; or [by exchange of] an attribute (ṣifa), by one attribute’s being exchanged for another really or in effect, when its inflection is by vowel-movement (ḥaraka) — “with the variation of (bi-khtilāf…”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: من العرب.",
     "en": "That is: from the Arabs."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: معرفة تتبع والسماع منهم مستغن عن تعلم ما جمعه المدون ورتبه، بخلاف من لم يتتبع أصلا، أو تتبع ولم يعرف أحكامها، فإنه محتاج إلى تعلم المدون.",
     "en": "That is: knowledge [gained] by tracing [Arab usage] and audition from them is independent of learning what the codifier (al-mudawwin) has collected and arranged — unlike one who has not traced [it] at all, or who has traced it but does not know its rulings, for he needs to learn what has been codified."},
    {"type": "pair",
     "ar": "وذلك التعلم إن كان مع الدليل، فذلك التعلم علم النحو اتفاقا، وإن لم يكن معه فهو علم النحو، أو حكاية عنه على اختلاف فيه.",
     "en": "And that learning, if it is accompanied by evidence (dalīl), is by agreement the science of grammar; and if it is not accompanied by it, then it is [either] the science of grammar or a report about it — there being a disagreement therein."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لذلك الشخص العارف.",
     "en": "That is: for that knowing person."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: المعرب.",
     "en": "That is: the muʿrab."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: كلام العرب.",
     "en": "That is: the speech of the Arabs."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: معرفة ذات المعرب.",
     "en": "That is: knowledge of the essence of the muʿrab."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: معرفة المعرب.",
     "en": "That is: knowledge of the muʿrab."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "المعرب.",
     "en": "The muʿrab."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: المعرب.",
     "en": "That is: the muʿrab."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "باختلاف العوامل.",
     "en": "By the variation of the governing agents."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: المعرب.",
     "en": "That is: the muʿrab."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "المراد بالتبدل الحقيقي تبدل ذات الدال، وبالتبدل الحكمي تبدل دلالته المقصودة مع بقاء الذات، فإن هذا التبدل في حكم تبدل الذات.",
     "en": "What is meant by real exchange (al-tabaddul al-ḥaqīqī) is the exchange of the very substance of the signifier (dhāt al-dāll); and by exchange in effect (al-tabaddul al-ḥukmī), the exchange of its intended signification while the substance remains — for this exchange has the status of the exchange of the substance."},

    # ---------------- Footnote 13 ----------------
    {"type": "note", "num": "١٣"},
    {"type": "pair",
     "ar": "أي: المعرب.",
     "en": "That is: the muʿrab."},

    # ---------------- Footnote 14 ----------------
    {"type": "note", "num": "١٤"},
    {"type": "pair",
     "ar": "أي: حالة شبيهة بالصفة لا صفة حقيقية؛ لأن الحركة لا تقوم بالحرف، بل تقوم بما يقوم به الحرف، لكنها تابعة له.",
     "en": "That is: a state resembling an attribute, not a real attribute; for the vowel-movement does not subsist in the [final] letter, but rather subsists in that in which the letter subsists — though it is subordinate to it."},
]
