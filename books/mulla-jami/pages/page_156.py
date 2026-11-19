# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 156 (printed ١٥٥)."""

PAGE_NUMBER = 156
PRINTED_PAGE = "١٥٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "واحترز به عن القسم الثاني من المبتدأ.",
     "en": "By it he excluded the second kind of mubtadaʾ."},
    {"type": "matn",
     "ar": "ولك أن تقول: المراد المسند به[[١]] إلى المبتدأ، أو تجعل الباء «به» بمعنى «إلى»[[٢]]، والضمير المجرور راجعا إلى المبتدأ،",
     "en": "You may also say: what is meant is “predicated (al-musnad bihi) of the mubtadaʾ”; or you may take the bāʾ of “bihi” in the sense of “ilā” (to), with the genitive pronoun referring to the mubtadaʾ;"},
    {"type": "matn",
     "ar": "وعلى التقديرين يخرج به القسم الثاني من المبتدأ[[٣]]، ويكون قوله: «المغاير للصفة المذكورة» تأكيدا.",
     "en": "on both constructions the second kind of mubtadaʾ is excluded by it, and his words “other than the aforementioned adjective” are a reinforcement (taʾkīd)."},
    {"type": "matn",
     "ar": "واعلم أن العامل في المبتدأ والخبر هو الابتداء، أي: تجريد الاسم عن العوامل اللفظية؛ ليسند إلى شيء[[٤]] أو يسند إليه[[٥]] شيء.",
     "en": "Know that the governor of the mubtadaʾ and the khabar is inception (al-ibtidāʾ), that is: the stripping of the noun of overt governors so that it may be predicated of something, or something may be predicated of it."},
    # The print sets a full stop after «المبتدأ» and begins a new line with «والخبر»;
    # the two lines form one statement and are kept together here.
    {"type": "matn",
     "ar": "فمعنى الابتداء عامل في المبتدأ. والخبر رافع لهما عند البصريين.",
     "en": "So the abstract notion of inception is the governor in the mubtadaʾ and the khabar, putting both of them in the nominative, according to the Baṣrans."},
    {"type": "matn",
     "ar": "وأما عند غيرهم:",
     "en": "As for others:"},
    {"type": "matn",
     "ar": "فقال بعضهم[[٦]]: الابتداء عامل في المبتدأ، والمبتدأ عامل في الخبر.",
     "en": "some of them said: inception is the governor in the mubtadaʾ, and the mubtadaʾ is the governor in the khabar."},
    {"type": "matn",
     "ar": "وقال آخرون[[٧]]: كل واحد من المبتدأ والخبر عامل في الآخر.",
     "en": "Others said: each of the mubtadaʾ and the khabar is the governor in the other."},
    {"type": "matn",
     "ar": "وعلى هذا لا يكونان مجردين عن العوامل اللفظية.",
     "en": "On this [view] the two are not stripped of overt governors."},

    {"type": "section", "ar": "[ الأصل في المبتدأ ]",
     "en": "The Norm for the Subject (al-Aṣl fī al-Mubtadaʾ)"},

    {"type": "matn",
     "ar": "(وأصل المبتدإ) أي: ما ينبغي أن يكون المبتدأ عليه إذا لم يمنع مانع (التقديم)",
     "en": "(And the norm for the mubtadaʾ—wa-aṣlu al-mubtadaʾi), that is: what the mubtadaʾ ought to be in when no impediment prevents it, (is precedence—al-taqdīmu)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إلى المبتدأ بقرينة أنهما ركنان متلازمان، كما أشار إليه بذكرهما معا في العنوان.",
     "en": "[Predicated] of the mubtadaʾ, by the indication that the two are mutually entailing pillars, as he pointed to by mentioning them together in the heading."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قال في الحاشية: وكأن النكتة في تغيير العبارة ألا يشتبه بالمسند إليه المذكور في تعريف المبتدأ،",
     "en": "He said in al-Ḥāshiya: it seems the subtle point (nukta) in changing the wording is that it not be confused with the “subject of predication” (musnad ilayhi) mentioned in the definition of the mubtadaʾ;"},
    {"type": "pair",
     "ar": "وحينئذ يظهر لقوله: «به» فائدة، وإلا لا حاجة إليه.",
     "en": "then his word “bihi” shows a benefit; otherwise there is no need for it."},
    {"type": "pair",
     "ar": "قد بينا وجه عدم الاحتياج إليه.",
     "en": "We have explained why it is not needed."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "كما يخرج به «يضرب» في «يضرب زيد»،",
     "en": "Just as “yaḍribu” in “yaḍribu Zaydun” is excluded by it."},
    {"type": "pair",
     "ar": "لكن فيه أن «ضارب» في «زيد ضارب» وفي «زيد ضارب أبوه» يخرج عنه؛ لأنه مسند إلى فاعله، لا إلى المبتدأ مع أنه خبر.",
     "en": "But there is [a difficulty] in it: “ḍārib” in “Zaydun ḍāribun” and in “Zaydun ḍāribun abūhu” (Zayd—his father is striking) is excluded from it, because it is predicated of its own agent, not of the mubtadaʾ, although it is a khabar."},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: إن الخبر هو مجموع اسم الفاعل وفاعله لا اسم الفاعل وحده،",
     "en": "O God, unless it is said: the khabar is the whole of the active participle and its agent, not the active participle alone;"},
    {"type": "pair",
     "ar": "لكن لما لم يكن المجموع قابلا للإعراب أجري الإعراب على الجزء القابل للإعراب،",
     "en": "but since the whole is not receptive of inflection, the inflection was applied to the part receptive of inflection;"},
    {"type": "pair",
     "ar": "أو يقال: المراد بالإسناد إلى المبتدأ أعم من أن يكون إسنادا إلى المبتدأ نفسه، كما في «زيد جسم» أو إلى ضميره أو إلى متعلقه.",
     "en": "or it is said: what is meant by predication of the mubtadaʾ is more general than predication of the mubtadaʾ itself, as in “Zayd is a body” (Zaydun jismun), or of its pronoun, or of something connected with it."},
    {"type": "pair",
     "ar": "وفيه نظر لأن «ضاربا» لم يسند إلى شيء أصلا؛ لأن الإسناد هو النسبة التامة، ونسبة «ضارب» إلى فاعله ليست تامة،",
     "en": "This is open to examination, because “ḍārib” is not predicated of anything at all; for predication is the complete relation (al-nisba al-tāmma), and the relation of “ḍārib” to its agent is not complete;"},
    {"type": "pair",
     "ar": "ولأنه يصدق على «يضرب» في «زيد يضرب أبوه»، و«يضرب» في «زيد يضرب» و«يضرب» في «زيد أبوه يضرب» مع أنها ليست أخبارا لـ«زيد».",
     "en": "and because it is true of “yaḍribu” in “Zaydun yaḍribu abūhu,” of “yaḍribu” in “Zaydun yaḍribu,” and of “yaḍribu” in “Zaydun abūhu yaḍribu,” although these are not predicates of “Zayd.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كما في القسم الثاني من المبتدأ.",
     "en": "As in the second kind of mubtadaʾ."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "كما في القسم الأول منه.",
     "en": "As in its first kind."},
    {"type": "pair",
     "ar": "وهذا القيد لإخراج تجرد الأسماء المعدودة؛ لأنه للعد لا للإسناد.",
     "en": "This qualification is to exclude the strippedness of enumerated nouns, because it is for counting, not for predication."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وهو سيبويه.",
     "en": "He is Sībawayh."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "وهم الكسائي والفراء ومن معهما.",
     "en": "They are al-Kisāʾī, al-Farrāʾ and those with them."},
]
