# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 69 (printed ٦٨)."""

PAGE_NUMBER = 69
PRINTED_PAGE = "٦٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "الموصولة: الحركة، أو الحرف، لا يرد العامل والمقتضي. ولو أبقيت على عمومها[[١]]",
     "en": "— the relative [“mā”]: [namely] the vowel or the letter, the governing agent and the requiring cause (muqtaḍī) are not comprised. And were it left in its generality,"},
    {"type": "matn",
     "ar": "لخرجا[[٢]] بالسببية المفهومة من قوله: «به»؛ فإن المتبادر من السبب هو السبب القريب، والعامل والمقتضي من الأسباب البعيدة.",
     "en": "the two would [still] be excluded by the causality understood from his words “bihi” (“by it”); for what comes first to mind from “cause” is the proximate cause, whereas the governing agent and the requiring cause are among the remote causes."},
    {"type": "matn",
     "ar": "وبقيد الحيثية خرجت حركة نحو: «غلامي»؛ لأنه[[٣]] معرب على اختيار المصنف، لكن اختلاف هذه الحركة على آخر المعرب، ليس من حيث إنه معرب[[٤]]، بل من حيث إنه ما قبل ياء المتكلم.",
     "en": "And by the restriction of “respect” (ḥaythiyya) there is excluded the vowel in such [a case] as “ghulāmī” (“my servant-boy”); for it is declinable according to the author’s choice, yet the variation of this vowel upon the ending of the declinable noun is not inasmuch as it is declinable, but rather inasmuch as it is that which precedes the yāʾ of the speaker (yāʾ al-mutakallim)."},
    {"type": "matn",
     "ar": "وبهذا القدر تم حد الإعراب جمعا[[٥]] ومنعا[[٦]]، لكن المصنف أراد أن ينبه على فائدة اختلاف وضع الإعراب[[٧]]، فضم إليه[[٨]] قوله: «ليدل على المعاني[[٩]] المعتورة عليه»،",
     "en": "With this much the definition (ḥadd) of inflection was complete, [both] as inclusive and as exclusive; yet the author wished to draw attention to the benefit of the institution of inflection, so he appended to it his words: “that it may indicate the meanings that alternate over it (al-muʿtawira ʿalayhi),”"},
    {"type": "matn",
     "ar": "وكأنه أراد هذا المعنى حيث قال[[١٠]]: ليس هذا من تمام الحد؛ لا أنه خارج عن الحد.",
     "en": "It is as though he intended this meaning where he said: “This is not part of the completion of the definition” — not that it is outside the definition."},
    {"type": "matn",
     "ar": "واللام في «ليدل»[[١١]] متعلق بأمر خارج عن الحد، يعني: وضع الإعراب[[١٢]] المفهوم",
     "en": "And the lām in “li-yadulla” (“that it may indicate”) is governed by a matter lying outside the definition — that is, the institution of inflection understood"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كلمة «لو» تشعر بترجيح الاحتمال الأول، وهو تخصيص «ما» بالحركة والحرف لاستعمالها فيما يمتنع وقوعه مع أن هذا الاحتمال أولى، فالأولى ذكر «إذ» بدل «لو».",
     "en": "The word “law” (“were”) hints at the preponderance of the first possibility — namely, the restriction of “mā” to the vowel and the letter — since [“law”] is used for that whose occurrence is precluded, whereas this [latter] possibility is more fitting; so it would be more apt to mention “idh” (“since”) in place of “law.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: العامل والمقتضي.",
     "en": "That is: the governing agent and the requiring cause."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: ما أضيف إليها.",
     "en": "That is: that to which it [the yāʾ] is annexed."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لوجوده قبل عامل الجر، بل قبل مطلق العامل. وكذلك الحال في الصورة المذكورة.",
     "en": "Because of its existing before the genitive-governing agent — indeed, before the agent absolutely. And likewise is the case in the aforementioned instance."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: جامعا لأفراده.",
     "en": "That is: inclusive of its individual instances."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: مانعا عن دخول غيره فيه.",
     "en": "That is: preventing the entry of what is other than it into it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وترجيح الإتيان به على «تركه»، وأراد التنبيه على فائدة وضع الإعراب في الأسماء دون الأفعال والحروف.",
     "en": "And [drawing attention to] the preference of bringing it in over omitting it; and he intended to alert [the reader] to the benefit of instituting inflection in the nouns, not in the verbs and the particles."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: الحد.",
     "en": "That is: to the definition."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "جمع معنى بمعنى ما يقوم بالشيء، ويقابله العين.",
     "en": "The plural of “maʿnā” in the sense of that which subsists in a thing; and “al-ʿayn” (the concrete entity) is its opposite."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "في شرحه على هذا الكتاب.",
     "en": "In his commentary on this book."},
    {"type": "pair",
     "ar": "والأوجه أن المصنف ومن قال: هو علة وضع الإعراب أرادوا أنه متعلق بوضع الإعراب المفهوم من فحوى الكلام، وإلا لم ينطبق الغرض على الفعل؛",
     "en": "And the more fitting [view] is that the author, and whoever said “it [the lām] is the cause (ʿilla) of the institution of inflection,” meant that it is connected to the institution of inflection understood from the tenor of the discourse; otherwise the purpose would not apply to the verb;"},
    {"type": "pair",
     "ar": "لأن الدعوى على تقدير تعلقه باختلاف الآخر لغرض الدلالة على المعاني.",
     "en": "because the claim, on the supposition of its being connected to the difference of the ending, is [made] for the purpose of indicating the meanings."},
    {"type": "pair",
     "ar": "وهذا الغرض لا يستدعي اختلاف الآخر، بل وضع الإعراب مطلقا.",
     "en": "And this purpose does not require the difference of the ending, but rather the institution of inflection absolutely."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "معطوف على اسم «إن» وخبرها.",
     "en": "[It is] conjoined to the noun of “inna” and its predicate."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "أي: وضع الإعراب في الأسماء ليدل على المعاني، ويتضح به المعاني في نفس الأسماء من غير استعانة إلى العامل والقرينة، فذلك للاعتناء بشأنها.",
     "en": "That is: the institution of inflection in the nouns so that it may indicate the meanings, and so that the meanings become clear thereby within the nouns themselves without recourse to the agent and the contextual indicator (qarīna); and that is out of concern for their [the nouns’] importance."},
]
