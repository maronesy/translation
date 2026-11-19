# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 70 (printed ٦٩)."""

PAGE_NUMBER = 70
PRINTED_PAGE = "٦٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "من فحوى الكلام، فإنه بعيد[[١]] عن الفهم غاية البعد، فاللام فيه متعلق بقوله: «اختلف»، يعني: اختلف آخره.",
     "en": "from the tenor of the discourse — for it is exceedingly remote from comprehension — then the lām in it is governed by his words “ukhtulifa” (“is made to differ”); that is, “its ending is made to differ.”"},
    {"type": "matn",
     "ar": "(ليدل) الاختلاف، أو ما به الاختلاف (على المعاني) يعني: الفاعلية[[٢]]، والمفعولية، والإضافة (المعتورة) على صيغة اسم الفاعل[[٣]] (عليه) أي: على المعرب، متعلق بـ«معتورة» على تضمين معنى مثل معنى الورود والاستيلاء.",
     "en": "(li-yadulla — “that it may indicate”) — [namely] the difference, or that by which the difference [comes about] — (ʿalā al-maʿānī — “the meanings”) — that is, agency (fāʿiliyya), object-hood (mafʿūliyya), and annexation (iḍāfa) — (al-muʿtawira — “those that alternate”) — [read] according to the form of the active participle (ism al-fāʿil) — (ʿalayhi — “over it”) — that is, over the declinable noun; [it is] governed by “muʿtawira,” on the basis of the implication of a meaning like that of “coming upon” (wurūd) and “taking hold” (istīlāʾ)."},
    {"type": "matn",
     "ar": "يقال: اعتوروا الشيء، وتعاوروه، إذا تداولوه، أي: أخذه جماعة واحدا بعد واحد على سبيل المناوبة والبدلية، لا على سبيل الاجتماع.",
     "en": "One says: “iʿtawarū al-shayʾa” and “taʿāwarūhu” when they take it in turns — that is, a group takes it, one after another, by way of alternation and mutual substitution (badaliyya), not by way of [simultaneous] togetherness."},
    {"type": "matn",
     "ar": "فإذا تداولت المعاني المقتضية للإعراب على المعرب متعاقبة متناوبة غير مجتمعة لتضادها، ينبغي أن يكون علاماتها[[٤]] أيضا كذلك[[٥]]، فوقع بسببها اختلاف في آخر المعرب.",
     "en": "So when the meanings that require inflection succeed one another over the declinable noun — in succession and alternation, not conjoined [all at once] on account of their mutual opposition — then their markers too ought to be likewise; hence, on their account, a difference occurs in the ending of the declinable noun."},
    {"type": "matn",
     "ar": "فوضع أصل الإعراب للدلالة على تلك المعاني، ووضع بحيث يختلف به[[٦]] آخر المعرب، لاختلاف تلك المعاني.",
     "en": "Thus the root of inflection was instituted to indicate those meanings, and it was instituted such that by it the ending of the declinable noun would differ, in accordance with the difference of those meanings."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إذ لا نظر إلى وضعه له لا قصدا ولا تبعا.",
     "en": "Since no regard is had to its being instituted for it, neither by primary intent nor by way of dependency (tabaʿan)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: المعاني المعتورة هي كون الاسم عمدة وفضلة بلا واسطة حرف الجر أو بواسطته.",
     "en": "Al-Shaykh al-Raḍī said: The alternating meanings are the noun’s being a principal element (ʿumda) or a surplus element (faḍla), whether without the mediation of a genitive particle or through its mediation."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا على صيغة اسم المفعول كما توهم بعضهم حتى يكون المعنى: أن الأسماء تأخذها على سبيل المناوبة.",
     "en": "Not according to the form of the passive participle (ism al-mafʿūl), as some have wrongly supposed, such that the meaning would be: that the nouns take them by way of alternation."},
    {"type": "pair",
     "ar": "وذلك لأن توصيف المعاني بهذا الوصف ليس إلا لأن المعاني باعتبار هذا الوصف تقتضي الإعراب،",
     "en": "That is because the qualifying of the meanings by this description is only because the meanings, in view of this description, require inflection;"},
    {"type": "pair",
     "ar": "والوصف الذي به اقتضاء الإعراب هو كون أحدها طاريا أبدا لا كون أحدها مطروا عليه، فإذن تعين الكسر، وتوافقه أيضا الرواية.",
     "en": "and the description by which inflection is required is the fact that one of them is ever supervening (ṭārin), not the fact that one of them is that upon which [another] supervenes (maṭrūw ʿalayhi); hence the kasra [reading of “muʿtawira” as active participle] is determined, and the transmitted reading (riwāya) also agrees with it."},
    {"type": "pair",
     "ar": "ويرشدك إلى ما ذكرناه ما قاله الشيخ الرضي: وهو أن المعاني في الكلمة قد يطرأ بعضها على بعض، ولا بد للطاري من علامة مميزة له من المطرو عليه.",
     "en": "And what guides you to what we have mentioned is what al-Shaykh al-Raḍī said: namely, that the meanings in a word — some of them may supervene upon others, so the supervening [element] must have a marker distinguishing it from that upon which it supervenes."},
    {"type": "pair",
     "ar": "ومن ثم احتاج المجاز إلى قرينة، والطاري الغير اللازم لا يلزم أن يطلب له أخف العلامات، بل قد يغير له صيغة الكلمة كما في التصغير والتكسير.",
     "en": "Hence the figurative usage (majāz) came to need a contextual indicator (qarīna); and as for the non-necessary supervening [element], it is not necessary that the lightest of markers be sought for it — rather, the form of the word may be changed for it, as in the diminutive (taṣghīr) and the broken plural (taksīr)."},
    {"type": "pair",
     "ar": "وقد يجتلب له حرف كما في المثنى، وقد يكون كلمة مستقلة كالمضاف إليه الدال على معنى في المضاف،",
     "en": "A letter may be adjoined for it, as in the dual; and it may be an independent word, like the term to which annexation is made (al-muḍāf ilayhi), which indicates a meaning in the annexed term (al-muḍāf);"},
    {"type": "pair",
     "ar": "وإن كان طريان المعنى لازما للكلمة، فإن كان الطارئ واحدا ككون الفعل عمدة فيما تركب منه ومن غيره فلا حاجة إلى العلامة؛ لأنها تطلب للملتبس بغيره.",
     "en": "And if the supervening of the meaning is necessary to the word: if the supervening [element] is a single one — like the verb’s being a principal element in that which is composed of it and of something else — then there is no need for the marker, because it is sought only for that which is liable to confusion with something else."},
    {"type": "pair",
     "ar": "وإن كان الطارئ اللازم أحد الشيئين أو الأشياء، فاللائق بالحكمة أن يطلب له أخف علامة تمكن لازمة، ومثل هذا المعنى إنما يكون في الاسم،",
     "en": "And if the necessary supervening [element] is one of two things, or of [several] things, then what befits wisdom is that the lightest marker that can be a permanent [concomitant] be sought for it; and a meaning of this sort occurs only in the noun,"},
    {"type": "pair",
     "ar": "فجعلت علامته أبعاض حروف المد التي هي أخف الحروف، وجعلت في بعض الأسماء حروف المد التي لم تجلب.",
     "en": "so the parts of the letters of prolongation (ḥurūf al-madd), which are the lightest of letters, were made its marker; and in some nouns the letters of prolongation that were not adjoined were made [its marker]."},
    {"type": "pair",
     "ar": "ومن هذا التقرير يظهر وجه ما يقال: إن الأصل في الأسماء الإعراب، وفي الأفعال والحروف البناء.",
     "en": "And from this exposition there becomes evident the basis of what is said: that the original state (aṣl) in nouns is inflection (iʿrāb), and in verbs and particles [it is] indeclinability (bināʾ)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وهي: الرفع والنصب والجر.",
     "en": "They are: the nominative (rafʿ), the accusative (naṣb), and the genitive (jarr)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: بسبب المعاني المختلفة أصلا.",
     "en": "That is: on account of the differing meanings in the first place."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: بأصل الإعراب.",
     "en": "That is: by the root of inflection."},
]
