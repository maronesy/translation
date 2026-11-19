# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 324 (printed ٣٢٣)."""

PAGE_NUMBER = 324
PRINTED_PAGE = "٣٢٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… إلى الوصف بأسماء الأجناس،» at the foot of PDF p. 323 (mid-sentence).
    {"type": "matn",
     "ar": "والضمير ليس باسم جنس، وقد أضيف إليه على سبيل الشذوذ كقول الشاعر:",
     "en": "…and the pronoun is not a generic noun. It has been annexed to it, anomalously, as in the poet’s words:"},
    {"type": "verse",
     "ar": "إنما يعرف[[١]] ذا الفضـ      ـل من الناس ذووه",
     "en": "Only those who possess it recognize the man of merit among people."},
    {"type": "matn",
     "ar": "ولو قيل: «لا يضاف إلى غير اسم الجنس» لكان أشمل، فكأنه خص المضمر[[٢]] بالذكر[[٣]]؛",
     "en": "Had it been said, “it is not annexed to anything but a generic noun,” it would have been more comprehensive; it seems he singled out the pronoun for mention"},
    {"type": "matn",
     "ar": "لأنه كان لبعض تلك الأسماء حكم خاص عند إضافته إلى ياء المتكلم، فنفي إضافته إلى المضمر مطلقا نفيا لاختصاصه بحكم باعتبار إضافته إليه",
     "en": "because some of those nouns had a special rule when annexed to the yāʾ of the speaker; so he denied its annexation to a pronoun absolutely, thereby denying that it has a special rule by virtue of being annexed to it."},
    # REVIEW: «إلى الأسماء الأجناس» as printed (article on the first term of an annexation); transcribed as printed.
    {"type": "matn",
     "ar": "(ولا يقطع) أي: «ذو»[[٤]] (عن الإضافة)؛ لأن جعله وصلة إلى الأسماء الأجناس ليس إلا بإضافته إليها.",
     "en": "(Nor is it cut off), that is, “dhū,” (from annexation), because its being made a means of reaching generic nouns is only through its annexation to them."},

    {"type": "section", "ar": "[التوابع]",
     "en": "The Appositives (al-Tawābiʿ)"},

    {"type": "matn",
     "ar": "(التوابع) وهو: جمع «تابع»، منقول من الوصفية إلى الاسمية، والفاعل الاسمي يجمع على «فواعل»[[٥]] كـ«الكاهل»[[٦]] على «الكواهل».",
     "en": "(The appositives, al-tawābiʿ): it is the plural of “tābiʿ” (follower), transferred from adjectival to nominal status; and the substantive of the pattern fāʿil is pluralized on fawāʿil, as “kāhil” on “kawāhil.”"},
    {"type": "matn",
     "ar": "والمراد بها: توابع المرفوعات والمنصوبات والمجرورات التي هي من أقسام الاسم[[٧]]،",
     "en": "What is meant by them is the appositives of the nominatives, accusatives and genitives, which belong to the divisions of the noun;"},
    {"type": "matn",
     "ar": "فلا ينتقض حدها بخروج نحو: «إن أن» و«ضرب ضرب»[[٨]] لعدم كونهما من أفراد المحدود.",
     "en": "so its definition is not undermined by the exclusion of such as “inna anna” and “ḍaraba ḍaraba,” since these are not instances of what is defined."},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 323 (Footnote 5 there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "إليه.",
     "en": "…to it."},
    {"type": "pair",
     "ar": "وأما أسماء الأجناس من نحو الضرب والقتل فإنها وإن لم تكن مما يوصف بها إلا أنها من جنس ما يقع صفة كالضارب.",
     "en": "As for generic nouns such as “al-ḍarb” (striking) and “al-qatl” (killing), though they are not among what is used to describe, they belong to the genus of what serves as an attribute, like “al-ḍārib” (the striker)."},
    {"type": "pair",
     "ar": "وأيضا لو حذف المضاف الموصوف به والمضاف إليه ضميرا، وعلم لم يجز قيامهما مقامه.",
     "en": "Further, were the annexed noun used as the attribute elided while what it is annexed to is a pronoun or a proper name, they could not take its place."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ونحو: اللهم صل على محمد وذويه.",
     "en": "And such as: “O Allah, bless Muḥammad and his kin (dhawīhi).”"},
    {"type": "pair",
     "ar": "وما وقع في كلام بعض المتأخرين: وأصلي على نبيه محمد وآله وذويه، فذلك اقتباس من الدعاء المأثور.",
     "en": "As for what occurs in the words of some later authors, “and I invoke blessings on His Prophet Muḥammad, his family and his kin,” that is borrowed from the transmitted supplication."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن المناسب للمقام النظر إلى حال إضافته إلى المضمر الخاص، لكن عدل عنه إلى نوعه.",
     "en": "He means: what suited the context was to consider its annexation to the particular pronoun [the yāʾ of the speaker], but he turned from that to its kind."},
    {"type": "pair",
     "ar": "وأما العدول إلى جنسه فبعيد.",
     "en": "Turning to its genus, however, would be far-fetched."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كان ما ذكره مقتضيا لاختصاص ياء المتكلم بالذكر في مقام النفي؛ لأن ثبوت بعض الأحكام إنما يكون بالإضافة إليه،",
     "en": "What he mentioned required singling out the yāʾ of the speaker in the denial, because certain rules hold only through annexation to it;"},
    {"type": "pair",
     "ar": "فلما أفاد الأشمل كان المناسب أداء حق الشمول.",
     "en": "but since he expressed the more comprehensive, it was fitting to give comprehensiveness its due."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وكذا متصرفاته. وقد جاء بعض متصرفاته مقطوعا على سبيل الشذوذ نحو: «ولكني أريد به الذوينا».",
     "en": "Likewise its inflected forms. Some of its inflected forms have come cut off [from annexation], anomalously, as in “but I mean by it the dhawīna.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وكذا الفاعلة الوصفية دون الفاعل الوصفي.",
     "en": "Likewise the adjectival fāʿila, but not the adjectival fāʿil."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وهو اسم بحسب الأصل. قال قدس سره في الحاشية: الكاهل ما بين الكتفين، انتهى.",
     "en": "It is a noun by origin. He, may his secret be sanctified, said in the gloss: “al-kāhil is what lies between the shoulders”; end [of quotation]."},
    {"type": "pair",
     "ar": "وأما تابع: فهو اسم بحسب العارض.",
     "en": "As for “tābiʿ,” it is a noun by an accidental [transfer]."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: حقيقة أو حكما. فلا يشكل بالجمل الوصفية والجمل التي هي معطوفات على ما له إعراب.",
     "en": "That is, really or by legal fiction (ḥukman). So no difficulty arises from adjectival clauses and from clauses conjoined to something that has a case position."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "يعني: في «ضرب ضرب زيد» لا في «زيد ضرب ضرب» فافهم.",
     "en": "He means: in “ḍaraba ḍaraba Zaydun,” not in “Zaydun ḍaraba ḍaraba”; so understand."},
    # REVIEW: the sentence «… ويجري يعني: التأكيد اللفظي …» reads oddly; transcribed as printed.
    {"type": "pair",
     "ar": "والاحتياج إلى تخصيص المعرف بجعل \"أن\" و\"ضرب\" من التوابع، والدليل عليه قول المصنف فيما بعد، ويجري يعني: التأكيد اللفظي في الألفاظ كلها،",
     "en": "The need to restrict what is defined arises from making “anna” and “ḍaraba” appositives; the evidence for this is the author’s statement later, “and it runs,” meaning: verbal corroboration (al-taʾkīd al-lafẓī) runs in all expressions."},
    {"type": "pair",
     "ar": "وأرى أن جعل التأكيد كالمعطوف أعم من التابع أهون من جعل التابع أعم.",
     "en": "I consider that making corroboration, like the conjoined noun, broader than the appositive is easier than making the appositive broader."},
]
