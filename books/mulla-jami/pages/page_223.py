# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 223 (printed ٢٢٢)."""

PAGE_NUMBER = 223
PRINTED_PAGE = "٢٢٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "إلى حرف مد مجانس حركة آخر المندوب[[١]] من كسرة أو ضمة،",
     "en": "…to a long-vowel letter matching the vowel of the end of the mandūb, whether kasra or ḍamma;"},
    {"type": "matn",
     "ar": "كما إذا أردت ندبة غلام مخاطبة (قلت: وا غلامكيه) لا «وا غلامكاه»؛ لالتباسه بندبة غلام مخاطب.",
     "en": "as when you wish to lament the servant of a woman addressed: (you say “wā ghulāmakīh”), not “wā ghulāmakāh,” since that would be confused with lamenting the servant of a man addressed."},
    {"type": "matn",
     "ar": "(و) إذا أردت ندبة غلام جماعة مخاطبين قلت: (وا غلامكموه)؛ إذ الميم أصلها الضم[[٢]]،",
     "en": "(And) when you wish to lament the servant of a group addressed, you say: (“wā ghulāmakumūh”), since the mīm originally takes the ḍamma;"},
    {"type": "matn",
     "ar": "لا «غلامكماه» لالتباسه بندبة غلام مخاطبين اثنين.",
     "en": "not “ghulāmakumāh,” since that would be confused with lamenting the servant of two persons addressed."},
    {"type": "matn",
     "ar": "(و) جاز (لك الهاء) أي: إلحاقها بهذا المدات (في) حال (الوقف) لبيانها.",
     "en": "(And) it is permitted (to you [to add] the hāʾ), that is, to attach it to these long vowels (in) the state of (pause), to make them clear."},
    {"type": "matn",
     "ar": "(ولا يندب) من قسم المندوب المتفجع عليه عدما[[٣]] (إلا) الاسم (المعروف[[٤]]) الذي اشتهر المندوب به؛",
     "en": "(And only) the (known) noun—by which the lamented one is well known—(is lamented), of the kind of mandūb that is lamented in its non-existence,"},
    {"type": "matn",
     "ar": "ليعذر النادب بمعرفته في ندبته والتفجع عليه",
     "en": "so that the mourner may be excused, through its being known, in his lamentation and his grieving over him."},
    {"type": "matn",
     "ar": "(فلا يقال: «وا رجلاه»)؛ إذ ما اشتهر بهذا اللفظ مندوب خاص انتقل الذهن إليه ويعرف به؛ ليعذر النادب بالندبة عليه.",
     "en": "(So one does not say “wā rajulāh”), since no particular lamented one is well known by this word such that the mind would move to him and he would be known by it, so that the mourner would be excused for lamenting him."},
    {"type": "matn",
     "ar": "(وامتنع) إلحاق الألف بصفة المندوب، بل يجب أن يلحق بالموصوف مثل: «وا زيداه الطويل»؛",
     "en": "(And) attaching the alif to the qualifier of the mandūb (is disallowed); rather it must be attached to the qualified noun, as in “wā Zaydāh al-ṭawīl” (O Zayd, the tall);"},
    {"type": "matn",
     "ar": "لأن اتصاله بالصفة ليس كاتصال المضاف بالمضاف إليه؛ لأنه جيء به لتمام المضاف[[٥]] فهو كالجزء",
     "en": "because its connection with the qualifier is not like the connection of the annexed noun with the noun annexed to it; for the latter is brought to complete the annexed noun, so it is like a part of it;"},
    {"type": "matn",
     "ar": "بخلاف الصفة، فإنه جيء بها بعد تمام الموصوف للتخصيص أو التوضيح،",
     "en": "unlike the qualifier, which is brought after the qualified noun is complete, for specification or clarification."},
    {"type": "matn",
     "ar": "فلهذا جاز مثل: «يا أمير المؤمنيناه» ولم يجز (مثل: وا زيد الطويلاه خلافا ليونس)،",
     "en": "For this reason the like of “yā amīra al-muʾminīnāh” (O Commander of the Faithful) is permitted, while (the like of “wā Zaydu al-ṭawīlāh” is) not permitted, (in disagreement with Yūnus);"},
    {"type": "matn",
     "ar": "فإنه يجوز إلحاق الألف بآخر الصفة،",
     "en": "for he permits attaching the alif to the end of the qualifier,"},
    {"type": "matn",
     "ar": "فإن اتصال الموصوف بالصفة، وإن كان في اللفظ أنقص من الاتصال بين المضاف والمضاف إليه، إلا أنه أتم منه من جهة المعنى،",
     "en": "since the connection of the qualified noun with the qualifier, though in wording less complete than the connection between the annexed noun and the noun annexed to it, is more complete than it in meaning,"},
    {"type": "matn",
     "ar": "لاتحادهما بالذات، فإن الطويل هو زيد لا غير، بخلاف المضاف",
     "en": "because the two are one in essence: “the tall” is Zayd and no other; unlike the annexed noun…"},

    {"type": "rule"},

    # ---------------- Footnote 7 of p.222, continued ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "مدة من جنسها، ولا يغير حركة البناء للزومها.",
     "en": "…a long vowel of its own kind, and does not change the indeclinable vowel, since that vowel is fixed."},
    {"type": "pair",
     "ar": "قال سيبويه: تقول في ندبة يا غلام بإسقاط ياء الإضافة يا غلاما.",
     "en": "Sībawayh said: in lamenting “yā ghulām,” with the possessive yāʾ dropped, you say “yā ghulāmā.”"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: الأولى أن يقال: يا غلامي لحصول اللبس بندبة يا غلام بالضم.",
     "en": "Shaykh al-Raḍī said: it is better to say “yā ghulāmī,” since there is confusion with the lamentation of “yā ghulāmu” with the ḍamma."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قال بعض المحققين: والأظهر أن الواو والياء منقلبتان من الألف لحفظ حركة آخر المندوب.",
     "en": "One of the verifying scholars said: the more evident view is that the wāw and the yāʾ are changed from the alif, to preserve the vowel of the end of the mandūb."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "دفع دخل مقدر، وهو أن الواو كيف يكون مجانسا لحركة الآخر، فإن الآخر في غلامكم ساكن،",
     "en": "[This] answers an implied objection: how can the wāw match the vowel of the final letter, when the final letter in “ghulāmakum” is unvowelled?"},
    {"type": "pair",
     "ar": "فدفع بأن الميم في الأصل مضمومة حتى أن بعض القراء ضموا الميم في أنتم وكم.",
     "en": "He answered that the mīm originally takes a ḍamma, so much so that some of the Qurʾān readers gave the mīm a ḍamma in “antum” and “kum.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا التقييد غير مفهوم من عبارة المصنف، والعلة التي ذكرت في اشتراط المفرد فيه في المتفجع عليه يجري في المتفجع عليه وجودا أيضا.",
     "en": "This restriction is not understood from the author’s wording; and the reason given for requiring a single noun in what is lamented over applies also to what is lamented over in its existence."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سواء كان علما أو غير علم نحو: وا من قلع باب خيبراه.",
     "en": "Whether it is a proper name or not, as in “wā man qalaʿa bāba Khaybarāh” (O he who tore off the gate of Khaybar)."},
    {"type": "pair",
     "ar": "وما حكاه الكوفيون من قولهم: وا رجلا مسبحاه فشاذ.",
     "en": "What the Kūfans relate of their saying “wā rajulan musabbiḥāh” is anomalous (shādhdh)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن الاسم إنما يتم بالتنوين، أو اللام، أو بنون التثنية أو الجمع، أو الإضافة بخلاف الصفة،",
     "en": "Because a noun is completed only by the tanwīn, or the definite article, or the nūn of the dual or plural, or annexation; unlike the qualifier,"},
    {"type": "pair",
     "ar": "فإنه جيء بعد تمام الموصوف، فلهذا جاز الفصل بين الصفة والموصوف في سعة الكلام دون المضاف والمضاف إليه.",
     "en": "which comes after the qualified noun is complete. For this reason separating the qualifier from the qualified noun is permitted in ordinary speech, but not separating the annexed noun from the noun annexed to it."},
]
