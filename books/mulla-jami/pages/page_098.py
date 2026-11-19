# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 98 (printed ٩٧)."""

PAGE_NUMBER = 98
PRINTED_PAGE = "٩٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "في هذه الباب، حملا له على ذوات الراء في الأعلام المؤنثة، مثل: «حضار وطمار»، فإنهما مبنيتان، وليس فيهما إلا سببان[[١]]: العلمية والتأنيث، والسببان لا يوجبان البناء، فاعتبر فيهما العدل لتحصيل سبب البناء[[٢]].",
     "en": "in this chapter, by way of assimilating it to the [nouns] ending in rāʾ among the feminine proper names, such as “Ḥaḍāri” and “Ṭamāri,” for these two are indeclinable, and there is in them nothing but two causes: proper-name status and femininity; yet these two causes do not necessitate indeclinability, so deviation (ʿadl) was taken into account in them in order to secure a cause of indeclinability."},
    {"type": "matn",
     "ar": "فلما اعتبر فيهما العدل لتحصيل سبب البناء، اعتبر فيما عداهما مما جعلوه معربا غير منصرف أيضا، حملا على نظائره مع عدم الاحتياج إليه، لتحقق السببين لمنع الصرف: العلمية والتأنيث.",
     "en": "So when deviation was taken into account in these two in order to secure a cause of indeclinability, it was also taken into account in what lies beyond them among those [nouns] which they made declinable but diptote — by way of assimilation to its analogues, even without any need for it, because the two causes for the denial of full inflection are [already] realized: proper-name status and femininity."},
    {"type": "matn",
     "ar": "فاعتبار العدل فيه إنما هو للحمل على نظائره، لا لتحصيل سبب منع الصرف، ولهذا يقال: «ذكر باب قطام» ههنا ليس في محله؛ لأن الكلام فيما قدر فيه العدل، لتحصيل سبب منع الصرف.",
     "en": "So the taking of deviation into account in it is only for the sake of assimilation to its analogues, not to secure a cause of denying full inflection; and for this reason it is said that “the mention of the category of Qaṭāmi” here is out of place, since the discussion concerns that in which deviation is presumed in order to secure a cause of denying full inflection."},
    {"type": "matn",
     "ar": "وإنما قال: «في بني تميم»؛ لأن الحجازيين يبنونه، فلا يكون مما نحن فيه.",
     "en": "He said only “among Banū Tamīm” because the Ḥijāzīs make it indeclinable, so it would not be of the kind we are dealing with."},
    {"type": "matn",
     "ar": "والمراد من بني تميم أكثرهم، فإن الأقلين منهم لم يجعلوا ذوات الراء مبنية، بل جعلوها غير منصرف، فلا حاجة إلى اعتبار العدل فيها، لتحصيل سبب البناء، وحمل ما عداها عليها.",
     "en": "By “Banū Tamīm” the majority of them is meant, for the minority among them did not make the [nouns] ending in rāʾ indeclinable, but rather made them diptote; so there is no need to take deviation into account in them in order to secure a cause of indeclinability, nor to assimilate the rest to them."},

    # ---------------- Section heading printed on the page ----------------
    {"type": "section", "ar": "[الوصف]",
     "en": "The Adjectival Quality (al-Waṣf)"},

    {"type": "matn",
     "ar": "(الوصف[[٣]]) وهو كون الاسم دالا على ذات مبهمة[[٤]] مأخوذة مع بعض صفاتها،",
     "en": "(The adjectival quality — al-waṣf): it is the noun’s signifying an indeterminate essence taken together with some of its attributes,"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه أنه لو أريد أنه ليس فيهما شيء إلا السببان، فهو ظاهر المنع، وإن أريد أنه ليس فيهما موجب بناء إلا سببان، ففيه أنهما ليسا موجبين للبناء، وفيهما وزن فعال، وهو يوجب البناء.",
     "en": "The objection to it is: if it is meant that there is nothing in them but the two causes, that is evidently deniable; and if it is meant that there is in them no necessitator of indeclinability except the two causes, the objection is that the two are not necessitators of indeclinability, while there is in them the pattern faʿāli, and it does necessitate indeclinability."},
    {"type": "pair",
     "ar": "فالصواب: وليس فيهما إلا الوزن، والوزن لا يستقل في إيجاب البناء.",
     "en": "So the correct [statement] is: there is in them nothing but the pattern, and the pattern does not on its own necessitate indeclinability."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو العدل والوزن لا المجموع.",
     "en": "That is, [the cause is] the deviation together with the pattern, not the combination [alone]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "اللام للعهد الخارجي. والوصف يطلق على معنيين: أحدهما: الصفة، وهو الاسم الدال على ذات مبهمة إلى آخره.",
     "en": "The lām is for external definite reference. “Al-waṣf” is applied to two meanings: the first is the adjective (al-ṣifa), namely the noun signifying an indeterminate essence, and so on [to the end of the definition]."},
    {"type": "pair",
     "ar": "وثانيهما: ما ذكره الشارح من المعنى المصدري.",
     "en": "The second is what the commentator mentioned, namely the verbal-noun (maṣdarī) sense."},
    {"type": "pair",
     "ar": "وهذا هو علة منع الصرف؛ لأنها حالة في الاسم الغير المنصرف لا نفس الصفة؛ لأنها عين الاسم وذاته، وهي ليست بعلة، فبهذا ظهر وجه تفسير الشارح بكون الاسم إلى آخره.",
     "en": "And this [second sense] is the cause of denying full inflection, because it is a state present in the diptote noun, not the adjective itself — since the adjective is the very noun and its essence, and it is not a cause. By this the point of the commentator’s explaining it as “the noun’s being …” and so on becomes clear."},
    {"type": "pair",
     "ar": "قوله: (الوصف) لم يعرف المصنف في هذا الباب إلا العدل؛ لأن غيره إما معرف في هذا الكتاب في محله، وإما مستغن عن البيان، لشهرته فيما بين المحصلين أو عرف العدل لعدوله فيه عن تعريف السلف، بخلاف الأسباب الباقية حيث لم يعدل فيها.",
     "en": "His words “al-waṣf”: the author defined nothing in this chapter except deviation, because [everything] besides it is either defined in this book in its [proper] place, or dispensed with definition because of its being well known among the accomplished [scholars]; or he defined deviation because in it he departed from the definition of the predecessors, unlike the remaining causes, in which he did not depart [from them]."},
    {"type": "pair",
     "ar": "والشارح فسر من الأسباب الباقية ما لم يفسره المصنف في محله.",
     "en": "The commentator, of the remaining causes, expounded that which the author did not expound in its [proper] place."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لم يتعين إلا ببعض الصفات التي أخذت معها. وفيه نظر؛ لأن الأوصاف المأخوذة من صفات مقيسة إلى ذوات معينة لا تدل على ذات مبهمة، بل تدل على تلك الذوات المعينة، فإن الفياض المأخوذ",
     "en": "It is determinate only through some of the attributes taken together with it. But this is questionable, for adjectives derived from attributes measured against particular essences do not signify an indeterminate essence, but rather signify those particular essences; for “al-fayyāḍ” (the abundantly overflowing), derived"},
]
