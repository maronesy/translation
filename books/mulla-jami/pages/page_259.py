# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 259 (printed ٢٥٨)."""

PAGE_NUMBER = 259
PRINTED_PAGE = "٢٥٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والتاء» from the foot of PDF p. 258.
    {"type": "matn",
     "ar": "للمبالغة[[١]].",
     "en": "…being for intensification (mubālagha)."},
    {"type": "matn",
     "ar": "وبعضهم: بجعلها صفة لمصدر أي: إرسالة كافة[[٢]].",
     "en": "Some [answered] by taking it as an adjective qualifying a maṣdar, that is: “a sending [that is] kāffa.”"},
    {"type": "matn",
     "ar": "وبعضهم: بجعلها مصدرا[[٣]] كالكاذبة والعافية.",
     "en": "And some by taking it as a maṣdar, like kādhiba and ʿāfiya."},
    {"type": "matn",
     "ar": "والكل تكلف وتعسف[[٤]].",
     "en": "All of these are strained and forced."},
    {"type": "matn",
     "ar": "(وكل ما دل على هيئة) أي: على صفة سواء كان الدال مشتقا أو جامدا[[٥]] (صح أن يقع حالا) من غير أن يؤول الجامد بالمشتق؛",
     "en": "(Whatever denotes a state [hayʾa]), that is, a quality, whether the word denoting it is derived (mushtaqq) or underived (jāmid), (may properly occur as a ḥāl), without the underived word being construed as a derived one;"},
    {"type": "matn",
     "ar": "لأن المقصود من الحال بيان الهيئة، وهو حاصل به[[٦]]،",
     "en": "for what is intended by the ḥāl is to make the state clear, and that is achieved by it."},
    {"type": "matn",
     "ar": "وهذا رد على جمهور النحاة حيث شرطوا اشتقاق الحال، وتكلفوا في تأويل الجوامد بالمشتق.",
     "en": "This is a rejoinder to the majority of grammarians, since they made derivation a condition of the ḥāl and went to strained lengths to construe underived words as derived."},
    {"type": "matn",
     "ar": "ومع هذا فلا شك أن الأغلب في الحال الاشتقاق",
     "en": "Even so, there is no doubt that the ḥāl is most often derived;"},
    {"type": "matn",
     "ar": "(مثل) «بسرا» و«رطبا» في قولهم: (هذا بسرا[[٧]]) وهو ما بقي فيه حموضة[[٨]] (أطيب منه",
     "en": "(such as) “busran” and “ruṭaban” in their saying: (“This, as busr [unripe dates]”)—busr being [dates] in which some sourness remains—(“is better than it…"},

    {"type": "rule"},

    # ---------------- Footnote 8 of p. 258, continued ----------------
    {"type": "note", "num": ""},   # continued from PDF p. 258, footnote ٨
    {"type": "pair",
     "ar": "الإرسال، وليس كذلك لتراخيه عنه؟",
     "en": "…of the sending, yet it is not so, since it comes later than it?"},
    {"type": "pair",
     "ar": "قلنا: الحال مقدرة، والتقدير لا يلزم أن يكون من صاحب الحال كما مرت الإشارة إليه.",
     "en": "We say: the ḥāl is anticipated (muqaddara), and the anticipation need not be on the part of the owner of the ḥāl, as was indicated earlier."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كالكافية والشافية.",
     "en": "As in al-Kāfiya and al-Shāfiya."},
    {"type": "pair",
     "ar": "وكثير منهم ذهبوا إلى أن تاء المبالغة مخصوصة بفعال وفعول ومفعال.",
     "en": "Many of them held that the tāʾ of intensification is restricted to the patterns faʿʿāl, faʿūl and mifʿāl."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: عامة شاملة.",
     "en": "That is: general and all-embracing."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: تكف كفا. والجملة حال مقدرة.",
     "en": "That is: “you restrain [them] with a restraining (takuffu kaffan)”; and the clause is an anticipated ḥāl."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أما كون الأول تكلفا، فلأن تاء المبالغة في الفاعل غير معلوم الوقوع حتى أنكرها البعض في غير فعال وفعول ومفعال،",
     "en": "As for the first being strained: the tāʾ of intensification on the active participle (fāʿil) is not known to occur, so that some denied it outside faʿʿāl, faʿūl and mifʿāl;"},
    {"type": "pair",
     "ar": "والاستشهاد بالكافية والشافية غير سديد؛ لأنه يحتمل تقدير موصوف مؤنث كالفائدة وغيرها.",
     "en": "and citing al-Kāfiya and al-Shāfiya as evidence is not sound, since a feminine qualified noun such as al-fāʾida (“the treatise”) and the like may be understood."},
    {"type": "pair",
     "ar": "وأما كون الثاني تكلفا فلا حاجة إلى تقدير الموصوف.",
     "en": "As for the second being strained: there is no need to understand a qualified noun."},
    {"type": "pair",
     "ar": "وأما كون الثالث تكلفا، فلأن إتيانه مصدرا غير معلوم.",
     "en": "As for the third being strained: its occurring as a maṣdar is not known."},
    {"type": "pair",
     "ar": "وأما كون الثالث تعسفا، فلأن كافة كقاطبة غير مضافة لازمة الحالية بمعنى جميعا.",
     "en": "As for the third being forced: kāffa, like qāṭiba, is not annexed and is always a ḥāl, meaning “all together.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: من الأحوال الغير المشتقة قياسا الحال الموطئة، وهي اسم جامد موصوف بصفة هي الحال في الحقيقة،",
     "en": "Shaykh al-Raḍī said: among the regularly underived ḥāls is the preparatory ḥāl (al-ḥāl al-muwaṭṭiʾa), which is an underived noun qualified by an adjective that is in reality the ḥāl;"},
    {"type": "pair",
     "ar": "فكان الاسم الجامد وطأ الطريق لما هو حال في الحقيقة، نحو قوله تعالى: ﴿إنا أنزلناه قرآنا عربيا﴾ (سورة يوسف:٢)، ونحو: جاء زيد رجلا بهيا.",
     "en": "the underived noun thus paves the way for what is in reality the ḥāl, as in His words, the Exalted: “We have sent it down as an Arabic Qurʾān” (Qurʾān, Sūrat Yūsuf 12:2), and as in “Zayd came, a handsome man.”"},
    # REVIEW: print reads «جاء زيدا أسدا» (accusative زيدا after جاء); transcribed as printed.
    {"type": "pair",
     "ar": "ومنها ما يقصد به التشبيه نحو: جاء زيدا أسدا، أي: مثل أسد وشجاعا.",
     "en": "Among them is that by which comparison is intended, as in “Zayd came, a lion,” that is, like a lion and brave."},
    {"type": "pair",
     "ar": "ومنها الحال في نحو: بعت الشاء شاة ودرهما.",
     "en": "Among them is the ḥāl in such as “I sold the sheep, a sheep and a dirham [each].”"},
    {"type": "pair",
     "ar": "وضابطته: أن تقصد التقسيط، فتجعل لكل جزء من أجزاء المجزأ قسطا، وتنصب ذلك القسط على الحال،",
     "en": "Its rule is that you intend apportionment (taqsīṭ): you assign to each part of the thing divided a share and put that share in the accusative as a ḥāl,"},
    {"type": "pair",
     "ar": "وتأتي بعده بجزء تابع بواو إما مع واو العطف، أو بحرف الجر نحو: بعت البر قفيزين بدرهم.",
     "en": "and after it you bring a dependent part, either with the conjunctive wāw or with a preposition, as in “I sold the wheat, two qafīzs for a dirham.”"},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن المقصود من النعت أيضا بيان للهيئة.",
     "en": "Against this: what is intended by the adjective (naʿt) is also to make the state clear."},
    {"type": "pair",
     "ar": "ومع ذلك اشترط المصنف فيه أن يكون مشتقا أو جامدا يكون وضعه لغرض المعنى، فينبغي أن يكون الحال أيضا كذلك؛",
     "en": "Even so, the author stipulated for it that, derived or underived, it be coined for the purpose of [conveying a] meaning; so the ḥāl ought to be likewise,"},
    {"type": "pair",
     "ar": "إذ لا اعتداد بما يدل على الهيئة، وليس الغرض من وضعه تلك.",
     "en": "since no account is taken of what denotes a state when that is not the purpose of its coinage."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بفتح الباء، وقد يضم، كذا في القاموس.",
     "en": "With a fatḥa on the bāʾ, and it may take a ḍamma; so in al-Qāmūs."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الأظهر أن يقال: ما بقي فيه نوع عفوصة.",
     "en": "It would be more apt to say: [busr is] that in which some astringency (ʿufūṣa) remains."},
    {"type": "pair",
     "ar": "أول ما بدا من النخل طلح، ثم خلال بالفتح، ثم بلح بالتحريك، ثم بسر، ثم رطب، ثم تمر.",
     "en": "The first thing to appear on the palm is ṭalḥ, then khalāl (with a fatḥa), then balaḥ (with vowelled letters), then busr, then ruṭab, then tamr."},
]
