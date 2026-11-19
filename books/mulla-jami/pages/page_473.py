# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 473 (printed ٤٧٢)."""

PAGE_NUMBER = 473
PRINTED_PAGE = "٤٧٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… ولأنه لما كان فيما هو» at the foot of PDF p. 472.
    {"type": "matn",
     "ar": "الأصل فيه، وهو استعماله بـ«من» لا يثنى ولا يجمع ولا يؤنث بعد مشابهته عن اسم الفاعل، فلا يعمل لمشابهته أيضا.",
     "en": "…its basic case, namely its use with “min”, not made dual, plural or feminine, its resemblance to the active participle (ism al-fāʿil) became remote, so it does not govern by virtue of resemblance either."},
    {"type": "matn",
     "ar": "(إلا إذا كان) اسم التفضيل (صفة) أي: وصفا سببيا[[١]] هو في اللفظ (لشيء) معتمدا عليه بأن يقع نعتا له، أو خبرا عنه، أو حالا",
     "en": "(Except when) the elative (is an attribute), that is, a causal (sababī) qualification, which in the wording is (of one thing), resting on it by occurring as its epithet (naʿt), its predicate, or a circumstantial,"},
    {"type": "matn",
     "ar": "(وهو في المعنى صفة لمسبب) مشترك[[٢]] بين ذلك الشيء وبين غيره[[٣]]",
     "en": "(while in meaning it is an attribute of something connected to it [musabbab]), shared between that thing and something else,"},
    {"type": "matn",
     "ar": "(مفضل) ذلك المسبب (باعتبار[[٤]] الأول) أي: باعتبار تقييده بذلك الشيء الذي اعتبر أولا (على نفسه) أي: على نفس ذلك المسبب",
     "en": "(preferred), that musabbab, (in regard to the first), that is, in regard to its being restricted to that thing which was considered first, (over itself), that is, over that same musabbab"},
    {"type": "matn",
     "ar": "(باعتبار غيره) أي: باعتبار تقييده بغيره أي: غير ذلك الأول، فيكون باعتبار الأول مفضلا، وباعتبار الثاني مفضلا عليه",
     "en": "(in regard to something else), that is, in regard to its being restricted to something else, other than that first; so in regard to the first it is the one preferred, and in regard to the second the one surpassed,"},
    {"type": "matn",
     "ar": "(منفيا) خبر بعد خبر لـ«كان»، أو حال عن اسمه، أو صفة لمصدر محذوف أي: تفضيلا منفيا",
     "en": "(negated) — a second predicate of “kāna”, or a circumstantial from its subject, or the qualifier of an elided maṣdar, that is, “a negated preference” —"},
    {"type": "matn",
     "ar": "(مثل: «ما رأيت رجلا أحسن في عينه الكحل منه في عين زيد»).",
     "en": "(as in “I have not seen a man in whose eye kohl is more beautiful than it is in the eye of Zayd”)."},
    {"type": "matn",
     "ar": "فـ«رجلا» هو الشيء الذي ثبت له اسم التفضيل في اللفظ.",
     "en": "Thus “a man” is the thing to which the elative is attributed in the wording,"},
    {"type": "matn",
     "ar": "و«الكحل» مسبب مشترك بين عين الرجل وبين عين زيد مفضل باعتبار عين الرجل، مفضل عليه باعتبار عين زيد،",
     "en": "and “kohl” is the musabbab shared between the man’s eye and Zayd’s eye: preferred in regard to the man’s eye, and surpassed in regard to Zayd’s eye."},
    {"type": "matn",
     "ar": "وإنما اشترط أن يكون في اللفظ ثابتا لشيء، وفي المعنى لمسببه ليحصل له صاحب يعتمد عليه،",
     "en": "It was stipulated that it be attributed in the wording to a thing and in meaning to that thing’s musabbab only so that it should have a possessor to rest on,"},
    {"type": "matn",
     "ar": "ويحصل[[٥]] له مظهر تعلق بذلك الصاحب حتى يتيسر عمله فيه كالصفة المشبهة[[٦]]؛ لانحطاط رتبتهما عن رتبة اسم",
     "en": "and that it should have an explicit noun connected to that possessor, so that its government in it becomes feasible, like the resembling adjective (al-ṣifa al-mushabbaha), since the rank of both falls below the rank of the…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بيان لحاصل قوله: صفة، وهو في المعنى سبب، وإشارة إلى أن المجموع شرط واحد، فشروط العمل ثلاثة كما صرحوا به،",
     "en": "An explanation of the upshot of his words “an attribute, while in meaning [of] a sabab”, and an indication that the whole is one condition; so the conditions of government are three, as they stated explicitly."},
    {"type": "pair",
     "ar": "ولم يقل صفة سببية؛ إذ الاصطلاح الوصف السببي وغير السببي، كما في المفتاح والتلخيص لا الصفة السببية وغير السببية.",
     "en": "He did not say “a causal attribute (ṣifa sababiyya)”, since the technical usage is “causal qualification (waṣf sababī)” and “non-causal”, as in al-Miftāḥ and al-Talkhīṣ, not “causal attribute” and “non-causal”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «نقل عنه المشهور» (one might expect «عدل عن المشهور»); transcribed as printed, translated by sense.
    {"type": "pair",
     "ar": "ولذا لم يقل لمسببه بالإضافة الموهمة للاختصاص. نقل عنه المشهور في اصطلاحهم أن يطلق على المتعلق اسم السبب دون المسبب، ولا مناقشة فيه.",
     "en": "For this reason he did not say “of its musabbab”, with an annexation suggesting exclusivity. He departed from what is well known in their usage, namely that the name sabab, not musabbab, is applied to the connected [noun] (mutaʿalliq); and there is no quarrel over terms."},
    {"type": "pair",
     "ar": "ولعله سماه مسببا؛ لأن الكحل في هذا المثال مسبب عين الرجل وعين زيد؛ لأن عينهما سبب الكحل وهو مسبب لهما.",
     "en": "Perhaps he called it musabbab because kohl in this example is the musabbab of the man’s eye and Zayd’s eye, since their eye is the cause (sabab) of the kohl and it is a musabbab of them."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "على ما حمل قول المصنف يخرج عنه نحو: «ما رأيت زيدا أحسن في عينه الكحل اليوم منه في عينه أمس»",
     "en": "On the way the author’s words were taken, there would be excluded from it a case like “I have not seen Zayd with kohl more beautiful in his eye today than it is in his eye yesterday”;"},
    {"type": "pair",
     "ar": "فينبغي أن يطلق المسبب ولا يفسر غيره في قوله: باعتبار غيره بغير الأول، بل يفسر بغير تقييده السابق بالأول.",
     "en": "so musabbab should be left unrestricted, and “something else” in his words “in regard to something else” should not be explained as “other than the first”, but as “other than its earlier restriction to the first”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: بالنظر يقال: اعتبرت الشيء إذا نظرت إليه ورغبت في حاله.",
     "en": "That is, by consideration; one says “iʿtabartu al-shayʾ” when you looked at a thing and attended to its state."},
    {"type": "pair",
     "ar": "وهو حال من الضمير المرفوع في المفضل، أي: متلبسا به. وكذا الثاني حال من نفسه،",
     "en": "It is a circumstantial from the nominative pronoun in “mufaḍḍal”, that is, “being attended by it”; likewise the second is a circumstantial from “nafsihi”;"},
    {"type": "pair",
     "ar": "وليسا متعلقين بمفضل حتى يلزم تعدية شبه الفعل بحرفي جر متفقين لفظا ومعنى، وهو خلاف ما اتفقوا عليه، كذا في الرضي.",
     "en": "they are not attached to “mufaḍḍal”, for then it would follow that a verb-like word is made transitive by two prepositions identical in wording and meaning, which is contrary to what they agreed upon; so in al-Raḍī."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بالنصب عطف على يحصل الأول، وهما متعلقان بأن يكون على ترتيب اللف والنشر.",
     "en": "With the subjunctive, coordinated to the first “yaḥṣula”; both are attached to “that it be”, in the order of convolution and unfolding (al-laff wa-l-nashr)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فإنه أيضا لا بد لعمله من موصوف في اللفظ، ومتعلق مسبب لذلك الموصوف ليعمل فيه.",
     "en": "For it too, in order to govern, requires a qualified noun in the wording and a connected musabbab of that qualified noun in which to govern."},
]
