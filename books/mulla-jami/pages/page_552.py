# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 552 (printed ٥٥١)."""

PAGE_NUMBER = 552
PRINTED_PAGE = "٥٥١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(وقد يكونان) أي: «عن»، و«على» (اسمين[[١]]) يعلم ذلك (بدخول «من» عليهما)",
     "en": "(And they are sometimes), that is, “ʿan” and “ʿalā”, (nouns); this is known (by “min” entering upon them),"},
    {"type": "matn",
     "ar": "نحو: «من عن يميني» أي: من جانب يميني، و«من عليه» أي: من فوقه.",
     "en": "as in “min ʿan yamīnī”, that is, from the side of my right, and “min ʿalayhi”, that is, from above it."},

    {"type": "section", "ar": "[الكاف]",
     "en": "Al-Kāf"},

    {"type": "matn",
     "ar": "(والكاف):",
     "en": "(And the kāf [is]):"},
    {"type": "matn",
     "ar": "١-(للتشبيه) نحو: «زيد كالأسد».",
     "en": "1. (for comparison (tashbīh)), as in “Zaydun ka-l-asadi” (Zayd is like the lion);"},
    {"type": "matn",
     "ar": "٢-(وزائدة) نحو: ﴿ليس كمثله شيء﴾[[٢]]؛ إذ التقدير: «ليس مثله[[٣]] شيء»، على بعض الوجوه.",
     "en": "2. (and redundant (zāʾida)), as in “There is nothing like unto Him”, since the underlying form is “laysa mithlahu shayʾun” (nothing is like Him), on some of the interpretations;"},
    {"type": "matn",
     "ar": "٣-(وقد يكون) أي: الكاف (اسما) بمعنى «مثل»[[٤]]، نحو:",
     "en": "3. (and it is sometimes), that is, the kāf, (a noun) in the sense of “mithl” (likeness), as in:"},
    {"type": "verse",
     "ar": "يضحكن[[٥]] عن كالبرد المنهم",
     "en": "They smile, revealing [teeth] like melting hail,"},
    {"type": "matn",
     "ar": "أي: عن أسنان مثل البرد الذائب للطافته.",
     "en": "that is, revealing teeth like melting hail, on account of its fineness."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بمعنى «جانب» و«فوق»، فيبنيان حينئذ لكونهما على لفظ الحرفين، ومناسبين لهما معنى،",
     "en": "In the sense of “jānib” (side) and “fawq” (above); they are then indeclinable, because they have the form of the two particles and resemble them in meaning;"},
    {"type": "pair",
     "ar": "فيلزم عن الإضافة بخلاف «على».",
     "en": "so “ʿan” [as a noun] necessarily takes a genitive complement (iḍāfa), unlike “ʿalā”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة الشورى: ١١.",
     "en": "Qurʾān, Sūrat al-Shūrā 42:11."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بالنصب.",
     "en": "[Read] with the accusative."},
    {"type": "pair",
     "ar": "وقوله: «على بعض الوجوه» إشارة إلى أن لهذا الكلام وجوها، وليس زيادة الكاف إلا في وجه.",
     "en": "His words “on some of the interpretations” indicate that this statement has several interpretations, and the kāf is redundant in only one of them."},
    {"type": "pair",
     "ar": "وأما الباقي فمنه ما لا زيادة فيه شيء،",
     "en": "As for the rest, among them is one in which nothing is redundant,"},
    {"type": "pair",
     "ar": "وهو أن نفي مثل المثل كناية عن نفي المثل؛ إذ لو وجد المثل لكان للمثل مثل، وهو الله تعالى؛ لأن المماثلة من الجانبين.",
     "en": "namely, that negating a likeness of the likeness is a metonymy (kināya) for negating the likeness; for were there a likeness, the likeness would have a likeness, namely Allah, the Exalted, since likeness is mutual."},
    {"type": "pair",
     "ar": "وهذا وجه تلقاه الفحول بالقبول، ورجحوه بأن الكناية أبلغ من التصريح، وعدم الزيادة أحق بالترجيح،",
     "en": "This is an interpretation the masters received with acceptance; they preferred it on the grounds that metonymy is more eloquent than explicit statement, and that the absence of redundancy has the better claim to preference."},
    {"type": "pair",
     "ar": "وفيه بحث، وهو أن نفي مثل المثل لا يستلزم نفي المثل؛ لأن الشيء ليس مثل مثله،",
     "en": "There is room for discussion in this: negating a likeness of the likeness does not entail negating the likeness, because a thing is not the like of its like;"},
    {"type": "pair",
     "ar": "بل المثل المشارك للشيء في صفة مع كون الشيء أقوى منه فيها، وبمنزلة الأصل، والمثل بمنزلة الملحق به المتقارب منه،",
     "en": "rather, the like is what shares a quality with the thing while the thing is stronger in it than it and stands as the original, whereas the like stands as what is attached to it and close to it."},
    {"type": "pair",
     "ar": "ما لا زيادة فيه للكاف، بل الزائد هو المثل.",
     "en": "[Among them is also one] in which the kāf is not redundant; rather, the redundant word is “mithl”."},
    {"type": "pair",
     "ar": "وكان وجهه أن الحكم بزيادة الكاف هو الحكم بالزيادة قبل الحاجة، بخلاف الحكم بزيادة المثل.",
     "en": "Its rationale seems to be that judging the kāf redundant is judging [a word] redundant before the need [for it has been met], unlike judging “mithl” redundant."},
    {"type": "pair",
     "ar": "ورجح الأول بأن الحكم بزيادة الاسم سيما إذا كان الحرف حرفا واحدا،",
     "en": "The first was preferred on the grounds that judging a noun redundant [is weaker than judging a particle so], especially when the particle consists of a single letter."},
    # REVIEW: the sentence «ورجح الأول بأن الحكم بزيادة الاسم سيما إذا كان الحرف حرفا واحدا» appears
    # to lack a predicate (e.g. "is weaker / less fitting"); transcribed as printed.
    {"type": "pair",
     "ar": "ويرجحه أيضا أن الحكم بزيادة المثل يوجب دخول الكاف على الضمير في التقدير.",
     "en": "It is also preferred because judging “mithl” redundant entails the kāf entering upon a pronoun in the underlying form."},
    {"type": "pair",
     "ar": "قال الرضي: اعلم أنه إذا أمكن في كل حرف جر يتوهم خروجه عن أصله، وكونه بمعنى كلمة أخرى، وزيادته أن يبقى على أصل معناه الموضوع له،",
     "en": "Al-Raḍī said: Know that whenever it is possible, in any preposition that is imagined to depart from its original [meaning], to be in the sense of another word, or to be redundant, that it remain on the original meaning for which it was coined,"},
    {"type": "pair",
     "ar": "ويضمن فعله المعدى به معنى من المعاني يستقيم به الكلام، فهو الأولى بل هو الواجب",
     "en": "and that the verb made transitive by it be given the implied sense (taḍmīn) of some meaning by which the speech is set right, then that is the better course — indeed it is obligatory."},
    {"type": "pair",
     "ar": "فلا نقول: إن «على» بمعنى «من» في قوله: ﴿الذين إذا اكتالوا على الناس﴾ (المطففين:٢)،",
     "en": "So we do not say that “ʿalā” is in the sense of “min” in His words “those who, when they take a measure from (ʿalā) people” (al-Muṭaffifīn 83:2);"},
    {"type": "pair",
     "ar": "بل يضمن «اكتالوا» معنى «تحكموا» في الاكتيال وتسلطوا.",
     "en": "rather, “iktālū” is given the implied sense of “taḥakkamū” (they exercised control) in taking measure, and “tasallaṭū” (they dominated)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولا يقع كذلك عند سيبويه والمحققين إلا في الضرورة.",
     "en": "According to Sībawayh and the verifying scholars, it does not occur thus except under [metrical] necessity (ḍarūra)."},
    # REVIEW: «الأخفس والفاسي» printed thus; presumably for «الأخفش والفارسي» (al-Akhfash and
    # al-Fārisī, as in Mughnī al-labīb). Transcribed as printed; English gives the intended names.
    {"type": "pair",
     "ar": "وقال كثير منهم الأخفس والفاسي: يجوز في الاختيار نحو: «زيد كالأسد» أن يكون الكاف في موضع رفع، والأسد مخفوضا بالإضافة.",
     "en": "Many, among them al-Akhfash and al-Fārisī [printed “al-Akhfas” and “al-Fāsī”], said: it is permissible in free choice, as in “Zaydun ka-l-asadi”, for the kāf to be in the position of the nominative and “al-asad” to be in the genitive by annexation."},
    {"type": "pair",
     "ar": "ويقع مثل هذا في كتب المعربين كثيرا، كذا في المغني.",
     "en": "The like of this occurs frequently in the books of those who parse [texts]; so it is in al-Mughnī."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وقبله بيض ثلاث كنعاج جم، بيض صفة محذوف أي: نساء بيض جمع بيضاء.",
     "en": "Before it [comes]: “bīḍun thalāthun ka-niʿājin jummin” (three fair ones, like hornless wild cows); “bīḍ” is an adjective of an omitted noun, that is, fair women; it is the plural of “bayḍāʾ”."},
    {"type": "pair",
     "ar": "والمراد بالنعاج هنا: بقرات الوحش. وكثيرا ما يشبه بها النساء في العيون والأعناق.",
     "en": "What is meant by “niʿāj” here is wild cows; women are often likened to them in their eyes and necks."},
    {"type": "pair",
     "ar": "والجم: جمع جماء، وهي التي لا قرن لها.",
     "en": "“Al-jumm” is the plural of “jammāʾ”, which is the one that has no horn."},
]
