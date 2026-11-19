# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 405 (printed ٤٠٤)."""

PAGE_NUMBER = 405
PRINTED_PAGE = "٤٠٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «نحو: «أي وقت مجيئك؟» أي: أي وقت كائن» at the foot of PDF p. 404.
    {"type": "matn",
     "ar": "مجيئك؟ فـ«أي وقت» على تقدير انتصابه بالظرفية مرفوع المحل بالخبرية،",
     "en": "…your coming?” So “ayya waqtin”, on supposing it accusative as an adverb, is nominative in position as a predicate."},
    {"type": "matn",
     "ar": "والوجوه الباقية مثل: «أيهم ضربت؟ وبأيهم مررت؟ وأيهم قائم؟».",
     "en": "The remaining possibilities are as in “ayyahum ḍarabta?” (which of them did you strike?), “bi-ayyihim mararta?” (by which of them did you pass?) and “ayyuhum qāʾim?” (which of them is standing?)."},
    # The first hemistich of the verse, printed centred, followed by a row of dots in place of the second hemistich.
    {"type": "verse",
     "ar": "(وفي مثل: «كم عمة لك يا جرير وخالة»)          ..........................",
     "en": "(And in such a case as “How many a paternal aunt you have, O Jarīr, and maternal aunt…”)"},
    {"type": "matn",
     "ar": "يعني: فيما احتمل الاستفهام والخبر وذكر المميز وحذفه (ثلاثة أوجه)",
     "en": "That is, in what admits interrogation and statement, and the mention and the omission of the specifier, (there are three possibilities)."},
    {"type": "matn",
     "ar": "هكذا في كثير من النسخ، وفي بعضها: «وفي مثل تمييز كم عمة» أي: ما هو تمييز باعتبار بعض الوجوه[[١]].",
     "en": "So it reads in many of the manuscripts; in some of them: “and in such a case as the specification of kam ʿammatin”, that is, what is a specification with regard to some of the possibilities."},
    {"type": "matn",
     "ar": "فعلى النسخة الأولى: يحتمل أن يعتبر الأوجه الثلاثة في «كم»:",
     "en": "On the first reading, the three possibilities may be taken to concern “kam”:"},
    {"type": "matn",
     "ar": "أحدها: رفعه بالابتداء.",
     "en": "the first, its being nominative as mubtadaʾ;"},
    {"type": "matn",
     "ar": "والآخران: نصبه على الظرفية، أو على المصدرية، فإنه أشار فيما سبق بقوله: «منصوبا معمولا على حسبه» إلى كثرة وجوه النصب،",
     "en": "the other two, its being accusative as an adverb or as a maṣdar; for he alluded earlier, by his words “accusative, governed according to it”, to the multiplicity of the ways of the accusative."},
    {"type": "matn",
     "ar": "ولا يخفى أن هذا ألصق بما سبق من وجوه إعراب «كم»،",
     "en": "It is clear that this is closer to what preceded on the ways of inflecting “kam”."},
    {"type": "matn",
     "ar": "ويحتمل أن يعتبر في مميزها -أعني: «عمة»- فأحدها: الرفع بالابتداء استفهامية كانت أو خبرية، والآخران: النصب على تقدير كونها استفهامية، والجر على تقدير كونها خبرية.",
     "en": "They may also be taken to concern its specifier, namely “ʿamma”: the first is the nominative as mubtadaʾ, whether [kam] is interrogative or predicative; the other two are the accusative, on supposing it interrogative, and the genitive, on supposing it predicative."},
    {"type": "matn",
     "ar": "ولا يخفى أن هذا الوجه مبني على اعتبار جواز حذف مميزها، وهو غير مذكور فيما سبق،",
     "en": "It is clear that this interpretation rests on taking into account that its specifier may be omitted, which has not been mentioned earlier;"},
    {"type": "matn",
     "ar": "فكان الأليق تأخير هذا[[٢]] عن قوله: «وقد يحذف في مثل: كم مالك؟»[[٣]].",
     "en": "so it would have been more fitting to place this after his words “and it may be omitted in such a case as kam māluka?” (how much is your wealth?)."},
    {"type": "matn",
     "ar": "وأما النسخة الأخرى: فلا تحتمل إلا الوجه الأخير، والبيت للفرزدق يهجو جريرا",
     "en": "As for the other reading, it admits only the last interpretation. The verse is by al-Farazdaq, satirizing Jarīr…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "والأظهر أن المراد ما هو تمييز بحسب الظاهر.",
     "en": "The more evident view is that what is meant is what is a specification in outward form."},
    {"type": "pair",
     "ar": "فإن قلت: فليكن الأوجه الثلاثة في تمييز هذا التركيب ذكر التمييز نصبا وجرا وحذفه، فلا حاجة إلى حمل التمييز على التمييز في بعض الأوجه؟",
     "en": "If you say: let the three possibilities in the specification of this construction be the mention of the specifier in the accusative, in the genitive, and its omission; then there is no need to take “specification” as specification in some of the possibilities?"},
    {"type": "pair",
     "ar": "قلت: يلزم أن يكون الوجوه أربعة ذكره نصبا وجرا وحذفه كذلك، فلا يحسن جعلها ثلاثة.",
     "en": "I say: it would follow that the possibilities are four—its mention in the accusative and in the genitive, and its omission likewise [in both]—so it would not be right to make them three."},
    # Printed in smaller type at the end of the footnote (an added gloss).
    {"type": "pair",
     "ar": "قال عبد الحكيم: وهو النصب والجر. وأما باعتبار الرفع فهو مرفوع على الابتداء.",
     "en": "ʿAbd al-Ḥakīm said: that is, the accusative and the genitive; as for the nominative, it is nominative as mubtadaʾ."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ليكون الأصل مقدما على الفرع.",
     "en": "So that the principal comes before the derivative."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكم ضربت؟ تأخر الفرع عن الأصل،",
     "en": "And “kam ḍarabta?” (how many [times] did you strike?): the derivative comes after the principal."},
    {"type": "pair",
     "ar": "فعلى هذا التوجيه مع التمحل في التمييز بحمله على التمييز في بعض الوجوه فوات حسن الترتيب،",
     "en": "On this explanation, together with the strained reading of “specification” by taking it as specification in some of the possibilities, the good order is lost."},
    {"type": "pair",
     "ar": "فالأولى أن يقال: المراد بالأوجه الثلاثة نصب عمة وجرها مع الإفراد وجرها مع الجمعية.",
     "en": "So it is better to say: what is meant by the three possibilities is the accusative of “ʿamma”, its genitive in the singular, and its genitive in the plural."},
    # REVIEW: «تنظير الحذف هذا المميز» printed; «لحذف» may be intended. Transcribed as printed.
    {"type": "pair",
     "ar": "والمراد بقوله: وقد يحذف أنه قد يحذف مثل مميز «كم» عمة لك يا جرير وخالة، فإنه الذي سبق آنفا، فيكون إشارة إلى ثلاثة أوجه أخر باعتبار المميز المحذوف،",
     "en": "What is meant by his words “and it may be omitted” is that a specifier like that of “kam” in “kam ʿammatin laka yā Jarīru wa-khālatin” may be omitted, for it is what has just preceded; so it alludes to three further possibilities with regard to the omitted specifier."},
    {"type": "pair",
     "ar": "ويكون نحو: «كم مالك؟ وكم ضربت؟» تنظير الحذف هذا المميز وتبيينا لاحتمال المحذوف والمصدر كما في «كم ضربت؟» أو المقدر كما في «كم مالك؟» فتأمل.",
     "en": "Such cases as “kam māluka?” and “kam ḍarabta?” are then a parallel for the omission of this specifier, and an indication that what is omitted may be the maṣdar, as in “kam ḍarabta?”, or something supplied, as in “kam māluka?”. So reflect."},
]
