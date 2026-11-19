# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 454 (printed ٤٥٣)."""

PAGE_NUMBER = 454
PRINTED_PAGE = "٤٥٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فكما لا يدخل لام التعريف على «أن» مع الفعل ينبغي» at the foot of PDF p. 453 (mid-sentence).
    {"type": "matn",
     "ar": "ألا يدخل على المصدر المقدر به، ولكن جوزوا[[١]] ذلك على قلة، فرقا بين شيء وبين المقدر به.",
     "en": "…not to enter upon the verbal noun construed as it; but they permitted this rarely, to distinguish between a thing and what it is construed as."},
    {"type": "matn",
     "ar": "قيل: لم يأت في القرآن شيء من المصادر المعرفة باللام عاملا في فاعل أو مفعول صريح، بل قد جاء عاملا بحرف الجر، نحو: ﴿لا يحب الله الجهر بالسوء﴾[[٢]].",
     "en": "It has been said: nothing among the verbal nouns made definite by the lām occurs in the Qurʾān governing an explicit agent or object; rather, it occurs governing by means of a preposition, as in “Allah does not love the public utterance of evil”."},
    {"type": "matn",
     "ar": "(فإن كان) أي: المصدر (مفعولا مطلقا) صرفا من غير اعتبار إبداله من الفعل (فالعمل للفعل) من غير تجويز أن يكون للمصدر؛",
     "en": "(If it is), that is, the verbal noun, (an absolute object) purely, without regard to its substituting for the verb, (then the governing belongs to the verb), without allowing that it belong to the verbal noun;"},
    {"type": "matn",
     "ar": "إذ لا يجوز إعمال الضعيف مع وجدان القوي، سواء كان الفعل مذكورا نحو: «ضربت ضربا زيدا»، أو محذوفا غير لازم نحو: «ضربا زيدا».",
     "en": "for it is not permitted to make the weak govern when the strong is present, whether the verb is mentioned, as in “ḍarabtu ḍarban Zaydan” (I struck Zayd a striking), or omitted but not necessarily so, as in “ḍarban Zaydan” (a striking of Zayd!)."},
    {"type": "matn",
     "ar": "(وإن كان) أي: المصدر[[٣]] مفعولا مطلقا واقعا (بدلا منه) أي: من الفعل، وهو ما كان حذف فعله لازما نحو: «سقيا له، وشكرا له، وحمدا له»",
     "en": "(And if it is), that is, the verbal noun, an absolute object occurring (as a substitute for it), that is, for the verb, namely what has its verb necessarily omitted, as in “saqyan lahu” (may he be watered), “shukran lahu” (thanks to him) and “ḥamdan lahu” (praise to him),"},
    {"type": "matn",
     "ar": "(فالوجهان) أي: فيجوز فيه وجهان: عمل الفعل للأصالة[[٤]]، وعمل المصدر للنيابة.",
     "en": "(then both ways [are permitted]), that is, two ways are permitted in it: the governing of the verb, by virtue of being the original, and the governing of the verbal noun, by virtue of standing in its place."},
    {"type": "matn",
     "ar": "وقيل: عمل المصدر للمصدرية، وعمله للبدلية، ففي قوله: «وجهان» وجهان.",
     "en": "It has been said: the governing of the verbal noun is by virtue of its being a verbal noun, or its governing is by virtue of its being a substitute; so in his words “two ways” there are two ways [of interpretation]."},
    {"type": "matn",
     "ar": "وإنما فصل بين قسمي المصدر -أعني: ما لم يكن مفعولا مطلقا، وما كان إياه بالجمل المعترضة- لبيان بعض أحكام عمل المصدر؛",
     "en": "He separated the two kinds of verbal noun, namely what is not an absolute object and what is one, by the parenthetical sentences, only in order to set out some of the rules of the verbal noun’s governing;"},
    {"type": "matn",
     "ar": "لأن عمل المصدر في القسم الأول أكثر وأظهر، فلو أخرت عن القسمين لتوهم تعلقها بالقسمين على السواء.",
     "en": "for the verbal noun’s governing in the first kind is more frequent and more evident; had they been postponed until after both kinds, it would have been supposed that they pertain to both kinds equally."},

    {"type": "section", "ar": "[اسم الفاعل]",
     "en": "The Active Participle (Ism al-Fāʿil)"},

    {"type": "matn",
     "ar": "(اسم الفاعل: ما اشتق) أي: اسم اشتق (من فعل) أي: حدث موضوعا[[٥]]",
     "en": "(The active participle is what is derived), that is, a noun derived, (from a verb), that is, from an event, coined…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «إذني زيد بقوله ذلك» (a clear print, no space after the colon); the form «إذني» is odd, perhaps for «أذاني» or «آذنني». Transcribed as printed; the English renders the sense tentatively.
    {"type": "pair",
     "ar": "وأيضا قد يقع عاملا بدون التقدير، نحو قول العرب: إذني زيد بقوله ذلك،",
     "en": "Further, it sometimes governs without that construal, as in the saying of the Arabs “idhnī Zaydun bi-qawlihi dhālika” [roughly: Zayd’s saying that troubled me],"},
    {"type": "pair",
     "ar": "وقول أعرابي: اللهم إن استغفاري مع إصراري للؤم، وإن تركي استغفارك مع علمي بسعة عفوك لعجز، كذا في شرح التسهيل.",
     "en": "and the saying of a Bedouin: “O Allah, my seeking Your forgiveness while I persist [in sin] is baseness, and my abandoning seeking Your forgiveness while I know the breadth of Your pardon is incapacity”; so in Sharḥ al-Tashīl."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة النساء: ١٤٨.",
     "en": "Qurʾān, Sūrat al-Nisāʾ 4:148."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: أن ضمير «كان» راجع إلى المصدر، وبدلا خبره بتقدير الموصوف.",
     "en": "He means that the pronoun of “kāna” refers back to the verbal noun, and “badalan” is its predicate, with the qualified noun understood."},
    {"type": "pair",
     "ar": "وإنما لم يقل: أي: المفعول المطلق بدلا منه رعاية لجزالة المعنى؛",
     "en": "He did not say “that is, the absolute object as a substitute for it” out of regard for the soundness of the sense;"},
    {"type": "pair",
     "ar": "لأن الكلام في المصدر وموافقة المعطوف عليه، فإن الضمير فيه راجع إلى المصدر.",
     "en": "for the discussion is about the verbal noun, and [out of regard for] agreement with what it is coordinated with, since the pronoun in that refers back to the verbal noun."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ووجوب الإضمار العارض لا أثر له في تقدير العمل.",
     "en": "The necessity of concealment, being accidental, has no effect on construing the governing."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إشارة إلى أنه يتضمن معنى الوضع، واللام صلة الوضع.",
     "en": "This indicates that it includes the sense of coining (waḍʿ), and the lām is the complement of “coining”."},
    {"type": "pair",
     "ar": "ولك أن تقول في الاشتقاق معنى الوضع؛ لأنه وضع للنوع، واللام للأجل.",
     "en": "You may say that “derivation” has the sense of coining, since it is coining for the kind, and the lām is of purpose."},
]
