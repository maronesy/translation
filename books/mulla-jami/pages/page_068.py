# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 68 (printed ٦٧)."""

PAGE_NUMBER = 68
PRINTED_PAGE = "٦٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "الإعراب، بل هناك حدوث الإعراب بدخول العامل؟",
     "en": "— the inflection; rather, there [comes about] the origination of inflection through the entry of the governing agent?"},
    {"type": "matn",
     "ar": "قلت: هذا حكم آخر[[١]] من أحكام المعرب، والاختلاف حكم آخر، فلو لم يدخل أحد الحكمين في الآخر، لا فساد فيه[[٢]].",
     "en": "I say: This is one ruling among the rulings of the declinable noun, and the difference (ikhtilāf) is another ruling; so were one of the two rulings not to enter into the other, there is no harm in that."},
    {"type": "matn",
     "ar": "فإن للمعرب أحكاما كثيرة لم تذكر ههنا، فليكن هذا الحكم أيضا من هذا القبيل.",
     "en": "For the declinable noun has many rulings not mentioned here, so let this ruling too be of that sort."},
    {"type": "matn",
     "ar": "غاية الأمر: أن هذا الحكم لا يكون من خواصه الشاملة.",
     "en": "The utmost of the matter is that this ruling would not be among its all-encompassing properties."},
    {"type": "matn",
     "ar": "(الإعراب: ما) أي: حركة أو حرف[[٣]] (اختلف آخره) أي: آخر المعرب من حيث هو معرب ذاتا أو صفة[[٤]] (به)[[٥]] أي: بتلك الحركة أو الحرف.",
     "en": "(al-Iʿrāb: mā — “Inflection is that…”) — that is, a vowel (ḥaraka) or a letter (ḥarf) — (ukhtulifa ākhiruhu — “whose ending is made to differ”) — that is, the ending of the declinable noun inasmuch as it is declinable, whether in its essence (dhātan) or in its quality (ṣifatan) — (bihi — “by it”) — that is, by that vowel or letter."},
    {"type": "matn",
     "ar": "وحين يراد[[٦]] بـ«ما»",
     "en": "And when there is intended by “mā” —"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إذا سبق على التركيب مع العوامل عاملان معنويان لم يكن التركيب للاسم المعدود مع العامل؛ لأنا نقول: التركيب للاسم المعدود، لكن لا ابتداء بل ثانيا.",
     "en": "If two abstract agents precede the combination with the agents, then the combination of the enumerated noun with the agent would not [be from the outset]; because we say: the combination belongs to the enumerated noun, yet not from the outset but secondarily."},
    {"type": "pair",
     "ar": "ومع ذلك تركيب الاسم المعدود مع العامل ابتداء إذا لم يسبق عليه تركيب الاسم المعدود مع العامل، وإن سبق عليه تركيب لا مع العامل.",
     "en": "Even so, the combination of the enumerated noun with the agent is “from the outset” if it is not preceded by [another] combination of the enumerated noun with the agent, even if it is preceded by a combination [that is] not with the agent."},
    {"type": "pair",
     "ar": "ولو لم يكن التركيب تابعا للاسم المعدود لم يكن لتقييد التركيب بابتداء معنى.",
     "en": "And were the combination not consequent upon the enumerated noun, there would be no meaning to qualifying the combination with “from the outset.”"},
    {"type": "pair",
     "ar": "حاصله: أن حكم الشيء لا يلزم أن يكون لازما له.",
     "en": "Its upshot: the ruling of a thing need not be a necessary concomitant of it."},
    {"type": "pair",
     "ar": "إن قلت: يجوز أن يقيد الاختلاف بالعوامل بأحد الأزمنة، وحينئذ يكون لازما للمعرب وإن لم يكن قبل تقييده بالظرف لازما له؟",
     "en": "If you say: it is permissible to qualify the difference [wrought] by the agents with [respect to] one of the times, in which case it would be a necessary concomitant of the declinable noun, even if, before its qualification by the temporal circumstance, it was not a concomitant of it?"},
    {"type": "pair",
     "ar": "قلنا: فيه صرف الكلام عن الظاهر بلا ضرورة مع أنه بعد ذلك التقييد أيضا غير لازم لجواز أن يتحقق معرب لم يتحقق معه عوامل في شيء من الأزمنة.",
     "en": "We say: In that there is a diverting of the statement from its apparent sense without necessity; moreover, even after that qualification it is still not a necessary concomitant, since it is possible that a declinable noun be realized with which no governing agents are realized at any of the times."},
    {"type": "pair",
     "ar": "نعم قابلية الاختلاف بالعوامل من لوازمه.",
     "en": "Yes — the susceptibility to difference through the agents is among its necessary concomitants."},
    {"type": "pair",
     "ar": "ولما كان المتبادر فعلية الاختلاف لم يتعرض له.",
     "en": "And since what comes first to mind is the actuality of the difference, he did not take it up."},
    {"type": "pair",
     "ar": "وقيل: المراد بالاختلاف الأول معنى يشمل الاختلاف الذي مبدأه حاله البنائي، والاختلاف الثاني الوجود.",
     "en": "It has been said: what is meant by the first “difference” is a meaning that includes the difference whose starting-point is its indeclinable (bināʾī) state, and the second “difference” is [actual] existence."},
    {"type": "pair",
     "ar": "وقد عبر عنه بالاختلاف للمشاكلة، وبالعوامل يعني جنس العامل، فإن اللام الداخلة على الجمع قد تبطل الجمعية، ولا يخفى بعد ذلك كله.",
     "en": "He expressed it as “difference” for the sake of formal correspondence (mushākala); and by “the agents” he means the genus of the agent, for the definite article (lām) entering upon a plural may nullify the plurality. And the remoteness of all this is not hidden."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في عدم الدخول.",
     "en": "That is: in the non-entering [of one ruling into the other]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كان القرينة عليه شهرة أمر الإعراب بأنه حركة، أو حرف، أو ما سيذكره في ضبط إعراب الأسماء، ولا يخفى بعده.",
     "en": "The indication (qarīna) for it is the well-known fact concerning inflection — that it is a vowel, or a letter, or what he will mention in [his] regulation of the inflection of nouns. And its remoteness is not hidden."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أما اختلاف الآخر، أي: تحوله ذاتا، فكما يتحول واو «أبوك» ألف «أباك». وأما تحوله صفة، فكما يتحول ضمة «زيد» إلى فتحة.",
     "en": "As for the difference of the ending — namely, its transformation in essence (dhātan) — it is as the wāw of “abūka” turns into the alif of “abāka”; and as for its transformation in quality (ṣifatan), it is as the ḍamma of “Zayd” turns into a fatḥa."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "اعترض عليه بأن التعريف غير جامع؛ لأن تغير «مسلمان» و«مسلمون» ليس في الآخر؛ إذ الآخر هو النون.",
     "en": "It has been objected against it that the definition is not comprehensive (jāmiʿ), because the change in “muslimāni” and “muslimūna” is not in the ending, since the ending is the nūn."},
    {"type": "pair",
     "ar": "وأجابوا عنه: بأن النون فيهما كالتنوين في المفرد.",
     "en": "They answered it: that the nūn in the two is like the nunation (tanwīn) in the singular."},
    {"type": "pair",
     "ar": "ولعلهم أرادوا به أن هذه الحيثية لما وجدت فيه في بعض الأوقات جاز أن يجعل الحرف السابق عليه بالنظر إلى هذه الحيثية في حكم الآخر، وإن كان بالنظر إلى كونه علامة للتثنية والجمع ليس في حكم الآخر.",
     "en": "Perhaps they meant by it that, since this respect (ḥaythiyya) is found in it at certain times, it is permissible to treat the letter preceding it — in view of this respect — as having the status of the ending, even though, in view of its being a marker of the dual and the plural, it does not have the status of the ending."},
    {"type": "pair",
     "ar": "وإنما قلنا: «في بعض الأوقات»؛ لأنه قد لا يكون بمنزلة التنوين.",
     "en": "We said “at certain times” only because it may not be in the position of the nunation."},
    {"type": "pair",
     "ar": "وذلك في المثنى والجمع المعرفين باللام لامتناع اجتماع اللام والتنوين.",
     "en": "And that is in the dual and plural made definite by the [article] lām, owing to the impossibility of the coexistence of the lām and the nunation."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "مبني للمفعول من «أراد يريد».",
     "en": "[It is] in the passive voice (mabnī li-l-mafʿūl), from “arāda / yurīdu.”"},
]
