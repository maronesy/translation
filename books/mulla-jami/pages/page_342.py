# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 342 (printed ٣٤١)."""

PAGE_NUMBER = 342
PRINTED_PAGE = "٣٤١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «ويكون من قبيل عطف الجملة على الجملة، ولا مانع منه.» at the foot of PDF p. 341 (new sentence).
    {"type": "matn",
     "ar": "ولما كان لقائل أن يقول[[١]]: هذه القاعدة منتقضة بقولهم: «الذي يطير فيغضب زيد الذباب»،",
     "en": "Since someone might say: this rule is broken by their saying “alladhī yaṭīru fa-yaghḍabu Zaydun al-dhubābu” (that which flies, and so Zayd grows angry, is the fly),"},
    {"type": "matn",
     "ar": "فإن «يطير» فيه ضمير يعود إلى الموصول، و«يغضب» المعطوف عليه ليس فيه ذلك الضمير،",
     "en": "for “yaṭīru” contains a pronoun referring back to the relative noun, while “yaghḍabu”, which is conjoined to it, does not contain that pronoun,"},
    {"type": "matn",
     "ar": "فأجاب عنه بقوله: (وإنما جاز «الذي يطير فيغضب زيد الذباب»؛ لأنها) أي: «الفاء» في هذا التركيب (فاء السببية)",
     "en": "he answered it with his words: (“alladhī yaṭīru fa-yaghḍabu Zaydun al-dhubābu” is permitted only because it), that is, the “fāʾ” in this construction, (is the fāʾ of causation) (fāʾ al-sababiyya),"},
    {"type": "matn",
     "ar": "أي: فاء لها نسبة إلى السببية بأن يكون معناها السببية لا العطف، فلا يرد نقضا على تلك القاعدة،",
     "en": "that is, a fāʾ that is related to causation: either its meaning is causation, not conjunction, so it does not stand as a counter-instance to that rule;"},
    {"type": "matn",
     # REVIEW: the standard example is «الذي يطير فيغضب زيد الذباب»; «إذا» here is as printed.
     "ar": "أو يكون معناها السببية مع العطف لكنها تجعل الجملتين كجملة واحدة[[٢]]، فيكتفى بالربط في الأول، والمعنى: «الذي إذا يطير فيغضب زيد الذباب»،",
     "en": "or its meaning is causation together with conjunction, but it makes the two sentences like a single sentence, so the link in the first suffices, the meaning being “alladhī idhā yaṭīru fa-yaghḍabu Zaydun al-dhubābu” (that which, when it flies, Zayd grows angry, is the fly);"},
    {"type": "matn",
     "ar": "أو يفهم منها سببية الأولى للثانية، فالمعنى: «الذي يطير فيغضب زيد لسببيته الذباب»،",
     "en": "or from it the causation of the second by the first is understood, so the meaning is “that which flies, and Zayd grows angry because it is the cause, is the fly”."},
    {"type": "matn",
     "ar": "ويمكن أن يقدر فيه ضمير أي: الذي يطير فيغضب زيد بطيرانه الذباب.",
     "en": "A pronoun may also be supposed in it, that is, “that which flies, and Zayd grows angry at its flying, is the fly”."},
    {"type": "matn",
     "ar": "(وإذا عطف) أي: إذا وقع العطف[[٣]] بناء (على) وجود (عاملين) بأن عطف اسمان على معموليهما بعاطف واحد،",
     "en": "(When conjunction is made), that is, when conjunction occurs based (on) the presence of (two governors), in that two nouns are conjoined to the two words they govern by a single conjunctive particle."},
    {"type": "matn",
     "ar": "وقال بعض شارحي اللباب: الأظهر عندي أن العطف ههنا محمول على معناه اللغوي -أي: إمالة الاسمين نحو العاملين- بأن يجعلا معموليهما",
     "en": "One of the commentators on al-Lubāb said: “The more evident view to me is that ʿaṭf here is taken in its lexical meaning—that is, inclining the two nouns toward the two governors—by making them the words they govern.”"},
    {"type": "matn",
     "ar": "وأكثر الشارحين على أن المعنى على معمولي عاملين[[٤]]،",
     "en": "Most of the commentators hold that the meaning is “on the two governed words of two governors”."},
    {"type": "matn",
     "ar": "وإنما قال: «على معمولي عاملين» لا «على معمولي عامل واحد»، فإنه جائز اتفاقا نحو: «ضرب زيد عمرا وعمرو خالدا»، ولا على أكثر من اثنين، فإنه لا خلاف في امتناعه",
     "en": "He said “on the two governed words of two governors”, not “on the two governed words of a single governor”, because that is permitted by agreement, as in “ḍaraba Zaydun ʿAmran wa-ʿAmrun Khālidan” (Zayd struck ʿAmr, and ʿAmr Khālid); nor “on more than two”, because there is no disagreement over its being barred."},
    {"type": "matn",
     "ar": "(مختلفين) أي: غير متحدين بأن يكون الثاني عين الأول، وذلك لدفع وهم من يتوهم أن مثل: «ضرب",
     "en": "(That differ), that is, that are not one, in the sense of the second being identical with the first; this is to remove the misconception of whoever imagines that such as “ḍaraba…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «يسند» printed; the sense may call for «بسند» (on the basis of); transcribed as printed.
    {"type": "pair",
     "ar": "يحتمل أن يكون قول المصنف: وإنما جاز جوابا لمنع عدم جواز ما عدا الرفع في «ما زيد بقائم ولا ذاهب عمرو» يسند جواز: الذي يطير فيغضب زيد الذباب.",
     "en": "The author’s words “is permitted only” may be an answer to a rebuttal of the impermissibility of anything but the nominative in “mā Zaydun bi-qāʾimin wa-lā dhāhibun ʿAmrun”, [a rebuttal] that relies on the permissibility of “alladhī yaṭīru fa-yaghḍabu Zaydun al-dhubābu”."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وذلك لاتصال بينهما بالسببية، أفاد الشيخ الرضي ما حاصله:",
     "en": "That is because of the connection between them through causation. Shaykh al-Raḍī stated what amounts to the following:"},
    {"type": "pair",
     "ar": "أن الجملة التي يلزمها الضمير كالصلة والصفة وخبر المبتدأ إذا عطفت عليها جملة أخرى متعلقة بها بأن كان مضمونها بعد مضمون الأولى متراخيا عنه أو لا، أو بغير ذلك جاز تجرد إحداهما عن الضمير اكتفاء بأختها.",
     "en": "when a sentence that requires a pronoun, such as the relative clause, the qualifying clause and the predicate of the subject, has conjoined to it another sentence connected with it—in that its content comes after the content of the first, with an interval or without, or in some other way—one of the two may be bare of the pronoun, its sister sufficing."},
    {"type": "pair",
     "ar": "وذلك لأن ذلك التعلق يجعل المجموع أمرا واحدا،",
     "en": "That is because this connection makes the whole a single thing."},
    # REVIEW: «فليغرب» printed in the example (one would expect «فيغرب»); transcribed as printed.
    {"type": "pair",
     "ar": "فنقول: الذي جاء فليغرب الشمس زيد؛ لأن المعنى: الذي يعقب مجيئه غروب الشمس زيد. وكذا الحال في ثم.",
     "en": "So we say: “alladhī jāʾa fa-li-yaghrubi al-shamsu Zaydun” (the one who came, and then the sun set, is Zayd), since the meaning is “the one whose coming is followed by sunset is Zayd”. The same holds of “thumma”."},
    {"type": "pair",
     "ar": "وأما الواو، فلما كان للجمع المطلق لم يجز ذلك فيه إلا إذا ساعدته القرينة على التعلق كأن يقول: الذي قام وقعدت هند في تلك الحال زيد.",
     "en": "As for the wāw, since it is for unqualified combination, this is not permitted with it unless a contextual indication supports the connection, as when one says: “alladhī qāma wa-qaʿadat Hindun fī tilka al-ḥāl Zaydun” (the one who stood, while Hind sat in that state, is Zayd)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: قوله: إذا عطف مسند إلى ضمير مصدره من قبيل: حيل بين العير والنزوان.",
     "en": "He means: his words “idhā ʿuṭifa” have as their subject the pronoun of its verbal noun, of the type “ḥīla bayna al-ʿayri wa-l-nazawāni” (it was intervened between the ass and leaping)."},
    {"type": "pair",
     "ar": "وقوله: على عاملين ليس نائبا عن الفاعل، بل مصدر عطف أي: عطفا مبنيا على عاملين. ولا يخفى أنه بعيد جدا.",
     "en": "His words “ʿalā ʿāmilayn” are not the proxy agent (nāʾib al-fāʿil); rather, [the subject is] the verbal noun of ʿuṭifa, that is, “a conjunction based on two governors”. It is not hidden that this is very far-fetched."},
    {"type": "pair",
     "ar": "وما قال بعض شارحي اللباب: أبعد منه، والحق مع أكثر الشارحين، فلا ينبغي أن يتجاوز.",
     "en": "What one of the commentators on al-Lubāb said is more far-fetched than it; the truth lies with most of the commentators, and one should not go beyond it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بحذف المضاف. وإنما حذف المضاف ليقع الحكم على مناطه،",
     "en": "By elision of the annexed noun. The annexed noun was elided only so that the ruling falls on its basis (manāṭ),"},
    {"type": "pair",
     "ar": "فإن مناط عدم الجواز تعدد العامل لا تعدد المعمول. ولذا جاز العطف على معمولي عامل واحد.",
     "en": "for the basis of impermissibility is the multiplicity of the governor, not the multiplicity of the governed; hence conjunction to the two governed words of a single governor is permitted."},
]
