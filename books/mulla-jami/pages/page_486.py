# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 486 (printed ٤٨٥)."""

PAGE_NUMBER = 486
PRINTED_PAGE = "٤٨٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # The page opens with a new sentence; PDF p. 485 ends at a full stop.
    # REVIEW: a stray full stop is printed after «واحدا كان» in mid-sentence («واحدا كان. أو مثنى»); transcribed as printed.
    {"type": "matn",
     "ar": "(والتاء للمخاطب) مطلقا واحدا كان. أو مثنى أو مجموعا، مذكرا كان أو مؤنثا[[١]].",
     "en": "(And the tāʾ is for the one addressed), absolutely, whether single, dual or plural, masculine or feminine."},
    # REVIEW: printed «والمنؤنثين» (with an extra nūn) for «والمؤنثين»; transcribed as printed, translated as «المؤنثين».
    {"type": "matn",
     "ar": "(وللمؤنث) الواحدة (وللمؤنثين غيبة) أي: حال كون المؤنث[[٢]] والمنؤنثين غائبات أو ذوي غيبة.",
     "en": "(And for the feminine) singular (and for the two feminines, in absence), that is, while the feminine and the two feminines are absent, or possessed of absence."},
    {"type": "matn",
     "ar": "(والياء للغائب غيرهما) أي: غير القسمين المذكورين، وهما واحد المؤنث الغائبة، ومثناه.",
     "en": "(And the yāʾ is for the absent other than these two), that is, other than the two aforementioned categories, namely the singular of the absent feminine and its dual."},
    {"type": "matn",
     "ar": "فقوله: «غيرهما» بالجر على البدلية من الغائب؛ لأنه وإن لم يصر بالإضافة معرفة، لكنه خرجت بها عن النكارة الصرفة، فهو في قوة النكرة الموصوفة،",
     "en": "So his word “ghayrihimā” is in the genitive as a substitute (badal) for “the absent”; for although it does not become definite through the annexation, it has thereby left pure indefiniteness, so it has the force of a qualified indefinite noun;"},
    {"type": "matn",
     "ar": "أو بالنصب حال، وهو الأولى لموافقة السابق.",
     "en": "or it is in the accusative as a circumstantial (ḥāl), and this is preferable for its agreement with what precedes."},
    {"type": "matn",
     "ar": "(وحروف المضارعة مضمومة[[٣]] في الرباعي) أي: فيما ماضيه على أربعة أحرف أصلية كـ«يدحرج» أو لا كـ«يخرج».",
     "en": "(The letters of the muḍāriʿ are vowelled with ḍamma in the quadriliteral), that is, in what has a past form of four letters, radical as in “yudaḥriju”, or not, as in “yukhriju”."},
    {"type": "matn",
     "ar": "(ومفتوحة[[٤]] فيما سواه) أي: فيما سوى ما ماضيه على أربعة أحرف، مثل: «يتدحرج» و«يستخرج» ونحوهما.",
     "en": "(And with fatḥa in what is other than it), that is, in what is other than that whose past form has four letters, such as “yatadaḥraju” and “yastakhriju” and the like."},
    {"type": "matn",
     "ar": "(ولا يعرب من الفعل غيره) أي: غير المضارع، لعدم علة الإعراب فيه[[٥]].",
     "en": "(And no verb other than it is inflected), that is, other than the muḍāriʿ, owing to the absence of the cause of inflection (iʿrāb) in it."},
    {"type": "matn",
     "ar": "ولما كان هذا الكلام في قوة قولنا: «وإنما يعرب المضارع» صح أن يتعلق به قوله:",
     "en": "Since this statement has the force of our saying “only the muḍāriʿ is inflected”, it is valid for his words to be connected with it:"},
    {"type": "matn",
     "ar": "(إذا لم يتصل به نون تأكيد) ثقيلة كانت أو خفيفة (ولا نون جمع المؤنث)؛ لأنه إذا اتصل به إحداهما يكون مبنيا[[٦]]؛ لأن نون التأكيد لشدة الاتصال بمنزلة جزء الكلمة،",
     "en": "(when no nūn of emphasis is joined to it), whether heavy or light, (nor the nūn of the feminine plural); for when one of them is joined to it, it is indeclinable, because the nūn of emphasis, owing to the closeness of the connection, is like a part of the word,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فالمراد بالمفرد: ما اتصف بالإفراد، وليس من باب التغليب؛ إذ لم يرد به كلاهما.",
     "en": "So what is meant by the singular is what is characterized by singularity; it is not a case of predominance (taghlīb), since both are not meant by it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يمكن جعل غيبته مصدرا حينيا إلا أن جعلها حالا أنسب بنظائرها.",
     "en": "It is possible to take “ghaybatan” as a temporal verbal noun (maṣdar ḥīnī), but taking it as a circumstantial is more fitting to its parallels."},
    {"type": "pair",
     "ar": "ولو قال المصنف: والغائبة والغائبتين لكان أظهر وأخصر.",
     "en": "Had the author said “and the absent feminine and the two absent feminines”, it would have been clearer and more concise."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأنه لما فتح أول الماضي ينبغي أن يخالفه أول المضارع لمكان التباين بينهما.",
     "en": "Because, since the beginning of the past is vowelled with fatḥa, the beginning of the muḍāriʿ ought to differ from it, on account of the distinctness between the two."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فيما سواه للتخفيف الذي استدعاه كثرة الاستعمال كما في الثلاثي أو كثرة الحروف كما فيما عداه.",
     "en": "In what is other than it, for the lightening called for by frequency of use, as in the triliteral, or by the number of letters, as in what is beyond it."},
    {"type": "pair",
     "ar": "وأما إهراق يهريق واسطاع يسطيع، فرباعي زيد فيه الهاء والسين على غير القياس.",
     "en": "As for “ahrāqa, yuhrīqu” and “isṭāʿa, yusṭīʿu”, each is a quadriliteral to which the hāʾ and the sīn were added irregularly."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو توارد المعاني المختلفة كما في الاسم أو المشابهة التامة به،",
     "en": "That [cause] is the succession of different meanings [upon it], as in the noun, or complete resemblance to it."},
    {"type": "pair",
     "ar": "ولم يذكر دليل الحكم الثبوتي المستفاد من الحصر؛ لأنه سيبينه في قوله: ويرتفع إلى آخره مفصلا.",
     "en": "He did not mention the proof of the affirmative ruling conveyed by the restriction (ḥaṣr), because he will explain it in detail in his words “and it is put in the nominative…” to the end."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وقيل: إنه معرب تقديرا لثقل محل الإعراب بالحركة كما في «غلامي».",
     "en": "It has been said: it is inflected by supposition (taqdīran), owing to the heaviness of the seat of inflection with the vowel, as in “ghulāmī” (my servant)."},
    {"type": "pair",
     "ar": "ولا يخفى عليك الفرق بينهما وبين غلامي، فإنهما لشدة الاتصال صارتا كالجزء منه، فلم يبق ما قبلهما محل الإعراب أصلا بخلاف «غلامي».",
     "en": "The difference between these two and “ghulāmī” is not hidden from you: owing to the closeness of the connection they have become like a part of it, so what precedes them does not remain the seat of inflection at all, unlike “ghulāmī”."},
]
