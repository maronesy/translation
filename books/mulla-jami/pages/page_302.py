# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 302 (printed ٣٠١)."""

PAGE_NUMBER = 302
PRINTED_PAGE = "٣٠١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the list of conditions after «(وإذا زيدت «إن» مع «ما»)» on PDF p. 301.
    {"type": "matn",
     "ar": "(أو انتقض النفي بـ«إلا») نحو: «ما زيد إلا قائم».",
     "en": "…(or the negation is cancelled by “illā”), as in “mā Zaydun illā qāʾimun” (Zayd is nothing but standing),"},
    {"type": "matn",
     "ar": "(أو تقدم الخبر) على الاسم نحو: «ما قائم زيد» (بطل العمل) أي: عمل «ما» إذا كان مع واحد من هذه الأمور الثلاثة:",
     "en": "(or the predicate comes first) before the noun, as in “mā qāʾimun Zaydun” (standing is not Zayd), (the governing is annulled), that is, the governing of “mā,” when it occurs with any one of these three things."},
    {"type": "matn",
     "ar": "أما إذا زيدت «إن» فلأن «ما» عامل ضعيف[[١]] عمل لشبه «ليس»، فلما فصل بينها وبين معمولها لم يعمل.",
     "en": "When “in” is added, it is because “mā” is a weak governor that governs on account of its resemblance to “laysa”; so when it is separated from what it governs, it does not govern."},
    {"type": "matn",
     "ar": "وأما إذا انتقض النفي بـ«إلا»: فلأن عملها لمعنى النفي، فلما انتقض بطل العمل.",
     "en": "When the negation is cancelled by “illā,” it is because its governing is due to the meaning of negation; so when that is cancelled, the governing is annulled."},
    {"type": "matn",
     "ar": "وأما إذا تقدم الخبر: فلتغير الترتيب مع ضعفها في العمل.",
     "en": "When the predicate comes first, it is because of the change of order, together with its weakness in governing."},
    {"type": "matn",
     "ar": "(وإذا عطف عليه) أي: على خبرهما[[٢]] (بموجب) بكسر الجيم أي: بعاطف يفيد الإيجاب بعد النفي، وهو «بل ولكن»",
     "en": "(And when there is coordinated with it), that is, with their predicate, (by an affirming [particle]) (mūjib), with kasra on the jīm, that is, by a coordinating particle that conveys affirmation after negation, namely “bal” and “lākin,”"},
    {"type": "matn",
     "ar": "نحو: «ما زيد مقيما بل مسافر»، و«ما عمرو قائما لكن قاعد»",
     "en": "as in “mā Zaydun muqīman bal musāfirun” (Zayd is not staying; rather, he is travelling) and “mā ʿAmrun qāʾiman lākin qāʿidun” (ʿAmr is not standing, but sitting),"},
    {"type": "matn",
     "ar": "(فالرفع) أي: فحكم المعطوف الرفع[[٣]] لا غير؛ لكونهما بمنزلة «إلا» في نقض النفي.",
     "en": "(then the nominative [applies]), that is, the rule for the coordinated word is the nominative and nothing else, because these two are equivalent to “illā” in cancelling the negation."},

    {"type": "section", "ar": "[المجرورات]",
     "en": "The Genitives (al-Majrūrāt)"},

    {"type": "matn",
     "ar": "(المجرورات: هو ما اشتمل) أي: اسم اشتمل، ليخرج الحروف الأواخر التي هي محال الإعراب،",
     "en": "(The genitives: it is what contains), that is, a noun that contains, so as to exclude the final letters that are the loci of inflection (iʿrāb);"},
    {"type": "matn",
     "ar": "فإنه لا يطلق عليها المرفوعات والمنصوبات والمجرورات اصطلاحا؛ لأنها أقسام الاسم.",
     "en": "for the terms “nominatives,” “accusatives” and “genitives” are not applied to them technically, since these are divisions of the noun."},
    {"type": "matn",
     "ar": "(على علم المضاف إليه) أي: علامة المضاف إليه من حيث هو مضاف إليه -يعني الجر[[٤]]- سواء كان بالكسرة أو الفتحة أو الياء لفظا أو تقديرا[[٥]].",
     "en": "(the sign of the noun to which another is annexed) (al-muḍāf ilayhi), that is, the mark of the muḍāf ilayhi as such, meaning the genitive (jarr), whether by kasra, fatḥa or yāʾ, overtly or by supposition."},
    {"type": "matn",
     "ar": "وإنما قلنا: «من حيث هو مضاف إليه»؛ لأن الجر ليس علامة لذات المضاف",
     "en": "We said “as such” only because the genitive is not a sign of the muḍāf [ilayhi] in its essence…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو لكراهة إبراز «إن» النافية في معرض العامل.",
     "en": "Or because it is disliked to present the negative “in” in the guise of a governor."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "منصوبا كان أو مجرورا بالياء الزائدة.",
     "en": "Whether it is in the accusative or in the genitive with the redundant bāʾ."},
    # REVIEW: print reads «بالياء الزائدة» (yāʾ); the redundant particle with the predicate of mā is the bāʾ (ما زيد بقائم), so «بالباء» is probably meant; transcribed as printed, translated as bāʾ.

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حملا على المحل.",
     "en": "By construction on the [original] position (maḥall)."},
    {"type": "pair",
     "ar": "قال الشيخ عبد القاهر: هو خبر مبتدأ محذوف، أي: بل هو مسافر، ولكن هو قاعد.",
     "en": "Shaykh ʿAbd al-Qāhir [al-Jurjānī] said: it is the predicate of an elided subject, that is, “rather, he is travelling” and “but he is sitting.”"},
    {"type": "pair",
     "ar": "وقيل: عطف على سبيل التوهم؛ إذ كثيرا ما يقع خبر «ما» مرفوعا عند انعزالها عن العمل.",
     "en": "It has also been said: it is coordinated by way of supposition (tawahhum), since the predicate of “mā” often occurs in the nominative when it is removed from governing."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أراد بالجر الكسرة وما يقوم مقامها لا المعنى المصدري يوضحه قوله: سواء كان بالكسرة إلى آخره، فلا يتوهم الدور.",
     "en": "By “jarr” he meant the kasra and what stands in its place, not the verbal-noun sense; his words “whether by kasra…” make this clear, so no circularity is to be imagined."},
    # REVIEW: print reads «بين الجمع»; «بين الجميع» ("among all of them") seems meant; transcribed as printed.
    {"type": "pair",
     "ar": "وقوله: لفظا أو تقديرا متعلق بالكسرة والفتحة والياء أيضا نحو: غلام أخي القوم، ولم يقل: أو محلا؛ لأنه غير مشترك بين الجمع.",
     "en": "His words “overtly or by supposition” also relate to the kasra, the fatḥa and the yāʾ, as in “ghulāmu akhī l-qawmi” (the slave of the brother of the people); he did not say “or in position” because that is not common to all of them."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يقل: أو محلا؛ لأن المصنف ذاكر أقسام المعرب.",
     "en": "He did not say “or in position” because the author is enumerating the divisions of the declinable noun (muʿrab)."},
]
