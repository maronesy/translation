# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 348 (printed ٣٤٧)."""

PAGE_NUMBER = 348
PRINTED_PAGE = "٣٤٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «أجري بقية الباب عليه.» at the foot of PDF p. 347 (new paragraph).
    {"type": "matn",
     "ar": "وإنما قيد الضمير بالمرفوع لجواز تأكيد الضمير المنصوب والمجرور بالنفس والعين بلا تأكيدهما بالمنفصل نحو: «ضربتك نفسك، ومررت بك نفسك» لعدم اللبس،",
     "en": "He restricted the pronoun to the nominative because the accusative and genitive pronouns may be corroborated by al-nafs and al-ʿayn without being corroborated by a separate pronoun, as in “ḍarabtuka nafsaka” (I struck you yourself) and “marartu bika nafsika” (I passed by you yourself), since there is no confusion;"},
    {"type": "matn",
     "ar": "وبالمتصل لجواز تأكيد المرفوع المنفصل بـ«النفس والعين» بلا تأكيده بمنفصل نحو: «أنت نفسك قائم» لعدم اللبس.",
     "en": "and to the connected, because the separate nominative may be corroborated by al-nafs and al-ʿayn without corroboration by a separate pronoun, as in “anta nafsuka qāʾimun” (you yourself are standing), since there is no confusion."},
    {"type": "matn",
     "ar": "وإنما قيد بـ«النفس والعين» لجواز تأكيد المرفوع المتصل بـ«كل وأجمعين» بلا تأكيد بمنفصل نحو: «القوم جاؤوني كلهم أجمعون» لعدم التباس التأكيد بالفاعل؛",
     "en": "He restricted it to al-nafs and al-ʿayn because the connected nominative may be corroborated by “kull” and “ajmaʿīn” without corroboration by a separate pronoun, as in “al-qawmu jāʾūnī kulluhum ajmaʿūna” (the people came to me, all of them together), since the corroborative is not confused with the agent;"},
    {"type": "matn",
     "ar": "لأن «كلا وأجمعين» يليان العوامل قليلا، بخلاف «النفس والعين»، فإنهما يليانها كثيرا.",
     "en": "for “kull” and “ajmaʿīn” rarely follow governors directly, unlike al-nafs and al-ʿayn, which often do."},
    {"type": "matn",
     "ar": "(و«أكتع» وأخواه) يعني: «أبتع وأبصع» (أتباع) بفتح الهمزة على ما هو المشهور (لـ«أجمع»[[١]]) يعني: تستعمل هذه الكلمات الثلاث بتبعيته لا بالأصالة، لكونه أدل منها على المقصود، وهو الجمعية.",
     "en": "(“Aktaʿ” and its two sisters), that is, “abtaʿ” and “abṣaʿ”, (are followers [atbāʿ]), with fatḥa on the hamza according to the well-known reading, (of “ajmaʿ”): these three words are used as followers of it, not independently, because it indicates the intended meaning, togetherness (al-jamʿiyya), better than they do."},
    {"type": "matn",
     "ar": "(فلا يتقدم) يعني: أكتع وأخواه (عليه) أي: على «أجمع» لو اجتمعت معه (وذكرها) أي: ذكر «أكتع» مع أخويه (دونه) أي: دون ذكر «أجمع» (ضعيف)",
     "en": "(So they do not precede), that is, aktaʿ and its two sisters, (it), that is, “ajmaʿ”, if they occur with it; (and mentioning them), that is, mentioning “aktaʿ” with its two sisters, (without it), that is, without mentioning “ajmaʿ”, (is weak),"},
    {"type": "matn",
     "ar": "لعدم ظهور دلالتها على معنى الجمعية، وللزوم ذكر ما من شأنه التبعية بدون الأصل.",
     "en": "because their indication of the meaning of togetherness is not evident, and because it entails mentioning what is by nature a follower without the original."},

    {"type": "section", "ar": "[البدل]",
     "en": "The Substitute (al-Badal)"},

    {"type": "matn",
     # REVIEW: «إلي» printed with a dotted yāʾ (إلي المتبوع) in the bold matn of al-Kāfiya; transcribed as printed.
     "ar": "(البدل: تابع مقصود بما نسب إلي المتبوع[[٢]]) أي: بقصد النسبة إليه بنسبة ما نسب إلى المتبوع",
     "en": "(The substitute [badal] is an appositive intended by what is attributed to the word followed), that is, the attribution is intended to it, through the attribution of what is attributed to the word followed,"},
    {"type": "matn",
     "ar": "(دونه[[٣]]) أي: دون المتبوع، أي: لا يكون النسبة إلى المتبوع مقصودة ابتداء بنسبة ما نسب إليه، بل يكون النسبة إليه توطئة[[٤]] وتمهيدا للنسبة إلى التابع[[٥]]،",
     "en": "(not it), that is, not the word followed: the attribution to the word followed is not primarily intended by the attribution of what is attributed to it; rather, the attribution to it is a preparation (tawṭiʾa) and a lead-in to the attribution to the appositive,"},
    {"type": "matn",
     "ar": "سواء كان ما نسب إليه مسندا إليه أو غيره، مثل: «جاءني زيد أخوك»، و«ضربت زيدا أخاك»، و«مررت بزيد أخيك».",
     "en": "whether what it is attributed to is a subject of predication or otherwise, as in “jāʾanī Zaydun akhūka” (Zayd, your brother, came to me), “ḍarabtu Zaydan akhāka” (I struck Zayd, your brother) and “marartu bi-Zaydin akhīka” (I passed by Zayd, your brother)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     # REVIEW: «أن يقول» is followed directly by «، فتأمل فاعرف» with no wording of what he should say; the sentence appears incomplete. Transcribed as printed.
     "ar": "وطريق الجمع بين ألفاظ التأكيد، وكيفية ترتيبه أن يقول، فتأمل فاعرف.",
     "en": "The way of combining the corroborative words, and the manner of ordering them, is that he should say …; so reflect and understand."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يخرج من التعريف البدل من المنسوب نحو: ضيفي زيد أخوك، والعبارة الصحيحة البدل تابع مقصود بالنسبة دون متبوعه.",
     "en": "A substitute for the thing attributed is excluded by the definition, as in “ḍayfī Zaydun akhūka” (my guest is Zayd, your brother). The correct wording is: the substitute is an appositive intended by the attribution, not the word it follows."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ظرف لنسب، أو حال من المستتر فيه أي: متجاوزا من المتبوع.",
     "en": "It is an adverbial qualifier of “nusiba”, or a circumstantial qualifier (ḥāl) of the pronoun latent in it, that is, “passing beyond the word followed”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذا غير ظاهر في بدل الغلط.",
     "en": "This is not evident in the substitute of error (badal al-ghalaṭ)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: حقيقة أو حكما كما في بدل الغلط، فإنه وإن لم يجعل توطئة، بل كان سبق لسان، لكنه في حكم التوطئة،",
     "en": "That is, in reality or by status, as in the substitute of error: although it was not made a preparation, but was a slip of the tongue, it has the status of a preparation,"},
    {"type": "pair",
     "ar": "فإنه في حكم الساقط وموجب التقرير والتمكن في حق البدل.",
     "en": "for it is treated as dropped, and it brings about the establishment and firm placement of the substitute."},
]
