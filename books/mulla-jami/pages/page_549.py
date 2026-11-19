# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 549 (printed ٥٤٨)."""

PAGE_NUMBER = 549
PRINTED_PAGE = "٥٤٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فلا يقال: «أقسمت» at the foot of PDF p. 548 (mid-sentence).
    {"type": "matn",
     "ar": "والله»، وذلك لكثرة استعمالها في القسم[[١]]، فهي أكثر استعمالا من أصلها، أعني: الباء.",
     "en": "…wa-llāhi” (I swore, by Allah); that is because of its frequent use in oaths, for it is more frequently used than its original, namely the bāʾ."},
    {"type": "matn",
     "ar": "(لغير السؤال) يعني: لا يستعمل الواو[[٢]] في السؤال، فلا يقال: «والله أخبرني؟» كما يقال: «بالله أخبرني؟» حطا للواو عن درجة الباء.",
     "en": "(For other than a request), meaning: the wāw is not used in a request; so one does not say “wa-llāhi, tell me!” as one says “bi-llāhi, tell me!”, which lowers the wāw beneath the rank of the bāʾ."},
    {"type": "matn",
     "ar": "(مختصة بالظاهر) يعني: الواو مختصة[[٣]] بالاسم الظاهر، سواء كان الاسم الظاهر اسم الله أو غيره،",
     "en": "(Restricted to the explicit [noun]), meaning: the wāw is restricted to the explicit noun, whether that explicit noun is the name of Allah or something else;"},
    {"type": "matn",
     "ar": "فلا يقال: «وك لأفعلن»، مثلا، بل يقال: «والله»، أو «رب الكعبة».",
     "en": "so one does not say, for instance, “wa-ka la-afʿalanna” (by You, I shall surely do it), but rather “wa-llāhi” or “[wa-]rabbi l-kaʿba” (by the Lord of the Kaʿba)."},
    {"type": "matn",
     "ar": "وذلك الاختصاص أيضا لحط رتبته عن رتبة الأصل -وهو الباء- بتخصيصه بأحد القسمين، وخص الظاهر لأصالته[[٤]].",
     "en": "That restriction too serves to lower its rank beneath the rank of the original, namely the bāʾ, by restricting it to one of the two kinds; and he assigned the explicit noun to it because of its being primary."},

    {"type": "section", "ar": "[تاء القسم]",
     "en": "The Tāʾ of Oaths"},

    {"type": "matn",
     "ar": "(والتاء مثلها) أي: مثل الواو في اشتراطها[[٥]] بحذف الفعل، وكونها لغير السؤال.",
     "en": "(And the tāʾ is like it), that is, like the wāw in being conditional on the elision of the verb, and in being for other than a request."},
    {"type": "matn",
     "ar": "(مختصة باسم الله[[٦]] تعالى) من الأسماء الظاهرة حطا لمرتبتها عن مرتبة أصلها الذي هو الواو، بتخصيصها ببعض المظهر،",
     "en": "(Restricted to the name of Allah, the Exalted,) among the explicit nouns, which lowers its rank beneath the rank of its original, the wāw, by restricting it to some explicit nouns;"},
    {"type": "matn",
     "ar": "وخص منه ما هو أصل في باب القسم، وهو اسم الله تعالى.",
     "en": "and of them he assigned to it what is primary in the chapter of oaths, namely the name of Allah, the Exalted."},

    {"type": "section", "ar": "[باء القسم]",
     "en": "The Bāʾ of Oaths"},

    {"type": "matn",
     "ar": "(والباء أعم منهما) أي: من الواو والتاء (في الجميع) أي: في جميع ما ذكر من",
     "en": "(And the bāʾ is more general than both), that is, than the wāw and the tāʾ, (in all), that is, in all that has been mentioned of…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإنها لكثرة الاستعمال تدل على الفعل المحذوف، وتقتضي التخفيف لطول الكلام بفعل القسم، والمقسم به، والمقسم عليه.",
     "en": "For, because of its frequent use, it indicates the elided verb, and it calls for lightening, since the sentence is long with the verb of swearing, that by which one swears, and that which one swears to."},
    {"type": "pair",
     "ar": "قال العصام: يعني: حذف فعل القسم لظهور الواو في القسم بخلاف الباء؛ لأن الواو أكثر استعمالا،",
     "en": "Al-ʿIṣām said: he means that the verb of swearing is elided because the wāw is evidently [used] in oaths, unlike the bāʾ, since the wāw is more frequently used."},
    {"type": "pair",
     "ar": "وفيه نظر؛ لأن الباء يستعمل في السؤال وغيره، ومع الظاهر والمضمر",
     "en": "This is open to objection, because the bāʾ is used in requests and otherwise, and with the explicit noun and the pronoun."},
    {"type": "pair",
     "ar": "فوجه الظهور أن للباء معاني كثيرة شائعة غير القسم بخلاف الواو.",
     "en": "The reason for [the wāw’s] evidentness is rather that the bāʾ has many common meanings other than the oath, unlike the wāw."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أشار بهذا التقرير إلى أنه حكم مستقل كما عرفت سابقا،",
     "en": "By this exposition he indicated that it is an independent rule, as you learned earlier;"},
    {"type": "pair",
     "ar": "يعني: لا يكون جوابه ما يدل على الطلب كالأمر، والنهي، والاستفهام.",
     "en": "meaning: its complement (jawāb) is not something that signifies a demand (ṭalab), such as a command, a prohibition or a question."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أشار إلى أن قوله: مختصة خبر لقوله: واو القسم،",
     "en": "He indicated that his word “restricted” is a predicate of his words “the wāw of oaths”."},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون حالا من ضمير «يكون» كما وهم لما مر من لزوم كونه محطا للحصر.",
     "en": "It may not be a circumstantial qualifier (ḥāl) of the pronoun in “yakūn”, as has been wrongly supposed, because of what preceded: that it would then necessarily be the focus of the restriction."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فإن الضمير فرع الظاهر، عبر عنه به للاختصار، والأصل أولى بالاستعمال.",
     "en": "For the pronoun is a derivative of the explicit noun, used to express it for brevity, and the original is more entitled to be used."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يقل في اختصاصها بالظاهر، وإن كان مثلها شاملا له، أيضا لانفهامه من قوله: مختصة باسم الله، ففي إدخاله في مثلها تكرار.",
     "en": "He did not say “and in its restriction to the explicit noun”, although [the word] “like it” covers that too, because it is understood from his words “restricted to the name of Allah”; so including it under “like it” would be repetition."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "من إضافة العام إلى الخاص، ولو قال: مختصة بلفظ الله لكان أوضح.",
     "en": "[This is] an annexation of the general to the particular; had he said “restricted to the word Allāh” it would have been clearer."},
]
