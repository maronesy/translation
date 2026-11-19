# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 577 (printed ٥٧٦)."""

PAGE_NUMBER = 577
PRINTED_PAGE = "٥٧٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 576 ends with a complete sentence; this page continues the discussion of «ها».
    {"type": "matn",
     "ar": "وتدخل «ها» خاصة من المفردات على أسماء الإشارة حتى لا يغفل المخاطب عن الإشارة التي لا يتعين معانيها إلا بها،",
     "en": "Among single words, “hā” enters specifically upon demonstrative nouns, so that the addressee does not overlook the pointing, without which their meanings are not determined,"},
    {"type": "matn",
     "ar": "نحو: «هذا، وهاتا، وهذان، وهاتان، وهؤلاء».",
     "en": "as in “hādhā”, “hātā”, “hādhāni”, “hātāni” and “hāʾulāʾi”."},

    {"type": "section", "ar": "[حروف النداء]",
     "en": "The Vocative Particles (Ḥurūf al-Nidāʾ)"},

    {"type": "matn",
     "ar": "(حروف النداء: «يا» أعمها) استعمالا؛ لأنها تستعمل لنداء القريب والبعيد.",
     "en": "(The vocative particles: “yā” is the most general of them) in use, for it is used to call both the near and the far."},
    {"type": "matn",
     "ar": "(و«أيا» و«هيا» للبعيد، و«أي») بفتح الهمزة وسكون الياء.",
     "en": "(“Ayā” and “hayā” are for the far, and “ay”), with a fatḥa on the hamza and a sukūn on the yāʾ,"},
    {"type": "matn",
     "ar": "(و«الهمزة» للقريب) وكأنه أراد بالقريب ما عدا البعيد، فيدخل فيه المتوسط أيضا.",
     "en": "(and the hamza are for the near). It seems that by “the near” he meant whatever is not far, so that the intermediate is included in it too."},
    {"type": "matn",
     "ar": "فإن القريب ينقسم إلى قريب متصف بأصل القرب من غير زيادة، وله كلمة «أي»، وإلى: أقرب متصف بزيادة القرب، وله الهمزة،",
     "en": "For the near divides into a near that has nearness in its basic degree without excess, to which the word “ay” belongs, and a nearer that has an excess of nearness, to which the hamza belongs;"},
    {"type": "matn",
     "ar": "بخلاف البعيد، فإنه لم يذكر له مرتبتان. فالقريب بالمعنى المقابل للأقرب هو المتوسط بين كمال البعد وكمال القرب.",
     "en": "unlike the far, for which two degrees are not mentioned. So the near, in the sense that contrasts with the nearer, is the intermediate between complete farness and complete nearness."},

    {"type": "section", "ar": "[حروف الإيجاب]",
     "en": "The Particles of Affirmation (Ḥurūf al-Ījāb)"},

    {"type": "matn",
     "ar": "(حروف الإيجاب: «نعم»، و«بلى»، و«إي») بكسر الهمزة وسكون الياء.",
     "en": "(The particles of affirmation (ījāb): “naʿam”, “balā”, “ī”), with a kasra on the hamza and a sukūn on the yāʾ,"},
    {"type": "matn",
     "ar": "(و«أجل»، و«جير»، و«إن») بكسر الهمزة وفتح النون المشددة.",
     "en": "(“ajal”, “jayri” and “inna”), with a kasra on the hamza and a fatḥa on the doubled nūn."},
    {"type": "matn",
     "ar": "ومن بيان معاني تلك الحروف يتبين وجه تسميتها بحروف الإيجاب.",
     "en": "From the explanation of the meanings of these particles the reason for calling them particles of affirmation becomes clear."},
    {"type": "matn",
     "ar": "(فـ«نعم» مقررة لما سبقها) أي: محققة لمضمونه استفهاما كان أو خبرا.",
     "en": "(“Naʿam” confirms what precedes it), that is, it establishes its content, whether a question or a statement."},
    {"type": "matn",
     "ar": "فهي في جواب: «أقام زيد؟» بمعنى: قام زيد، وفي جواب: «ألم يقم زيد؟» بمعنى: لم يقم زيد.",
     "en": "So in answer to “did Zayd stand?” it means “Zayd stood”, and in answer to “did Zayd not stand?” it means “Zayd did not stand”."},
    {"type": "matn",
     "ar": "و«بلى» في جواب: «ألم يقم زيد؟» بمعنى: قام زيد.",
     "en": "“Balā”, in answer to “did Zayd not stand?”, means “Zayd stood”."},
    {"type": "matn",
     "ar": "فمعنى «بلى» في جواب: ﴿ألست بربكم﴾[[١]]: أنت ربنا، ولو قيل في موضع «بلى» ههنا: «نعم» لكان كفرا، فإن معناه حينئذ: لست بربنا.",
     "en": "So the meaning of “balā” in answer to “Am I not your Lord?” is “You are our Lord”; had “naʿam” been said here in place of “balā”, it would have been unbelief, for its meaning would then be “You are not our Lord”."},
    {"type": "matn",
     "ar": "وقيل: يجوز استعمال «نعم» ههنا بجعلها تصديقا للإثبات المستفاد من إنكار النفي. وقد اشتهر هذا في العرف.",
     "en": "It has been said that using “naʿam” here is permissible by taking it as assent to the affirmation derived from disavowing the negation; and this has become well known in customary usage."},
    {"type": "matn",
     "ar": "فلو قال أحد: «يا زيد أليس لي عليك ألف درهم؟» وقال زيد: «نعم»، يكون إقرار ويقوم مقام «بلى» لتقرير الإثبات بعد النفي.",
     "en": "So if someone said “O Zayd, do I not have a thousand dirhams owed to me by you?” and Zayd said “naʿam”, it is an acknowledgement (iqrār), and stands in place of “balā” in confirming the affirmation after the negation."},
    # REVIEW: printed «يكون إقرار» (grammatically «إقرارا» would be expected); transcribed as printed.
    {"type": "matn",
     "ar": "(و«بلى» مختصة بإيجاب النفي) يعني: ينقض النفي المتقدم، ويجعله إيجابا سواء",
     "en": "(And “balā” is specific to affirming a negation), that is, it overturns the preceding negation and makes it an affirmation, whether…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الأعراف: ١٧٢.",
     "en": "Qurʾān, Sūrat al-Aʿrāf 7:172."},
]
