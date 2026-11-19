# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 433 (printed ٤٣٢)."""

PAGE_NUMBER = 433
PRINTED_PAGE = "٤٣٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وإذا اعتبر مع علامة» at the foot of PDF p. 432.
    {"type": "matn",
     "ar": "التثنية استغني به عن ذكر الاثنين على حدة، فاختاروا لحوق العلامة التي هي أخف عن ذكرهما،",
     "en": "…of the dual, mention of ithnān separately is dispensed with by it. So they chose the attachment of the mark, which is lighter than mentioning the two [the number and the specifier];"},
    {"type": "matn",
     "ar": "ولا شك أن رجلان أخف من اثنا رجل،",
     "en": "and there is no doubt that “rajulān” is lighter than “ithnā rajul”."},
    {"type": "matn",
     "ar": "وذلك الاستغناء إنما يكون (لإفادته) أي: إفادة لفظ التمييز (النص المقصود) أي: التنصيص على العدد، والتصريح به الذي قصد ذلك التنصيص والتصريح (بالعدد) أي: بذكر اسم العدد،",
     "en": "That dispensing occurs only (because it conveys), that is, because the word of the specifier conveys, (the intended explicit statement), that is, stating the number explicitly and expressly, which explicit and express statement was intended (by the number), that is, by mentioning the number noun;"},
    {"type": "matn",
     "ar": "فلما أفاد التمييز ذلك التنصيص استغني في إفادته عن ذكر العدد على حدة.",
     "en": "so since the specifier conveyed that explicit statement, mention of the number separately was dispensed with in conveying it."},
    {"type": "matn",
     "ar": "(وتقول[[١]] في المفرد من العدد) أي: في الواحد من المتعدد (باعتبار تصييره) أي: بسبب اعتبار تصييره[[٢]]،",
     "en": "(You say, for the single one of a number), that is, for one of a multiple, (with regard to its making), that is, by reason of regarding its making,"},
    {"type": "matn",
     "ar": "أي: تصيير ذلك المفرد عددا أنقص منه أزيد عليه بواحد (الثاني) في المذكر.",
     "en": "that is, that single one’s making a number less than it into one greater by one: (al-thānī) (the second, i.e. the one making two) for the masculine."},
    {"type": "matn",
     "ar": "فقوله: «الثاني» مقول القول، وذلك القول إنما هو باعتبار تصييره الواحد اثنين بانضمامه إليه،",
     "en": "So his word “al-thānī” is the object of “you say”, and that saying is only with regard to its making one into two by being joined to it;"},
    {"type": "matn",
     "ar": "فيكون معنى ثاني الواحد مصيره بانضمامه إليه اثنين،",
     "en": "so the meaning of “thānī al-wāḥid” (the second of one) is: that which makes it two by being joined to it."},
    {"type": "matn",
     "ar": "وإنما ابتدأ من الثاني؛ إذ ليس قبل الواحد عدد حتى يكون الواحد مصيره واحدا",
     "en": "He started from “the second” only because there is no number before one such that one would make it one."},
    {"type": "matn",
     "ar": "(والثانية) في المؤنث على هذا القياس، وهكذا (إلى العاشر) في المذكر (والعاشرة) في المؤنث",
     "en": "(And al-thāniya) for the feminine, by the same analogy; and so on (up to al-ʿāshir) for the masculine (and al-ʿāshira) for the feminine,"},
    {"type": "matn",
     "ar": "(لا غير) أي: لا تقول: غير ذلك، فلا يجري ذلك فيما تحت الاثنين، ولا فيما فوق العشرة؛ إذ ما فوقه مركبات لا يتيسر اشتقاق اسم الفاعل منها[[٣]].",
     "en": "(and no others), that is, you do not say anything other than that; so this does not apply below two, nor above ten, since what is above it are compounds from which deriving an active participle is not feasible."},
    {"type": "matn",
     "ar": "(وتقول) في المفرد (وباعتبار حاله) أي: مرتبته[[٤]] من المتعدد من غير اعتبار معنى التصيير",
     "en": "(And you say), for the single one, (and with regard to its state), that is, its rank within the multiple, without regard to the meaning of making,"},
    {"type": "matn",
     "ar": "(الأول والثاني) إذا وقع في المرتبة الأولى والثانية في المذكر (والأولى والثانية) في المؤنث كذلك من غير اعتبار معنى التصيير،",
     "en": "(al-awwal and al-thānī) [the first and the second] when it occurs in the first and second rank, for the masculine, (and al-ūlā and al-thāniya) for the feminine likewise, without regard to the meaning of making."},
    {"type": "matn",
     "ar": "وإنما لم يقل: الواحد والواحدة؛ لأنهما لا يدلان على المرتبة، فأبدل منهما الأول والأولى للدلالة عليها",
     "en": "He did not say “al-wāḥid” and “al-wāḥida” only because they do not indicate rank; so he replaced them with “al-awwal” and “al-ūlā” to indicate it."},
    {"type": "matn",
     "ar": "وهكذا (إلى العاشر والعاشرة والحادي عشر) في المذكر (والحادية عشرة) في المؤنث",
     "en": "And so on (up to al-ʿāshir and al-ʿāshira, and al-ḥādī ʿashar) for the masculine (and al-ḥādiya ʿashrata) for the feminine,"},
    {"type": "matn",
     "ar": "(و) كذلك (الثاني عشر والثانية عشرة إلى التاسع عشر والتاسعة عشرة).",
     "en": "(and) likewise (al-thānī ʿashar and al-thāniya ʿashrata, up to al-tāsiʿ ʿashar and al-tāsiʿa ʿashrata)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "في الحواشي الهندية: تقول \"أنت\" وقد صرح بذكر أمثال أن تقول: صيغة الخطاب،",
     "en": "In the Indian glosses: “taqūlu” [means] “you”; and he has stated this expressly by mentioning [phrases] like “an taqūla” (that you say): [so it is] the form of address."},
    {"type": "pair",
     "ar": "ويحتمل الغيبة بإرجاع الضمير المستكن إلى العرب، أي: يقول العرب:",
     "en": "It may also be the third person, referring the concealed pronoun to the Arabs, that is, “the Arabs say”."},
    {"type": "pair",
     "ar": "ويرجح ما اختاره قوله: وإن شئت قلت: حادي أحد عشر إلى تاسع تسعة عشر، فتعرب الأول.",
     "en": "What he chose is supported by his words “and if you wish, you say: ḥādī aḥada ʿashar … tāsiʿ tisʿata ʿashar, and you decline the first”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "مصدر مضاف إلى الفاعل ومفعولاه محذوفان قدرهما الشارح رحمه الله.",
     "en": "A maṣdar annexed to its agent; its two objects are elided, and the commentator, may Allah have mercy on him, supplied them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ينتقض بحادي عشر أحد عشر ونظائره إذا أخذ اسم الفاعل من أول جزء لتلك المركبات.",
     "en": "This is broken by “ḥādī ʿashar aḥada ʿashar” and its like, when the active participle is taken from the first part of those compounds."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا يخفى أن التصيير أيضا حال من الأحوال، فلا يحسن مقابلته بالحال، وفسر الحال بالمرتبة؛",
     "en": "It is not hidden that making is also one of the states, so it is not apt to set it against “state”; and so he interpreted “state” as rank."},
    # REVIEW: «تلك المعدود» is printed (feminine demonstrative with masculine noun); transcribed as printed.
    # REVIEW: a stray mark is printed before «إلى» («والثاني ٔإلى»); omitted here.
    {"type": "pair",
     "ar": "لأنه لو قصد باعتبار حاله بمعنى أنه واحد من تلك المعدود من غير بيان مرتبته، يقال: واحد الثلاثة والأربعة وواحدتها، ولا يشتق له لفظ الأول والثاني إلى غير ذلك.",
     "en": "For if, by “with regard to its state”, it were meant that it is one of those counted, without stating its rank, one would say “wāḥid al-thalātha” (one of the three), “[wāḥid] al-arbaʿa” and “wāḥidatuhā”, and the words “al-awwal”, “al-thānī” and so on would not be derived for it."},
]
