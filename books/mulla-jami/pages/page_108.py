# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 108 (printed ١٠٧)."""

PAGE_NUMBER = 108
PRINTED_PAGE = "١٠٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "السببين[[١]] (صيغة منتهى الجموع[[٢]]) وهي: «الصيغة التي كان أولها مفتوحا، وثالثها ألفا، وبعد الألف حرفان[[٣]] متحركان، أو ثلاثة أحرف أوسطها ساكن»،",
     "en": "…the two causes. (The pattern of the ultimate plurals, ṣīghat muntahā al-jumūʿ), and it is: “the pattern whose first [letter] is voweled with fatḥa, whose third is an alif, and after the alif are two voweled letters, or three letters whose middle is quiescent,”"},
    {"type": "matn",
     "ar": "وهي التي لا تجمع جمع التكسير مرة أخرى، ولهذا سميت صيغة منتهى الجموع؛ لأنها جمعت في بعض الصور مرتين[[٤]] تكسيرا، فانتهى تكسيرها المغير للصيغة.",
     "en": "and it is that which is not [again] made a broken plural a second time; and for this reason it is called “the pattern of the ultimate plurals,” because in some instances it has been made a broken plural twice, so that its pattern-altering broken pluralization comes to an end (muntahā)."},
    {"type": "matn",
     "ar": "فأما جمع السلامة: فإنه لا يغير الصيغة، فيجوز أن يجمع جمع السلامة، كما يجمع «أيامن» جمع «أيمن» على «أيامنين»، و«صواحب» جمع «صاحبة» على «صواحبات»،",
     "en": "As for the sound plural (jamʿ al-salāma), it does not alter the pattern, so [such a form] may take a sound plural — just as “ayāmin,” the plural of “aymun,” is pluralized as “ayāminīn,” and “ṣawāḥib,” the plural of “ṣāḥiba,” as “ṣawāḥibāt,”"},
    {"type": "matn",
     "ar": "وإنما اشترطت بذلك، لتكون صيغته مصونة عن قبول التغيير[[٥]]، فتؤثر.",
     "en": "and this condition was imposed only so that its pattern would remain guarded against admitting alteration (taghyīr), and thereby take effect [in preventing declension]."},
    {"type": "matn",
     "ar": "(بغير هاء[[٦]]) منقلبة عن تاء التأنيث[[٧]] حالة الوقف، أو المراد بها تاء التأنيث، باعتبار ما يؤول إليه حالة الوقف، فلا يرد نحو: «فواره» جمع «فارهة».",
     "en": "(Without a hāʾ) — [a hāʾ] which is converted from the tāʾ of femininity in the state of pause (waqf); or by it is meant the tāʾ of femininity, in view of what it turns into in the state of pause. Thus the like of “fawārih,” the plural of “fāriha,” does not constitute a counter-instance."},
    {"type": "matn",
     "ar": "وإنما اشترط كونها بغير هاء[[٨]]؛ لأنها لو كانت مع هاء كانت على زنة المفردات ك«فرازنة»، فإنها على زنة «كراهية وطواعية» بمعنى: الكراهة والطاعة.",
     "en": "It was made a condition that it (the pattern) be without a hāʾ only because, were it with a hāʾ, it would be on the measure of singulars — like “farāzina,” for it is on the measure of “karāhiya” and “ṭawāʿiya,” in the sense of “dislike” (al-karāha) and “obedience” (al-ṭāʿa)."},
    {"type": "matn",
     "ar": "فيدخل في قوة جمعيته فتور، ولا حاجة إلى إخراج نحو: «مدائني»[[٩]]، فإنه مفرد محض[[١٠]] ليس جمعا، لا في الحال ولا في المآل، وإنما الجمع «مدائن»، وهو لفظ آخر، بخلاف",
     "en": "so a weakening enters into the strength of its plurality. And there is no need to exclude the like of “madāʾinī,” for it is a pure singular, not a plural — neither actually nor eventually; rather the plural is “madāʾin,” which is a different word — unlike […]"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأظهر شرط تأثيره. وما ذكره بعيد عن الفهم.",
     "en": "The more evident [reading] is “the condition of its taking effect (taʾthīr).” What he mentioned is remote from [ready] understanding."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "منتهى مصدر ميمي، مضاف إلى الفاعل، أي: صيغة ينتهي بها جموع التكسير، بمعنى أن تلك الصيغة من حيث إنها غير قابلة للتكسير،",
     "en": "“Muntahā” is a mīmī verbal noun (maṣdar mīmī), annexed to its agent (fāʿil), that is: “a pattern at which the broken plurals terminate,” meaning that this pattern is such that it does not admit [further] broken pluralization."},
    {"type": "pair",
     "ar": "فلا يرد النقض بـ«رجال» بناء على أنه بخصوصه غير قابل للتكسير، فإن وزن فعال قابل للتكسير، ولذا يجمع حمار على حمير.",
     "en": "So the refutation by “rijāl” does not apply — on the basis that it in particular does not admit [further] broken pluralization — for the measure “fiʿāl” does admit broken pluralization, and this is why “ḥimār” is pluralized as “ḥumur.”"},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أولهما مكسور، أو ثلاثة أولها مكسور. فلا يرد النقض بصحارى وكمالات.",
     "en": "The first of the two is kasra-voweled, or, [when they are] three, the first of them is kasra-voweled. So the counter-instance of “ṣaḥārā” and “kamālāt” does not apply."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: لأنها صيغة جمع جمع، وهو تعليل للعلة المستفادة من قوله: لهذا.",
     "en": "That is: because it is a pattern of a plural of a plural; and this is an explanation of the cause implied by his words “for this reason (li-hādhā).”"},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فتصير لازمة، فيصح أن يرفع أصلا، وهو الصرف.",
     "en": "so it (the pattern) becomes fixed and inseparable (lāzima), whereby it becomes valid to remove [a thing] fundamentally — namely full declension (al-ṣarf)."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الباء للملابسة، والغير بمعنى النفي، والمعنى بلا هاء، بل لا بهاء، كما في قولك: كنت بغير مال، فإن المعنى: كنت بلا مال، بل لا بمال لا أنك كنت بما يغاير المال،",
     "en": "The bāʾ [in “bi-ghayr”] is for accompaniment (mulābasa), and “ghayr” has the sense of negation; the meaning is “without a hāʾ,” indeed “not [being] with a hāʾ” — as in your saying “I was without wealth (bi-ghayr māl),” for the meaning is “I was without wealth,” indeed “not with any wealth,” not that “you were [endowed] with something other than wealth.”"},
    {"type": "pair",
     "ar": "وهو خبر آخر لشرطه، أو صفة لقوله: صيغة.",
     "en": "And it (this phrase) is another predicate of “its condition (sharṭuhu),” or an adjective qualifying his word “pattern (ṣīgha).”"},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فعلى الأول: يكون قوله: بغير هاء مقيدا بحالة الوقف، وعلى الثاني: يكون مقيدا بخلافه.",
     "en": "On the first [interpretation], his words “without a hāʾ” are restricted to the state of pause; and on the second, they are restricted to its opposite."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وهنا نكتة جليلة يجب أن ينبه عليها، وهو أنه قال المصنف هنا: بغير هاء، وفي وزن الفعل غير قابل للتاء فرقا بين الجمع ووزن الفعل في ذلك؛",
     "en": "Here is a fine subtlety that must be pointed out: namely that the author said here “without a hāʾ,” whereas under [the cause of] the verbal measure [he said] “not admitting the tāʾ,” [thereby drawing] a distinction between the plural and the verbal measure in that respect;"},
    {"type": "pair",
     "ar": "لأن «يعمل» منصرف مع خلوه عن التاء لمجيء «يعملة»، و«جوارب» في جمع «جورب» بمعنى لفافة الرجل غير منصرف مع مجيء جواربة.",
     "en": "for “yaʿmul” is declinable despite its being free of the tāʾ, because of the occurrence of “yaʿmula”; whereas “jawārib,” the plural of “jawrab” (meaning a man’s foot-wrapping), is indeclinable despite the occurrence of “jawāriba.”"},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "بزيادة ياء النسبة، كما قيل مع أنه لو زيد لخرج نحو: كراسي مع أنه غير منصرف.",
     "en": "[It is a pure singular] by the addition of the yāʾ of relative attribution (yāʾ al-nisba), as has been said — even though, were it (that yāʾ) added [as a criterion of exclusion], the like of “karāsī” would be excluded, notwithstanding that it is indeclinable."},

    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "لا يصح إلا معاملة المفرد بخلاف فرازنة، فإنه جمع محض لا يصح إلا معاملة الجمع.",
     "en": "Only the treatment proper to a singular is valid for it — unlike “farāzina,” for that is a pure plural, for which only the treatment proper to a plural is valid."},
]
