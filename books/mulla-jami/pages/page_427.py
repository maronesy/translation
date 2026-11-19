# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 427 (printed ٤٢٦)."""

PAGE_NUMBER = 427
PRINTED_PAGE = "٤٢٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وتذكير الثاني في المذكر لكراهة اجتماع تأنيثين من جنس» at the foot of PDF p. 426.
    {"type": "matn",
     "ar": "واحد فيما هو كالكلمة الواحدة، بخلاف «إحدى عشرة، واثنتا عشرة» فإن التأنيث فيهما من جنسين.",
     "en": "…in what is like a single word; unlike “iḥdā ʿashrata” and “ithnatā ʿashrata”, for the feminine marking in them is of two kinds."},
    {"type": "matn",
     "ar": "وأما تذكير الثاني في «أحد عشر واثنا عشر» فمحمول على التذكير في «ثلاثة عشر».",
     "en": "As for the masculine of the second part in “aḥada ʿashara” and “ithnā ʿashara”, it is modelled on the masculine in “thalāthata ʿashara”."},
    {"type": "matn",
     "ar": "والتاء في «ثنتان» بدل من لام الكلمة[[١]]، فلم يتمحض للتأنيث، ولهذا حكمنا عليه بأنه جنس آخر من التأنيث،",
     "en": "The tāʾ in “thintān” is a substitute for the final radical of the word, so it is not purely for the feminine; this is why we judged it to be another kind of feminine marking."},
    {"type": "matn",
     "ar": "وفي «اثنتان» وإن كانت للتأنيث، إلا أنها حملت على «ثنتان».",
     "en": "In “ithnatān”, although it is for the feminine, it was modelled on “thintān”."},
    {"type": "matn",
     "ar": "وأما تأنيث الجزء الثاني في المؤنث؛ لأنه لما وجب[[٢]] تذكيره المذكر -لما عرفت- وجب تأنيثه للمؤنث لانتفاء المانع، وهو عدم الفرق بين المذكر والمؤنث.",
     "en": "As for the feminine of the second part in the feminine: since its being masculine was necessary for the masculine—for the reason you have learned—its being feminine was necessary for the feminine, the obstacle being absent, namely the lack of distinction between masculine and feminine."},
    {"type": "matn",
     "ar": "(وتميم تكسر الشين) عند التركيب (في المؤنث) أي: من «عشرة» تحرزا عن توالي أربع فتحات مع ثقل التركيب في «إحدى عشرة، واثنتا عشرة»، أو خمس في «ثلاث عشرة إلى تسع عشرة»",
     "en": "(Tamīm give the shīn a kasra) in compounding (in the feminine), that is, the shīn of “ʿashara”, to avoid a succession of four fatḥas together with the heaviness of compounding in “iḥdā ʿashrata” and “ithnatā ʿashrata”, or of five in “thalātha ʿashrata” to “tisʿa ʿashrata”;"},
    {"type": "matn",
     "ar": "(والحجازيون يسكنونها) وهي اللغة الفصيحة؛ لأن السكون أخف عن الفتح.",
     "en": "(while the people of the Ḥijāz give it a sukūn), which is the eloquent usage, because sukūn is lighter than fatḥa."},
    {"type": "matn",
     "ar": "(و) تقول: (عشرون وأخواتها) بكسر التاء؛ لأنه منصوب[[٣]] بالعطف على «عشرون» المنصوب محلا بمفعولية القول،",
     "en": "(And) you say: (ʿishrūn and its sisters), with a kasra on the tāʾ [of akhawātihā], because it is in the accusative by coordination with “ʿishrūn”, which is accusative in position as the object of “saying”."},
    {"type": "matn",
     "ar": "وهي: «ثلاثون وأربعون وخمسون إلى تسعين» (فيهما) أي: في المذكر والمؤنث من غير فرق، وهي عقود ثمانية.",
     "en": "They are “thalāthūn”, “arbaʿūn”, “khamsūn” up to “tisʿūn”, (for both), that is, for the masculine and the feminine without distinction; they are eight decades."},
    {"type": "matn",
     "ar": "وتقول فيما زاد على كل عقد من تلك العقود إلى عقد آخر (أحد وعشرون) في المذكر (إحدى وعشرون) في المؤنث،",
     "en": "For what exceeds each of those decades up to the next decade you say (aḥad wa-ʿishrūn) for the masculine, (iḥdā wa-ʿishrūn) for the feminine."},
    {"type": "matn",
     "ar": "ولما غير «الواحد والواحدة» ههنا بدون التركيب[[٤]]؛ لأن",
     "en": "Since “wāḥid” and “wāḥida” were changed here without compounding, because…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أعني: الياء؛ لأنه من الثني لا من اثنتان، فهي للتأنيث؛ لأن همزة الوصل عوض عنها أي: عن الياء.",
     "en": "I mean the yāʾ, because it is from al-thany, not from ithnatān; there [in ithnatān] it is for the feminine, because the conjunctive hamza (hamzat al-waṣl) is a compensation for it, that is, for the yāʾ."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: الصواب فلأنه، والجواب أنه جزاء إما بتقدير فيقال إلى آخره أو حذف الفاء في جواب أما جائز مع قول محذوف نص عليه في الرضي.",
     "en": "It has been said: the correct form is “fa-li-annahu”. The answer: it is an apodosis, either by supposing “fa-yuqālu …” and so on, or [because] eliding the fāʾ in the apodosis of ammā is permitted together with an elided “saying”—this is stated explicitly in al-Raḍī."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ومن قال: إن الإعراب المحلي إنما يكون للمبني، وعشرون ليس مبنيا، وهو ظاهر إنما المحتمل أن يكون محكيا،",
     "en": "Whoever said: “positional inflection (al-iʿrāb al-maḥallī) belongs only to the indeclinable, and ʿishrūn is not indeclinable—that is evident; what is possible is only that it be quoted (maḥkī);"},
    {"type": "pair",
     "ar": "فالصواب المنصوب تقديرا لثقل آخر بالحركة الحكائية فقد غلط بوجوه:",
     "en": "so the correct [wording] is ‘accusative by supposition, because its end is weighed down by the vowel of quotation’”—has erred in several respects:"},
    {"type": "pair",
     "ar": "أما أولا: فلأن الإعراب المحلي يكون للمعرب أيضا، قالوا: يجوز الرفع في المعطوف على اسم «إن» بعد مضي الخبر حملا على المحل،",
     "en": "First, because positional inflection belongs to the declinable as well: they said that the nominative is permitted in what is coordinated with the noun of “inna” after the predicate has passed, by construction on the position;"},
    {"type": "pair",
     "ar": "ورفع «ظريف» في «لا غلام رجل ظريف في الدار» حملا على محل «لا غلام رجل».",
     "en": "and “ẓarīf” is in the nominative in “lā ghulāma rajulin ẓarīfun fī l-dāri” (there is no servant of a man, witty, in the house) by construction on the position of “lā ghulāma rajulin”."},
    {"type": "pair",
     "ar": "وأما ثانيا: فلأن «عشرون» مبني لكونه حكاية عن المبني، أعني: عشرون على التعداد.",
     "en": "Second, because “ʿishrūn” [here] is indeclinable, being a quotation of the indeclinable, namely “ʿishrūn” as used in counting."},
    {"type": "pair",
     "ar": "وأما ثالثا: فلأن ثقل آخره بالحركة الحكائية لا ينافي الإعراب بالحرف.",
     "en": "Third, because the weighing down of its end by the vowel of quotation does not conflict with inflection by a letter."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وللتصريح بقوله: أحد وعشرون إحدى وعشرون نكتة أخرى سوى ما ذكرها،",
     "en": "His explicit statement “aḥad wa-ʿishrūn, iḥdā wa-ʿishrūn” has another subtle point besides the one he mentioned:"},
    # REVIEW: «عطف القعود» is printed so; the context requires «العقود» (decades). Transcribed as printed.
    {"type": "pair",
     "ar": "وهو أنه أراد التنبيه على أن المراد بقوله: ثم بالعطف بلفظ ما تقدم عطف القعود على الزائد عليها،",
     "en": "namely, he wished to point out that what is meant by his words “then by coordination, with the wording of what preceded” is the coordination of the decades with what exceeds them;"},
    {"type": "pair",
     "ar": "فصرح بصورة العطف فقال: ثم بالعطف ليتبادر منه تلك الصورة.",
     "en": "so he stated the form of coordination explicitly, saying “then by coordination”, so that that form would come to mind from it."},
    {"type": "pair",
     "ar": "ولهذا لم يصرح في مائة وألف بصورة العطف، بل أجملها ليحمل",
     "en": "For this reason he did not state the form of coordination explicitly for “hundred” and “thousand”, but left it general, so that it would be taken…"},
]
