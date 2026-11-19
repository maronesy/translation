# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 370 (printed ٣٦٩)."""

PAGE_NUMBER = 370
PRINTED_PAGE = "٣٦٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(مخير) بين الإتيان بنون الوقاية … وعلى السكون في «لدن» وبين» from PDF p. 369.
    {"type": "matn",
     "ar": "تركها تحرزا عن اجتماع النونات ولو حكما[[١]]، كما في «لعل» لقرب اللام من النون في المخرج، وحملا على أخواتها كما في «ليت».",
     "en": "…omitting it, to avoid a concurrence of nūns, even if only in status, as in “laʿalla”, because the lām is close to the nūn in point of articulation, and by analogy with its sisters, as in “layta”."},
    {"type": "matn",
     "ar": "(ويختار) لحوق نون الوقاية (في «ليت»[[٢]]) من بين أخوات «إن» لعدم مانع في ذاتها، والحمل على أخواتها خلاف الأصل",
     "en": "(It is preferred) that the nūn of protection be attached (in “layta”), among the sisters of “inna”, because there is no impediment in the word itself, and treating it by analogy with its sisters is contrary to the norm;"},
    {"type": "matn",
     "ar": "(و«من»، و«عن»، و«قد»، و«قط») وهما بمعنى «حسب» للمحافظة على السكون اللازم الذي هو الأصل في البناء مع قلة الحروف.",
     "en": "(and in “min”, “ʿan”, “qad” and “qaṭ”) — the latter two in the sense of “ḥasb” (enough) — to preserve the fixed quiescence that is the norm in indeclinability, given the fewness of their letters."},
    # REVIEW: «لنقل التضعيف» printed; the sense calls for «لثقل التضعيف» (heaviness of the doubling); transcribed as printed, translated per the sense.
    {"type": "matn",
     "ar": "(وعكسها) أي: عكس «ليت» («لعل») في الاختيار، فالمختار فيها ترك النون لنقل التضعيف وكثرة الحروف.",
     "en": "(Its converse), that is, the converse of “layta” in preference, is (“laʿalla”): what is preferred in it is omitting the nūn, because of the heaviness of the doubled letter and the number of letters."},
    {"type": "matn",
     "ar": "(ويتوسط بين المبتدأ والخبر[[٣]] قبل العوامل[[٤]]) مثل: «زيد هو القائم» (وبعدها) أي: بعد العوامل نحو: ﴿كنت أنت الرقيب﴾[[٥]]",
     "en": "(There comes between the subject and the predicate, before the governors) — such as “Zaydun huwa l-qāʾimu” (Zayd, he is the one standing) — (and after them), that is, after the governors, as in “kunta anta l-raqība” (You were the Watcher)"},
    {"type": "matn",
     "ar": "(صيغة مرفوع) ولم يقل: «ضمير مرفوع» لمكان الاختلاف[[٦]] في كونه ضميرا (منفصل مطابق للمبتدأ[[٧]]) إفرادا وتثنية",
     "en": "(a form of a separate nominative) — he did not say “a nominative pronoun”, because of the disagreement over whether it is a pronoun — (that agrees with the subject) in singular, dual…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ويحمل «لعل» على لغاتها.",
     "en": "And “laʿalla” is treated by analogy with its dialectal variants."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "المشهور فيه أن النون لازمة إلا لضرورة الشعر.",
     "en": "The well-known view about it is that the nūn is required, except under poetic necessity."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه تجريد أو تأكيد؛ لأن حق المبتدأ والخبر ألا يقع بينهما فصل.",
     "en": "There is in this either abstraction (tajrīd) or emphasis, because the subject and predicate are properly such that no separation falls between them."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: اللفظية لأنها المتبادر، ولا حاجة إليه إلا أنه ذكر توطئة لقوله: أو بعدها،",
     "en": "That is, the verbal [governors], since they are what first comes to mind. There is no need for it, except that he mentioned it as a lead-in to his words “or after them”."},
    {"type": "pair",
     "ar": "وهما وإن لم يكونا بعد العوامل مبتدأ وخبرا، لكن يصح التعبير عنهما بالمبتدأ والخبر حقيقة؛",
     "en": "Although after the governors the two are not a subject and predicate, they may still properly be called subject and predicate in the literal sense,"},
    {"type": "pair",
     "ar": "لأن المبتدأ والخبر ليسا مشتقين حتى يجب اتصاف ما صدق بهما بمفهومهما حين تعلق الحكم بها،",
     "en": "because “subject” and “predicate” are not derived terms, such that what they apply to would have to bear their concept at the time the ruling attaches to it;"},
    {"type": "pair",
     "ar": "وليس التركيب من قبيل «رأيت هذا الشاب في شبابه وصباه»؛ لأنه تعليق بالمشتق، وجمع بين الحقيقة والمجاز،",
     "en": "nor is the construction of the type “I saw this young man in his youth and boyhood”, since that is attachment to a derived term and a combining of the literal and the figurative."},
    {"type": "pair",
     "ar": "فمن تمسك في كون ما نحن فيه حقيقة يكون هذا التركيب حقيقة، فقد غفل،",
     "en": "So whoever relies, for what we are discussing being literal, on this construction being literal has been heedless;"},
    {"type": "pair",
     "ar": "والقول بأنه من الجمع بين الحقيقة والمجاز، ومن قبيل عموم المجاز بعيد عن الصحة والجواز.",
     "en": "and the claim that it is a combination of the literal and the figurative, or of the type of generalized figurative usage (ʿumūm al-majāz), is far from soundness and permissibility."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة المائدة: ١١٧.",
     "en": "Qurʾān, Sūrat al-Māʾida 5:117."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فأراد بيان الفصل على وجه لا يكون فيه اختلاف؛",
     "en": "So he wished to describe the separating [word] in a way that involves no disagreement,"},
    {"type": "pair",
     "ar": "إذ كونه على صيغة ضمير مرفوع منفصل متفق، وإن اختلف في كونه ضميرا وبعد كونه ضميرا في كونه ضميرا مرفوعا كما ستعرف،",
     "en": "since its being in the form of a separate nominative pronoun is agreed upon, even though there is disagreement over whether it is a pronoun, and, granted that it is a pronoun, over whether it is a nominative pronoun, as you will learn."},
    # REVIEW: «بين الجمع» printed; the sense may call for «بين الجميع»; transcribed as printed.
    {"type": "pair",
     "ar": "وفيه أن قوله: صيغة ضمير مرفوع يتبادر منه أنه ليس بضمير مرفوع، فليس مشتركا بين الجمع وأمرا متفقا، فاختياره للتنبيه على رجحانه عنده.",
     "en": "Against this: his words “the form of a nominative pronoun” suggest at first that it is not a nominative pronoun, so it is not common to all and agreed upon; his choosing it is therefore to signal that this view is preponderant in his eyes."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ولا يصح أن يجعل مطابقا للخبر كما يكون في الضمير،",
     "en": "It cannot be made to agree with the predicate, as happens with a pronoun,"},
    {"type": "pair",
     "ar": "فلا يصح كون ضمير المرفوعات هو ما اشتمل فصلا على تقدير كون المرفوعات مبتدأ، فمن تمسك به في دعوى أنه قد يطابق الخبر فقد سها.",
     "en": "so the pronoun in “al-marfūʿāt huwa mā ishtamala…” cannot be a separating pronoun on the supposition that “al-marfūʿāt” is the subject; whoever relies on it to claim that it sometimes agrees with the predicate has erred."},
    {"type": "pair",
     "ar": "قال عبد الغفور: ليشاكله، وقد يجعل مطابقا للخبر كما قيل: إن التذكير في ضمير المرفوعات باعتبار الخبر.",
     "en": "ʿAbd al-Ghafūr said: [it agrees with the subject] so as to correspond to it; but it is sometimes made to agree with the predicate, as has been said: the masculine in the pronoun of “al-marfūʿāt” is with respect to the predicate."},
]
