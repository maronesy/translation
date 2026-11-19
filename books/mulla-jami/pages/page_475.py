# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 475 (printed ٤٧٤)."""

PAGE_NUMBER = 475
PRINTED_PAGE = "٤٧٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وثانيهما: أن يجعل «أحسن» قبل تسلط النفي عليه مجردا عن الزيادة عرفا[[١]]؛ لأن نفي الزيادة لا يلائم المدح،",
     "en": "The second: that “aḥsan”, before negation takes hold of it, is treated as stripped of excess by usage, because negating the excess does not suit praise."},
    {"type": "matn",
     "ar": "فبقي أصل الحسن وتوجه النفي إلى حسن رجل مقيسا إلى حسن زيد؛ إما بالمساواة، أو بكونه دونه، والقياس بكونه دونه لا يناسب المقام،",
     "en": "So the basic beauty remains, and the negation is directed at a man’s beauty measured against Zayd’s beauty, either by equality or by its being below it; and measurement by its being below it does not fit the context."},
    {"type": "matn",
     "ar": "فرجع المعنى إلى: «ما رأيت رجلا حسن في عينه الكحل حسنه في عين زيد»، فانتفى المساواة والزيادة بالطريق الأولى لما اقتضاه المقام،",
     "en": "So the meaning comes down to: “I have not seen a man in whose eye kohl is beautiful as its beauty in Zayd’s eye”; thus equality is negated, and excess all the more, as the context requires."},
    {"type": "matn",
     "ar": "ولا يبعد أن يقصد بنفي المساواة نفي الزيادة أيضا؛ لأن الزائد على شيء ما يساويه مع زيادة،",
     "en": "It is not far-fetched that by negating equality the negation of excess is also intended, since what exceeds a thing is what equals it with an addition;"},
    # REVIEW: printed «فانتفى لزائد أيضا» (one would expect «الزائد»); transcribed as printed.
    {"type": "matn",
     "ar": "فيصح أن يقصد به عرفا نفي المساواة مطلقا، ولو في ضمن الزائد، فانتفى لزائد أيضا،",
     "en": "so it is sound that by it, by usage, the negation of equality absolutely is intended, even within what exceeds; so it is negated for what exceeds too."},
    {"type": "matn",
     "ar": "فيحصل من جميع ذلك أن حسن كحل كل عين رجل دون حسن كحل عين زيد، وذلك كمال المدح.",
     "en": "From all of this it results that the beauty of the kohl of every man’s eye is below the beauty of the kohl of Zayd’s eye, and that is the utmost of praise."},
    {"type": "matn",
     "ar": "فإن قلت: لو كان زوال الزيادة التفضيلية[[٢]] بالنفي[[٣]] يقتضي جواز عمل اسم التفضيل في المظهر",
     "en": "If you say: if the removal of the comparative excess by negation entailed the permissibility of the elative governing an explicit noun,"},
    {"type": "matn",
     "ar": "ينبغي أن يكون عمله في مثل: «ما رأيت رجلا أفضل أبوه من زيد» جائزا كما جاز في المثال المذكور؟",
     "en": "then its government in a case like “I have not seen a man whose father is more excellent than Zayd” should be permissible, as it was in the example mentioned?"},
    {"type": "matn",
     "ar": "قلنا: فرق بين المثالين، فإن المفضل والمفضل عليه في المثال المذكور متحدان بالذات،",
     "en": "We say: there is a difference between the two examples. In the example mentioned the one preferred and the one surpassed are one in essence,"},
    {"type": "matn",
     "ar": "والأصل في اسم التفضيل أن يكون المفضل والمفضل عليه فيه مختلفين بالذات، ففي صورة الاتحاد ضعف المعنى التفضيلي،",
     "en": "while the basic case of the elative is that the one preferred and the one surpassed differ in essence; so in the case of identity the comparative meaning is weak,"},
    {"type": "matn",
     "ar": "فإذا زال بالنفي زال بالكلية، ولم يبق له قوة أن يعود حكمه بعد الزوال،",
     "en": "and when it is removed by negation it is removed entirely, and it has no strength left for its rule to return after removal;"},
    {"type": "matn",
     "ar": "بخلاف: «ما رأيت رجلا أفضل أبوه من زيد»، فإن المفضل والمفضل عليه فيه مختلفان بالذات، فلا ضعف في معناه التفضيلي،",
     "en": "unlike “I have not seen a man whose father is more excellent than Zayd”, for there the one preferred and the one surpassed differ in essence, so there is no weakness in its comparative meaning,"},
    {"type": "matn",
     "ar": "فله قوة أن يعود حكمه بعد الزوال، وهو عدم جواز عمله في المظهر",
     "en": "and it has the strength for its rule to return after removal, namely the impermissibility of its governing an explicit noun;"},
    {"type": "matn",
     "ar": "(مع أنهم لو رفعوا) «أحسن» بالخبرية، والكحل بالابتداء (لفصلوا بينه) أي: بين «أحسن» (وبين معموله) أي: ما عمل فيه «أحسن» من حيث إنه[[٤]] اسم تفضيل",
     "en": "(besides which, had they put in the nominative) “aḥsan” as predicate and “kohl” as subject, (they would have separated between it), that is, between “aḥsan”, (and what it governs), that is, what “aḥsan” governs insofar as it is an elative…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لا يخفى أنه لا يتأتى ذلك مع وجود «من» التفضيلية؛ إذ لا يبقى وجه لذكرها.",
     "en": "It is evident that this cannot hold while the comparative “min” is present, since no reason would remain for mentioning it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإن قلت: هذا السؤال لا يخص زوال الزيادة التفضيلية بالنفي، بل يتوجه على زوال الزيادة التفضيلية سواء كان برجوع النفي إلى الزيادة أو بوجه آخر؟",
     "en": "If you say: this question is not specific to the removal of the comparative excess by negation; rather it applies to the removal of the comparative excess whether by the negation reverting to the excess or in another way?"},
    {"type": "pair",
     "ar": "قلت: نعم، لكن تأول عبارة الشارح بجعل الباء في قوله: بالنفي بمعنى «مع» لا للسببية حتى يعم التوجيهين السابقين.",
     "en": "I say: yes; but the commentator’s expression is to be interpreted by taking the bāʾ in his words “bi-l-nafy” in the sense of “with”, not as causal, so that it covers both preceding explanations."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: بسبب النفي. فهذا الاعتراض مختص بالمعنى الأول؛",
     "en": "That is, by reason of negation. So this objection is specific to the first meaning,"},
    {"type": "pair",
     "ar": "لأن العرف على التجريد عن الزيادة إنما جرى فيما يكون التغاير بين المفضل والمفضل عليه فيما يكونان متغايرين بالذات،",
     "en": "because the usage of stripping [the elative] of excess has run only where there is difference between the one preferred and the one surpassed, where they are different in essence;"},
    # REVIEW: printed «فإن قوله: «في الجواب»، فإذا أزال بالنفي ينادي على فساده» — the quotation marks and punctuation are odd; transcribed as printed, translated by sense.
    {"type": "pair",
     "ar": "فلا يجوز أن يكون الباء بمعنى «مع» كما وهم، فإن قوله: «في الجواب»، فإذا أزال بالنفي ينادي على فساده.",
     "en": "so the bāʾ cannot mean “with”, as has been imagined; for his words in the reply, “so when it is removed by negation”, proclaim its wrongness."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا من حيث إن فيه معنى الزيادة، فإنه يعمل بهذه الحيثية في المفضل عليه.",
     "en": "Not insofar as it contains the meaning of excess, for in that respect it governs the one surpassed."},
]
