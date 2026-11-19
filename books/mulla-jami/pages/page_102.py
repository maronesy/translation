# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 102 (printed ١٠١)."""

PAGE_NUMBER = 102
PRINTED_PAGE = "١٠١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "سببية منع الصرف (العلمية) أي: علمية الاسم المؤنث، ليصير التأنيث لازما[[١]]؛ لأن الأعلام محفوظة عن التصرف بقدر الإمكان[[٢]]،",
     "en": "…[its] being a cause of preventing full declension is (proper-namehood, al-ʿalamiyya) — that is: the proper-namehood of the feminine noun — so that its feminization may become permanent[[١]]; for proper names are guarded from [morphological] alteration as far as possible[[٢]],"},
    {"type": "matn",
     "ar": "ولأن العلمية وضع ثان، وكل حرف وضعت الكلمة عليه لا ينفك عن الكلمة[[٣]].",
     "en": "and because proper-namehood is a second coining, and every letter upon which the word is [re]coined does not become separable from the word[[٣]]."},
    {"type": "matn",
     "ar": "(و) التأنيث (المعنوي[[٤]] كذلك) أي: كالتأنيث اللفظي بالتاء[[٥]] في اشتراط العلمية فيه،",
     "en": "(And) the (semantic feminization[[٤]] is likewise) — that is: like the morphological feminization by the tāʾ[[٥]] in that proper-namehood is stipulated for it,"},
    {"type": "matn",
     "ar": "إلا أن بينهما فرقا، فإنها في التأنيث اللفظي بالتاء شرط لوجوب منع الصرف، وفي المعنوي شرط لجوازه.",
     "en": "except that there is a difference between the two: in morphological feminization by the tāʾ it (proper-namehood) is a condition for the obligatoriness of preventing declension, whereas in the semantic [feminization] it is a condition for its permissibility."},
    {"type": "matn",
     "ar": "ولا بد في وجوبه من شرط آخر[[٦]] كما أشار إليه بقوله: (وشرط تحتم تأثيره[[٧]])",
     "en": "And its obligatoriness requires a further condition[[٦]], as he indicated by his words: (“And the condition for the necessitation of its effect”[[٧]])"},
    {"type": "matn",
     "ar": "أي: شرط وجوب تأثير التأنيث المعنوي في منع الصرف أحد الأمور الثلاثة:",
     "en": "that is: the condition for the obligatoriness of the semantic feminization's effect upon the prevention of declension is one of three things:"},
    {"type": "matn",
     "ar": "١-(زيادة على الثلاثة) أي: زيادة حروف الكلمة على ثلاثة، مثل: «زينب».",
     "en": "1 — (“exceeding three”) — that is: the word's letters exceeding three, like “Zaynab.”"},
    {"type": "matn",
     "ar": "٢-(أو تحرك) الحرف (الأوسط[[٨]]) من حروفها الثلاثة، مثل: «سقر».",
     "en": "2 — (“or the vowelling of”) the (middle[[٨]]) letter of its three letters, like “Saqar.”"},
    {"type": "matn",
     "ar": "٣-(أو العجمة) مثل: «ماه وجور».",
     "en": "3 — (“or non-Arab origin,” al-ʿujma) — like “Māh” and “Jūr.”"},
    {"type": "matn",
     "ar": "وإنما اشترط في وجوب تأثير التأنيث المعنوي[[٩]] أحد الأمور الثلاثة، ليخرج",
     "en": "One of these three things was stipulated for the obligatoriness of the semantic feminization's effect[[٩]] only in order to exclude"},  # continues on the next page

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إذ التاء التي للتأنيث غير لازمة للكلمة، بل يؤتى بها عند إرادة الذات المؤنث.",
     "en": "Since the tāʾ that marks feminization is not permanent to the word, but is rather brought in when the feminine entity is intended."},
    {"type": "pair",
     "ar": "وأما التاء التي هي جزء الكلمة كتاء حجارة وتجارة، فهي فرع تاء التأنيث في باب منع الصرف، فشرطه العلمية في الاسم المشتمل عليها أيضا بتبعية تاء التأنيث، وإن كانت هي لازمة للكلمة.",
     "en": "As for the tāʾ that is [itself] part of the word — like the tāʾ of “ḥijāra” (stones) and “tijāra” (trade) — it is a subsidiary of the feminine tāʾ in the chapter of preventing declension; so its condition, [namely] proper-namehood, [applies] to the noun containing it as well, by way of its following the feminine tāʾ, even though it (that tāʾ) is permanent to the word."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إشارة إلى أنه قد يتصرف في الأعلام أيضا بالترخيم ونحوه.",
     "en": "An indication that proper names too may sometimes undergo alteration — by apocopation (tarkhīm) and the like."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بقدر الإمكان.",
     "en": "That is: as far as possible."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: ما يكون تاؤه مقدرة، ولا مجال لتقدير الألف للزومها.",
     "en": "That is: that whose tāʾ is [merely] implicit; and there is no room to posit the alif [here], because of its permanence."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: لأن المقدر عندهم أضعف من الظاهر، وشرط الظاهر العلمية.",
     "en": "It has been said: because, in their view, the implicit is weaker than the overt, and the condition of the overt [feminine marker] is proper-namehood."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: أشار إلى ما ذكره من الأمرين، وهو أن العلمية في المعنوي شرط الجواز، وأحد الأمور هو شرط الوجوب.",
     "en": "That is: he alluded to the two matters he mentioned — namely that, in the semantic [feminization], proper-namehood is the condition of permissibility, while one of the [three] things is the condition of obligatoriness."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: مع العلمية أحد الأمور الثلاثة. فعبارة المصنف قاصرة. ولا يبعد أن يجعل الضمير للمعنوي وجد فيه شرط العلمية.",
     "en": "That is: [what is required is] one of the three things together with proper-namehood; so the author's wording falls short. Yet it is not far-fetched to take the pronoun as referring to the semantic [feminization] in which the condition of proper-namehood is already present."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "جعل الأوسط عبارة عن أوسط الثلاثة المذكورة في قوله: زيادة على الثلاثة، وحينئذ لزم أن يكون لتحرك الأوسط شرط الوجوب في الثلاثي.",
     "en": "He took “the middle [letter]” to mean the middle of the three mentioned in his words “exceeding three”; on this reckoning it would follow that the vowelling of the middle [letter] is the condition of obligatoriness [only] in the triliteral."},
    {"type": "pair",
     "ar": "وعلى هذا القياس تكون العجمة شرط الوجوب في الساكن الأوسط منه. والأحسن أن تحرك الأوسط عبارة عن تحرك أوسط الكلمة ثلاثيا كان أو خماسيا، فإذا سمي بإبرهم من لغات إبراهيم مؤنث يجتمع فيه الشرائط الثلاثة للوجوب.",
     "en": "By the same analogy, non-Arab origin would be the condition of obligatoriness in that which has a quiescent middle [letter]. The better [view] is that “the vowelling of the middle [letter]” means the vowelling of the middle of the word, whether triliteral or quinqueliteral; so that if a feminine [entity] is named with “Ibrahim” — one of the [variant] forms of “Ibrāhīm” — all three conditions for obligatoriness are combined in it."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "وإنما لم يجعل الأمور الثلاثة شرط تحتم تأثير العلمية؛ لأن العلمية تجتمع مع أسباب أخر، وتؤثر من غير اشتراط هذه الأمور.",
     "en": "The three things were not made a condition for the necessitation of proper-namehood's effect only because proper-namehood combines with other causes and has effect without these things being stipulated."},
]
