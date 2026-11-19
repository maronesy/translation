# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 301 (printed ٣٠٠)."""

PAGE_NUMBER = 301
PRINTED_PAGE = "٣٠٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «لئلا يكون إجحافا.» at the foot of PDF p. 300 (new sentence).
    {"type": "matn",
     "ar": "وقولهم: «لا كزيد» إن جعلنا الكاف اسما جاز أن يكون «كزيد» اسما، والخبر محذوفا أي: «لا مثله موجود»،",
     "en": "As for their saying “lā ka-Zaydin” (none like Zayd): if we take the kāf as a noun, “ka-Zaydin” may be the noun [of lā] with the predicate elided, that is, “no one like him is existent”;"},
    {"type": "matn",
     "ar": "وجاز أن يكون خبرا أي: «لا أحد مثل زيد»، وإن جعلناه حرفا، فالاسم محذوف أي: «لا أحد كزيد».",
     "en": "and it may be the predicate, that is, “there is no one like Zayd.” If we take it as a particle, the noun is elided, that is, “there is no one like Zayd.”"},

    {"type": "section", "ar": "[خبر ما ولا المشبهتين بليس]",
     "en": "The Predicate of Mā and Lā That Resemble Laysa"},

    {"type": "matn",
     "ar": "(خبر «ما» و«لا» المشبهتين) في النفي[[١]] والدخول على الجملة الاسمية (بـ«ليس»: هو المسند بعد دخولهما) أي: دخول «ما» و«لا».",
     "en": "(The predicate of “mā” and “lā” that resemble) in negation and in entering upon the nominal sentence (“laysa” is that which is predicated after their entry), that is, after the entry of “mā” and “lā.”"},
    {"type": "matn",
     "ar": "(وهي) أي: خبرية[[٢]] خبر «ما» و«لا» لهما، وكذا اسمية اسمهما لهما (لغة حجازية)",
     "en": "(And it), that is, the predicate of “mā” and “lā” being their predicate, and likewise their noun being their noun, (is the usage of the Ḥijāz)."},
    {"type": "matn",
     "ar": "وخص الخبرية بالذكر؛ لأن إعمالهما وجعل اسمهما وخبرهما اسما وخبرا لهما إنما يظهر باعتبار الخبر، فجعل الخبر خبرا لهما إنما هو في لغة أهل الحجاز.",
     "en": "He singled out predicatehood for mention because their governing, and the making of their noun and predicate a noun and predicate belonging to them, appears only with respect to the predicate; so making the predicate their predicate belongs only to the usage of the people of the Ḥijāz."},
    {"type": "matn",
     "ar": "وأما بنو تميم فحيث لا يذهبون[[٣]] إلى إعمالهما لا يجعلون الخبر خبرا لهما، ولا الاسم اسما لهما، بل هما مبتدأ وخبر على ما كانا عليه قبل دخولهما عليهما،",
     "en": "As for the Banū Tamīm, since they do not hold that the two govern, they make neither the predicate their predicate nor the noun their noun; rather, the two are a subject (mubtadaʾ) and predicate, as they were before [mā and lā] entered upon them."},
    {"type": "matn",
     "ar": "ولغة أهل الحجاز هي التي جاء عليها التنزيل قال الله تعالى ﴿ما هذا بشرا﴾[[٤]]، و﴿ما هن أمهاتهم﴾[[٥]].",
     "en": "The usage of the people of the Ḥijāz is the one on which the Revelation came. Allah the Exalted said: “This is not a human being” (mā hādhā basharan), and “They are not their mothers” (mā hunna ummahātihim)."},
    {"type": "matn",
     "ar": "(وإذا زيدت «إن» مع «ما») أي: بعد «ما»، نحو: «ما إن زيد قائم»،",
     "en": "(And when “in” is added with “mā”), that is, after “mā,” as in “mā in Zaydun qāʾimun” (Zayd is not standing),"},
    {"type": "matn",
     "ar": "قيل: إنما خصت «ما» بالذكر؛ لأنها لا تزاد مع «لا» في استعمالاتهم،",
     "en": "it has been said: “mā” was singled out for mention only because [in] is not added with “lā” in their usage."},
    {"type": "matn",
     "ar": "وهي زائدة عند البصريين[[٦]]، ونافية مؤكدة[[٧]] عند الكوفيين.",
     "en": "It is redundant (zāʾida) according to the Baṣrans, and a reinforcing negative according to the Kūfans."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: print reads «وألحق» (with hamza on the alif); probably «والحق» ("the truth is") is meant; transcribed as printed.
    {"type": "pair",
     "ar": "قال الشيخ الرضي: إن «ما وليس» لنفي الحال عند النحاة. وألحق أنهما لمطلق النفي.",
     "en": "Shaykh al-Raḍī said: “mā” and “laysa” are for negating the present according to the grammarians; and the truth is that they are for negation without restriction."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن الضمير راجع إلى الخبرية المستفادة من خبر «ما ولا».",
     "en": "He means that the pronoun refers to the predicatehood conveyed by “the predicate of mā and lā.”"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: لا ينقل عن أحد رفع اسم «لا» ونصب خبرها.",
     "en": "Shaykh al-Raḍī said: it is not transmitted from anyone that the noun of “lā” is put in the nominative and its predicate in the accusative."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وذلك لأن قياس العوامل أن تختص بالقبيل الذي تعمل فيه من الاسم والفعل لتكون متمكنة بثبوتها في مركزها، وما مشتركة بين الاسم والفعل.",
     "en": "That is because the rule for governing words (ʿawāmil) is that they be confined to the class, noun or verb, in which they govern, so that they are firmly established by remaining in their proper place; and mā is shared between the noun and the verb."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة يوسف: ٣١.",
     "en": "Qurʾān, Sūrat Yūsuf 12:31."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة المجادلة: ٢.",
     "en": "Qurʾān, Sūrat al-Mujādila 58:2."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وليست «إن» النافية، بل التي تزاد مع «لما» و«ما» المصدرية أيضا.",
     "en": "It is not the negative “in,” but the one that is also added with “lammā” and with the infinitival (maṣdariyya) “mā.”"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الظاهر أنه عند الكوفيين أيضا نافية زيدت لتأكيد نفي «ما»، وإلا فالنفي على النفي إثبات.",
     "en": "Shaykh al-Raḍī said: the evident view is that, for the Kūfans too, it is a negative added to reinforce the negation of “mā”; otherwise, negation upon negation is affirmation."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وإلا فالنفي على النفي يفيد الإثبات.",
     "en": "Otherwise, negation upon negation yields affirmation."},
    {"type": "pair",
     "ar": "وفيه أن هذا يخالف ما قالوا من أنه لا يجوز الجمع بين حرفين متفقي المعنى إلا مفصولا بينهما.",
     "en": "Against this [it is said] that it contradicts what they said, namely that two particles of the same meaning may not be combined unless they are separated."},
]
