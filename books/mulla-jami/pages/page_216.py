# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 216 (printed ٢١٥)."""

PAGE_NUMBER = 216
PRINTED_PAGE = "٢١٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "و«يا ابن أم، ويا ابن عم» بحذف الياء والاكتفاء بالكسرة.",
     "en": "…and “yā ibna ummi” and “yā ibna ʿammi,” dropping the yāʾ and letting the kasra suffice;"},
    {"type": "matn",
     "ar": "و«يا ابن أما، ويا ابن عما» بإبدال الياء ألفا.",
     "en": "and “yā ibna ummā” and “yā ibna ʿammā,” replacing the yāʾ with an alif."},
    {"type": "matn",
     "ar": "(وقالوا) بزيادة وجه آخر شذ في المضاف إلى ياء المتكلم («يا ابن أم» و«يا ابن عم») بحذف الألف، والاكتفاء بالفتحة لكثرة الاستعمال، وطول اللفظ، وثقل التضعيف.",
     "en": "(And they said), with an additional form that is anomalous in what is annexed to the yāʾ of the speaker, (“yā ibna umma” and “yā ibna ʿamma”), dropping the alif and letting the fatḥa suffice, because of frequent use, the length of the expression, and the heaviness of the doubled consonant."},

    {"type": "section", "ar": "[ترخيم المنادى]",
     "en": "Curtailment of the Vocative (Tarkhīm)"},

    {"type": "matn",
     "ar": "ولما كان من خصائص النداء الترخيم[[١]]، شرع في بيانه، فقال: (وترخيم المنادى جائز) أي: واقع[[٢]] في سعة الكلام[[٣]] من غير ضرورة شعرية دعت إليه،",
     "en": "Since curtailment (tarkhīm) is among the properties of the vocative, he began to explain it, saying: (Curtailment of the vocative is permitted), that is, it occurs in the latitude of speech (saʿat al-kalām) without a poetic necessity calling for it;"},
    {"type": "matn",
     "ar": "فإن دعت إليه ضرورة، فبالطريق الأولى (وهو في غيره) أي: غير المنادى واقع (ضرورة) أي: لضرورة شعرية[[٤]] داعية إليه لا في سعة الكلام.",
     "en": "if a necessity calls for it, then all the more so. (And in other than it)—that is, other than the vocative—it occurs (by necessity), that is, owing to a poetic necessity calling for it, not in the latitude of speech."},
    {"type": "matn",
     "ar": "(وهو) أي: ترخيم المنادى[[٥]] (حذف[[٦]] في آخره) أي: في آخر المنادى[[٧]] (تخفيفا)",
     "en": "(It)—that is, curtailment of the vocative—(is an elision at its end), that is, at the end of the vocative, (for lightening)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: الترخيم في سعة الكلام.",
     "en": "That is, curtailment in the latitude of speech."},
    {"type": "pair",
     "ar": "والترخيم من رخم الكلام من باب كرم أو نصر بمعنى: لان وسهل، فهو رخيم.",
     "en": "Tarkhīm is from rakhuma or rakhama al-kalām—of the pattern of karuma or naṣara—meaning it became soft and easy; so it is rakhīm."},
    {"type": "pair",
     "ar": "والجارية إذا صارت سهلة النطق يقال: رخيمة.",
     "en": "When a girl becomes easy of speech, she is called rakhīma."},
    {"type": "pair",
     "ar": "ومنه الترخيم في الأسماء؛ لأنه سهل النطق بها.",
     "en": "From this comes curtailment in nouns, because it makes pronouncing them easy."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: أن الجواز وقوعي.",
     "en": "He means that the permissibility is one of actual occurrence."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا القيد يتبادر إليه الذهن. ويؤيده مقابلة الجواز للضرورة.",
     "en": "This qualification is what first comes to mind, and the contrast of permissibility with necessity supports it."},
    {"type": "pair",
     "ar": "ولك ألا تقيد بجعل الجواز شاملا للضرورة.",
     "en": "You may also leave it unqualified, taking permissibility to include necessity."},
    {"type": "pair",
     "ar": "وإنما وقع ترخيم المنادى في السعة لكون المقصود في النداء هو المنادى له، فيقصد سرعة الفراغ منه إلى ما هو المقصود مع ندرة الالتباس؛",
     "en": "Curtailment of the vocative occurs in the latitude [of speech] only because what is intended in the vocative is that for which one calls; so one aims to be done with it quickly and move to what is intended, while confusion is rare,"},
    {"type": "pair",
     "ar": "لأن الإنسان في حال ندائه أكثر انتباها لاسمه منه في غير حال النداء.",
     "en": "because a person, when called, is more alert to his name than when not called."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: print reads «فاعلمها»; probably «فاعلهما»; transcribed as printed.
    {"type": "pair",
     "ar": "إشارة إلى أنه مفعول له، لكن فعله فعل الترخيم المفهوم من الكلام لا فعل الجواز؛",
     "en": "An indication that it is an object of reason (mafʿūl lahu); but its verb is the verb of curtailing understood from the speech, not the verb of permitting,"},
    {"type": "pair",
     "ar": "لأنه صفة الترخيم، والضرورة والاضطرار صفة المرخم، فلم يتحد فاعلمها،",
     "en": "because [permissibility] is an attribute of curtailment, while necessity and constraint are an attribute of the one who curtails; so their agents are not one,"},
    {"type": "pair",
     "ar": "وحذف اللام مشروط باتحاد الفاعل والحمل على عدم الاشتراط، كما ذهب إليه بعضهم بعيد؛ لأنه يخالف مذهب المصنف.",
     "en": "and dropping the lām is conditional on the agent being the same. Taking it as not conditional, as some have held, is far-fetched, because it conflicts with the author’s position."},
    # REVIEW: print reads «أذمى»; the known verse (Dhū al-Rumma) reads «إذ مي»; transcribed as printed.
    {"type": "pair",
     "ar": "ولك أن ترفع ضرورة على الخبرية، أي: الترخيم في غيره أثر ضرورة نحو قوله: «ديار مية أذمى تساعفنا»، الأصل مية.",
     "en": "You may also put “ḍarūra” in the nominative as a predicate, that is: curtailment in other than it is an effect of necessity, as in his words “the abodes of Mayya, when Mayy favours us,” the original [of the curtailed Mayy] being Mayya."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الرخمة بالمعجمة كالرحمة بالمهملة صيغة ومعنى.",
     "en": "Rakhma, with the dotted [khāʾ], is like raḥma, with the undotted [ḥāʾ], in form and meaning."},
    {"type": "pair",
     "ar": "ويقال: كلام رخيم أي: رقيق والترخيم التليين والحذف.",
     "en": "One says “kalām rakhīm,” that is, gentle speech; and tarkhīm is softening and elision."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأظهر أن يتقدم تعريف الترخيم على حكمه، لكن قدمه؛ لأنه المقصود.",
     "en": "It would be more evident for the definition of curtailment to precede its ruling; but he put [the ruling] first because it is what is intended."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     # REVIEW: printed «خذف» (khāʾ) for «حذف»; transcribed as printed, translated as حذف.
     "ar": "فخرج خذف ياء يا غلامي؛ لأنه ليس آخر المنادى بدليل اعتبار الإعراب فيما قبله،",
     "en": "So the dropping of the yāʾ of “yā ghulāmī” is excluded, because it is not the end of the vocative, as shown by the iʿrāb being reckoned on what precedes it;"},
    {"type": "pair",
     "ar": "ودخل فيه حذف الكلمة الأخيرة في بعلبك بدليل إجراء الإعراب عليها.",
     "en": "and the dropping of the last word in Baʿlabakk is included in it, as shown by the iʿrāb being applied to it."},
]
