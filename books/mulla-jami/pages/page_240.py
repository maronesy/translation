# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 240 (printed ٢٣٩)."""

PAGE_NUMBER = 240
PRINTED_PAGE = "٢٣٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لخرج مثل هذا المثال» from the foot of PDF p. 239.
    {"type": "matn",
     "ar": "منه، فإن ذكر «يوم الجمعة» فيه ليس من حيث إنه فعل فيه فعل مذكور، بل من حيث إنه وقع عليه فعل مذكور.",
     "en": "…from it; for the mention of “Friday” in it is not inasmuch as a mentioned action is done in it, but inasmuch as a mentioned action falls upon it."},
    {"type": "matn",
     "ar": "ولا يخفى على تقدير اعتبار قيد الحيثية لا حاجة إلى قوله: «مذكور» إلا لزيادة تصوير المعرف.",
     "en": "It is not hidden that, on the supposition that the qualification of respect is taken into account, there is no need for his word “mentioned” except to depict the thing defined more fully."},
    {"type": "matn",
     "ar": "قوله: (من زمان أو مكان[[١]]) بيان لـ«ما» الموصولة أو الموصوفة، إشارة إلى قسمي المفعول فيه[[٢]]، وتمهيد لبيان حكم كل واحد منهما.",
     "en": "His words (whether time or place) explain the relative or the qualified “mā,” pointing to the two kinds of the mafʿūl fīhi and preparing for the statement of the rule of each of them."},
    {"type": "matn",
     "ar": "وهو أي: المفعول فيه ضربان:",
     "en": "It—that is, the mafʿūl fīhi—is of two types:"},
    {"type": "matn",
     "ar": "١-ما يظهر فيه «في»، وهو مجرور بها.",
     "en": "1. that in which “fī” (in) appears, and it is in the genitive by it;"},
    {"type": "matn",
     "ar": "٢-وما يقدر فيه «في»، وهو منصوب بتقديرها.",
     "en": "2. and that in which “fī” is implied, and it is in the accusative through its being implied."},
    {"type": "matn",
     "ar": "وهذا خلاف اصطلاح القوم، فإنهم لا يطلقون المفعول فيه إلا على المنصوب بتقدير «في».",
     "en": "This is contrary to the technical usage of the grammarians, for they apply “mafʿūl fīhi” only to what is in the accusative with “fī” implied."},
    {"type": "matn",
     "ar": "وأما المجرور بها فهو مفعول به بواسطة حرف الجر لا مفعول فيه.",
     "en": "As for what is in the genitive by it, it is an object by means of a preposition, not a mafʿūl fīhi."},
    {"type": "matn",
     "ar": "وخالفهم المصنف حيث جعل المجرور أيضا مفعولا فيه، ولذلك قال: (وشرط نصبه) أي: شرط نصب المفعول فيه (تقدير «في»)؛ إذ التلفظ بها يوجب الجر.",
     "en": "The author differed from them in making the genitive also a mafʿūl fīhi; for this reason he said: (The condition of its accusative), that is, the condition of the accusative of the mafʿūl fīhi, (is that “fī” be implied), since pronouncing it requires the genitive."},
    {"type": "matn",
     "ar": "(وظروف الزمان كلها) مبهما كان الزمان أو محدودا[[٣]] (تقبل ذلك) أي: تقدير «في»؛",
     "en": "(Adverbs of time, all of them)—whether the time is indefinite (mubham) or delimited (maḥdūd)—(admit that), that is, the implying of “fī”;"},
    {"type": "matn",
     "ar": "لأن المبهم منها جزء مفهوم الفعل، فيصح انتصابه بلا واسطة كالمصدر،",
     "en": "because the indefinite among them is part of the concept of the verb, so its taking the accusative without an intermediary is valid, like the maṣdar;"},
    {"type": "matn",
     "ar": "والمحدود منها محمول عليه أي: على المبهم لاشتراكهما في الزمانية نحو: «صمت دهرا، وأفطرت اليوم».",
     "en": "and the delimited among them is assimilated to it, that is, to the indefinite, since both share in being time; as in “I fasted for an age (dahran), and I broke the fast today (al-yawma).”"},
    {"type": "matn",
     "ar": "(وظروف المكان إن كان) مكانا (مبهما[[٤]] قبل ذلك) أي: تقدير «في» حملا على الزمان المبهم، لاشتراكهما في الإبهام، نحو: «جلست خلفك»",
     "en": "(Adverbs of place, if it is) a place that is (indefinite, admit that), that is, the implying of “fī,” by assimilation to indefinite time, since both share in indefiniteness; as in “I sat behind you (khalfaka).”"},
    {"type": "matn",
     "ar": "(وإلا) أي: وإن لم يكن مبهما، بل يكون محدودا (فلا) تقبل تقدير «في»؛ إذ لم يمكن حمله على الزمان المبهم",
     "en": "(Otherwise), that is, if it is not indefinite but delimited, (then they do not) admit the implying of “fī,” since it cannot be assimilated to indefinite time…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قد يجعل المصدر حينا بحذف المضاف، أو يجعل المصدر مجازا عن الحين لاشتراكها في مدلولية الفعل، وعلامة المظروفية والظرفية.",
     "en": "The maṣdar is sometimes made a time by eliding the annexing noun, or the maṣdar is made a metaphor for the time, since they share in being signified by the verb and in the mark of being contained and containing."},
    {"type": "pair",
     "ar": "وقد يجعل العين مكانا نحو: جلست في الشمس أي: في مكانها إذا أريد بالشمس النور، أو في مكان أثرها إذا أريد بها الجرم.",
     "en": "A concrete thing (ʿayn) is sometimes made a place, as in “I sat in the sun,” that is, in its place, if by “the sun” the light is meant; or in the place of its effect, if the [celestial] body is meant by it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أن قوله: من زمان ليس قيدا احترازيا بناء على أن في محمولة على الظرفية الحقيقية، فليس كل مجرور بـ«في» مفعولا فيه.",
     "en": "[This is] an indication that his words “whether time” are not a restrictive qualification, on the basis that “fī” is taken in the sense of real containment; so not everything in the genitive by “fī” is a mafʿūl fīhi."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اتفق القوم على أن المبهم من الزمان ما لم يعتبر له حد ونهاية كالحين والمحدود ما اعتبر فيه ذلك كاليوم والليلة والشهر والسنة.",
     "en": "The grammarians agree that indefinite time is that for which no bound or end is considered, like “ḥīn” (a while), and delimited time is that in which that is considered, like the day, the night, the month and the year."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «إلي المكان» (final yāʾ for alif maqṣūra in «إلى»); transcribed as printed.
    {"type": "pair",
     "ar": "جعل الضمير راجعا إلى المكان، وإلا لوجب أن يقول: إن كانت",
     "en": "He took the pronoun [in “kāna”] to refer to the place; otherwise he would have had to say “in kānat.”"},
    {"type": "pair",
     "ar": "ولما كانت إضافة الظروف إلي المكان بيانية لم يحتج الجملة الواقعة خبرا إلى عائد؛ لأن عائد المبين عائد المبين.",
     "en": "Since the annexation of “adverbs” to “place” is explicative, the sentence serving as predicate needs no returning pronoun [to “adverbs”], because the returning pronoun of what explains is the returning pronoun of what is explained."},
]
