# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 356 (printed ٣٥٥)."""

PAGE_NUMBER = 356
PRINTED_PAGE = "٣٥٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فيذكرون ألقاب المبني في المعرب وبالعكس، والمراد أن» at the foot of PDF p. 355.
    # REVIEW: «هذا الألقاب» printed (one would expect «هذه الألقاب»); transcribed as printed.
    {"type": "matn",
     "ar": "الحركات[[١]] والسكنات البنائية لا يعبر عنها[[٢]] البصريون إلا بهذه الألقاب لا أن هذا الألقاب لا يعبر بها إلا عنها؛",
     "en": "…the Baṣrans express the vowels and quiescences of indeclinability only by these designations—not that these designations are used to express nothing but them;"},
    {"type": "matn",
     "ar": "لأنهم كثيرا ما يطلقونها على الحركات الإعرابية[[٣]] أيضا كما مر في صدر الكتاب حيث قال: «بالضمة رفعا[[٤]]، والفتحة نصبا والكسرة جرا»",
     "en": "for they often apply them to the vowels of inflection as well, as passed at the beginning of the book, where he said “by the ḍamma in the nominative, the fatḥa in the accusative and the kasra in the genitive”,"},
    {"type": "matn",
     "ar": "وعلى غيرها كما يقال: «الراء» في «رجل» مثلا مفتوحة، والجيم مضمومة.",
     "en": "and to others besides, as when it is said that the rāʾ in “rajul”, for example, is “maftūḥa” (with fatḥa) and the jīm “maḍmūma” (with ḍamma)."},
    {"type": "matn",
     "ar": "(وحكمه[[٥]]) أي: حكم المبني وأثره المترتب على بنائه (ألا يختلف آخره) أي: آخر المبني لكن لا مطلقا بل (لاختلاف العوامل)؛",
     "en": "(Its rule), that is, the rule of the indeclinable and the effect consequent on its indeclinability, (is that its ending does not change), that is, the ending of the indeclinable—not absolutely, however, but (through the change of governors);"},
    {"type": "matn",
     "ar": "إذ قد يختلف آخره لا لاختلاف العوامل نحو: «من الرجل، ومن امرؤ، ومن زيد».",
     "en": "for its ending may change, but not through the change of governors, as in “mina al-rajuli”, “man imruʾun” and “man Zaydun”."},
    {"type": "matn",
     "ar": "(وهي) أي: المبني والتأنيث باعتبار الخبر (المضمرات، وأسماء الإشارات، والموصولات، والمركبات، والكنايات[[٦]]، وأسماء الأفعال، والأصوات[[٧]])",
     "en": "(They are)—that is, the indeclinable, the feminine [pronoun] being in view of the predicate—(the pronouns, the demonstratives, the relative nouns, the compounds, the allusive nouns (kināyāt), the verbal nouns (asmāʾ al-afʿāl) and the sounds)"},
    {"type": "matn",
     "ar": "بالرفع عطف على «أسماء الأفعال» لا على «الأفعال» لتصديره بحث الأصوات فيما بعد بالأصوات لا بأسماء الأصوات",
     "en": "—in the nominative, conjoined to “asmāʾ al-afʿāl”, not to “al-afʿāl”, since he later heads the discussion of sounds with “the sounds”, not “the names of sounds”—"},
    {"type": "matn",
     "ar": "(وبعض الظروف) وإنما قال: «بعض الظروف»[[٨]]؛ لأن جميعها ليست بمبنية بل بعضها.",
     "en": "(and some of the adverbs of time and place) (ẓurūf). He said “some of the adverbs” only because not all of them are indeclinable, but only some."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "رد لما قيل: من أن كلامه يدل على اختصاص الضم والفتح والكسر بالمبني.",
     "en": "A reply to what has been said: that his words indicate that ḍamm, fatḥ and kasr are specific to the indeclinable."},
    {"type": "pair",
     "ar": "ولعله فهم ذلك الاختصاص من قوله: ألقابه؛ لأن لقب الشيء مختص به،",
     "en": "Perhaps he understood that specificity from his word “its designations”, because a thing’s designation is specific to it."},
    {"type": "pair",
     "ar": "فعلى ما ذكره الشارح كان معناه: أن تلك الأمور ألقاب لحركات المبني لا بخصوصها.",
     "en": "On what the commentator has said, its meaning is that these things are designations for the vowels of the indeclinable, not specifically for them alone."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "نبه به على أن المراد باللقب ما يعبر به عن شيء جريا على اللغة لا قسم العلم كما هو مصطلح الصناعة،",
     "en": "By this he drew attention to the fact that what is meant by “designation” (laqab) is that by which a thing is expressed, following lexical usage, not the category of proper noun, as in the technical terminology of the discipline;"},
    {"type": "pair",
     "ar": "فإن التعبير بها عنها لا بخصوصها لاشتراكها بين الحركات الإعرابية والبنائية وغيرهما.",
     "en": "for they express them, but not specifically, since they are shared among the vowels of inflection, of indeclinability and others."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "ويطلقون السكون على الجزم بحذف الحركة.",
     "en": "And they apply “sukūn” to the jussive (jazm) formed by dropping the vowel."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "قد يناقش فيه بالفرق بين ما معه التاء، وما ليست معه.",
     "en": "This may be disputed on the basis of the difference between what has the tāʾ with it and what does not."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وحقه: أن يؤخر عن تقسيم المبني إلا أنه قدمه؛ لأن غيره جعله تعريفا للمبني،",
     "en": "Its proper place was after the division of the indeclinable, but he put it first because others made it a definition of the indeclinable."},
    {"type": "pair",
     "ar": "فنبه على أنه حكمه الذي لا يعرف إلا بعد معرفته تعقب تعريفه بقوله: وحكمه تنبيها على وجه العدول هذا،",
     "en": "So he indicated that it is its rule, which is known only after it is known, by following its definition with his words “and its rule”, to point out the reason for this departure."},
    # REVIEW: «مبنى الأصل» printed with alif maqṣūra (elsewhere «مبني الأصل»); transcribed as printed.
    {"type": "pair",
     "ar": "وفيه نظر؛ لأن حكم المبني مطلقا ليس ذلك، بل ما ناسب مبنى الأصل منه.",
     "en": "This is open to question, because that is not the rule of the indeclinable without qualification, but of that part of it which resembles what is indeclinable by origin."},
    {"type": "pair",
     "ar": "وأما الذي بناؤه لعدم التركيب، فحكمه أن يختلف آخره باختلاف العوامل.",
     "en": "As for that whose indeclinability is due to the absence of compounding, its rule is that its ending changes with the change of governors."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأولى أن يقول: وبعض الكنايات؛ لأن بعضها معرب كفلان وفلانة.",
     "en": "It would have been better to say “and some of the allusive nouns”, because some of them are declinable, such as “fulān” and “fulāna” (so-and-so)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قيل: إنها ليست أسماء؛ لأنها ليست موضوعة، لكنها جارية مجرى الأسماء المبنية في البناء، فلهذا عدها منها.",
     "en": "It has been said that they are not nouns, because they are not coined [for a meaning]; but they behave like indeclinable nouns in indeclinability, and for this reason he counted them among them."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ولم يقل: بعض الموصولات مع أن أي معربة وحدها لقلتها، ولئلا يتوهم أنه على مذهب من جعل اللذان واللتان معربين،",
     "en": "He did not say “some of the relative nouns”, although “ayy” alone is declinable, because of its rarity, and so that it is not imagined that he follows the school of those who made “alladhāni” and “allatāni” declinable."},
    {"type": "pair",
     "ar": "لكن ينبغي أن يقول: وبعض المركبات؛ لأن المركبات قسمان: قسم مبني من نحو: خمسة عشر، وقسم معرب وهو بعلبك.",
     "en": "But he should have said “and some of the compounds”, because compounds are of two kinds: an indeclinable kind, such as “khamsata ʿashara” (fifteen), and a declinable kind, namely “Baʿlabakk”."},
    {"type": "pair",
     "ar": "قيل: وينبغي أن يقول: وبعض الكنايات أيضا ليخرج فلان وفلانة.",
     "en": "It has been said: he should also have said “and some of the allusive nouns”, to exclude “fulān” and “fulāna”."},
]
