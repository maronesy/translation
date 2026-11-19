# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 402 (printed ٤٠١)."""

PAGE_NUMBER = 402
PRINTED_PAGE = "٤٠١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وكلاهما) لو قال: «كلتاهما» لكان أوفق؛ لتأنيث الاستفهامية والخبرية، فهو على» at the foot of PDF p. 401.
    {"type": "matn",
     "ar": "تأويل «كلا هذين النوعين»، وهما «كم» الاستفهامية والخبرية، أي: كل واحد منهما",
     "en": "…the interpretation “both of these two kinds”, namely interrogative and predicative “kam”; that is, each of them"},
    {"type": "matn",
     "ar": "(يقع مرفوعا ومنصوبا ومجرورا) ثم بين موقع كل واحد منهما بقوله:",
     "en": "(occurs in the nominative, the accusative and the genitive). Then he explained the position of each of them by his words:"},
    {"type": "matn",
     "ar": "(فكل ما) أي: كل واحد من «كم» الاستفهامية[[١]] والخبرية يكون (بعده فعل) أو شبه فعل[[٢]] لفظا أو تقديرا (غير مشتغل عنه بضميره) أو متعلق ضميره،",
     "en": "(So whatever), that is, each instance of interrogative or predicative “kam”, (is followed by a verb) or a quasi-verb, expressed or implied, (not diverted from it by its pronoun (ghayr mushtaghil ʿanhu bi-ḍamīrihi)) or by what is connected with its pronoun,"},
    {"type": "matn",
     "ar": "فهو من حيث هو كذلك (كان منصوبا معمولا على حسبه) أي: على حسب عمل هذا الفعل[[٣]]، وعمله لا يكون إلا بحسب المميز[[٤]]،",
     "en": "it, insofar as it is such, (is accusative, governed according to it), that is, according to the government of this verb; and its government is only according to the specifier."},
    {"type": "matn",
     "ar": "وذلك أنك تقول: «كم يوما ضربت؟» فـ«كم» منصوب على الظرفية مع اقتضاء الفعل للمفعول به والمصدر والمفعول فيه وغير ذلك من المنصوبات، فتعينه لأحد المنصوبات إنما هو بحسب المميز،",
     "en": "That is because you say “kam yawman ḍarabta?” (on how many days did you strike?), and “kam” is accusative as an adverb (ẓarfiyya), although the verb calls for a direct object, a maṣdar, an adverbial object and other accusatives; so its being fixed to one of the accusatives is only according to the specifier."},
    {"type": "matn",
     "ar": "فالاستفهامية نحو: «كم رجلا ضربت؟» في المفعول به[[٥]]، و«كم ضربة ضربت؟» في المفعول المطلق، و«كم يوما سرت؟» في المفعول فيه،",
     "en": "The interrogative: as “kam rajulan ḍarabta?” (how many men did you strike?) for the direct object (mafʿūl bihi), “kam ḍarbatan ḍarabta?” (how many blows did you strike?) for the absolute object (mafʿūl muṭlaq), and “kam yawman sirta?” (for how many days did you travel?) for the adverbial object (mafʿūl fīhi)."},
    {"type": "matn",
     "ar": "والخبرية مثل: «كم غلام ملكت، وكم ضربة ضربت، وكم يوم سرت».",
     "en": "The predicative: as “kam ghulāmin malakta” (how many a slave you have owned!), “kam ḍarbatin ḍarabta” (how many a blow you have struck!), and “kam yawmin sirta” (how many a day you have travelled!)."},
    {"type": "matn",
     "ar": "وإنما جعلنا الفعل[[٦]] أو شبهه أعم من أن يكون ملفوظا أو مقدرا، ليدخل في قاعدة النصب مثل قولك: «كم رجلا ضربته؟»[[٧]]؛ إذا جعلته من قبيل الإضمار على",
     "en": "We made the verb or quasi-verb broader than being expressed or implied only so that the rule of the accusative includes such a case as your saying “kam rajulan ḍarabtahu?” (how many men did you strike?), when you treat it as a case of suppression [of the verb] on…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «فالاستفهامية» printed; «في الاستفهامية» seems intended. Transcribed as printed.
    {"type": "pair",
     "ar": "اكتفى بثلاثة أمثلة من المفاعيل فالاستفهامية والخبرية؛ لأن المعروف انتصابهما على أنه مفعول بهما أو ظرف أو مصدر.",
     "en": "He confined himself to three examples of objects for the interrogative and the predicative, because what is known is that they are accusative as a direct object, an adverb or a maṣdar."},
    {"type": "pair",
     "ar": "وأما خبر «كان» نحو: كم درهما كان مالك، والمفعول الثاني من باب «ظننت» نحو: كم درهما ظننت مالك، فهما داخلان في المفعول به.",
     "en": "As for the predicate of “kāna”, as in “kam dirhaman kāna māluka” (how many dirhams was your wealth?), and the second object of the class of “ẓanantu”, as in “kam dirhaman ẓananta mālaka” (how many dirhams did you suppose your wealth?), both fall under the direct object."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "نبه على أن المراد بالفعل ما يعمه وشبهه ليشمل نحو: كم يوما أنت سائر، وكم رجلا أنت ضارب.",
     "en": "He pointed out that what is meant by “verb” is what covers it and the quasi-verb, so as to include such cases as “kam yawman anta sāʾir” (for how many days are you travelling?) and “kam rajulan anta ḍārib” (how many men are you striking?)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: «معمولا «لا»» printed (sic); the sense is that the pronoun of «حسبه» refers to the government understood from «معمولا», not to the verb's requirement. Transcribed as printed.
    {"type": "pair",
     "ar": "يعني: أن ضمير «حسبه» راجع إلى العمل المفهوم من معمولا «لا» إلى اقتضاء الفعل على ما في الرضي.",
     "en": "That is: the pronoun of “ḥasabihi” refers to the government understood from “maʿmūlan”, not to the verb’s requirement, as stated in al-Raḍī."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أشار به إلى دفع ما اعترض به الرضي أنه ينتقض بـ«كم يوم ضربت؟»؛ لأنه ليس منصوبا على حسب اقتضاء فعل بعده، فإنه يقتضي منصوبات كثيرة، وليس نصبه إلا على الظرفية،",
     "en": "By this he alluded to repelling al-Raḍī’s objection that it is contradicted by “kam yawm ḍarabta?”, since it is not accusative according to the requirement of the verb after it: that verb calls for many accusatives, yet its accusative is only adverbial."},
    {"type": "pair",
     "ar": "فأجاب الشارح بأن اقتضاءه بـ«كم يوما» ليس إلا بالظرفية، وملاك اقتضائه المميز.",
     "en": "So the commentator answered that its requirement with “kam yawman” is only adverbial, and the basis of its requirement is the specifier."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الرضي: وليس بمعروف انتصابها إلا مفعولا بها أو ظرفا أو مصدرا أو خبرا كان نحو: «كم كان مالك؟» أو مفعولا ثانيا لباب «ظن» نحو: «كم ظننت مالك؟».",
     "en": "Al-Raḍī said: its being accusative is not known except as a direct object, an adverb, a maṣdar, the predicate of kāna, as in “kam kāna māluka?” (how much was your wealth?), or the second object of the class of “ẓanna”, as in “kam ẓananta mālaka?” (how much did you suppose your wealth?)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فعلى هذا قوله: كان منصوبا، وإلا فهو مرفوع كان معناه تعيين النصب والرفع لكونه راجحا مختارا،",
     "en": "On this basis, his words “it is accusative; otherwise it is nominative” mean the fixing of the accusative and the nominative as being the preponderant, preferred [option];"},
    {"type": "pair",
     "ar": "فلا يرد أنه على تقدير الاشتغال بالضمير يجوز الرفع بأن يقدر الضمير العائد إلى «كم»؛ لأنه ضعيف كما في الرضي.",
     "en": "so the objection does not arise that, on supposing diversion by the pronoun, the nominative is permitted by supposing the pronoun referring to “kam”, because that is weak, as stated in al-Raḍī."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أجاز الفاضل الهندي جعله داخلا في قوله: وإلا فمرفوع أي: يجوز رفعه، وحمل قوله: منصوبا على وجوب النصب.",
     "en": "Al-Fāḍil al-Hindī allowed it to be included under his words “otherwise it is nominative”, that is, its nominative is permitted, and he took his words “accusative” to mean that the accusative is obligatory."},
    {"type": "pair",
     "ar": "ويرده ما ذكره الرضي أن «كم رجلا ضربت؟» يجوز رفعه، لكنه ضعيف.",
     "en": "Against him is what al-Raḍī mentioned: that in “kam rajulan ḍarabta?” the nominative is permitted, but weak."},
]
