# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 482 (printed ٤٨١)."""

PAGE_NUMBER = 482
PRINTED_PAGE = "٤٨١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Begins a new sentence; PDF p. 481 ended with a full stop.
    {"type": "matn",
     "ar": "فخرج بهذا القيد الحرف؛ لأنه ليس مستقلا بالمفهومية.",
     "en": "By this restriction the particle is excluded, because it is not independent in being understood."},
    {"type": "matn",
     "ar": "(مقترن) وضعا (بأحد الأزمنة الثلاثة) في الفهم من لفظه الدال عليه، فهو صفة[[١]] بعد صفة للمعنى، يخرج به الاسم عن حد الفعل.",
     "en": "(Conjoined), by coining (waḍʿ), (with one of the three times) in being understood from the expression that indicates it; it is an adjective of “meaning” after an adjective, and by it the noun is excluded from the definition of the verb."},
    {"type": "matn",
     "ar": "وبقولنا: «وضعا» يخرج أسماء الأفعال؛ لأن جميعها منقولة: إما عن المصادر أو غيرها كما سبق.",
     "en": "By our saying “by coining”, the verbal nouns (asmāʾ al-afʿāl) are excluded, for all of them are transferred, either from verbal nouns or from other things, as has preceded."},
    {"type": "matn",
     "ar": "ودخل فيه[[٢]] الأفعال المنسلخة عن الزمان، نحو: «عسى وكاد» لاقتران معناها به بحسب الوضع،",
     "en": "Included in it are verbs stripped of time, such as “ʿasā” and “kāda”, because their meaning is conjoined with it by coining;"},
    {"type": "matn",
     "ar": "ويصدق على المضارع أنه مقترن بأحد الأزمنة الثلاثة، لوجود الأحد في الاثنين[[٣]]؛",
     "en": "and it is true of the imperfect (muḍāriʿ) that it is conjoined with one of the three times, because the one is present in the two,"},
    {"type": "matn",
     "ar": "ولأنه مقترن بحسب كل وضع بواحد وإن عرض الاشتراك من تعدد الوضع.",
     "en": "and because by each coining it is conjoined with one, even though ambiguity (ishtirāk) arises from the multiplicity of coinings."},

    {"type": "section", "ar": "[خواص الفعل]",
     "en": "The Properties of the Verb"},

    {"type": "matn",
     "ar": "(ومن خواصه) أي: خواص الفعل:",
     "en": "(Among its properties), that is, the properties of the verb:"},
    {"type": "matn",
     "ar": "١-(دخول «قد»)؛ لأنها إنما تستعمل لتقريب الماضي إلى الحال، أو لتقليل الفعل[[٤]]، أو تحقيقه، وشيء من ذلك لا يتحقق إلا في الفعل.",
     "en": "1. (The entry of “qad”), because it is used only to bring the past near to the present, or to express the infrequency of the act, or its certainty; and none of these is realized except in the verb."},
    {"type": "matn",
     "ar": "٢-(و) دخول («السين»[[٥]] و«سوف») لدلالة الأول على الاستقبال القريب، والثاني على الاستقبال البعيد.",
     "en": "2. (And) the entry of (“sīn” and “sawfa”), because the first indicates the near future and the second the distant future."},
    {"type": "matn",
     "ar": "٣-(و) دخول (الجوازم)؛ لأنها وضعت[[٦]]: إما لنفي الفعل كـ«لم» و«لما»، أو لطلبه كـ«لام الأمر» أو للنهي عنه كـ«لاء النهي»، أو لتعليق الشيء بالفعل كـ«أدوات الشرط».",
     "en": "3. (And) the entry of (the jussive particles, jawāzim), because they were coined either to negate the act, like “lam” and “lammā”, or to request it, like “the lām of command”, or to forbid it, like “the lā of prohibition”, or to make something contingent on the act, like “the conditional particles”."},
    {"type": "matn",
     "ar": "وكل من هذه المعاني لا يتصور إلا في الفعل.",
     "en": "Each of these meanings is conceivable only in the verb."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الفاء لمجرد التراخي في الذكر، فإن بيان فوائد القيود متأخر عن ذكرها.",
     "en": "The fāʾ is merely for sequence in mention, for the explanation of the benefits of the restrictions comes after mentioning them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «أفاد التقييد في الإثبات الدخول» — the wording is unusual; transcribed as printed and translated literally.
    {"type": "pair",
     "ar": "عطف على قوله: خرج. وإنما أفاد التقييد في الإثبات الدخول؛ لأنه في الحقيقة تعميم لقوله: مقترن؛",
     "en": "Coordinated with his word “kharaja” (is excluded). The restriction conveyed, in affirming, inclusion only because it is in reality a generalization of his word “conjoined”;"},
    {"type": "pair",
     "ar": "لأن معنى قوله: وضعا سواء كان مقترنا استعمالا أو لا.",
     "en": "for the meaning of his word “by coining” is: whether or not it is conjoined in usage."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فالمراد بأحد الأزمنة أحدها مطلقا لا أحدها فقط.",
     "en": "So what is meant by “one of the times” is one of them absolutely, not one of them only."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فإن قلت: المراد بالفعل الحدث؛ إذ لا معنى لتقليل الفعل الاصطلاحي أو تحقيقه، فلا يصح قوله: وشيء من ذلك لا يتحقق إلا في الفعل؟",
     "en": "If you say: what is meant by “the act” is the event, since there is no sense in the infrequency or certainty of the technical verb; so his saying “none of these is realized except in the verb” is not sound?"},
    {"type": "pair",
     "ar": "قلت: كأنه أراد الفعل الاصطلاحي. وأراده بقوله: لتقليل الفعل مدلول الفعل",
     "en": "I say: it is as though he meant the technical verb, and by his saying “to express the infrequency of the act” he meant what the verb signifies;"},
    {"type": "pair",
     "ar": "إلا أن الظاهر حينئذ أن يقول: شيء من ذلك لا يتحقق إلا فيه بالضمير، فتأمل.",
     "en": "except that the evident thing in that case would be to say “none of these is realized except in it”, with the pronoun. So reflect."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اللام للعهد أي: سين الاستقبال دون سائر السينات.",
     "en": "The article denotes the known referent, that is, the sīn of the future, not other sīns."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولأن الشيء ما لم يخص الشيء لم يعمل فيه.",
     "en": "And because a thing does not govern another so long as it is not specific to it."},
]
