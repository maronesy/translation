# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 416 (printed ٤١٥)."""

PAGE_NUMBER = 416
PRINTED_PAGE = "٤١٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «ويرد عليه أنه يلزم أن يكون المبتدأ في مثل قولك: «مذ يومان» نكرة، والخبر» from PDF p. 415.
    {"type": "matn",
     "ar": "معرفة[[١]]، وذلك غير جائز.",
     "en": "…definite, and that is not permissible."},
    {"type": "matn",
     "ar": "واعلم أنهما إذا كانا مبتدأ أو خبرا فهما اسمان صريحان لا ظرفان، فلا يصح عدهما من الظروف المبنية،",
     "en": "Know that when they are an inchoative or a predicate, they are plain nouns, not adverbials, so it is not correct to count them among the indeclinable adverbials,"},
    {"type": "matn",
     "ar": "إلا أن يراد بظرفيتهما كونهما من أسماء الزمان، لا أنهما يقعان ظرفا في تراكيبهم.",
     "en": "unless by their being adverbials is meant their being among the nouns of time, not that they occur as adverbials in [the Arabs’] constructions."},
    {"type": "matn",
     "ar": "(ومنها) أي: من الظروف المبنية («لدى») بالألف المقصورة[[٢]] («ولدن») بفتح اللام، وضم الدال، وسكون النون",
     "en": "(And among them), that is, among the indeclinable adverbials, are (“ladā”), with the shortened alif, (and “ladun”), with fatḥa on the lām, ḍamma on the dāl and sukūn on the nūn;"},
    {"type": "matn",
     "ar": "(وقد جاء «لدن») بفتح اللام، وسكون الدال، وكسر النون («ولدن») بفتح اللام والدال، وسكون النون («ولدن») بضم اللام، وسكون الدال، وكسر النون",
     "en": "(and there has also come “ladni”), with fatḥa on the lām, sukūn on the dāl and kasra on the nūn; (and “ladan”), with fatḥa on the lām and the dāl and sukūn on the nūn; (and “ludni”), with ḍamma on the lām, sukūn on the dāl and kasra on the nūn;"},
    {"type": "matn",
     "ar": "(«ولد») بفتح اللام، وسكون الدال («ولد») بضم اللام، وسكون الدال («ولد») بفتح اللام، وضم الدال،",
     "en": "(and “lad”), with fatḥa on the lām and sukūn on the dāl; (and “lud”), with ḍamma on the lām and sukūn on the dāl; (and “ladu”), with fatḥa on the lām and ḍamma on the dāl."},
    {"type": "matn",
     "ar": "وبناؤها لوضع بعضها وضع الحروف وحمل البقية عليه.",
     "en": "They are indeclinable because some of them have the coinage of particles, and the rest are assimilated to it."},
    {"type": "matn",
     "ar": "وكلها بمعنى: «عند»[[٣]]، والفرق أنه يقال: «المال عند زيد» فيما يحضر عنده",
     "en": "All of them mean “ʿinda” (at, with); the difference is that one says “al-mālu ʿinda zaydin” (the property is with Zayd) of what is present with him…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 415 (footnote ٤) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "التسهيل: وإنما اخترته؛ لأن فيه إجراء «مذ ومنذ» على طريقة واحدة، وهي كونهما ظرفين مضافين إلى جملة بعدهما مع صحة المعنى، فهو أولى من اختلاف الاستعمال.",
     "en": "…al-Tashīl: I chose it only because it treats “mudh” and “mundhu” in a single way, namely as adverbials annexed to a sentence after them, with the meaning sound; and this is better than a divergence of usage."},
    {"type": "pair",
     "ar": "وفيه تخليص من الابتداء بنكرة بلا مسوغ إن ادعى التنكر، ومن تعريف غير معتاد إن ادعى التعريف.",
     "en": "It also avoids beginning with an indefinite without warrant, if indefiniteness is claimed, and an unusual kind of definiteness, if definiteness is claimed."},
    {"type": "pair",
     "ar": "وفيه تخليص من جعل جملتين في حكم جملة واحدة غير رابط ظاهر ولا مقدر، انتهى.",
     "en": "It also avoids treating two sentences as one without a linking element, either explicit or supposed.” End of quotation."},
    {"type": "pair",
     "ar": "وقد عرفت بما حررنا لك اندفاع جميع ذلك عن مذهب البصريين.",
     "en": "From what we have set out for you, you have learned that all of this is answered on the Baṣran doctrine."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ويمكن دفع الفساد الثاني بجعل «مذ» بمعنى جميع مدة زمان «ما رأيته فيه»،",
     "en": "The second fault can be answered by taking “mudh” in the sense of the whole period of the time of “mā raʾaytuhu fīhi” (in which I have not seen him)."},
    # REVIEW: «ويريد عليه» printed so (expected ويرد عليه); transcribed as printed.
    {"type": "pair",
     "ar": "ويريد عليه أيضا أنه يلزم تأخير المبتدأ فيما كان معرفتين في «ما رأيته مذ يوم الجمعة»، ويندفع بما ذكر في الجواب، والله تعالى أعلم بالصواب.",
     "en": "It is also objected against him that the inchoative would have to come later where both are definite, in “mā raʾaytuhu mudh yawmu l-jumuʿa”; this is answered by what was mentioned in the reply. Allah the Exalted knows best what is right."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهو بمعنى «عند»، فلا وجه للحكم ببنائها لمجرد لموافقتها في بعض الحروف بـ«لدن» مع عدم الموافقة في المعنى؛",
     "en": "It means “ʿinda”, so there is no ground for judging it indeclinable merely because it agrees with “ladun” in some letters while not agreeing with it in meaning,"},
    {"type": "pair",
     "ar": "إذ «لدن» بمعنى «من عند»، فهو متضمن لمعنى «من»، فلذا بنى،",
     "en": "since “ladun” means “min ʿindi” (from the presence of), and so it includes the meaning of “min”, and for this reason it is indeclinable."},
    {"type": "pair",
     "ar": "ولا يرد عدم الجهة لبناء «من لدن» حينئذ؛ لأنه يكفي بجهة البناء كون «لدن» في «من لدن» على لفظ ما هو مبني",
     "en": "Nor can it be objected that there is then no ground for the indeclinability of “min ladun”, because it suffices as a ground of indeclinability that “ladun” in “min ladun” has the form of what is indeclinable;"},
    {"type": "pair",
     "ar": "على أنه لا يوجب دخول «من» عليه عدم تضمنه لمعناه لجواز أن يكون الدخول للتأكيد.",
     "en": "besides, the entry of “min” upon it does not entail that it does not include its meaning, since the entry may be for emphasis."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: كلها مشتركة في هذا المعنى إلا أن «لدن» ولغاتها المذكورة يلزمها الابتداء، فلذا يلزمها من ظاهرة، وهو الأغلب، أو مقدرة فهي بمعنى «من عند».",
     "en": "That is, all of them share this meaning, except that “ladun” and its variant forms mentioned are bound to [the sense of] beginning; for this reason “min” is bound to them, either explicit, which is most common, or supposed, so that they mean “min ʿindi”."},
    {"type": "pair",
     "ar": "وأما لدى فهو بمعنى «عند» ولا يلزمه معنى الابتداء، كذا في الرضي.",
     "en": "As for “ladā”, it means “ʿinda”, and the sense of beginning is not bound to it; so in al-Raḍī."},
    {"type": "pair",
     "ar": "وبهذا ظهر عدم صحة ما قيل: إن بناء «لدن» لتضمنه معنى «من»؛ لأن لزوم «من» معها ظاهرة أو مقدرة ينافي التضمن كما في أسماء الشرط والاستفهام.",
     "en": "By this the incorrectness of what has been said becomes clear, namely that “ladun” is indeclinable because it includes the meaning of “min”; for “min” being bound to it, explicit or supposed, is incompatible with inclusion, as in the conditional and interrogative nouns."},
    {"type": "pair",
     "ar": "وقال في شرح التسهيل للفاضل المصري: «لدن» مبنية لشبهها بالحروف في لزومها استعمالا واحدا، وهو كونها مبتدأ غاية،",
     "en": "In the commentary on al-Tashīl by the learned Egyptian scholar he said: “ladun” is indeclinable because it resembles the particles in being bound to a single use, namely being the starting point of an extent,"},
    {"type": "pair",
     "ar": "وامتنع الإخبار عنها وبها، ولا يبنى عليها المبتدأ بخلاف «عند ولدى»،",
     "en": "and it cannot be the subject or the predicate of a statement, nor can an inchoative be built upon it, unlike “ʿinda” and “ladā”;"},
    {"type": "pair",
     "ar": "فإنهما لا يلزمان استعمالا واحدا، بل يكونان لابتداء الغاية وغيرها، ويبنى عليهما المبتدأ",
     "en": "for these are not bound to a single use, but serve for the starting point of an extent and for other things, and an inchoative can be built upon them."},
    {"type": "pair",
     "ar": "ومعنى «عند» القرب حسا أو معنى نحو: «عندي أنك غني»، وربما فتحت عينها أو ضمت، ويلزمها النصب إلا إذا انجرت بـ«من» كذا في الرضي.",
     "en": "The meaning of “ʿinda” is nearness, physical or notional, as in “ʿindī annaka ghaniyyun” (in my view you are rich); its ʿayn is sometimes given fatḥa or ḍamma, and it is bound to the accusative unless it is put in the genitive by “min”; so in al-Raḍī."},
]
