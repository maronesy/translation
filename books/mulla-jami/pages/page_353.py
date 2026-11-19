# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 353 (printed ٣٥٢)."""

PAGE_NUMBER = 353
PRINTED_PAGE = "٣٥٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «… و«عمر» عطف بيان له.» at the foot of PDF p. 352 (new sentence).
    {"type": "matn",
     "ar": "وقصته: أنه أتى أعرابي إلى عمر بن الخطاب رضي الله تعالى عنه فقال: إن أهلي بعيد وإني على ناقة دبراء عجفاء نقباء، واستحمله،",
     "en": "Its story: a Bedouin came to ʿUmar ibn al-Khaṭṭāb, may Allah the Exalted be pleased with him, and said: “My people are far away, and I am on a she-camel that is galled, emaciated and worn in the hoof”, and he asked him for a mount."},
    {"type": "matn",
     "ar": "فظنه كاذبا، فلم يحمله، فانطلق الأعرابي، فحمل بعيره، ثم استقبل البطحاء، وجعل يقول وهو يمشي خلف بعيره:",
     "en": "ʿUmar thought him a liar and did not give him a mount. So the Bedouin went off, loaded his camel, then faced the Baṭḥāʾ, and began to say, walking behind his camel:"},
    {"type": "verse",
     "ar": "أقسم بالله أبو حفص عمر          ما مسها من نقب ولا دبر",
     "en": "Abū Ḥafṣ ʿUmar swore by Allah / that she has no worn hoof and no gall;"},
    {"type": "verse",
     "ar": "اغفر له اللهم إن كان فجر          ……………",
     "en": "forgive him, O Allah, if he swore falsely. / …"},
    # REVIEW: the closing guillemet after «التقيا» has no matching opening one after «قال:»; transcribed as printed.
    # Note: marker [٢] is printed after «صدق صدق», but footnote ٢ comments on «فجعل إذا قال» (expecting «يقول»).
    {"type": "matn",
     "ar": "وعمر مقبل من أعلى الوادي، فجعل إذا قال: «اغفر له اللهم إن كان فجر[[١]]»، قال: اللهم صدق صدق[[٢]] حتى التقيا»،",
     "en": "ʿUmar was coming from the upper part of the valley, and whenever [the Bedouin] said “forgive him, O Allah, if he swore falsely”, he said: “O Allah, he spoke the truth, he spoke the truth”, until they met."},
    {"type": "matn",
     "ar": "فأخذ بيده، فقال: «ضع عن راحلتك»، فوضع فإذا هي نقبة عجفاء، فحمله على بعيره وزوده وكساه.",
     "en": "He took him by the hand and said: “Unload your mount.” He unloaded, and she was indeed worn in the hoof and emaciated; so he gave him a camel as a mount, provided him with provisions and clothed him."},
    {"type": "matn",
     "ar": "(وفصله) أي: فرقه (من البدل لفظا) أي: من حيث الأحكام اللفظية واقع (في مثل:",
     "en": "(Its distinction), that is, its difference, (from the substitute in wording), that is, with respect to the rulings of wording, occurs (in the like of:"},
    {"type": "verse",
     "ar": "«أنا ابن التارك البكري بشر»)          ……………",
     "en": "“I am the son of the one who left the Bakrī, Bishr”) / …"},
    {"type": "matn",
     "ar": "فإن قوله: «بشر» إن جعل عطف بيان للبكري جاز، وإن جعل بدلا منه لم يجز؛ لأن البدل في حكم تكرير العامل،",
     "en": "For his word “Bishr”, if made an explicative apposition to “al-Bakrī”, is permitted; but if made a substitute for it, it is not permitted, because the substitute is in the position of a repetition of the governor,"},
    {"type": "matn",
     "ar": "فيكون التقدير: «أنا ابن التارك بشر»، وهو غير جائز، كما ذكر فيما سبق في «الضارب زيد»، وآخره:",
     "en": "so the implied form would be “anā ibnu al-tāriki Bishrin”, which is not permitted, as was mentioned earlier regarding “al-ḍāribu Zaydin”. Its ending is:"},
    {"type": "verse",
     "ar": "……………          عليه الطير ترقبه وقوعا",
     "en": "… / the birds over him, watching him, alighting."},
    {"type": "matn",
     "ar": "و«عليه الطير» ثاني مفعولي «التارك» إن جعلناه بمعنى المصير[[٣]]، وإلا فهو حال،",
     "en": "“ʿAlayhi al-ṭayru” is the second of the two objects of “al-tārik” if we take it in the sense of “making [something] become”; otherwise it is a circumstantial clause (ḥāl)."},
    {"type": "matn",
     "ar": "وقوله: «ترقبه» حال من «الطير» إن كان فاعلا لـ«عليه»، وإن كان مبتدأ فهو حال من الضمير المستكن في «عليه»،",
     "en": "His word “tarqubuhu” is a ḥāl from “al-ṭayr” if [al-ṭayr] is the agent of “ʿalayhi”; if it is a subject (mubtadaʾ), it is a ḥāl from the pronoun latent in “ʿalayhi”."},
    {"type": "matn",
     "ar": "و«وقوعا» جمع «واقع» حال من فاعل «ترقبه»، أي: واقعين حوله مترقبة لإزهاق روحه؛ لأن الإنسان ما دام به رمق، فإن الطير لا يقربه.",
     "en": "“Wuqūʿan”, the plural of “wāqiʿ”, is a ḥāl from the agent of “tarqubuhu”, that is, alighting around him, waiting for his soul to depart; for as long as a man has a breath of life in him, the birds do not come near him."},
    {"type": "matn",
     "ar": "وأما الفرق المعنوي بينهما، فقد تبين فيما سبق.",
     "en": "As for the difference in meaning between the two, it was made clear earlier."},
    {"type": "matn",
     "ar": "والمراد بمثل: «أنا ابن التارك البكري بشر»: كل ما كان عطف بيان للمعرف باللام الذي أضيف إليه الصفة المعرفة باللام نحو: «الضارب الرجل زيد»،",
     "en": "What is meant by “the like of ‘anā ibnu al-tāriki al-Bakriyyi Bishrin’” is every case of an explicative apposition to a noun defined by the article to which an adjective defined by the article is annexed, as in “al-ḍāribu al-rajuli Zaydin”."},
    {"type": "matn",
     "ar": "ويمكن أن يراد به ما هو أعم من هذا الباب، أي: كل ما خالف حكمه إذا كان عطف بيان حكمه إذا كان",
     "en": "It may also be meant to cover what is more general than this class, that is, every case whose ruling when it is an explicative apposition differs from its ruling when it is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: كذب، يقال: يمين فاجرة.",
     "en": "That is, he lied; one says “yamīn fājira” (a false oath)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الظاهر: يقول، لأن خبر أفعال المقاربة لا يكون إلا مضارعا.",
     "en": "The expected form is “yaqūlu”, because the predicate of the verbs of approximation (afʿāl al-muqāraba) can only be an imperfect (muḍāriʿ)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: ضمن فيه معنى الجعل.",
     "en": "That is, the sense of “making” (jaʿl) is incorporated in it."},
]
