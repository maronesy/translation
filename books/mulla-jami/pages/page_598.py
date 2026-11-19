# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 598 (printed ٥٩٧)."""

PAGE_NUMBER = 598
PRINTED_PAGE = "٥٩٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ومع غيرهما على ضربين:» at the foot of PDF p. 597.
    # REVIEW: in the first paragraphs of this page the imperatives of غزا are printed with
    # hamzat al-qaṭʿ («أغزوا»، «أغزي»، «أغز»، «أغزن»، «أغزوا الكفار»، «أغزي الجيش»، «أغزون»),
    # whereas further down the same forms are printed «اغزوا»، «اغزي»، «اغزون». Transcribed as printed.
    {"type": "matn",
     "ar": "١-إما مع ضمير بارز، وهو شيئان: جمع المذكر، نحو: «أغزوا، وارموا، واخشوا» والواحدة المؤنثة نحو: «أغزي وارمي واخشي».",
     "en": "1. Either with an overt pronoun, which is of two kinds: the masculine plural, as in “ughzū, irmū, ikhshaw” (raid, throw, fear), and the feminine singular, as in “ughzī, irmī, ikhshay”;"},
    {"type": "matn",
     "ar": "٢-وإما مع ضمير مستتر، وهو الواحد المذكر نحو: «أغز، وارم، واخش».",
     "en": "2. or with a concealed pronoun, which is the masculine singular, as in “ughzu, irmi, ikhsha”."},
    {"type": "matn",
     "ar": "فالنون مع الضمير البارز كالكلمة المنفصلة، نحو: «أغزن وارمن يا قوم» بحذف الواو، كما حذفت في نحو: «أغزوا الكفار، وارموا الغرض»،",
     "en": "So the nūn with an overt pronoun is like a separate word, as in “ughzunna wa-rmunna yā qawmi” (raid and throw, O people), with the wāw elided, just as it is elided in, for example, “ughzu l-kuffāra wa-rmu l-gharaḍa” (raid the unbelievers and shoot at the target);"},
    {"type": "matn",
     "ar": "وكذا «أغزن وارمن يا امرأة» بحذف الياء كما حذفت في «أغزي الجيش وارمي الغرض»،",
     "en": "likewise “ughzinna wa-rminna yā mraʾatu” (raid and throw, O woman), with the yāʾ elided, just as it is elided in “ughzi l-jaysha wa-rmi l-gharaḍa” (raid the army and shoot at the target);"},
    {"type": "matn",
     "ar": "وتضم الواو المفتوح ما قبلها نحو: «اخشون» كما ضممتها مع المنفصلة تقول: «اخشين» كـ«اخشي الرجل».",
     "en": "and the wāw preceded by a fatḥa takes a ḍamma, as in “ikhshawunna”, just as you give it a ḍamma with a separate word; [and] you say “ikhshayinna”, like “ikhshayi l-rajula” (fear the man)."},
    {"type": "matn",
     "ar": "(فإن لم يكن) أي: الضمير البارز، وهو في الواحد المذكر، نحو: «أغز وارم، واخش» (فكالمتصل) أي: فالنون كالكلمة المتصلة،",
     "en": "(And if there is not), that is, an overt pronoun — which is in the masculine singular, as in “ughzu, irmi, ikhsha” — (then [it is] like the joined), that is, the nūn is like a joined word;"},
    {"type": "matn",
     "ar": "ويعني بها: ألف التثنية، تقول: «أغزون وارمين واخشين» برد اللامات وفتحها كما قلت: «اغزوا، وارميا، واخشيا».",
     "en": "by this he means the alif of the dual. You say “ughzuwanna, irmiyanna, ikhshayanna”, restoring the final radicals (lāmāt) and giving them a fatḥa, just as you said “ughzuwā, irmiyā, ikhshayā”."},
    {"type": "matn",
     "ar": "(ومن ثم) أي: لأجل أنه مع غير الضمير البارز كالمتصل، مع الضمير البارز كالمنفصل",
     "en": "(Hence), that is, because with other than an overt pronoun it is like the joined, and with an overt pronoun like the separate,"},
    {"type": "matn",
     "ar": "(قيل: «هل ترين؟») في: «هل ترى؟» كما يقال: «تريان»، هذا مثال لغير البارز الذي تحركت لامه بالفتح كما يفتح مع المتصل.",
     "en": "(one says “hal tarayanna?”) for “hal tarā?” (do you see?), just as one says “tarayāni”. This is an example of the non-overt [pronoun], whose final radical takes a fatḥa, as it takes a fatḥa with the joined."},
    # REVIEW: printed «لم تروا القوم؟» with a question mark after a «لم» clause; transcribed as printed.
    {"type": "matn",
     "ar": "(و) هل («ترون؟») في «هل ترون؟» بإسقاط نون الجمع وإلحاق نون التأكيد، وضم الواو كضمها في «لم تروا القوم؟» هذا مثال ما فيه ضمير بارز يضم لأجل النون.",
     "en": "(And) “hal (tarawunna?)” for “hal tarawna?”, dropping the nūn of the plural, attaching the nūn of corroboration, and giving the wāw a ḍamma as in “lam tarawu l-qawma?”. This is an example of what has an overt pronoun that takes a ḍamma because of the nūn."},
    {"type": "matn",
     "ar": "(و) هل («ترين؟») في مثل «هل ترين؟» بإثبات الياء وكسرها كما يقال: «لم تري الناس»، هذا مثال ما فيه ضمير بارز يكسر لأجل النون.",
     "en": "(And) “hal (tarayinna?)” for, for example, “hal tarayna?”, keeping the yāʾ and giving it a kasra, as one says “lam tarayi l-nāsa” (did you not see the people). This is an example of what has an overt pronoun that takes a kasra because of the nūn."},
    {"type": "matn",
     "ar": "(و«اغزون؟») عطف على «هل ترين؟» لا على «ترين» أي: ومن ثم قيل: «اغزون» برد الواو المحذوفة كما يرد مع ضمير التثنية في «اغزوا»",
     "en": "(And “ughzuwanna”) is coordinated with “hal tarayanna?”, not with “tarayinna”; that is: hence one says “ughzuwanna”, restoring the elided wāw, as it is restored with the pronoun of the dual in “ughzuwā”;"},
    # REVIEW: the matn lemma «اغزن؟» and «واغزن؟» carry a question mark in print, though they are imperatives; transcribed as printed.
    {"type": "matn",
     "ar": "و«اغزن؟» في «اغزوا» بحذف الواو المضموم ما قبلها، كما قيل: «اغزوا القوم»، «واغزن؟» في «اغزي» بحذف الياء المكسور ما قبلها كـ«اغزي القوم».",
     "en": "and “ughzunna” for “ughzū”, eliding the wāw preceded by a ḍamma, just as one says “ughzu l-qawma” (raid the people); and “ughzinna” for “ughzī”, eliding the yāʾ preceded by a kasra, as in “ughzi l-qawma”."},
    {"type": "matn",
     "ar": "وهذه الأمثلة وقعت على ترتيب تصريفها الواقع في كتب التصريف، بعضها لما هو مع الضمير البارز كالمنفصل، وبعضها لما هو مع غير الضمير البارز كالمتصل، كما أشرنا إليه.",
     "en": "These examples come in the order of their conjugation found in the books of morphology (taṣrīf): some for what is, with an overt pronoun, like the separate, and some for what is, with other than an overt pronoun, like the joined, as we have indicated."},
]
