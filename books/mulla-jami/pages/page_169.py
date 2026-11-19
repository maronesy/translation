# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 169 (printed ١٦٨)."""

PAGE_NUMBER = 169
PRINTED_PAGE = "١٦٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "الفاء فيه. وأما إذا لم يقصد، فلم يجب دخوله فيه، بل يجب عدمه.",
     "en": "…the fāʾ into it is obligatory. But when it is not intended, its entry into it is not obligatory; rather its absence is obligatory."},
    {"type": "matn",
     "ar": "(وذلك) المبتدأ المتضمن معنى الشرط إما (الاسم الموصول بفعل[[١]] أو ظرف[[٢]]) أي: الذي جعلت صلته جملة فعلية أو ظرفية مؤولة بجملة فعلية ههنا بالاتفاق.",
     "en": "“And that”—the mubtadaʾ implicitly containing the meaning of the condition—is either “the noun made relative (al-ism al-mawṣūl) by a verb or an adverbial phrase (ẓarf),” that is, one whose relative clause has been made a verbal sentence, or an adverbial one construed as a verbal sentence—here by agreement."},
    {"type": "matn",
     "ar": "وإنما اشترط أن يكون صلته فعلا أو ظرفا مؤولا بالفعل، ليتأكد مشابهته الشرط؛ لأن الشرط لا يكون إلا فعلا،",
     "en": "He stipulated that its relative clause be a verb or an adverbial phrase construed as a verb only so that its resemblance to the condition would be reinforced, since the condition can only be a verb."},
    {"type": "matn",
     "ar": "وفي حكم الاسم الموصول المذكور الاسم الموصوف به[[٣]].",
     "en": "Taking the ruling of the relative noun mentioned is the noun qualified by it."},
    {"type": "matn",
     "ar": "(أو النكرة الموصوفة بهما[[٤]]) أي: بأحدهما، وفي حكمها الاسم المضاف إليها",
     "en": "“Or the indefinite noun qualified by the two,” that is, by one of them; and taking its ruling is the noun annexed to it;"},
    {"type": "matn",
     "ar": "(مثل: «الذي يأتيني[[٥]]») هذا مثال للاسم الموصول بفعل.",
     "en": "“as in: ‘He who comes to me’ (alladhī yaʾtīnī)”—this is an example of the noun made relative by a verb;"},
    {"type": "matn",
     "ar": "(أو) الذي (في الدار[[٦]]) هذا مثال للاسم الموصول بظرف، (فله درهم).",
     "en": "“or” he who [is] “in the house”—this is an example of the noun made relative by an adverbial phrase—“shall have a dirham” (fa-lahu dirhamun)."},
    {"type": "matn",
     "ar": "وأما مثال للاسم الموصوف بالاسم الموصول المذكور، فقوله تعالى: ﴿قل إن الموت الذي تفرون منه فإنه ملاقيكم[[٧]]﴾[[٨]]،",
     "en": "As for an example of the noun qualified by the relative noun mentioned, it is His words, the Exalted: “Say: the death from which you flee will surely meet you,”"},
    {"type": "matn",
     "ar": "(و) مثل: («كل رجل يأتيني[[٩]]») هذا مثال للاسم الموصوف بفعل.",
     "en": "“and” the like of “Every man who comes to me”—this is an example of the noun qualified by a verb."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ماضيا كان باقيا على معناه أو غيره على خلاف الشرط، فإنه لا يكون إلا مستقبلا في المعنى، والأول هنا قليل، والشرط لا يكون ظرفا أيضا.",
     "en": "Whether it is a past [verb] retaining its meaning or otherwise—unlike the condition, which can only be future in meaning; the former is rare here. And the condition cannot be an adverbial phrase either."},
    {"type": "pair",
     "ar": "قيل: لا ينحصر هذا فيما ذكره؛ لأن المبتدأ الذي دخل عليه «أما» والمبتدأ الذي يكون أحد الأسماء المتضمنة بمعنى الشرط أيضا كذلك،",
     "en": "It has been said: this is not restricted to what he mentioned, because the mubtadaʾ on which “ammā” has entered, and the mubtadaʾ that is one of the nouns implicitly containing the meaning of the condition, are likewise so."},
    {"type": "pair",
     "ar": "وهذا مما يقضى منه العجب، فإن مدخول «أما» والأسماء المتضمنة لمعنى الشرط كالشرط في الفاء، وليست مصححة لدخولها.",
     "en": "This is astonishing; for what “ammā” enters upon and the nouns implicitly containing the meaning of the condition are like the condition with respect to the fāʾ, and they do not [merely] make its entry valid."},
    {"type": "pair",
     "ar": "ولا نقض بالاسم الموصول باسم الفاعل والمفعول؛ لأنه الموصول بفعل معنى.",
     "en": "There is no counter-case in the noun made relative by an active or passive participle, because it is made relative by a verb in meaning."},
    {"type": "pair",
     "ar": "قال عبد الغفور: أو ما في قوته كاسمي الفاعل والمفعول الواقعين صلة للام الموصولة.",
     "en": "ʿAbd al-Ghafūr said: or what is equivalent to it, such as the active and passive participles occurring as the relative clause of the relative lām."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أراد به الزمان والمكان والجار والمجرور.",
     "en": "By it he meant [adverbs of] time and place, and the preposition with its object."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأنهما في حكم لفظ واحد. وكذا الحال في المضاف والمضاف إليه.",
     "en": "Because the two count as a single expression. The same holds for the annexed noun and the noun annexed to (al-muḍāf wa-l-muḍāf ilayhi)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ينبغي أن يقول: «به»؛ لأن العائد إلى المعطوف والمعطوف عليه بـ«أو» يفرد.",
     "en": "He ought to have said “bihi” (by it); because the pronoun referring to two terms conjoined by “aw” is singular."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الأغلب في صلة الموصول صيغة الاستقبال. وقد جاء الماضي بمعنى الاستقبال أيضا، وهو غير نادر.",
     "en": "The prevailing form in the relative clause is the future form. The past has also come in the sense of the future, and this is not rare."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ليست لفظة «أو» للتردد، بل للتخيير بين العبارتين.",
     "en": "The word “aw” is not for doubt, but for choice between the two expressions."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "إن قيل: الموصول ليس عاما؛ إذ لا يريد أن كل موت تفرون منه يلقاكم؛ إذ رب موت فر منه الشخص فما لاقاه كالموت بالقتل،",
     "en": "If it is said: the relative is not general here, since He does not mean that every death you flee from will meet you; for many a death has a person fled from and not met, such as death by being killed;"},
    {"type": "pair",
     "ar": "فالمراد الجنس، وصحة دخول الفاء مبنية على العموم؛ إذ به يصير مشبها بأسماء الشرط في العموم والإبهام، فتكون الفاء فيه زائدة أو يكون الموصول خبرا؟",
     "en": "so what is meant is the genus; yet the validity of the fāʾ's entry rests on generality, since by it [the relative] comes to resemble the conditional nouns in generality and indeterminacy; so is the fāʾ in it redundant, or is the relative the khabar?"},
    {"type": "pair",
     "ar": "قلنا: قال الشيخ الرضي: لا يجب العموم في الموصول كما في أسماء الشرط لما ذكرنا في وجه المخالفة، نعم، الأغلب فيه العموم.",
     "en": "We say: Shaykh al-Raḍī said: generality is not required in the relative as it is in the conditional nouns, for the reason we mentioned regarding how they differ; though generality is indeed the more common in it."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سورة الجمعة: ٨.",
     "en": "Qurʾān, Sūrat al-Jumuʿa 62:8."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فإن قلت: المبتدأ هو «كل» لا «رجل»، فيكون مثالا للمضاف إلى الموصوف بفعل لا للمبتدأ النكرة الموصوفة بفعل؟",
     "en": "If you say: the mubtadaʾ is “kull,” not “rajul,” so it is an example of the noun annexed to [a noun] qualified by a verb, not of the indefinite mubtadaʾ qualified by a verb?"},
    {"type": "pair",
     "ar": "قلت: لا نسلم ذلك، بل الموصوف في هذا المثال هو «كل رجل».",
     "en": "I say: we do not grant that; rather, what is qualified in this example is “kullu rajulin.”"},
]
