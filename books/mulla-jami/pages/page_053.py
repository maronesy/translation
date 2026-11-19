# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 53 (printed ٥٢)."""

PAGE_NUMBER = 53
PRINTED_PAGE = "٥٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (continued from p. ٥١) ----------------
    {"type": "matn",
     "ar": "ملحوظ في ذاته، يصلح أن يحكم عليه وبه، ومعقول هو مدرك تبعا، وآلة لملاحظة غيره[[١]]، فلا يصلح لشيء منهما[[٢]].",
     "en": "…observed in its own essence, fit to be predicated upon and by; and an intelligible that is apprehended dependently and [serves] as an instrument for observing something other than itself[[١]], and so is fit for neither of the two[[٢]]."},
    {"type": "matn",
     "ar": "فالابتداء مثلا إذا لاحظه العقل قصدا[[٣]] وبالذات، كان معنى مستقلا بالمفهومية ملحوظا في ذاته[[٤]]، ولزمه تعقل متعلقه[[٥]] إجمالا[[٦]] وتبعا[[٧]]، من غير حاجة إلى ذكره، وهو بهذا الاعتبار مدلول لفظ الابتداء فقط[[٨]]،",
     "en": "So «inception» (al-ibtidāʾ), for example: when the intellect observes it intentionally[[٣]] and essentially, it is a meaning independent in conceivability (mafhūmiyya), observed in its own essence[[٤]]; and its correlate[[٥]] is conceived along with it summarily[[٦]] and dependently[[٧]], without need to mention it; and in this respect it is the signified of the word «ibtidāʾ» alone[[٨]],"},
    {"type": "matn",
     "ar": "فلا حاجة في الدلالة عليه[[٩]] إلى ضم كلمة أخرى[[١٠]] إليه، لتدل على متعلقه.",
     "en": "so there is no need, in signifying it[[٩]], to adjoin another word[[١٠]] to it, in order to signify its correlate."},
    {"type": "matn",
     "ar": "وهذا هو المراد[[١١]] بقولهم: إن للاسم[[١٢]] والفعل معنى كائنا في نفس الكلمة الدالة عليه، إذا",
     "en": "This is what is meant[[١١]] by their statement: that the ism[[١٢]] (noun) and the fiʿl (verb) have a meaning subsisting in the very word that signifies it, when"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "بهذا المعنى. والمراد بالغير هو المتعلق.",
     "en": "In this sense. And what is meant by «the other» (al-ghayr) is the correlate (al-mutaʿallaq)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إذ الصالح لهما لا يكون إلا ما هو ملتفت إليه بالذات بداهة.",
     "en": "since what is fit for the two [i.e., to be predicated upon and by] can only be that which is attended to essentially, by self-evidence."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "منصوب على المصدرية، أي: ملاحظة قصدية، أو على الحالية، أي: حال كونه مقصودا وملابسا باعتبار الذات، أو على التمييز، أي: بطريق القصد.",
     "en": "It is manṣūb as a verbal noun (maṣdar) — i.e., an intentional observation — or as a circumstantial qualifier (ḥāl) — i.e., in the state of its being intended and adhered to by regard to essence — or as a specifier (tamyīz) — i.e., by way of intention."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "تفسير لقوله: مستقلا بالمفهومية.",
     "en": "An explanation of his words: «independent in conceivability (mafhūmiyya)»."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "بكسر اللام. والمتعلق ههنا ما أضيف إليه لفظ الابتداء، مثل «ابتداء الكتاب» أو «ابتداء القراءة» أو غير ذلك.",
     "en": "With a kasra on the lām [i.e., mutaʿalliq]. The correlate here is that to which the word «ibtidāʾ» is annexed, such as «the beginning of the book» or «the beginning of the recitation» and the like."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "نصب على التمييز من النسبة الإسنادية.",
     "en": "It is manṣūb as a specifier (tamyīz) derived from the predicative relation."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأن المتعلق الإجمالي الذي لا يتصور الابتداء بدونه، وهو شيء ما من مفهوم لفظ الابتداء. ولما كان ذلك المتعلق غير ملتفت إليه بالذات، بل ملتفت بالتبع، كفت دلالته، بخلاف دلالة هذه، فإنه لا بد حينئذ من ذكر متعلقه بضم كلمة أخرى ليدل عليه.",
     "en": "Because the general correlate is that without which inception cannot be conceived — it being some component of the concept of the word «ibtidāʾ». Since that correlate is not attended to essentially but only dependently, its signification suffices — unlike the signification of this [«min»], for in that case its correlate must be mentioned by adjoining another word to signify it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لا يقال: الحصر المستفاد من قوله: «فقط» ممنوع، لجواز أن يدل لفظ آخر أيضا على هذا المعنى كلفظ الأول؛ لأنا نقول: الحصر إضافي بالنسبة إلى الحرف، والمراد أنه مدلول لفظ الابتداء، ولا يمكن أن يكون مدلول «من»؛",
     "en": "One should not object: “the exclusivity derived from his words «only» (faqaṭ) is disallowed, since another word too might signify it in this sense, like the first word” — for we say: the exclusivity is relative with respect to the ḥarf; what is meant is that it is the signified of the word «ibtidāʾ» and cannot be the signified of «min»;"},
    {"type": "pair",
     "ar": "أو نقول: إن المراد من قوله: «فقط» أنه لا يحتاج إلى أمر آخر في كونه دالا عليه. وقوله: «لا حاجة في الدلالة ... إلى آخره» بيان له.",
     "en": "or we say: what is meant by his words «only» is that it needs nothing else to be its signifier; and his words «there is no need, in signifying it … » to the end are an elucidation of this."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "والدلالة هنا من «دل» المتعدي، كما أن قوله: «لتدل» من «دل» اللازم.",
     "en": "«Signification» (al-dalāla) here is from «dalla» in its transitive sense, just as his words «li-tadulla» (so that it may signify) are from «dalla» in its intransitive sense."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: لفظ الابتداء.",
     "en": "That is: the word «ibtidāʾ»."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "أي: عدم احتياج الكلمة في الدلالة على المعنى إلى انضمام أمر آخر هو المراد بكون المعنى في نفس الكلمة، المستفاد من قولهم: إن للاسم والفعل ...",
     "en": "That is: the word’s not needing, in signifying the meaning, the adjoining of some further thing — this is what is meant by the meaning’s being «in the word itself», as derived from their statement: “the ism and the fiʿl have…”"},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "يعني: أن ليس مرادهم بكون المعنى في نفس الكلمة أن مدلولها في نفس المعنى حتى يخلو الكلام عن الجدوى ويدخل الحرف فيه، بل معناه: أنها إذا انتقلت وحدها إلى ذهن السامع انتقل معها المعنى إليه، فكأن قالب الكلمة كظرف قد انتقل بما فيه، فلذا قيل: إن المعنى في نفس الكلمة.",
     "en": "Meaning: they do not intend, by the meaning’s being «in the word itself», that its signified lies in the meaning itself — such that the statement would be void of benefit and the ḥarf would fall under it. Rather its sense is: that when the word alone passes into the hearer’s mind, the meaning passes along with it, as though the mould of the word were a vessel that has moved along with its contents; hence it is said that the meaning is in the word itself."},
    {"type": "pair",
     "ar": "وما يقال: من أن للحرف معنى كائنا في غيره، فمعناه: أنه إذا انتقل وحده إلى ذهن السامع لم ينتقل معه المعنى، فكأن قالب الحرف كظرف خال، فلا يقال: معناه فيه، بل يقال: إنه في غيره إذ به يظهر.",
     "en": "As for what is said — that the ḥarf has a meaning subsisting in something other than itself — its sense is: that when it alone passes into the hearer’s mind, the meaning does not pass along with it, as though the mould of the ḥarf were an empty vessel; so it is not said that its meaning is in it, but rather that it is in another, since it is through the other that it appears."},
]
