# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 568 (printed ٥٦٧)."""

PAGE_NUMBER = 568
PRINTED_PAGE = "٥٦٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "section", "ar": "[ليت]",
     "en": "Layta"},

    {"type": "matn",
     "ar": "(وليت للتمني) أي: لإنشائه، فيدخل:",
     "en": "(And layta is for wishing (tamannī)), that is, for producing a wish; so it enters"},
    {"type": "matn",
     "ar": "على الممكن، نحو: «ليت زيدا قائم».",
     "en": "upon what is possible, as in “layta Zaydan qāʾimun” (would that Zayd were standing),"},
    {"type": "matn",
     "ar": "وعلى المستحيل نحو: «ليت الشباب يعود يوما».",
     "en": "and upon what is impossible, as in “would that youth returned one day”."},
    {"type": "matn",
     "ar": "(وأجاز الفراء: ليت زيدا قائما) بنصب المعمولين بناء على أن «ليت» للتمني،",
     "en": "(Al-Farrāʾ allowed “layta Zaydan qāʾiman”), with both governed terms in the accusative, on the basis that “layta” is for wishing,"},
    {"type": "matn",
     "ar": "فكأنه قيل: أتمنى زيدا قائما[[١]]، أي: أتمناه كائنا على صفة القيام[[٢]].",
     "en": "so it is as though one said “atamannā Zaydan qāʾiman” (I wish Zayd standing), that is, I wish him to be in the state of standing."},
    {"type": "matn",
     "ar": "فالجزآن منصوبان على المفعولين بمعنى «ليت».",
     "en": "So the two parts are in the accusative as the two objects of the meaning of “layta”."},
    {"type": "matn",
     "ar": "وأجاز الكسائي نصب الجزء الثاني بتقدير «كان» ومتمسكها قول الشاعر:",
     "en": "Al-Kisāʾī allowed the accusative of the second part by implying “kāna”; the evidence for both [views] is the poet’s words:"},
    # Only this one hemistich is printed (set in the left half of the line).
    {"type": "verse",
     "ar": "يا ليت أيام الصبا رواجعا",
     "en": "“Would that the days of youth were returning!”"},
    # REVIEW: printed «أيام الصباح» (al-ṣabāḥ, morning) where the verse just quoted has «الصبا» (youth); transcribed as printed.
    {"type": "matn",
     "ar": "فالفراء يقول: معناه: «أتمنى أيام الصباح رواجعا»،",
     "en": "Al-Farrāʾ says that its meaning is “I wish the days of al-ṣabāḥ [sic] returning”,"},
    # REVIEW: here and below «الصبى» is printed with alif maqṣūra, against «الصبا» in the verse; transcribed as printed.
    {"type": "matn",
     "ar": "والكسائي يقول: أي: «يا ليت أيام الصبى كانت رواجعا».",
     "en": "while al-Kisāʾī says it means “would that the days of youth were returning (kānat rawājiʿa)”."},
    {"type": "matn",
     "ar": "فالمحققون: على أن «رواجعا» منصوب على أنه حال من الضمير المستكن في خبرها المحذوف، أي: «ليت أيام الصبى لنا كائنة[[٣]] حال كونها راجعة».",
     "en": "The verifying scholars (al-muḥaqqiqūn) hold that “rawājiʿa” is in the accusative as a circumstantial qualifier (ḥāl) of the pronoun concealed in its elided predicate, that is: “would that the days of youth were ours, existing, in the state of returning”."},

    {"type": "section", "ar": "[لعل]",
     "en": "Laʿalla"},

    {"type": "matn",
     "ar": "(ولعل للترجي) أي: لإنشائه. ولا يدخل على المستحيل.",
     "en": "(And laʿalla is for hoping (tarajjī)), that is, for producing a hope. It does not enter upon what is impossible."},
    {"type": "matn",
     "ar": "ومعناه: توقع أمر مرجو، أو مخوف، كقوله تعالى: ﴿لعلكم تفلحون﴾[[٤]]، و﴿لعل الساعة قريب﴾[[٥]]، والغالب هو الأول.",
     "en": "Its meaning is the expectation of something hoped for or feared, as in His words, the Exalted: “so that perhaps you may prosper” and “perhaps the Hour is near”; the first is the more common."},
    {"type": "matn",
     "ar": "(وشذ الجر بها) أي: بكلمة «لعل» كما جاء في اللغة العقيلية[[٦]]، وأنشد السيرافي في ذلك:",
     "en": "(And putting [a noun] in the genitive with it is anomalous), that is, with the word “laʿalla”, as occurs in the dialect of ʿUqayl; al-Sīrāfī cited on this…"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وهو متعد إلى مفعولين، كذا في الحواشي الهندية.",
     "en": "It is transitive to two objects; so it is in the Indian glosses (al-Ḥawāshī al-Hindiyya)."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: معنى أتمنى كون زيد ذا قيام تمني حصول صفة القيام له.",
     "en": "He means: the meaning of “I wish Zayd to be standing” is wishing that the attribute of standing come about for him."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كائنة بدل من «لنا» أشار إلى نيابة الجار والمجرور المحذوف عن عامله، وتحتمل الضمير.",
     "en": "“Kāʾina” [stands] in place of “lanā”: he indicated that the prepositional phrase stands in for its elided governor and carries the pronoun."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة البقرة: ١٨٩.",
     "en": "Qurʾān, Sūrat al-Baqara 2:189."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة الشورى: ١٧.",
     "en": "Qurʾān, Sūrat al-Shūrā 42:17."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "على صيغة التصغير، في القاموس عقيل كزبير أبو قبيلة.",
     "en": "On the diminutive pattern; in al-Qāmūs: ʿUqayl, like Zubayr, is the forefather of a tribe."},
]
