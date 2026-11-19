# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 519 (printed ٥١٨)."""

PAGE_NUMBER = 519
PRINTED_PAGE = "٥١٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وقد تضمن كثير من الأفعال» at the foot of PDF p. 518 (mid-sentence).
    {"type": "matn",
     "ar": "التامة معنى الناقصة كما تقول: تتم التسعة بهذا عشرة أي: تصير عشرة تامة، و«كمل زيد عالما» أي: صار زيد عالما كاملا.",
     "en": "…complete [verbs] to imply the meaning of the defective [ones], as when you say “tatimmu al-tisʿatu bi-hādhā ʿasharatan” (the nine are completed by this as ten), that is, they become ten, complete; and “kamula zaydun ʿāliman” (Zayd was perfected as a scholar), that is, Zayd became a perfect scholar."},
    {"type": "matn",
     "ar": "(وقد جاء) «جاء» في قولهم: («ما جاءت حاجتك» ناقصة) ضميرها اسمها، و«حاجتك» خبرها:",
     "en": "(And “jāʾa” has come), “jāʾa” in their saying (“mā jāʾat ḥājataka”, as defective): its pronoun is its subject and “ḥājataka” its predicate;"},
    {"type": "matn",
     "ar": "إما بأن يكون «ما» نافية، و«جاءت» بمعنى: «كانت»[[١]]، وفيها ضمير لما تقدم من الغرارة[[٢]] ونحوها أي: لم تكن هذه على قدر ما يحتاج إليه،",
     "en": "either “mā” is negative and “jāʾat” is in the sense of “kānat”, with a pronoun in it referring to the heedlessness (gharāra) or the like mentioned before, that is, “this was not to the measure of what you need”;"},
    {"type": "matn",
     "ar": "أو استفهامية، والضمير في «جاءت» يعود إليها، وإنما أنث باعتبار خبرها كما في «من كانت أمك؟»",
     "en": "or it is interrogative, and the pronoun in “jāʾat” refers back to it; it is made feminine only in regard of its predicate, as in “man kānat ummaka?” (who was your mother?);"},
    {"type": "matn",
     "ar": "ومعناه: أية حاجة[[٣]] صارت حاجتك؟",
     "en": "and its meaning is: “what need has your need become?”"},
    {"type": "matn",
     "ar": "(و) وجاء أيضا «قعدت» ناقصة في قولهم: «أرهف شفرته»[[٤]] (حتى قعدت) أي: صارت الشفرة («كأنها حربة») أي: رمح قصير.",
     "en": "(And) “qaʿadat” has also come as defective in their saying “arhafa shafratahu” (he sharpened his blade) (“until it sat”), that is, the blade became, (“as though it were a ḥarba”), that is, a short spear."},
    {"type": "matn",
     "ar": "قال الأندلسي: لا يتجاوز «جاء وقعد»[[٥]] من الموضع الذي استعملها العرب فيه خلافا للفراء.",
     "en": "Al-Andalusī said: “jāʾa” and “qaʿada” are not extended beyond the place in which the Arabs used them, contrary to al-Farrāʾ."},
    {"type": "matn",
     "ar": "(وتدخل) هذه الأفعال وما كان نحوهن (على الجملة الاسمية) المركبة من المبتدأ والخبر[[٦]]",
     "en": "(They enter), these verbs and whatever is like them, (upon the nominal sentence) composed of a subject and a predicate"},
    {"type": "matn",
     "ar": "(لإعطاء الخبر) أي: لأجل إعطائها الخبر (حكم معناها) أي: معنى هذه الأفعال، يعني: أثره المترتب عليه[[٧]]",
     "en": "(to give the predicate), that is, for the sake of their giving the predicate, (the effect of their meaning), that is, the meaning of these verbs; he means: its consequence that follows from it;"},
    {"type": "matn",
     "ar": "مثل: «صار زيد غنيا»، فمعنى «صار» الانتقال،",
     "en": "as in “ṣāra zaydun ghaniyyan” (Zayd became rich): the meaning of “ṣāra” is transition,…"},

    {"type": "rule"},

    # ---------------- Footnote 7 of PDF p. 518, continued ----------------
    # Continues «ويقال في تفسير يتم التسعة» at the foot of PDF p. 518.
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "بهذا عشرة يتم التسعة بهذا صائرة عشرة.",
     "en": "…“bi-hādhā ʿasharatan”: “the nine are completed by this, becoming ten”."},
    {"type": "pair",
     "ar": "وثانيهما: عكس هذا كما ذكره الشارح.",
     "en": "The second of them is the reverse of this, as the Commentator mentioned it."},
    {"type": "pair",
     "ar": "فقوله: تامة وكاملا حالان لا صفتان كما توهم العبارة.",
     "en": "So his words “tāmmatan” and “kāmilan” are two circumstantials, not two attributes, as the wording might suggest."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في المفصل: بمعنى صارت.",
     "en": "In al-Mufaṣṣal: in the sense of “ṣārat”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهي الغفلة، فإن التركيب حدث من الخوارج حين أرسل إليهم علي رضي الله عنه ابن عباس رضي الله عنه",
     "en": "It is heedlessness (ghafla); for the construction originated with the Khawārij when ʿAlī, may Allah be pleased with him, sent Ibn ʿAbbās, may Allah be pleased with him, to them;"},
    {"type": "pair",
     "ar": "أي: ما جاءت غفلتنا حاجتك، أي: لم تجدنا غافلين كما تريدنا.",
     "en": "that is, “our heedlessness was not your need”, that is, “you did not find us heedless, as you wished us to be”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "والاستفهام إنكاري أي: لم تصر حاجة بين الحاجات متصفة بوصف كونها حاجة لك،",
     "en": "The interrogation is a denial, that is, no need among the needs has come to be qualified by being a need of yours."},
    {"type": "pair",
     "ar": "وروى برفع حاجتك، فخبره ما تقدم لتضمنه معنى الاستفهام.",
     "en": "It has been transmitted with “ḥājatuka” in the nominative, in which case its predicate is what precedes, because it contains the sense of interrogation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "في الصحاح: أرهفت سيفي أي: رققته والشفرة بالفتح السكين العظيم،",
     "en": "In al-Ṣiḥāḥ: “arhaftu sayfī” means “I thinned it”; and al-shafra, with a fatḥa, is the large knife."},
    {"type": "pair",
     "ar": "وما قيل: إنه في القاموس بالضم سهو.",
     "en": "What has been said, that in al-Qāmūs it is with a ḍamma, is an oversight."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولهذا جاء المصنف بالتركيبين اللذين هما وقعا فيهما،",
     "en": "For this reason the author brought the two constructions in which they occurred."},
    {"type": "pair",
     "ar": "لكنه قال في بعض تصانيفه: الحق في جاء الاطراد، فإنه يقال: جاء البر قفيزين.",
     "en": "But he said in one of his works: the truth regarding “jāʾa” is that it is regular, for one says “jāʾa al-burru qafīzayni” (the wheat came to two qafīz)."},
    {"type": "pair",
     "ar": "وقيل: في ضبط مواضع استعمال «قعد» أن يكون الخبر كأنه كذا.",
     "en": "It has been said, in defining the places where “qaʿada” is used: that the predicate be [of the form] “ka-annahu kadhā” (as though it were such)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "كأنه احترز بتقييد الجملة الاسمية عن مثل: أقائم زيد، وما قائم زيد، فإنهما جملتان اسميتان مركبتان من المبتدأ والفاعل.",
     "en": "It is as though, by qualifying the nominal sentence [as composed of subject and predicate], he guarded against such as “a-qāʾimun zaydun” and “mā qāʾimun zaydun”, for these are two nominal sentences composed of a subject and an agent."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إشارة إلى أن إضافة الحكم لامية لا بيانية على ما وهم.",
     "en": "An indication that the annexation of “ḥukm” [to “its meaning”] is of the lām type, not explicative, contrary to what was imagined."},
]
