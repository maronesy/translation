# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 152 (printed ١٥١)."""

PAGE_NUMBER = 152
PRINTED_PAGE = "١٥١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "«أعطي درهم زيدا»، وذلك عند الأمن من اللبس.",
     "en": "…“A dirham was given to Zayd” (uʿṭiya dirhamun Zaydan); and that is when there is safety from ambiguity (labs)."},
    {"type": "matn",
     "ar": "وأما عند عدمه[[١]]، فيجب إقامة المفعول الأول، نحو: «أعطي زيد عمرا».",
     "en": "But where it is absent, setting the first object [in the agent’s place] is obligatory, as in: “Zayd was given ʿAmr” (uʿṭiya Zaydun ʿAmran)."},

    {"type": "section", "ar": "[ المبتدأ والخبر ]",
     "en": "The Subject and the Predicate (al-Mubtadaʾ wa-l-Khabar)"},

    {"type": "matn",
     "ar": "(ومنها: المبتدأ[[٢]] والخبر) وفي بعض النسخ: «ومنه»[[٣]]،",
     "en": "(And among them are the subject and the predicate—wa-minhā al-mubtadaʾu wa-l-khabaru); in some copies: “and among it” (wa-minhu);"},
    {"type": "matn",
     "ar": "يعني: من جملة المرفوعات، أو من جملة المرفوع[[٤]]: المبتدأ والخبر،",
     "en": "meaning: among the nominatives (al-marfūʿāt), or among the nominative (al-marfūʿ), are the mubtadaʾ and the khabar."},
    {"type": "matn",
     "ar": "جمعهما في فصل واحد؛ للتلازم الواقع بينهما على ما هو الأصل فيهما[[٥]]، واشتراكهما في العامل المعنوي[[٦]].",
     "en": "He brought the two together in a single section because of the mutual entailment between them, according to what is the norm (aṣl) in them, and because they share the abstract governor (al-ʿāmil al-maʿnawī)."},
    {"type": "matn",
     "ar": "(فالمبتدأ: هو[[٧]] الاسم[[٨]]) لفظا[[٩]] أو تقديرا، ليتناول، نحو: ﴿وأن تصوموا خير",
     "en": "(So the mubtadaʾ is the noun—fa-l-mubtadaʾu huwa al-ismu), overtly or by implication (taqdīran), so that [the definition] includes such as: “And that you fast is better…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قلت: يجوز دفع الالتباس بلزوم المفعول الثاني في مركزه؟",
     "en": "If you say: may the ambiguity not be removed by the second object keeping to its [proper] position?"},
    {"type": "pair",
     "ar": "قلنا: خوف الالتباس باق؛ لأن التأخير وإن دل على أنه مفعول ثان،",
     "en": "We say: the danger of ambiguity remains; for the postposition, even though it indicates that it is a second object,"},
    {"type": "pair",
     "ar": "لكنه لما كان مع ذلك صالحا لأن يكون مفعولا أولا، وهو أولى بأن يقوم مقام الفاعل، أمكن أن تقع الحيرة والاشتباه،",
     "en": "yet since it is, along with that, fit to be a first object—and that is more entitled to stand in the place of the agent—perplexity and confusion may arise;"},
    {"type": "pair",
     "ar": "وكثيرا ما يحترز عن خوف اللبس.",
     "en": "and often one takes precautions against the danger of ambiguity."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "عطف على قوله: «فمنه الفاعل».",
     "en": "Conjoined to his words: “Among them is the agent.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأوجه أن المراد حينئذ: ومن الفاعل،",
     "en": "The more sound [view] is that what is then meant is: “and among [the appendages of] the agent”;"},
    {"type": "pair",
     "ar": "وفائدته التنبيه على أنه من ملحقات الفاعل، ولذا جعل الرفع علم الفاعلية.",
     "en": "its benefit is to draw attention to its being among the appendages (mulḥaqāt) of the agent; and for this reason the nominative was made the mark of agency."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "بيان لحاصل المعنى لا أن «من» للتبعيض.",
     "en": "An explanation of the gist of the meaning, not [a claim] that “min” is partitive (li-l-tabʿīḍ)."},
    {"type": "pair",
     "ar": "ويحتمل أن يراد التبعيض بتقدير المضاف، أي: من جملة أفراده.",
     "en": "It is possible that the partitive sense is intended, with an implied first term of annexation (muḍāf), that is: among its individual instances."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: في باب المبتدأ والخبر، وهو أن يكون المبتدأ مسندا إليه دون ما إذا كان مسندا،",
     "en": "That is: in the chapter of the mubtadaʾ and the khabar, namely that the mubtadaʾ is a subject of predication (musnad ilayhi), not where it is a predicate (musnad);"},
    {"type": "pair",
     "ar": "فإنه مبتدأ يصار إليه للضرورة،",
     "en": "for that is a mubtadaʾ resorted to out of necessity."},
    {"type": "pair",
     "ar": "فلهذا لم يكن «قائم» في «أقائم أبوه زيد» مبتدأ لاحتمال أن يكون خبرا لـ«زيد».",
     "en": "For this reason “qāʾim” in “a-qāʾimun abūhu Zaydun” (Is his father standing, Zayd?) is not a mubtadaʾ, because of the possibility that it is a khabar of “Zayd.”"},
    {"type": "pair",
     "ar": "وليس لهذا القسم من المبتدأ خبر؛ لأنه مع مرفوعه كلام تام كالفعل مع فاعله،",
     "en": "This kind of mubtadaʾ has no khabar, because together with what it puts in the nominative it is a complete utterance, like the verb with its agent;"},
    {"type": "pair",
     "ar": "فلا معنى لتقدير خبر مسند إليه، كما تكلفه كثير من النحاة.",
     "en": "so there is no sense in supposing an implied khabar predicated of it, as many grammarians have laboured to do."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وهو ههنا تجريد الاسم عن العوامل اللفظية للإسناد، أي: إسناده إلى شيء أو إسناد شيء إليه.",
     "en": "Here it is the stripping (tajrīd) of the noun of overt governors for the sake of predication, that is: its being predicated of something or something’s being predicated of it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قيل: أتى بصيغة الفصل الدالة على الحصر هنا دون الحدين السابقين مع أن الحصر مستفاد من مقام التعريف للزوم اطراده وانعكاسه،",
     "en": "It has been said: he used the form of the separating pronoun (ṣīghat al-faṣl), which indicates restriction (ḥaṣr), here and not in the two preceding definitions—although restriction is understood from the setting of definition, since a definition must be both inclusive and exclusive (iṭṭirād wa-inʿikās)—"},
    {"type": "pair",
     "ar": "إما لأنه اكتفى في بعض الحدود بدلالة صورة التصريح على صورة الاكتفاء،",
     "en": "either because he made do, in some of the definitions, with the explicit form indicating [the restriction] for the form in which it is left implicit;"},
    {"type": "pair",
     "ar": "أو لأنه أراد التصريح بالحصر ليكون ردا على من زعم أن اسم الفعل مبتدأ.",
     "en": "or because he wished to state the restriction explicitly so that it would be a rejection of whoever claimed that the verbal noun (ism al-fiʿl) is a mubtadaʾ."},
    {"type": "pair",
     "ar": "وفيه نظر، لأن صيغة الفصل تفيد حصر المسند لا حصر المسند إليه.",
     "en": "This is open to examination, because the form of separation conveys restriction of the predicate, not restriction of the subject of predication."},
    {"type": "pair",
     "ar": "ولو سلم ذلك فهي لتأكيد الحصر؛ لأن المسند إليه إذا عرف باللام يفيد حصره على المسند.",
     "en": "Even if that were granted, it would serve to reinforce the restriction, since the subject of predication, when made definite by the lām, conveys its restriction to the predicate."},
    {"type": "pair",
     "ar": "ولو سلم أنها لأصل الحصر، فنقول: إن اسم الفعل مبتدأ عند المصنف، فكيف يصح الحصر على زعمه؟",
     "en": "And even if it were granted that it serves for the restriction itself, we say: the verbal noun is a mubtadaʾ according to the author, so how can the restriction be valid on his own claim?"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: أراد حصر المبتدأ الذي اتفق عليه، ومن الواجب أن يحمل عليه ليصح التعريف.",
     "en": "O God, unless it is said: he intended the restriction of the mubtadaʾ that is agreed upon, and it must be construed so for the definition to be valid."},
    {"type": "pair",
     "ar": "ولا يخفى أن الحصر حينئذ ليس للرد.",
     "en": "It is not hidden that the restriction is then not for the sake of rejection."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "لم يرد بالاسم ما يقابل الصفة، كما تقتضيه مقابلته للصفة،",
     "en": "By “noun” he did not mean what is contrasted with the adjective (ṣifa), as its being contrasted with the adjective would require,"},
    {"type": "pair",
     "ar": "لجواز أن يكون هذا القسم من المبتدأ صفة مثل «ضارب» في «زيد ضارب» محمول على «زيد».",
     "en": "because it is possible for this kind of mubtadaʾ to be an adjective, like “ḍārib” in “Zayd is striking” (Zaydun ḍāribun), [which is] predicated of “Zayd.”"},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "أي: بلا تأويل، نحو: «زيد» في «زيد قائم»، أو تقديرا، أي: تأويلا.",
     "en": "That is: without interpretive recasting (taʾwīl), as “Zayd” in “Zayd is standing”; or by implication, that is: by interpretive recasting."},
    {"type": "pair",
     "ar": "فإن قوله: \"أن تصوموا\" في تأويل: صيامكم، والمضاف إليه خارج،",
     "en": "For His words “that you fast” are to be recast as “your fasting,” the second term of the annexation (muḍāf ilayhi) being outside [the definition];"},
    {"type": "pair",
     "ar": "وكذلك \"تسمع بالمعيدي خير من أن تراه\" في تقدير: سماعك بالمعيدي خير،",
     "en": "likewise “That you hear of al-Muʿaydī is better than that you see him” is in the implied sense of: “Your hearing of al-Muʿaydī is better”;"},
    {"type": "pair",
     "ar": "وكذلك قولك: زيد قائم قضية في تقدير هذا اللفظ، وقولك: الحيوان الناطق ينتقل بنقل قدميه،",
     "en": "and likewise your saying: “‘Zayd is standing’ is a proposition,” in the implied sense of “this expression,” and your saying: “‘Rational animal’ moves by moving its two feet”;"},
    {"type": "pair",
     "ar": "فكان داخلا في الاسم التقديري.",
     "en": "so it falls within the implied noun."},
]
