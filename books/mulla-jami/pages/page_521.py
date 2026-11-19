# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 521 (printed ٥٢٠)."""

PAGE_NUMBER = 521
PRINTED_PAGE = "٥٢٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… والجملة الواقعة بعدها خبرا لها مفسرا للضمير، كقوله:» at the foot of PDF p. 520.
    {"type": "verse",
     "ar": "إذا مت كان الناس صنفان شامت      وآخر مثن بالذي كنت أصنع",
     "en": "…“When I die, people will be of two kinds: one rejoicing at my misfortune, and another praising what I used to do.”"},
    {"type": "matn",
     "ar": "(وتكون تامة) عطف على قوله: «تكون ناقصة» أي: «كان» تكون تامة يتم بالمرفوع من غير حاجة إلى المنصوب",
     "en": "(And it is complete [tāmma]): this is coordinated with his words “it is incomplete”; that is, “kāna” is complete, being completed by the nominative term without need of the accusative,"},
    {"type": "matn",
     "ar": "(بمعنى: «ثبت») ووقع كقولهم: كانت الكائنة والمقدر كائن، وكقوله تعالى: ﴿كن فيكون[[١]]﴾[[٢]].",
     "en": "(in the sense of “thabata”) (it was established) and “waqaʿa” (it occurred), as in their saying “kānati al-kāʾinatu” (the event came about) and “al-muqaddaru kāʾinun” (what is decreed comes to be), and as in His words, the Exalted: “Be, and it is.”"},
    {"type": "matn",
     "ar": "(و) تكون (زائدة[[٣]]) وهي التي وجودها وعدمها لا يخل بالمعنى الأصلي،",
     "en": "(And) it is (redundant [zāʾida]), namely the one whose presence and absence do not impair the original meaning,"},
    {"type": "matn",
     "ar": "كقوله تعالى: ﴿كيف نكلم من كان في المهد صبيا﴾[[٤]] أي: كيف نكلم من هو في المهد حال كونه صبيا؟",
     "en": "as in His words, the Exalted: “How can we speak to one who is in the cradle, a child?”, that is: how can we speak to one who is in the cradle while being a child?"},
    {"type": "matn",
     "ar": "فـ«كان» زائدة لتحسين اللفظ؛ إذ ليس المعنى على المضي،",
     "en": "So “kāna” is redundant, for the embellishment of the wording, since the meaning is not one of pastness."},
    {"type": "matn",
     "ar": "وإنما ذكر هذين القسمين مع كونهما غير ناقصة استيفاء لجميع استعمالاتها.",
     "en": "He mentioned these two kinds, although they are not incomplete, only to cover all of its uses exhaustively."},
    {"type": "matn",
     "ar": "(و«صار» للانتقال) إما من صفة إلى صفة، نحو: «صار زيد عالما»، أو من حقيقة إلى حقيقة نحو: «صار الطين خزفا»،",
     "en": "(And “ṣāra” is for transition), either from one attribute to another, as in “ṣāra Zaydun ʿāliman” (Zayd became learned), or from one reality to another, as in “ṣāra al-ṭīnu khazafan” (the clay became pottery)."},
    {"type": "matn",
     "ar": "(وتكون تامة) بمعنى الانتقال من مكان إلى مكان، أو من ذات إلى ذات، ويتعدى بـ«إلى» نحو: «صار زيد من بلد إلى بلد كذا، أو من بكر إلى عمرو»،",
     "en": "(And it is complete), in the sense of transition from one place to another, or from one person to another, and it is made transitive by “ilā”, as in “Zayd moved from a town to such-and-such a town” or “from Bakr to ʿAmr”."},
    {"type": "matn",
     "ar": "ويلحق بـ«صار» مثل: «آل، ورجع، واستحال، وتحول، وارتد»، قال الله تعالى: ﴿فارتد بصيرا﴾[[٥]]، وقال الشاعر:",
     "en": "Joined to “ṣāra” are [verbs] such as “āla” (to return), “rajaʿa” (to return), “istaḥāla” (to be transformed), “taḥawwala” (to change) and “irtadda” (to turn back); Allah, the Exalted, said: “and he became seeing again”; and the poet said:"},
    {"type": "verse",
     "ar": "إن العداوة تستحيل مودة      ..................",
     "en": "“Enmity turns into affection …”"},
    {"type": "matn",
     "ar": "وقال:",
     "en": "And he said:"},
    {"type": "verse",
     "ar": "..................      فيا لك من نعمى تحولن أبوسا",
     "en": "“… O what blessings, that have turned into miseries!”"},
    {"type": "matn",
     "ar": "(و«أصبح»، و«أمسى»، و«أضحى» لاقتران مضمون الجملة بأوقاتها) المدلول عليها بموادها لا بصورها",
     "en": "(And “aṣbaḥa”, “amsā” and “aḍḥā” are for the conjunction of the content of the sentence with their times), which are indicated by their root material, not by their forms,"},
    {"type": "matn",
     "ar": "مثل: «أصبح زيد قائما»، و«أمسى زيد مسرورا»، و«أضحى زيد حزينا».",
     "en": "as in “aṣbaḥa Zaydun qāʾiman” (Zayd was standing in the morning), “amsā Zaydun masrūran” (Zayd was happy in the evening) and “aḍḥā Zaydun ḥazīnan” (Zayd was sad in the forenoon)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأظهر أن قوله تعالى: كن في موقع الإيجاد، بمعنى ثبت، وفي موقع جعل شيء موصوفا بشيء بمعنى كن كذا،",
     "en": "The more evident view is that His words, the Exalted, “Be”, in the context of bringing into existence, mean “be established”, and in the context of making a thing qualified by something, mean “be such-and-such”;"},
    # REVIEW: printed «ويكون في مقام الإيجاد وأيضا بمعنى كن موجودا»; the «و» before «أيضا» reads oddly. Transcribed as printed.
    {"type": "pair",
     "ar": "بل يحتمل أن يكون في الجميع ناقصة، ويكون في مقام الإيجاد وأيضا بمعنى كن موجودا.",
     "en": "indeed, it may be incomplete in all cases, and in the context of bringing into existence it also means “be existent”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة البقرة: ١١٧، سورة آل عمران: ٤٧، ٥٩، سورة الأنعام: ٧٣، سورة النحل: ٤٠، سورة مريم: ٣٥، سورة يس: ٨٢، سورة غافر: ٦٨.",
     "en": "Qurʾān, Sūrat al-Baqara 2:117; Sūrat Āl ʿImrān 3:47, 59; Sūrat al-Anʿām 6:73; Sūrat al-Naḥl 16:40; Sūrat Maryam 19:35; Sūrat Yā Sīn 36:82; Sūrat Ghāfir 40:68."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذه مختصة بلفظ «كان» بخلاف ما سبق، فإنها شاملة لجميع تصاريفها.",
     "en": "This is restricted to the form “kāna”, unlike what preceded, which covers all of its inflected forms."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة مريم:٢٩.",
     "en": "Qurʾān, Sūrat Maryam 19:29."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة يوسف:٩٦.",
     "en": "Qurʾān, Sūrat Yūsuf 12:96."},
]
