# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 494 (printed ٤٩٣)."""

PAGE_NUMBER = 494
PRINTED_PAGE = "٤٩٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(مثل: «مرض فلان حتى لا يرجونه»)» at the foot of PDF p. 493.
    {"type": "matn",
     "ar": "الآن، مثال لما أريد به الحال تحقيقا، فإنه قصد به نفي الرجاء في زمان التكلم.",
     "en": "…now): an example of what is meant as the present in actual fact, for by it the negation of hope at the time of speaking is intended."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل هذين الأمرين، أي: كون «حتى» عند إرادة الحال حرف ابتداء، ووجوب سببية ما قبلها لما بعدها",
     "en": "(For this reason), that is, on account of these two matters, namely “ḥattā” being a particle of inception when the present is intended, and the requirement that what precedes it be a cause of what follows it,"},
    {"type": "matn",
     "ar": "(امتنع) نظرا إلى الأمر الأول[[١]] (الرفع) أي: رفع ما بعد «حتى» (في) قولك: («كان سيري حتى أدخلها» في) وقت حصول[[٢]] (كان الناقصة) في هذا القول",
     "en": "(the nominative is excluded), in view of the first matter, that is, the nominative of what follows “ḥattā”, (in) your saying (“kāna sayrī ḥattā adkhulahā” (my travelling was until I entered it), in) the case of the occurrence of (the incomplete kāna (kāna al-nāqiṣa)) in this saying,"},
    {"type": "matn",
     "ar": "بأن يجعل «كان» فيه ناقصة لا تامة؛ لأنها لما كانت حرف ابتداء انقطع ما بعدها عما قبلها، فيبقى الناقصة بلا خبر، فيفسد المعنى،",
     "en": "by taking “kāna” in it as incomplete, not complete; because, since it [ḥattā] is a particle of inception, what follows it is cut off from what precedes it, so the incomplete [kāna] remains without a predicate and the meaning is spoiled;"},
    {"type": "matn",
     "ar": "بخلاف ما إذا كانت تامة؛ لأنها لا تقتضي الخبر.",
     "en": "unlike when it is complete, because then it does not require a predicate."},
    {"type": "matn",
     "ar": "(و) امتنع الرفع نظرا إلى الأمر الثاني (في) قولك: («أسرت حتى تدخلها؟»)؛",
     "en": "(And) the nominative is excluded, in view of the second matter, (in) your saying (“a-sirta ḥattā tadkhulahā?” (Did you travel until you entered it?));"},
    {"type": "matn",
     "ar": "لأنه حينئذ يكون ما بعدها خبرا مستأنفا مقطوعا بوقوعه[[٣]]، وما قبلها سببا لما بعدها، وهو مشكوك فيه؛ لوجود حرف الاستفهام،",
     "en": "because then what follows it would be a fresh statement whose occurrence is affirmed with certainty, and what precedes it would be a cause of what follows it, while that [cause] is in doubt, owing to the presence of the interrogative particle;"},
    {"type": "matn",
     "ar": "فيلزم الحكم بوقوع المسبب مع الشك في وقوع السبب، وهو محال.",
     "en": "so it would follow that the occurrence of the effect is asserted while the occurrence of the cause is doubted, which is absurd."},
    # REVIEW: printed «فأما أدخل الآن»; the sense suggests «فأنا أدخل الآن» (so I am entering now). Transcribed as printed.
    {"type": "matn",
     "ar": "(وجاز في) وقت حصول «كان» (التامة: «كان سيري حتى أدخلها») فإن معناه: «ثبت سيري فأما أدخل الآن» ولا فساد فيه",
     "en": "(And it is permissible in) the case of the occurrence of (the complete [kāna]: “kāna sayrī ḥattā adkhuluhā”), for its meaning is “my travelling took place, so as for [me], I am entering now”, and there is nothing wrong in it;"},
    {"type": "matn",
     "ar": "(و) جاز («أيهم سار حتى يدخلها») بالرفع؛ لأن السير في هذا المقام محقق، والشك إنما هو في تعيين الفاعل، فيجوز أن يكون المسبب متحقق الحصول.",
     "en": "(and) permissible is (“ayyuhum sāra ḥattā yadkhuluhā” (Which of them travelled, so that he is entering it?)) with the nominative; because the travelling in this context is certain, and the doubt concerns only the identity of the agent (fāʿil), so the effect may be certain of occurrence."},
    {"type": "matn",
     "ar": "فقوله: «أيهم» عطف بتقدير «جاز» على «جاز في التامة» لا على «كان سيري[[٤]] حتى أدخلها»؛ لعدم صلاحية[[٥]] تقييده بقوله: «في التامة» كالمعطوف عليه،",
     "en": "So his words “ayyuhum” are coordinated, with “is permissible” supplied, upon “is permissible in the complete [kāna]”, not upon “kāna sayrī ḥattā adkhuluhā”; because it is not apt to be qualified by his words “in the complete [kāna]” as the term coordinated upon is."},
    {"type": "matn",
     "ar": "وفي بعض النسخ هكذا: «وجاز في كان سيري حتى أدخلها في التامة» أي: جاز الرفع في هذا التركيب في وقت حصول كان التامة،",
     "en": "In some copies it reads thus: “And it is permissible in kāna sayrī ḥattā adkhuluhā, in the complete [kāna]”, that is, the nominative is permissible in this construction in the case of the occurrence of the complete kāna;"},
    {"type": "matn",
     "ar": "فعلى هذا قوله: «أيهم سار» عطف على «كان",
     "en": "on this reading, his words “ayyuhum sāra” are coordinated upon “kāna…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا بالنظر إلى الأمر الثاني، فإن كينونة السير على صفة، أو في نفسه سبب الدخول.",
     "en": "Not in view of the second matter, for the travelling’s being of a certain description, or [its being] in itself, is a cause of the entering."},
    # REVIEW: printed «تقدير الجر منتفيا»; the context (the predicate of incomplete kāna) suggests «الخبر» (predicate). Transcribed as printed.
    {"type": "pair",
     "ar": "وأما احتمال تقدير الجر منتفيا فمناف لما هو مدلول كان، أو لاعتبار أن الانتفاء صفة حصل السير عليها، وهو تكلف.",
     "en": "As for the possibility of supposing the genitive [construction] as negated, it is incompatible with what “kāna” signifies, or [it requires] regarding the negation as a description upon which the travelling took place, which is forced."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "على حذف ثلاثة مضافات.",
     "en": "On the basis of the omission of three first terms of genitive constructions (muḍāfāt)."},
    {"type": "pair",
     "ar": "قال الرضي: وقد يحذف مضاف ما بعدها وهلم جرا لقيام المضاف إليه الأخير مقامه.",
     "en": "Al-Raḍī said: the first term of what follows it may be omitted, and so on, because the last second term (muḍāf ilayhi) stands in its place."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بوقوع مدلوله بالنظر إلى الخبر، وإن احتمل عند العقل عدم الوقوع.",
     "en": "That is, the occurrence of what it signifies, in view of [its being] a statement, even if, for the intellect, its non-occurrence is possible."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أشار إلى أن المقصود بتقدير جاز ليس تعيين هذا الطريق، بل نفي عطفه على كان سيري،",
     "en": "He indicated that what is intended by supplying “is permissible” is not to fix this route, but to deny its coordination upon “kāna sayrī”;"},
    {"type": "pair",
     "ar": "فيجوز ألا يقدر جاز، فيكون عطفا على كان سيري بعد اعتبار تقييده بقوله: في التامة، لكنه خلاف الظاهر.",
     "en": "so “is permissible” may be left unsupplied, and it is then coordinated upon “kāna sayrī” after its qualification by his words “in the complete [kāna]” has been taken into account; but this goes against the apparent sense."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "مع أن تقديم القيد على المعطوف عليه يقتضي المشاركة فيه، بخلاف ما إذا تأخر، فإنه يحتمل المشاركة وعدمها",
     "en": "Besides, placing the qualifier before the term coordinated upon requires [the coordinated term’s] sharing in it, unlike when it comes after, for then it admits both sharing and not sharing."},
    {"type": "pair",
     "ar": "هذا ما قالوا، وهو الظاهر السابق إلى الفهم.",
     "en": "This is what they have said, and it is the apparent sense that comes first to the understanding."},
]
