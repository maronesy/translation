# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 378 (printed ٣٧٧)."""

PAGE_NUMBER = 378
PRINTED_PAGE = "٣٧٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(ويقال: «ذا» للقريب، و«ذلك» للبعيد، و«ذاك» للمتوسط) وأخر المتوسط؛ لأن» at the foot of PDF p. 377.
    {"type": "matn",
     "ar": "التوسط لا يتحقق إلا بعد تحقق الطرفين،",
     "en": "… intermediacy is realized only after the two extremes are realized."},
    {"type": "matn",
     "ar": "ولما رأى المصنف[[١]] كثرة استعمال كل من هذه الكلمات الثلاث مقام الآخرين منها لم يتخذ هذا الفرق مذهبا وأحاله إلى غيره،",
     "en": "Since the author saw how frequently each of these three words is used in place of the other two, he did not adopt this distinction as his own position but attributed it to others,"},
    {"type": "matn",
     "ar": "فقال: ويقال: (و«تلك»[[٢]] و«ذانك» و«تانك») حال كون هاتين الأخيرتين (مشددتين. و«أولالك» باللام) باللام،",
     "en": "saying: “and it is said”: (and “tilka”, “dhānnika” and “tānnika”), these last two being (with a doubled [nūn], and “ulālika” with the lām), with the lām,"},
    {"type": "matn",
     "ar": "أي: هذه الكلمات الأربع (مثل) كلمة («ذلك») في إفادة البعد،",
     "en": "that is, these four words are (like) the word (“dhālika”) in conveying distance."},
    {"type": "matn",
     "ar": "ولا يبعد أن يجعل ذلك إشارة إلى كلمة «ذلك»[[٣]] المذكورة سابقا.",
     "en": "It is not far-fetched to take “dhālika” [in his words] as pointing to the word “dhālika” mentioned earlier."},
    {"type": "matn",
     "ar": "وأما «تاك» و«تانك» و«ذانك» مخففتين، و«أولاك» بغير اللام للمتوسط، وما هو للمتوسط بعد حذف حرف الخطاب منه للقريب.",
     "en": "As for “tāka”, and “tānika” and “dhānika” with a single [nūn], and “ulāka” without the lām, they are for the intermediate; and what is for the intermediate becomes, once the particle of address is dropped from it, for the near."},
    {"type": "matn",
     "ar": "(وأما «ثم» و«هنا») بضم الهاء وتخفيف النون[[٤]] (و«هنا») بفتح الهاء وتشديد النون وهو الأكثر، وجاء بكسر الهاء أيضا",
     "en": "(As for “thamma” and “hunā”), with a ḍamma on the hāʾ and a single nūn, (and “hannā”), with a fatḥa on the hāʾ and a doubled nūn, which is the more common form, though it also occurs with a kasra on the hāʾ,"},
    {"type": "matn",
     "ar": "(فللمكان) الحقيقي الحسي (خاصة[[٥]]) لا يستعمل في غيره إلا مجازا على سبيل التشبيه[[٦]].",
     "en": "(they are for place) in the real, sensible sense (specifically); they are not used for anything else except figuratively, by way of comparison (tashbīh)."},
    {"type": "matn",
     "ar": "وأما ما عداها من أسماء الإشارة، فقد يستعمل في المكان وغيره.",
     "en": "As for the other demonstratives, they may be used for place and for other things."},

    {"type": "section", "ar": "[اسم الموصول]",
     "en": "The Relative Noun (al-Ism al-Mawṣūl)"},

    {"type": "matn",
     "ar": "(الموصول) أي: الموصول المعدود من المبنيات في اصطلاح النحاة: (ما لا يتم جزءا)",
     "en": "(The relative noun) (al-mawṣūl), that is, the relative noun counted among the indeclinables in the grammarians’ terminology, (is that which is not complete as a part),"},
    {"type": "matn",
     "ar": "أي: اسم لا يتم[[٧]] من حيث جزئيته يعني: لا يكون جزءا تاما[[٨]] إن كان",
     "en": "that is, a noun that is not complete with respect to its being a part; he means: it is not a complete part if it is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كذا ذكره الشيخ الرضي. وفيه شيء لأن استعمال كل في مقام الآخر بالتأويل كما ذكر في علم البلاغة.",
     "en": "Thus Shaykh al-Raḍī stated it. There is something to be said against it, because the use of each in place of the other is by way of interpretation (taʾwīl), as is mentioned in the science of rhetoric (balāgha)."},
    {"type": "pair",
     "ar": "فلك أن تقول: إنه قال: يقال: إشارة إلى الاستعمال، فإنه لو قال: وذا للقريب لم يفهم منه إلا الوضع.",
     "en": "So you may say: he said “it is said” to point to usage, for had he said “and dhā is for the near”, only the original assignment (waḍʿ) would have been understood from it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لما كان المخالفة بين ذا وأخواته في البعد اكتفى به.",
     "en": "Since the difference between dhā and its sisters lies in distance, he was content with it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن ما عداه غير صالح لذلك؛ إذ ليس في ما ذكر زيادتان إلا في ذلك.",
     "en": "Because anything else is unsuitable for this, since among what has been mentioned there are two additions only in “dhālika”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "للقريب، وهناك للمتوسط، وهنالك للبعيد. وثمة أيضا للبعيد، وهنا بالتشديد أيضا للبعيد،",
     "en": "[Hunā is] for the near, hunāka for the intermediate, and hunālika for the distant. Thamma is also for the distant, and hannā with the doubled [nūn] is also for the distant."},
    {"type": "pair",
     "ar": "وقد يلحقه الكاف، ولا تلحق ثمة.",
     "en": "The kāf is sometimes attached to it, but it is not attached to thamma."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: أخص خصوصا ذكرت للتأكيد.",
     "en": "That is, “I single [it] out specifically”; it is mentioned for emphasis."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بالمكان سواء كان ذلك الغير زمانا نحو: ﴿هنالك الولاية لله الحق﴾ (الكهف: ٤٤) أو غيره.",
     "en": "[By comparison] with place, whether that other thing is a time, as in “There, protection belongs to Allah, the True” (Qurʾān, Sūrat al-Kahf 18:44), or something else."},
    # REVIEW: the lemma is printed «وأما عداها» (the matn has «وأما ما عداها»); transcribed as printed.
    {"type": "pair",
     "ar": "وقوله: وأما عداها إشارة إلى وجه صحة تخصيص الاختصاص بالمكان بهذه الألفاظ،",
     "en": "His words “as for the others” point to the reason why it is correct to restrict the specialization to place to these words,"},
    {"type": "pair",
     "ar": "وهو أن غيرها من أسماء الإشارة يستعمل حقيقة في المكان وغيره،",
     "en": "namely, that the other demonstratives are used literally for place and for other things."},
    {"type": "pair",
     "ar": "وبينها وبين ما عداها فرق آخر؛ إذا استعملت في المكان، وهو أن هذه الألفاظ لا يكون إلا ظروفا، والمستعمل في المكان مما عداها لا يلزم أن يكون ظروفا.",
     "en": "Between them and the others there is a further difference when they are used for place: these words are only ever adverbs of place (ẓurūf), whereas those of the others that are used for place need not be adverbs."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: اسم لا يتم حال كونه جزءا، وهو بعيد عن المعنى المراد.",
     "en": "That is, [one could read it as] “a noun that is not complete while being a part”, but this is far from the intended meaning."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    # REVIEW: printed «الاختمال» (with khāʾ), evidently for «الاحتمال»; and «الرضى» with undotted yāʾ here (fn. 1 prints «الرضي»). Transcribed as printed.
    {"type": "pair",
     "ar": "ذكره الشيخ الرضى هذا الاختمال، وقال ذلك لأن الأفعال الناقصة لا حصر لها.",
     "en": "Shaykh al-Raḍī mentioned this possibility, and said this because the incomplete verbs (al-afʿāl al-nāqiṣa) are without limit."},
]
