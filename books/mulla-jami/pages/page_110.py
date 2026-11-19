# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 110 (printed ١٠٩)."""

PAGE_NUMBER = 110
PRINTED_PAGE = "١٠٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "وتقرير الجواب: أن «حضاجر» حال كونه علما للضبع (غير منصرف) لا للجمعية الحالية، بل للجمعية الأصلية[[١]]؛",
     "en": "The articulation of the reply is: that “ḥaḍājir,” in the state of its being a proper name for the hyena, (is indeclinable) — not on account of actual [present] plurality, but on account of original plurality (al-jamʿiyya al-aṣliyya);"},
    {"type": "matn",
     "ar": "(لأنه منقول عن الجمع[[٢]]) فإنه كان في الأصل جمع «حضجر» بمعنى: عظيم البطن، سمي به الضبع مبالغة في عظم بطنها، كأن كل فرد منها جماعة من هذا الجنس، فالمعتبر في منع صرفه، هو الجمعية الأصلية.",
     "en": "(because it is transferred from a plural) — for it was originally the plural of “ḥiḍajr,” meaning “great of belly”; the hyena was named by it as a hyperbole regarding the largeness of its belly, as though each individual of it were a whole company of this genus. So what is reckoned in preventing its declension is the original plurality."},
    {"type": "matn",
     "ar": "فإن قلت: لا حاجة في منع صرفه إلى اعتبار الجمعية الأصلية، فإن فيه العلمية والتأنيث؛ لأن الضبع هي أنثى الضبعان؟",
     "en": "If you say: there is no need, in preventing its declension, to reckon original plurality, for in it there are proper-namehood and femininity — since the ḍabuʿ (hyena, fem.) is the female of the ḍibʿān (male hyena)?"},
    {"type": "matn",
     "ar": "قلنا: علميته غير مؤثرة، وإلا لكان بعد التنكير منصرفا، والتأنيث غير مسلم؛ لأنه علم لجنس الضبع، مذكرا كان أو مؤنثا.",
     "en": "We say: its proper-namehood has no effect, otherwise it would be declinable after being made indefinite; and its femininity is not granted, because it is a proper name for the genus of the hyena, whether male or female."},
    {"type": "matn",
     "ar": "وإنما اكتفى المصنف في التنبيه على اعتبار الجمعية الأصلية بهذا القول، ولم يقل: «الجمع شرطه: أن يكون في الأصل» كما قال في الوصف؛ لئلا يتوهم[[٣]] أن الجمعية كالوصف[[٤]]،",
     "en": "The author contented himself, in alerting [the reader] to the reckoning of original plurality, with this statement, and did not say: “the plural — its condition is that it be [a plural] in the original,” as he said regarding the attribute (waṣf), lest it be imagined that plurality is like the attribute —"},
    {"type": "matn",
     "ar": "قد تكون أصلية معتبرة، وقد تكون عارضة غير معتبرة، وليس الأمر كذلك؛ إذ لا يتصور العروض في الجمعية.",
     "en": "[which] may be original and reckoned, or may be accidental (ʿāriḍa) and not reckoned — whereas the matter is not so, since accidentality (ʿurūḍ) cannot be conceived in plurality."},
    {"type": "matn",
     "ar": "(وسراويل) جواب عن سؤال مقدر تقديره أن يقال: قد تفصيت عن الإشكال[[٥]] الوارد على قاعدة الجمع بـ«حضاجر» بجعل الجمع أعم من أن يكون في الحال أو في الأصل،",
     "en": "(And sarāwīl) is a reply to an implicit question whose purport is that it be said: You have extricated yourself from the difficulty besetting the rule of the plural in the case of “ḥaḍājir,” by making “the plural” more general than [the distinction between] its being [a plural] actually or in the original;"},
    {"type": "matn",
     "ar": "فما تقول في سراويل فإنه اسم جنس يطلق على الواحد والكثير، ولا جمعية فيه لا في الحال ولا في الأصل؟",
     "en": "so what do you say about “sarāwīl,” for it is a generic noun applied to the single and to the many, and there is no plurality in it, neither actually nor in the original?"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الجمعية وإن كانت منافية للعلمية كالوصفية، لكن اعتبارها ليس مع اعتبار العلمية حتى يلزم اعتبار المتضادين في حكم واحد.",
     "en": "Plurality, although it is contrary to proper-namehood — as [is] attribution (waṣfiyya) — yet its being reckoned is not [simultaneous] with the reckoning of proper-namehood, such that the reckoning of two contraries in a single ruling would be entailed."},
    {"type": "pair",
     "ar": "ومن قال الجمعية غير منافية للعلمية لجواز تسمية الأشخاص برجال، فلم يأت بشيء؛ لأن نوع الإبهام مناف للعلمية لازم لمعنى الجمعية، كما أن الإبهام المنافي للعلمية لازم لمعنى الوصفية.",
     "en": "And whoever said that plurality is not contrary to proper-namehood — on the grounds that persons may be named “Rijāl (Men)” — has produced nothing [cogent]; for the kind of ambiguity (ibhām) that is contrary to proper-namehood is inseparable from the meaning of plurality, just as the ambiguity contrary to proper-namehood is inseparable from the meaning of attribution."},
    {"type": "pair",
     "ar": "نعم يجوز أن يبقى شائبة من معنى الجمعية في العلم، كما يجوز أن يبقى شائبة من معنى الوصفية فيه، كما إذا سميت شخصا ذا حمرة بالأحمر.",
     "en": "Yes, it is possible that a trace of the meaning of plurality remains in a proper name, just as a trace of the meaning of attribution may remain in it — as when you name a person possessed of redness “al-Aḥmar (the Red).”"},
    {"type": "pair",
     "ar": "قال في الحاشية: الضبع هي الأنثى، والضبعان هو المذكر. والجمع ضباعين كسرحان وسراحين.",
     "en": "He said in the ḥāshiya: the ḍabuʿ is the female, and the ḍibʿān is the male; and the plural [of ḍibʿān] is “ḍabāʿīn,” like “sirḥān” → “sarāḥīn.”"},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: عن معنى الجمع؛ لأن الجمع هو المنقول لا المنقول عنه.",
     "en": "That is: [transferred] from the meaning of the plural; because “the plural” [word] is that which is transferred, not that from which the transfer is made."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بل لأنه لا شرط له حتى يشترط به.",
     "en": "Rather [he refrained] because it (plurality) has no [antecedent] condition such that anything could be made conditional upon it."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وللإمكان اعتبار الجمعية المطلقة.",
     "en": "And [also] because of the possibility of reckoning plurality absolutely."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "في القاموس: أفصى تخلص من خير أو شر كتفصي، هذا كلامه.",
     "en": "In al-Qāmūs: “afṣā” means “he freed himself from a good or an evil,” like “tafaṣṣā” — these are his (al-Fīrūzābādī’s) words."},
    {"type": "pair",
     "ar": "وقد أشار بهذا التقدير إلى وجه تقديم حضاجر على سراويل، وفيه نظر، وله وجهان آخران هما أنه أقوى، ودفعه أوضح.",
     "en": "By this construal he alluded to the reason for placing “ḥaḍājir” before “sarāwīl”; but in this there is [room for] consideration, and there are two other aspects to it: that it (ḥaḍājir) is the stronger [example], and that the repelling of it is the clearer."},
]
