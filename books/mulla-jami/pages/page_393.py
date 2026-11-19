# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 393 (printed ٣٩٢)."""

PAGE_NUMBER = 393
PRINTED_PAGE = "٣٩٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وإنما قال: علما» at the foot of PDF p. 392.
    {"type": "matn",
     "ar": "ليخرج باب «فساق»، وإنما قال: للأعيان ليخرج باب «فجار»؛ لأنه وإن كان علما كما قالوا لكنه للمعاني لا للأعيان،",
     "en": "…to exclude the class of “fasāqi”; and he said “for concrete things” only to exclude the class of “fajāri”, since, although it is a proper name, as they said, it is for meanings, not for concrete things."},
    {"type": "matn",
     "ar": "وقوله: (مؤنثا) صفة علما، وذكره للتنبيه[[١]] على أنه لم يقع إلا كذلك (كـ«قطام») علما للمؤنث (و«غلاب»[[٢]]) كذلك",
     "en": "His words (feminine) qualify “a proper name”; he mentioned it to point out that it occurs only thus, (as “qaṭāmi”), a proper name for a female, (and “ghalābi”), likewise:"},
    {"type": "matn",
     "ar": "(مبني في) استعمال (أهل الحجاز) لمشابهته «فعال» بمعنى الأمر[[٣]] عدلا وزنة",
     "en": "(it is indeclinable in) the usage of (the people of the Ḥijāz), because it resembles “faʿāli” in the sense of the imperative in diversion and in measure;"},
    {"type": "matn",
     "ar": "(ومعرب في) استعمال (بني تميم، إلا ما في آخره) أي: إلا في «فعال علما للأعيان» الذي يكون في أخره (راء)",
     "en": "(and declinable in) the usage of (Banū Tamīm, except what has at its end), that is, except in “faʿāli as a proper name for concrete things” which has at its end, (a rāʾ):"},
    # REVIEW: «أخره» is printed here without madda (the lemma just before prints «آخره»); transcribed as printed.
    {"type": "matn",
     "ar": "فإن بني تميم اختلفوا فيه، فأكثرهم يوافقون الحجازيين في بنائه، وأقلهم لا يفرقون بين ذات الراء وغيرها بل يحكمون بإعراب الكل[[٤]]",
     "en": "for Banū Tamīm disagreed about it: most of them agree with the Ḥijāzīs in making it indeclinable, while the fewest of them do not distinguish between the form with rāʾ and the others but rule that all are declinable,"},
    {"type": "matn",
     "ar": "(نحو: «حضار») علما لـ«كوكب»،",
     "en": "(as “ḥaḍāri”), a proper name for a star."},
    {"type": "matn",
     "ar": "ووجه الأكثرين أن الراء[[٥]] حرف ثقيل لكونه في مخرجه كالمكرر، فاختير فيه البناء؛ لأنه أخف؛ إذ سلوك طريقة واحدة أسهل من سلوك طرائق مختلفة.",
     "en": "The reasoning of the majority is that rāʾ is a heavy letter, because at its point of articulation it is as if repeated; so indeclinability was chosen for it, since it is lighter, for following a single way is easier than following different ways."},

    {"type": "section", "ar": "[الأصوات]",
     "en": "Sound Words (al-Aṣwāt)"},

    {"type": "matn",
     "ar": "(الأصوات) اعلم أن الأصوات الجارية على لفظ الإنسان[[٦]]، إما منقولة إلى باب المصادر، ولزمت المصدرية ولم تصر اسم فعل، أو لم تلزم المصدرية وصارت اسم فعل.",
     "en": "(Sound words): know that the sounds that run on the tongue of a human being are either transferred to the class of maṣdars, and remained bound to being maṣdars without becoming verbal nouns (ism fiʿl), or did not remain bound to being maṣdars and became verbal nouns."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: الأظهر أنه احتراز عن قطام إذا سمي به مذكر، فإنه ليس علما مؤنثا؟",
     "en": "If you say: it is more apparent that it guards against qaṭāmi when a male is named by it, for then it is not a feminine proper name?"},
    {"type": "pair",
     "ar": "قلت: هو علم مؤنث؛ لأن الزائد على الثلاثة لا يخرج بتسمية مذكر به عن التأنيث",
     "en": "I say: it is a feminine proper name, because [a feminine name] of more than three letters does not leave femininity by a male being named by it."},
    {"type": "pair",
     "ar": "بقي أن الأظهر أنه احتراز عن ذهاب إذا جعل علما لمذكر.",
     "en": "There remains [the view] that it is more apparent that it guards against dhahābi when it is made a proper name for a male."},
    {"type": "pair",
     "ar": "ولا يخفى أن بناء فعال علما مؤنثا للأعيان ينتقض بذهاب إذا جعل علما لمؤنث، فإنه لا يبنى اتفاقا",
     "en": "It is clear that the indeclinability of faʿāli as a feminine proper name for concrete things is contradicted by dhahāb when it is made a proper name for a female, for it is not made indeclinable, by agreement;"},
    {"type": "pair",
     "ar": "إلا أن يقال: المراد بكونه علما كونه علما في أصل وضعه من غير نقل عن غير العلم،",
     "en": "unless it be said: what is meant by its being a proper name is its being a proper name in its original coinage, without transfer from something that is not a proper name."},
    {"type": "pair",
     "ar": "وحينئذ يتم كلام الشارح أيضا إن قيد مؤنثا ليس للاحتراز، فتأمل.",
     "en": "In that case the Commentator’s statement also holds, that the restriction “feminine” is not for exclusion. So reflect."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هما علم امرأة.",
     "en": "Both are names of a woman."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه ما ذكره في أختيه. ولا يجري فيه ما يجري فيهما،",
     "en": "Against this is what he mentioned regarding its two sisters; and what applies to them does not apply to it."},
    # REVIEW: «فيه» in «وكان فيه المبالغة» is printed with a malformed initial letter that looks like «ثيه»; read as «فيه».
    {"type": "pair",
     "ar": "فالوجه أن هذا القسم إما علم مرتجل، أو منقول عن المعنى الوصفي، فإن كان منقولا راعوا معناه الأصلي وكان فيه المبالغة،",
     "en": "The right view is that this class is either an improvised (murtajal) proper name or one transferred from a descriptive meaning: if it is transferred, they observed its original meaning, and there was intensity in it;"},
    {"type": "pair",
     "ar": "وإن كان مرتجلا حملوا على المنقول؛ لأنه أكثر من غيره.",
     "en": "and if it is improvised, they assimilated it to the transferred kind, because that is more frequent than the other."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فمعنى قول المصنف: معرب في بني تميم كلهم إلا ما آخره راء، فإنه ليس بمعرب في تميم كلهم، بل عند أقلهم.",
     "en": "So the meaning of the Author’s words is: declinable among all of Banū Tamīm, except what ends in rāʾ, for that is not declinable among all of Tamīm, but only among the fewest of them."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هذا وجه بديع ذكره الفاضل الهندي، وأوضحه الشارح،",
     "en": "This is an ingenious reason, mentioned by al-Fāḍil al-Hindī and clarified by the Commentator."},
    {"type": "pair",
     "ar": "والمشهور في كتبهم وجه آخر، وهو أن الإمالة في ذوات الراء مستحسنة، والمصحح له كسرها، فالتزم.",
     "en": "The well-known reason in their books is another: that inclination (imāla) in words with rāʾ is considered good, and what makes it valid is the kasra on [the rāʾ]; so it was made obligatory."},
    {"type": "pair",
     "ar": "قال عبد الغفور: أو أن وجه البناء في ذي الراء قصد الإمالة؛ إذ هي أمر مستحسن.",
     "en": "ʿAbd al-Ghafūr said: or the reason for indeclinability in the form with rāʾ is the aim of imāla, since it is something considered good."},
    {"type": "pair",
     "ar": "والمصحح للإمالة كسر الراء، وهي لا تحصل إلا بتقدير علة البناء؛ لأنه إذا أعربوا منع الصرف فلم يكسر.",
     "en": "What makes imāla valid is the kasra on the rāʾ, and that is obtained only by supposing a cause of indeclinability; for if they made it declinable, it would be diptote and so would not take kasra."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "بل على لفظ العرب.",
     "en": "Rather, on the tongue of the Arabs."},
]
