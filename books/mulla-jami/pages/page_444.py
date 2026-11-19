# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 444 (printed ٤٤٣)."""

PAGE_NUMBER = 444
PRINTED_PAGE = "٤٤٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… من أنه قد تقلب» at the foot of PDF p. 443 (mid-sentence).
    {"type": "matn",
     "ar": "المبدلة من أصل ياء[[١]]، وهذا أعم[[٢]] من أن يكون هذا الأصل واوا أو ياء.",
     "en": "…[the hamza] substituted from an original [letter] into a yāʾ; and this is more general than that original being a wāw or a yāʾ."},
    {"type": "matn",
     "ar": "(ويحذف نونه) أي: نون التثنية (للإضافة) أي: لأجل الإضافة؛",
     "en": "(And its nūn is dropped), that is, the nūn of the dual, (for annexation), that is, because of annexation (iḍāfa);"},
    {"type": "matn",
     "ar": "إذ النون لقيامها مقام التنوين يوجب تمام الكلمة وانقطاعها، والإضافة توجب الاتصال والامتزاج، فيتنافيان.",
     "en": "for the nūn, because it stands in the place of the tanwīn, entails the completion of the word and its being cut off, while annexation entails connection and blending; so the two are incompatible."},
    {"type": "matn",
     "ar": "(وحذفت تاء التأنيث) التي قياسها ألا يحذف عن آخر المثنى[[٣]] كـ«شجرتان، وثمرتان» (في «خصيان وأليان») على خلاف القياس،",
     "en": "(And the tāʾ of the feminine was dropped), whose rule is that it is not dropped from the end of the dual, as in “shajaratān” (two trees) and “thamaratān” (two fruits), (in “khuṣyān” and “alyān”), contrary to the rule,"},
    {"type": "matn",
     "ar": "مع جواز إثباتها فيهما على القياس اتفاقا،",
     "en": "while keeping it in both, according to the rule, is permitted by agreement."},
    {"type": "matn",
     "ar": "ووجه حذفها فيهما أن كل واحد من «الخصيتين والأليتين» لما اشتد اتصالها[[٤]] بالأخرى بحيث لا يمكن الانتفاع بها[[٥]] بدونها صارتا[[٦]] بمنزلة مفرد، وتاء التأنيث لا يقع في حشوه.",
     "en": "The reason for dropping it in both is that, since each one of “the two testicles” and “the two buttocks” is so closely joined to the other that no use can be made of it without the other, the two became like a single word, and the tāʾ of the feminine does not occur in the middle of a word."},
    {"type": "matn",
     "ar": "وقيل: «خصي وألي» مستعملان، وهما لغتان في «خصية وألية»؛ وإن كانتا أقل استعمالا منهما.",
     "en": "It has been said that “khuṣy” and “aly” are in use, and they are two dialectal variants of “khuṣya” and “alya”, though less used than them."},
    {"type": "matn",
     "ar": "ولما كان حذف النون قاعدة مستمرة، أتى في بيانه بالفعل المضارع المفيد للاستمرار،",
     "en": "Since dropping the nūn is a constant rule, he used in stating it the imperfect verb, which conveys continuity;"},
    {"type": "matn",
     "ar": "بخلاف حذف تاء التأنيث؛ إذ ليس له قاعدة، بل وقعت على خلاف القياس في مادة مخصوصة، فلهذا أتى في بيانه بالفعل الماضي.",
     "en": "unlike dropping the tāʾ of the feminine, for it has no rule, but has occurred contrary to the rule in a particular word; for this reason he used in stating it the perfect verb."},

    {"type": "section", "ar": "[المجموع]",
     "en": "The Plural"},

    {"type": "matn",
     "ar": "(المجموع: ما دل) أي: اسم[[٧]] دل (على) جملة (آحاد مقصودة) أي: يتعلق بها",
     "en": "(The plural (majmūʿ) is what indicates), that is, a noun that indicates, (units intended), as a group, that is, [units] to which…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وقد يقال: ولا يقاس عليه خلافا للكسائي، فلا ينفع في بيان قاعدة هذا القلب، بل يكون من الشواذ الخارجة عن القاعدة.",
     "en": "It may be said: and no analogy is drawn from it, contrary to al-Kisāʾī; so it is of no use in stating the rule of this conversion, but rather belongs to the anomalies that fall outside the rule."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فلا يدل على تخصيص جواز القلب بالياء في رداء فضلا عن أن يكون مشهورا.",
     "en": "So it does not indicate that the permissibility of conversion into a yāʾ is specific to “ridāʾ”, let alone that it is well known."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: printed «أخر» (without madda); read as «آخر» (“end”).
    {"type": "pair",
     "ar": "أي: أخر مفرد المثنى، فلا ينافي قوله: وتاء التأنيث، لا يقع في حشوه، فالأولى أن يقول: ألا يحذف عن المثنى.",
     "en": "That is, the end of the singular of the dual; so it does not conflict with his words “and the tāʾ of the feminine does not occur in the middle of a word”. It would be better for him to say: “that it is not dropped from the dual”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: اتصال كل واحدة بالأخرى.",
     "en": "That is, the joining of each one to the other."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: بكل واحدة بدونها أي: بدون الأخرى.",
     "en": "That is, of each one without it, that is, without the other."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: الخصيتان، ففي العبارة استخدام،",
     "en": "That is, the two testicles; so in the wording there is istikhdām (using a word in one sense and its pronoun in another),"},
    {"type": "pair",
     "ar": "فإن المراد من لفظة الخصيتين في قوله: كل واحدة من الخصيتين معناها، ومن ضمير صارتا لفظة الخصيتين.",
     "en": "for what is meant by the word “the two testicles” in his words “each one of the two testicles” is its meaning, while what is meant by the pronoun of “ṣāratā” (the two became) is the word “the two testicles”."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إشارة إلى أن غير الاسم لا يكون مجموعا، والفعل إنما يثنى ويجمع باعتبار فاعله.",
     "en": "[This is] an indication that what is not a noun is not pluralized; the verb is made dual and plural only with respect to its agent."},
    {"type": "pair",
     "ar": "ولا يتوهم خروج مسلمين ومسلمات لعدم كونهما كلمة لما يجيء في كلام الشارح قدس سره أن الواو والنون والألف",
     "en": "One should not imagine that “muslimīn” and “muslimāt” are excluded because they are not a single word, because of what comes in the commentator’s words, may his secret be sanctified, that the wāw and nūn, and the alif…"},
]
