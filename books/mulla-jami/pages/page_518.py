# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 518 (printed ٥١٧)."""

PAGE_NUMBER = 518
PRINTED_PAGE = "٥١٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «والانتقال والدوام» at the foot of PDF p. 517 (mid-sentence).
    {"type": "matn",
     "ar": "والاستمرار في بعضها،",
     "en": "…and continuation in some of them."},
    # REVIEW: printed «موضوع التقرير الفاعل» (definite التقرير before الفاعل); transcribed as printed.
    {"type": "matn",
     "ar": "ولو جعل[[١]] الموضوع له[[٢]] جزئيات ذلك التقرير فيقال: صار مثلا موضوع التقرير الفاعل على صفة على وجه الانتقال إليه في الزمان الماضي، وكذا كل فعل منها،",
     "en": "If what [they] were assigned for were made to be the particulars of that establishing — so that it is said, for example, that ṣāra is assigned for the establishing of the agent in an attribute by way of transition to it in past time, and likewise each verb among them —"},
    {"type": "matn",
     "ar": "فلا شك أن كل جزئي تمام الموضوع له بالنسبة إلى ما هو موضوع له، والصفة خارجة عنه، فخرج الأفعال التامة عنها،",
     "en": "then there is no doubt that each particular is the whole of what [the verb] is assigned for, in relation to that for which it is assigned, and the attribute lies outside it; so the complete verbs are excluded from it [the definition]."},
    {"type": "matn",
     "ar": "ولا يبعد[[٣]] أن يجعل اللام في قوله: «لتقرير الفاعل» للغرض لا صلة للوضع،",
     "en": "It is not far-fetched to take the lām in his words “li-taqrīr al-fāʿil” as denoting purpose, not as the complement of “assignment”;"},
    {"type": "matn",
     "ar": "ولا شك أن الغرض من وضع الأفعال الناقصة هو التقرير المذكور لا الصفات،",
     "en": "and there is no doubt that the purpose of assigning the defective verbs is the establishing mentioned, not the attributes,"},
    {"type": "matn",
     "ar": "بخلاف الأفعال التامة، فإن الغرض من وضعها مجموعها لا التقرير فحسب كما عرفت، فخرجت عن حدها،",
     "en": "unlike the complete verbs, for the purpose of assigning them is the whole of it, not the establishing alone, as you have learned; so they are excluded from its definition."},
    {"type": "matn",
     "ar": "فظهر بما ذكرنا أن هذا الحد لا يحتاج إلى قيد زائد[[٤]] لإخراج الأفعال التامة أصلا.",
     "en": "It is thus evident from what we have mentioned that this definition needs no additional qualification at all to exclude the complete verbs."},
    {"type": "matn",
     "ar": "(وهي) أي: الأفعال الناقصة («كان»، و«صار»، و«أصبح»، و«أمسى»، و«أضحى»، و«ظل»، و«بات»، و«آض» و«عاد»، و«غدا»، و«راح»، و«ما زال»، و«ما انفك»، و«ما فتئ») بالهمزة، وقيل: بالياء[[٥]]",
     "en": "(They), that is, the defective verbs, (are “kāna”, “ṣāra”, “aṣbaḥa”, “amsā”, “aḍḥā”, “ẓalla”, “bāta”, “āḍa”, “ʿāda”, “ghadā”, “rāḥa”, “mā zāla”, “mā infakka”, “mā fatiʾa”) with hamza — and it has been said: with yāʾ —"},
    {"type": "matn",
     "ar": "(و«ما برح»، و«ما دام»، و«ليس»)",
     "en": "(“mā bariḥa”, “mā dāma” and “laysa”)."},
    {"type": "matn",
     "ar": "ولم يذكر سيبويه منها سوى «كان، وصار، وما دام، وليس»، ثم قال: «وما كان نحوهن من الفعل مما لا يستغنى عن الخبر»،",
     "en": "Sībawayh mentioned of them only “kāna, ṣāra, mā dāma and laysa”, and then said: “and whatever verbs are like them, among those that cannot dispense with the predicate”."},
    {"type": "matn",
     "ar": "والظاهر أنها غير محصورة، وقد تضمن[[٦]] كثير[[٧]] من الأفعال",
     "en": "What is apparent is that they are not limited in number; many verbs may be made to imply (taḍmīn)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيكون المعنى ما وضع لها يصدق عليه التقرير المذكور،",
     "en": "The meaning would then be: what they are assigned for is something of which the establishing mentioned is true;"},
    {"type": "pair",
     "ar": "وعلى هذا التوجيه لا حاجة إلى اعتبار قيد العمدة، واللام صلة للوضع، كما هو الظاهر.",
     "en": "on this interpretation there is no need to take the qualification “principal element” into account, and the lām is the complement of “assignment”, as is apparent."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى تصحيح الحد بالتصرف في معاني الأفعال الناقصة، وجعلها مجرد التقرير بدعوى خروج ما زاد على التقرير عن معناها وكونها قيودا له.",
     "en": "An indication of correcting the definition by adjusting the meanings of the defective verbs and making them the bare establishing, by claiming that what exceeds the establishing lies outside their meaning and constitutes qualifications of it."},
    {"type": "pair",
     "ar": "ولا يخفى أنه مع ذلك أيضا لا يكون تمام الموضوع له التقرير، بل التقرير والتقييد",
     "en": "It is not hidden that even so the whole of what [they] are assigned for is not the establishing, but the establishing together with the qualification;"},
    {"type": "pair",
     "ar": "على أن جعل الزمان خارجا عن هذه الأفعال داخلا في الأفعال التامة تكلف وتحكم.",
     "en": "besides, making time external to these verbs while internal to the complete verbs is contrived and arbitrary."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه إشارة إلى بعده في الجملة؛ لأن المتبادر كون اللام صلة الوضع.",
     "en": "In it is an indication that it is somewhat far-fetched, since what first comes to mind is that the lām is the complement of “assignment”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كأنه إشارة إلى قيد ذكره المحقق الشريف أن المراد صفة خارجة عن مدلولها ترك ذكره لتبادره من العبارة.",
     "en": "It is as though an allusion to a qualification mentioned by al-Muḥaqqiq al-Sharīf: that what is meant is an attribute external to what they signify; he left it unmentioned because it is readily understood from the wording."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يوجد هذا في الكتب المشهورة من اللغة والنحو، ولذا قال صاحب غاية التحقيق: دون الياء.",
     "en": "This is not found in the well-known books of lexicography and grammar; hence the author of Ghāyat al-taḥqīq said: “not with yāʾ”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال المحقق التفتازاني في شرح الكشاف: حقيقة التضمين: أن يقصد بالفعل معناه الحقيقي مع فعل آخر يناسبه،",
     "en": "Al-Muḥaqqiq al-Taftāzānī said in Sharḥ al-Kashshāf: the reality of implication (taḍmīn) is that by the verb its proper meaning is intended together with another verb that suits it;"},
    {"type": "pair",
     "ar": "وله طرق أشهرها جعل الفعل المذكور حالا أو عكسه وههنا طريق آخر نحو: أحمد إليك أي: انتهى إليك حمدي، انتهى.",
     "en": "it has several methods, the best known being to make the mentioned verb a circumstantial (ḥāl), or the reverse; and here there is another method, as in “aḥmadu ilayka”, that is, “my praise has reached you”. End of quotation."},
    {"type": "pair",
     "ar": "فعلم أنه ليس يتعين له طريق الحالية، فجعل تامة كاملة صفة، كما تقتضيه سلامة الطبع أولى من جعلها حالا.",
     "en": "So it is known that the method of the circumstantial is not the only one for it; and to make a complete verb an attribute, as sound taste requires, is better than making it a circumstantial."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "التضمن: ملاحظة معنى فعل لازم بمعنى فعل مع ملاحظة معناه وإعماله عمله بهذه الملاحظة،",
     "en": "Implication: taking into account the meaning of an intransitive verb in the sense of [another] verb, while taking its own meaning into account, and making it govern as that one governs by virtue of this consideration."},
    {"type": "pair",
     "ar": "ولإبرازه في مقام التفسير طريقان: جعل الأصل ثابتا، والمضمن حالا.",
     "en": "To bring it out in explanation there are two methods: making the original [meaning] fixed and the implied one a circumstantial;"},
    {"type": "pair",
     "ar": "ويقال في تفسير يتم التسعة",
     "en": "and one says, in explaining “yatimmu al-tisʿata”…"},
]
