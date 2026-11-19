# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 384 (printed ٣٨٣)."""

PAGE_NUMBER = 384
PRINTED_PAGE = "٣٨٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وأخرت المخبر عنه يعني: زيدا وجعلته خبرا عن «الذي»،» at the foot of PDF p. 383.
    {"type": "matn",
     "ar": "و(قلت: «الذي ضربته زيد»).",
     "en": "… and (you said: “alladhī ḍarabtuhu Zaydun”) (the one I struck is Zayd)."},
    {"type": "matn",
     "ar": "(وكذلك) أي: مثل «الذي» (الألف واللام في الجملة الفعلية خاصة[[١]]؛ ليصح بناء اسمي الفاعل والمفعول منها[[٢]])،",
     "en": "(Likewise), that is, like “alladhī”, (is alif-lām, in the verbal sentence specifically, so that it is valid to form the active and passive participles from it),"},
    {"type": "matn",
     "ar": "فإن صلة الألف واللام لا يكون إلا اسم الفاعل أو اسم المفعول.",
     "en": "for the relative clause of alif-lām is only ever an active or a passive participle."},
    {"type": "matn",
     "ar": "ويمكن أن يؤخذ اسم الفاعل من المبني للفاعل، واسم المفعول من المبني للمفعول:",
     "en": "The active participle can be taken from the active-voice verb, and the passive participle from the passive-voice verb:"},
    {"type": "matn",
     "ar": "١-بشرط أن يكون الفعل الذي يتضمنه الجملة الفعلية متصرفا؛ إذ غير المتصرف نحو: «نعم، وبئس، وحبذا، وعسى، وليس» لا يجيء منه اسم فاعل ولا مفعول،",
     "en": "1. on condition that the verb contained in the verbal sentence be inflected (mutaṣarrif), since from an uninflected verb, such as “niʿma, biʾsa, ḥabbadhā, ʿasā and laysa”, no active or passive participle comes;"},
    {"type": "matn",
     "ar": "فلا يخبر بالألف عن زيد في «ليس زيد منطلقا».",
     "en": "so one cannot make a predication with the alif about Zayd in “laysa Zaydun munṭaliqan” (Zayd is not leaving)."},
    # REVIEW: the second item is printed «٢=» (with «=»), the first «١-»; transcribed as printed.
    {"type": "matn",
     "ar": "٢= وبشرط أن يكون في أول ذلك الفعل حرف لا يستفاد من اسمي الفاعل والمفعول معناها؛ كـ«السين وسوف وحرف النفي[[٣]] والاستفهام»،",
     "en": "2. and on condition that there be at the beginning of that verb no particle whose meaning cannot be conveyed by the active and passive participles, such as “sa- and sawfa, the particle of negation and [that of] interrogation”;"},
    {"type": "matn",
     "ar": "فلا يخبر باللام عن زيد في جملة «سيقوم زيد»، فإنه إذا بني اسم الفاعل من «سيقوم» يكون «قائما»، فيفوت معنى السين.",
     "en": "so one cannot make a predication with the lām about Zayd in the sentence “sa-yaqūmu Zaydun” (Zayd will stand), for when the active participle is formed from “sa-yaqūmu” it is “qāʾiman”, and the meaning of sa- is lost."},
    {"type": "matn",
     "ar": "(فإذا تعذر أمر منها) أي: من الأمور الثلاثة التي هي تصدير الموصول، ووضع عائد الموصول مقام ذلك الاسم[[٤]]، وتأخير ذلك الاسم خبرا (تعذر الإخبار).",
     "en": "(So when one of them is impossible), that is, one of the three things—putting the relative noun at the head, putting the relative noun’s returning pronoun in the place of that noun, and putting that noun after as predicate—(the predication is impossible)."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل أنه إذا تعذر أمر منها تعذر الإخبار (امتنع) الإخبار",
     "en": "(Hence), that is, because when one of them is impossible the predication is impossible, (it is barred) to make a predication …"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قلت: اسم الفاعل واسم المفعول قد يكونان مع مرفوعيهما جملة اسمية، نحو: «أضارب الزيدان» و«ما مضروب البكران»، فلم لا يصح الإخبار بهما؟",
     "en": "If you say: the active and passive participles together with their nominatives are sometimes a nominal sentence, as in “a-ḍāribun al-Zaydāni?” (are the two Zayds striking?) and “mā maḍrūbun al-Bakrāni” (the two Bakrs are not struck), so why is predication with them not valid?"},
    {"type": "pair",
     "ar": "قلنا: لأن هذين الحرفين يمنعان من وقوعهما صلة اللام.",
     "en": "We say: because these two particles prevent them from occurring as the relative clause of the lām."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    # REVIEW: printed «الضاربة» (tāʾ marbūṭa); the example requires «الضاربه» (participle + pronoun of Zayd); transcribed as printed, English follows the evident sense.
    {"type": "pair",
     "ar": "يشعر كلامه بأن ذلك في الإخبار عن زيد في المثال المذكور أخذ اسم الفاعل أو المفعول فتقول: الضاربة أنا زيد، أو تقول: المضروب لي زيد،",
     "en": "His words suggest that, in predicating about Zayd in the example given, this consists in taking the active or passive participle, so you say “al-ḍāribuhu anā Zaydun” (the one I am striking is Zayd), or you say “al-maḍrūbu lī Zaydun” (the one struck by me is Zayd)."},
    {"type": "pair",
     "ar": "فتنبه وينبه بالتعليل على ما صرح به الشارح من شروط الجملة الفعلية. ولذا أتى به مع أنه ليس من دأبه تعليل المسائل.",
     "en": "So take note; by the causal clause he draws attention to the conditions of the verbal sentence that the Commentator states explicitly. That is why he gave it, although it is not his practice to give reasons for questions."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه بحث؛ لأن السين تفيد التأخير كما أن صيغة المستقبل تفيد ذلك، وصيغة الماضي التقديم،",
     "en": "This is open to question, because sa- conveys futurity just as the future form conveys it, and the past form conveys priority;"},
    {"type": "pair",
     "ar": "فإذا لم يبالوا في الإخبار بالألف واللام بفوت الزمان الدال عليه الجملة جاز أن يبالوا بفوت ما يفيده السين أو سوف، فإنه بمنزلة الزمان،",
     "en": "so if, in predicating with alif-lām, they paid no heed to the loss of the time indicated by the sentence, they may [equally] disregard the loss of what sa- or sawfa conveys, for it is on a par with time."},
    {"type": "pair",
     "ar": "ولأنه لا يجوز أن يؤخذ من الفعل المنفي اسم الفاعل المعدول، فيقال في الإخبار عن زيد ولم يقم زيد: اللا قائم زيد.",
     "en": "Also, because it is not permissible to take from the negated verb the modified (maʿdūl) active participle, so that one would say, in predicating about Zayd in “lam yaqum Zaydun” (Zayd did not stand): “al-lā-qāʾimu Zaydun” (the non-standing one is Zayd)."},
    {"type": "pair",
     "ar": "فإن قلت: ينبغي أن يصح الإخبار عن زيد في زيد قائم بالألف واللام، فتقول: القائم زيد،",
     "en": "If you say: predication about Zayd in “Zaydun qāʾimun” with alif-lām ought to be valid, so you would say “al-qāʾimu Zaydun”,"},
    {"type": "pair",
     "ar": "قلت: القائم الذي جزء الجملة الأولى مفرد، والذي في القائم جملة وفي معنى الفعل، فلا يصح قيام أحدهما مقام الآخر.",
     "en": "I say: the qāʾim that is part of the first sentence is a single word, whereas the one in “al-qāʾim” is a sentence and has the meaning of a verb, so one cannot stand in the place of the other."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذا عند التفصيل أمران: وضع الضمير موضع المخبر عنه، وجعله للموصول، فالأمور أربعة، فاحفظها ليسهل عليك استنتاج جميع ما ذكره.",
     "en": "On analysis this is two things: putting the pronoun in the place of what is predicated about, and making it refer to the relative noun; so the things are four. Retain them, so that deriving all he mentioned becomes easy for you."},
]
