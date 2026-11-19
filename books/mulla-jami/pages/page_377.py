# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 377 (printed ٣٧٦)."""

PAGE_NUMBER = 377
PRINTED_PAGE = "٣٧٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «كما جيء به للتنبيه» at the foot of PDF p. 376.
    {"type": "matn",
     "ar": "على النسبة الإسنادية، كقولك: «ها زيد قائم» و«ها إن زيدا قائم».",
     "en": "…to the predicative relation, as when you say “hā Zaydun qāʾimun” (lo, Zayd is standing) and “hā inna Zaydan qāʾimun” (lo, indeed Zayd is standing)."},
    {"type": "matn",
     "ar": "(ويتصل بها) أي: بأواخر أسماء الإشارة (حرف الخطاب) وهو الكاف تنبيها على حال المخاطب من الإفراد والتثنية والجمع، والتذكير والتأنيث،",
     "en": "(There is joined to them), that is, to the ends of the demonstrative nouns, (the particle of address) (ḥarf al-khiṭāb), which is the kāf, to indicate the state of the one addressed as to singular, dual and plural, and masculine and feminine."},
    {"type": "matn",
     "ar": "وإنما جعلت هذه الكاف حرفا لامتناع وقوع الظاهر موقعها[[١]]، ولو كانت اسما لم يمتنع ذلك مثل: «ضربتك، وبك».",
     "en": "This kāf was made a particle only because an explicit noun cannot occur in its place; had it been a noun, that would not be barred, as in “ḍarabtuka” (I struck you) and “bika” (with you)."},
    {"type": "matn",
     "ar": "(وهي[[٢]]) أي: حرف الخطاب[[٣]] (خمسة[[٤]]) والقياس يقتضي الستة، واشترك خطاب الاثنين، فرجعت إلى خمسة",
     "en": "(They), that is, the particle of address, (are five). Analogy requires six, but the address to two is shared, so they come down to five,"},
    {"type": "matn",
     "ar": "مضروبة (في خمسة) من أنواع أسماء الإشارة، يعني: المفرد المذكر والمؤنث، ومثناهما وجمعهما، وهي ستة راجعة إلى خمسة؛ لاشتراك جمعهما،",
     "en": "multiplied (by five) kinds of demonstrative noun, namely: the masculine and feminine singular, their duals and their plural — which are six, coming down to five because their plural is shared."},
    {"type": "matn",
     "ar": "وإنما قلنا: «من أنواع أسماء الإشارة»[[٥]]؛ لأن أفراد المفرد المؤنث ترتقي إلى ستة",
     "en": "We said “kinds of demonstrative noun” only because the individual forms of the feminine singular rise to six."},
    {"type": "matn",
     "ar": "(فيكون) أي: الحاصل من الضرب (خمسة وعشرين، وهي) أي: تلك الخمسة والعشرون («ذاك إلى ذاكن»)",
     "en": "(So there are) — that is, the product of the multiplication — (twenty-five, and they are), that is, those twenty-five, (“dhāka” to “dhākunna”):"},
    {"type": "matn",
     "ar": "يعني: «ذاك» إذا أشرت إلى مذكر وخاطبت مذكرا، و«ذاكما» إذا أشرت إلى مذكر وخاطبت مذكرين، و«ذاكم» إذا أشرت إلى مذكر وخاطبت مذكرين",
     "en": "he means “dhāka” when you point to one male and address one male, “dhākumā” when you point to one male and address two males, and “dhākum” when you point to one male and address males;"},
    {"type": "matn",
     "ar": "(و) على هذا القياس («ذانك») و«ذينك» إذا أشرت إلى مذكرين وخاطبت مذكرا (إلى «ذانكن») و«ذينكن» إذا أشرت إلى مذكرين وخاطبت مؤنثات",
     "en": "(and), on the same pattern, (“dhānika”) and “dhaynika” when you point to two males and address one male, (to “dhānikunna”) and “dhaynikunna” when you point to two males and address females."},
    {"type": "matn",
     "ar": "(وكذلك البواقي) يعني: «تاك إلى تاكن» و«تيك إلى تيكن»، و«تانك وتينك إلى تانكن وتينكن»، و«أولئك بالمد وأولاك» بالقصر إلى «أولائكن وأولاكن».",
     "en": "(Likewise the rest): he means “tāka” to “tākunna”, “tīka” to “tīkunna”, “tānika” and “taynika” to “tānikunna” and “taynikunna”, and “ulāʾika” with madd and “ulāka” with qaṣr to “ulāʾikunna” and “ulākunna”."},
    {"type": "matn",
     "ar": "وأما «ذيك» فقد أورده الزمخشري والمالكي، وفي الصحاح لا تقل: «ذيك»، فإنه خطأ.",
     "en": "As for “dhīka”, al-Zamakhsharī and al-Mālikī cited it; but in al-Ṣiḥāḥ: “Do not say dhīka, for it is an error.”"},
    {"type": "matn",
     "ar": "(ويقال: «ذا» للقريب، و«ذلك» للبعيد، و«ذاك» للمتوسط[[٦]]) وأخر المتوسط؛ لأن",
     "en": "(“Dhā” is said for the near, “dhālika” for the far, and “dhāka” for the intermediate). He put the intermediate last because…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 376 (note ٨ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "وأنتم وهو وأخوتها كثير، ومنه قوله تعالى: «ها أنتم أولاء» (آل عمران:١١٩).",
     "en": "…“antum”, “huwa” and their sisters [such separation] is frequent; of this is the word of the Exalted: “Hā antum ulāʾi” (Here you are, those [who love them]) (Qurʾān, Sūrat Āl ʿImrān 3:119)."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # Printed with mixed quotation marks: «افعل» and "لا تفعل"; kept as printed.
    {"type": "pair",
     "ar": "فيه أن ضمير «افعل»، و\"لا تفعل\" مما يمتنع وقوع الظاهر موقعه مع أنه اسم،",
     "en": "There is the point that the pronoun of “ifʿal” (do!) and “lā tafʿal” (do not!) is among those in whose place an explicit noun cannot occur, although it is a noun."},
    {"type": "pair",
     "ar": "فالأولى أن يقال: لأن معناها غير مستقل بالمفهومية.",
     "en": "So it is better to say: because its meaning is not independently intelligible."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الحرف يذكر ويؤنث. واعتبر هنا تذكيره بقرينة تذكير اسم العدد، أعني: خمسة.",
     "en": "“Ḥarf” is treated as masculine and as feminine. Here its masculine gender is regarded, as indicated by the masculine form of the numeral, namely “khamsa”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإنه أقرب، ويحتمل أن يفسر بأسماء الإشارة.",
     "en": "For it is nearer; it may also be explained as [referring to] the demonstrative nouns."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تأنيث خمسة لتذكير مميزها، وهي حروف الخطاب والحروف يذكر ويؤنث.",
     "en": "“Khamsa” has the feminine ending because its specified noun is masculine, namely “ḥurūf al-khiṭāb” (particles of address); and “ḥurūf” is treated as masculine and as feminine."},
    {"type": "pair",
     "ar": "ولو اعتبر تأنيثه هنا وقال: وهي خمس لكان فيه تقرير لحرفية حروف الخطاب إلا أنه راعى المناسبة بقوله: في خمسة.",
     "en": "Had he regarded its feminine gender here and said “wa-hiya khams”, that would have confirmed the particle-status of the particles of address; but he observed correspondence with his words “fī khamsa”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: يرتقي مما يتصل به حروف الخطاب بلا خلاف إلى ستة، فلا يرد أن ما عد من الواحد سبعة.",
     "en": "He means: of those to which the particles of address are joined without dispute, [the feminine singular] rises to six; so there is no objection that what was counted for the singular is seven."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا يستعمل الكاف إلا للمتوسط أو البعيد واللام للتنصيص على البعيد.",
     "en": "The kāf is used only for the intermediate or the far, and the lām to specify the far explicitly."},
]
