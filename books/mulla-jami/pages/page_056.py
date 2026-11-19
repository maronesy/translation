# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 56 (printed ٥٥)."""

PAGE_NUMBER = 56
PRINTED_PAGE = "٥٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "…ما يدل على اعتبار كينونة المعنى في نفس الكلمة، ولهذا جزم المصنف هناك برجوعه إلى المعنى.",
     "en": "…what indicates that regard is had to the meaning’s being in the word itself; and for this reason the author decisively affirmed there that it [the pronoun] refers back to “the meaning.”"},
    {"type": "matn",
     "ar": "وبما سبق من التحقيق ظهر أنه لا يختل حد الاسم جمعا، ولا حد الحرف منعا بالأسماء اللازمة الإضافة، مثل: «ذو، وفوق، وتحت، وقدام، وخلف» إلى غير ذلك؛ لأن معانيها[[١]] مفهومات كلية مستقلة بالمفهومية[[٢]]، ملحوظة في حد ذاتها، لزمها تعقل متعلقاتها إجمالا[[٣]] وتبعا، من غير حاجة إلى ذكرها[[٤]].",
     "en": "From the verification (taḥqīq) already given it has become clear that the definition of the ism (noun) is not vitiated by non-comprehensiveness (jamʿan), nor the definition of the ḥarf (particle) by non-exclusiveness (manʿan), on account of the nouns that necessarily require annexation (iḍāfa) — such as “dhū, fawq, taḥt, quddām, khalf,” and the like — because their meanings are universal concepts independent in conceivability, regarded in their own right, such that the conception of their correlates attaches to them summarily and subordinately, without any need to mention them."},
    {"type": "matn",
     "ar": "لكن لما جرت العادة باستعمالها[[٥]] في مفهوماتها مضافة إلى متعلقات مخصوصة؛ لأنه لما كان الغرض من وضعها، لزم ذكرها، لفهم هذه الخصوصيات، لا لأجل فهم أصل المعنى، فهي دالة على معانيها معتبرة في حد نفسها لا في غيرها، فهي داخلة في حد الاسم لا في الحرف.",
     "en": "But since it has become customary to use them in their concepts as annexed to particular correlates — for since the purpose of coining them was the understanding of these particularities, mentioning them became necessary, not for the sake of understanding the basic meaning — they [therefore] signify their meanings as considered in their own right, not in something else; and so they fall under the definition of the ism, not that of the ḥarf."},
    {"type": "matn",
     "ar": "ولما كان الفعل دالا على معنى في نفسه باعتبار معناه التضمني، أعني: الحدث، وكان ذلك المعنى مقترنا بأحد الأزمنة الثلاثة في الفهم عن لفظ الفعل، أخرجه[[٦]] بقوله: (غير مقترن بأحد الأزمنة الثلاثة)[[٧]]، أي: غير مقترن مع أحد الأزمنة الثلاثة في الفهم عن لفظه الدال عليه.",
     "en": "And since the fiʿl (verb) signifies a meaning in itself by consideration of its connotative meaning — I mean the event (al-ḥadath) — and since that meaning is conjoined with one of the three times in the understanding derived from the wording of the verb, he excluded it by his words: “(not conjoined with any of the three times)” — that is: not conjoined with one of the three times in the understanding derived from its wording which signifies it."},
    {"type": "matn",
     "ar": "فهو[[٨]] صفة بعد صفة[[٩]] لـ«المعنى»[[١٠]].",
     "en": "So it is an adjective (ṣifa) after an adjective qualifying “the meaning” (al-maʿnā)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: معنى كل واحد من تلك الأسماء.",
     "en": "That is: the meaning of each one of those nouns."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يقال: لو كان كذلك لصح الإخبار عن فوق وتحت وقدام وخلف، أو الإخبار بها مع أنها لازمة الظرفية؛ لأنا نقول: المفهوم المستقل يقتضي صحة الحكم عليه أو به إذا أخذ في حد ذاته، ولا يقدح في استقلاله امتناع الحكم عليه أو به لما يعرضه، سواء كان ذلك العارض جزءا لمدلول ما يدل عليه ك«متى» أو خارجا عنه كالظروف المذكورة، فإن معنى الظرفية داخل في الأول خارج عن الثاني.",
     "en": "It should not be objected: were that so, it would be valid to predicate something of “fawq,” “taḥt,” “quddām,” and “khalf,” or to predicate by means of them, despite their necessarily being adverbial (lāzimat al-ẓarfiyya). For we say: an independent concept warrants the validity of predication upon it or by it when it is taken in its own right; and the impossibility of predicating upon it or by it does not impair its independence — [when that impossibility is] on account of something that accidentally attaches to it, whether that accident is a part of the signified of what signifies it, as in “matā” (when), or external to it, as in the adverbs mentioned; for the sense of adverbiality is internal to the first and external to the second."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "نصب على التمييز من نسبة اللزوم إلى فاعله، وهو التعقل.",
     "en": "[Ijmālan is] in the accusative as a specifier (tamyīz) derived from the attribution of the necessary-following to its agent, which is [the act of] conception (al-taʿaqqul)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: إلى ذكر متعلق كل واحد منها لكونها في الدلالة على معانيها مستقلة.",
     "en": "That is: to the mention of the correlate of each one of them, since they are independent in signifying their meanings."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: باستعمال كل واحد من تلك الأسماء.",
     "en": "That is: the use of each one of those nouns."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: أخرج المصنف الفعل.",
     "en": "That is: the author (al-muṣannif) excluded the verb."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "يعني زمانا أنت فيه، وزمانا قبله وزمانا بعده. وشهرة أمرها كفت مؤنة التفسير.",
     "en": "He means: a time in which you are, a time before it, and a time after it; and the notoriety of the matter has spared the trouble of explanation."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: قوله: غير مقترن بالجر.",
     "en": "That is: his words “ghayra muqtarinin” (not conjoined) are [to be read] in the genitive (bi-l-jarr)."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "وفي بعض النسخ: «وهو» بالواو، وهو الظاهر. وأما الفاء فهي للبيان؛ إذ التفريع غير مناسب. ثم هو مجرور على تقدير الوصفية. ويجوز نصبه بأن يكون حالا من المعنى، ورفعه بأن يكون خبر مبتدأ محذوف، أي: وهو غير مقترن بأحد الأزمنة الثلاثة، وإنما اختار الجر بالوصفية؛ لأن النصب على الحالية يحتاج إلى تكلف جعل المعنى مفعولا به، وحينئذ يحتاج إلى تقييد الدلالة بحال عدم الاقتران، والرفع على الخبرية يحتاج إلى ارتكاب الحذف.",
     "en": "In some copies it is “wa-huwa” with a wāw, which is the more apparent [reading]. As for the fāʾ, it is for [mere] explication, since [causal] subordination is not fitting here. Then it is in the genitive on the supposition of its being adjectival (waṣfiyya). It may also be put in the accusative, as being a ḥāl from “the meaning,” or in the nominative, as being the predicate of an omitted subject — that is: “and it is not conjoined with any of the three times.” He preferred the genitive by way of the adjectival [construction] only because the accusative as a ḥāl requires the strained assumption of making “the meaning” a direct object, and then requires restricting the signification to the state of non-conjunction; while the nominative as a predicate requires resorting to ellipsis."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أو حال عنه وهو بعيد.",
     "en": "Or [it is] a ḥāl (circumstantial qualifier) from it [the meaning], though that is far-fetched."},
]
