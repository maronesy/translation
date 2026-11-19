# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 174 (printed ١٧٣)."""

PAGE_NUMBER = 174
PRINTED_PAGE = "١٧٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "قائما») أو «قائمين» و«أن ضربت زيدا قائما» و«أكثر شربي السويق ملتوتا» و«أخطب ما يكون الأمير قائما»[[١]].",
     "en": "…standing”—ḍarbī Zaydan qāʾiman) or “[the two of us] standing” (qāʾimayn), and “that you struck Zayd standing” (an ḍarabta Zaydan qāʾiman), and “most of my drinking of sawīq is moistened” (aktharu shurbiya al-sawīqa maltūtan), and “the most eloquent the emir is, is standing” (akhṭabu mā yakūnu al-amīru qāʾiman)."},
    {"type": "matn",
     "ar": "فذهب البصريون إلى أن تقديره: «ضربي زيدا حاصل إذا كان قائما»[[٢]]،",
     "en": "The Baṣrans held that its implied form is: “My beating Zayd takes place when he is standing”;"},
    {"type": "matn",
     "ar": "فحذف «حاصل» كما يحذف متعلقات الظروف[[٣]] نحو: «زيد عندك»، فبقي «إذا كان قائما»،",
     "en": "then “takes place” was elided, just as what adverbials attach to are elided, as in “Zayd is with you” (Zaydun ʿindaka), and there remained “when he is standing”;"},
    {"type": "matn",
     "ar": "ثم حذف «إذا» مع شرطه[[٤]] العامل في الحال[[٥]]، وأقيم الحال مقام الظرف[[٦]]؛",
     "en": "then “idhā” was elided together with its condition, which governs the ḥāl, and the ḥāl was put in the place of the adverbial;"},
    {"type": "matn",
     "ar": "لأن في الحال معنى الظرفية، فالحال قائم مقام الظرف القائم مقام الخبر، فيكون الحال قائما مقام الخبر.",
     "en": "because the ḥāl carries the sense of adverbiality (ẓarfiyya); so the ḥāl stands in place of the adverbial that stands in place of the predicate, and thus the ḥāl stands in place of the predicate."},
    {"type": "matn",
     "ar": "وقال الرضي: هذا ما قيل فيه، وفيه تكلفات كثيرة[[٧]]، والذي يظهر لي أن تقديره بنحو: «ضربي زيدا يلابسه قائما»",
     "en": "Al-Raḍī said: this is what has been said about it, and it involves many strained constructions; what appears to me is that its implied form is something like: “My beating Zayd accompanies him standing”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: يجوز في هذا القسم رفع الحال على الخبرية بأن تقول: أخطب ما يكون الأمير قائم؛",
     "en": "Shaykh al-Raḍī said: in this category it is permissible to put the ḥāl in the nominative as the predicate, by saying: “akhṭabu mā yakūnu al-amīru qāʾimun”;"},
    {"type": "pair",
     "ar": "لأن أول الكلام كان مجازا، والمجاز يونس المجاز، فجعل آخره مجازا.",
     "en": "because the beginning of the utterance was figurative (majāz), and the figurative keeps company with the figurative, so he made its end figurative."},
    {"type": "pair",
     "ar": "فإن قلت: فلا يكون التركيب من مواقع وجوب حذف الخبر فلا يتم القاعدة؟",
     "en": "If you say: then the construction would not be among the instances of obligatory elision of the predicate, and so the rule would not hold?"},
    {"type": "pair",
     "ar": "قلت: إذا رفع «قائم» لم يكن التركيب من القاعدة لانتفاء الحال.",
     "en": "I say: when “qāʾim” is put in the nominative, the construction does not fall under the rule, since there is no ḥāl."},
    {"type": "pair",
     "ar": "ولا يخفى أن ما ذكره من جواز رفع الحال في هذا القسم مقيد بما إذا كان أوله مجازا كما أفاده تعليله أن يكون الحكم مبنيا على اطراد الباب،",
     "en": "It is not hidden that what he mentioned about the permissibility of putting the ḥāl in the nominative in this category is restricted to cases where its beginning is figurative, as his reasoning conveys: that the ruling is based on consistency within the category."},
    {"type": "pair",
     "ar": "وجوز الشيخ الرضي وغيره جعل المصدر في أخطب ما يكون الأمير حينيا أي: أوقات كونه،",
     "en": "Shaykh al-Raḍī and others permitted taking the maṣdar in “akhṭabu mā yakūnu al-amīru” as temporal (ḥīnī), that is: “the times of his being”;"},
    {"type": "pair",
     "ar": "فالمراد بالفعل المضاف إلى المصدر أعم من المضاف إليه بلا واسطة أو بواسطة.",
     "en": "so what is meant by the verb annexed to the maṣdar is more general than what is annexed to it without an intermediary or with one."},  # REVIEW: «فالمراد بالفعل المضاف إلى المصدر» — «بالفعل» confirmed at 700 dpi; whether it means 'the verb' or 'actually' (referring to the elative annexed to the maṣdar) is uncertain

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "تقديره: إذا كان ليحصل للحال عامل سوى المصدر؛ إذ المصدر لا يجوز أن يكون عاملا فيه كما ستعرفه.",
     "en": "[The reason for] supposing “idhā kāna” is so that the ḥāl may have a governor other than the maṣdar; for the maṣdar cannot govern it, as you will come to know."},
    {"type": "pair",
     "ar": "ولا يجوز أن يكون العامل حاصلا؛ لأن ذا الحال هو غير المصدر، وفاعل حاصل هو المصدر،",
     "en": "Nor can the governor be “ḥāṣil,” because the possessor of the ḥāl (dhū al-ḥāl) is other than the maṣdar, while the agent of “ḥāṣil” is the maṣdar;"},
    {"type": "pair",
     "ar": "فلو جعل حاصلا عاملا اختلف عامل الحال وصاحبه وهو لا يجوز عندهم،",
     "en": "so if “ḥāṣil” were made the governor, the governor of the ḥāl and [that of] its possessor would differ, which is not permitted according to them."},
    {"type": "pair",
     "ar": "وبهذا عرف أن من جوز الاختلاف له أن يخالف في تقدير: إذا كان، ويكتفي بتقدير: حاصل.",
     "en": "From this it is known that whoever permits the difference may dissent from supposing “idhā kāna” and be content with supposing “ḥāṣil.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى متعلق الظرف.",
     "en": "Better: “what the adverbial attaches to” [in the singular]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سمي مدخولها شرطا، وإن كانت \"إذا\" ظرفية لرائحة معنى الشرط،",
     "en": "What it governs is called a condition, even though “idhā” is adverbial, because of a trace of the sense of condition [in it];"},
    {"type": "pair",
     "ar": "و\"إذا\" هذه للاستمرار كما في قوله تعالى: ﴿وإذا قيل لهم لا تفسدوا﴾ (سورة البقرة:١١).",
     "en": "and this “idhā” is for continuity, as in His words, the Exalted: “And when it is said to them: Do not cause corruption” (Qurʾān, Sūrat al-Baqara 2:11)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إذ هذه ظرفية خالية عن معنى الشرط كما يخفى.",
     "en": "For this is adverbial, devoid of the sense of condition, as is hidden [sic]."},  # REVIEW: printed «كما يخفى» (checked at 700 dpi); the usual formula is «كما لا يخفى»; transcribed as printed

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: القائم مقام الخبر، فالمقام بضم الميم.",
     "en": "That is: the [adverbial] standing in place of the predicate; so “muqām” is with a ḍamma on the mīm."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال في الحاشية: وهي من حذف \"إذا\" مع الجملة المضاف إليها، ولم يثبت في غير هذا المكان،",
     "en": "He said in the Ḥāshiya: they arise from eliding “idhā” together with the clause annexed to it, which is not attested anywhere other than this place;"},
    {"type": "pair",
     "ar": "ومن العدول عن ظاهر معنى كان الناقصة إلى معنى التامة؛ لأن معنى قولهم: حاصل إذا كان قائما ظاهر في معنى الناقصة،",
     "en": "and from departing from the apparent sense of the incomplete (nāqiṣa) kāna to the sense of the complete (tāmma) one, for the meaning of their words “takes place when he is standing” is evidently in the sense of the incomplete one;"},
    {"type": "pair",
     "ar": "ومن قيام الحال مقام الظرف، انتهى.",
     "en": "and from the ḥāl standing in place of the adverbial. End of quotation."},
    {"type": "pair",
     "ar": "إنما عدلوا عنه لأن مثل هذا المنصوب لم يسمع مع كثرته إلا نكرة، ولو كان خبرا لسمع تعريفه مرة،",
     "en": "They departed from it only because an accusative such as this, despite its frequency, has been heard only as indefinite; had it been a predicate, it would have been heard as definite at least once;"},
    {"type": "pair",
     "ar": "ولأن الواو في الجملة الاسمية الواقعة موقع هذا المنصوب لازمة، ولو كانت خبرا لها لم يلزم الواو؛",
     "en": "and because the wāw is required in a nominal clause occurring in the position of this accusative, whereas had it been its predicate the wāw would not be required;"},
    {"type": "pair",
     "ar": "لأن دخول الواو في أخبار الأفعال الناقصة ليست إلا لتشبيهها بالحال. وذلك لا يقتضي اللزوم.",
     "en": "for the entry of the wāw into the predicates of the incomplete verbs is only because they are likened to the ḥāl, and that does not entail its being required."},
]
