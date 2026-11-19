# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 202 (printed ٢٠١)."""

PAGE_NUMBER = 202
PRINTED_PAGE = "٢٠١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues from p.201: «… المشابهة لفظا ومعنى لكاف الخطاب»
    {"type": "matn",
     "ar": "الحرفية[[١]]، وكونه مثلها إفرادا وتعريفا[[٢]]،",
     "en": "…that is a particle, and because it is like it in being single and definite."},
    {"type": "matn",
     "ar": "وذلك لأن «يا زيد» بمنزلة «أدعوك»، وهذه الكاف ككاف «ذلك» لفظا ومعنى.",
     "en": "That is because “yā Zaydu” is equivalent to “I call you” (adʿūka), and this kāf is like the kāf of “dhālika” in form and meaning."},
    {"type": "matn",
     "ar": "وإنما قلنا: «ذلك»؛ لأن الاسم لا يبنى إلا لمشابهته الحرف أو الفعل، ولا يبنى لمشابهته الاسم المبني.",
     "en": "We said “dhālika” only because a noun is made indeclinable only for its resemblance to a particle or a verb, and is not made indeclinable for its resemblance to an indeclinable noun."},
    {"type": "matn",
     "ar": "(مثل: «يا زيد» و«يا رجل») مثالان لما هو مبني على الضمة،",
     "en": "(Such as “yā Zaydu” and “yā rajulu”—O man): two examples of what is indeclinable on the ḍamma,"},
    {"type": "matn",
     "ar": "أولهما معرفة قبل النداء، وثانيهما معرفة بعد النداء.",
     "en": "the first of them definite before the vocative, the second definite after the vocative."},
    {"type": "matn",
     "ar": "(و«يا زيدان»[[٣]]) مثال المبني على الألف.",
     "en": "(And “yā Zaydāni”): an example of what is indeclinable on the alif."},
    {"type": "matn",
     "ar": "(ويا زيدون) مثال المبني على الواو.",
     "en": "(And yā Zaydūna): an example of what is indeclinable on the wāw."},
    {"type": "matn",
     "ar": "(ويخفض) أي: ينجر المنادى (بلام الاستغاثة[[٤]]) أي: بلام تدخله وقت الاستغاثة[[٥]] به،",
     "en": "(And it is put in the genitive—wa-yukhfaḍu), that is, the munādā takes the genitive, (by the lām of calling for help—bi-lām al-istighātha), that is, by a lām that enters it at the time of calling on it for help;"},
    {"type": "matn",
     "ar": "وهي لام التخصيص[[٦]] أدخلت على المستغاث دلالة[[٧]] على أنه مخصوص من بين أمثاله بالدعاء",
     "en": "it is the lām of specification (lām al-takhṣīṣ), placed on the one called for help (mustaghāth) to indicate that he is singled out from among his like for the call,"},
    {"type": "matn",
     "ar": "(نحو: «يا لزيد»[[٨]]) وإنما فتحت لئلا يلتبس بالمستغاث له[[٩]] إذا حذف المستغاث",
     "en": "(as in “yā la-Zaydin”—O Zayd, [help]!). It was given a fatḥa only so that it is not confused with [the lām of] the one for whom help is sought (mustaghāth lahu) when the mustaghāth is elided,"},
    {"type": "matn",
     "ar": "نحو: «يا للمظلوم»[[١٠]] أي: «يا قوم»،",
     "en": "as in “yā li-l-maẓlūmi” (O, for the wronged one!), that is: “O people.”"},
    {"type": "matn",
     "ar": "فإنه لو لم يفتح لام المستغاث لم يعلم أن المظلوم في هذا المثال مستغاث أو مستغاث له، ولم يعكس الأمر؛ لأن",
     "en": "For had the lām of the mustaghāth not been given a fatḥa, it would not be known whether “the wronged one” in this example is the one called for help or the one for whom help is sought. The matter was not reversed, because…"},

    {"type": "rule"},

    # ---------------- Footnote continued from p.201 (note ١٢ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "إلى الظاهر لئلا يتسارع إلى فهم كل واحد من الحضار أنه هو المخاطب والمدعو.",
     "en": "…to the explicit noun, lest each one of those present hasten to understand that he is the one addressed and called."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فقولهم: المبني ما ناسب مبني الأصل بمعنى المناسبة له بواسطة أو بغير واسطة.",
     "en": "So their saying “the indeclinable is what is akin to the originally indeclinable” means kinship to it with or without an intermediary."},
    {"type": "pair",
     "ar": "ويمكن أن يجعل علة البناء عروض الحاجة للمنادى في الدلالة على المعنى المراد منه إلى قرينة التخاطب كالضمير للمخاطب، فيبنى لتلك المشابهة بالحرف،",
     "en": "The cause of indeclinability may be taken to be that the munādā comes to need, in indicating the meaning intended by it, the context of address, like the second-person pronoun; so it is made indeclinable for that resemblance to the particle."},
    {"type": "pair",
     "ar": "وتلك الحاجة وإن فقدت بالعلم لكن لم يعتبر فقدانه طردا للباب.",
     "en": "Though that need is absent with the proper name, its absence was not taken into account, for the sake of keeping the rule uniform (ṭardan li-l-bāb)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إنما اعتبرهما ليتقوى جهة الاتحاد، ولا يلزم بناء المضاف وما في حكمه والنكرة الغير المعينة.",
     "en": "He took both into account only so that the respect of identity is strengthened, and so that indeclinability does not follow for the annexed noun, what has its status, and the unspecified indefinite."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إن قيل: العلم إذا ثنى أو جمع لزم فيه اللام بدلا من تعريفه الزائل بالتنكير، فكيف يصح هذان المثالان؟",
     "en": "If it is said: when a proper name is put in the dual or plural, the definite article becomes necessary in it in place of its definiteness, which is lost by its becoming indefinite; so how are these two examples sound?"},
    {"type": "pair",
     "ar": "أجيب عنه: بأن لفظة «يا» قائمة مقام اللام.",
     "en": "It was answered that the word “yā” stands in place of the article."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "خص لفظة «يا» بالاستغاثة.",
     "en": "The word “yā” is reserved for calling for help."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يعني: الإضافة لأدنى ملابسة، وليس من قبيل إضافة اللفظ إلى مدلوله، كما هو المتبادر.",
     "en": "He means: the annexation [in “lām al-istighātha”] is for the slightest connection, and is not of the type of annexing an expression to what it signifies, as first comes to mind."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "مقوية لـ«أدعو» المقدر لضعفه بالإضمار.",
     "en": "Strengthening the implied “adʿū” (I call), since it is weakened by being implied."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "على أنه مخصوص هذه الدلالة لا بد أن يكون لأمر يعتنى به،",
     "en": "[The indication] that he is singled out: this indication must be for a matter of concern;"},
    {"type": "pair",
     "ar": "وذلك الأمر المعتنى به يجوز أن يكون إغاثة أو تعجبا أو تهديدا إلى غير ذلك، لكن لم تقع تلك الدلالة حالة النداء إلا مع أحد الثلاثة.",
     "en": "that matter of concern may be rescue, wonder, threat and so on; but that indication does not occur in the vocative except with one of the three."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "قال بعض المحققين: لا يكون الاستغاثة بغير كلمة «يا»، ولا يكون لام الاستغاثة إلا في مقام الإغاثة أو التعجب أو التهديد.",
     "en": "One of the verifying scholars (muḥaqqiqīn) said: calling for help is not done with any word but “yā,” and the lām of calling for help occurs only in a setting of rescue, wonder or threat."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "واللام في المستغاث له متعلقة بما تعلق به لام المستغاث،",
     "en": "The lām in the mustaghāth lahu is attached to what the lām of the mustaghāth is attached to."},
    {"type": "pair",
     "ar": "وقد يستعمل المستغاث له بمن نحو: يا الله من ألم الفراق، وهو متعلق بما دل عليه ما قبله من الكلام أي: أستغيث بالله من ألم الفراق.",
     "en": "The mustaghāth lahu is sometimes used with “min,” as in “O Allah, from the pain of separation!”; it is attached to what the preceding words indicate, that is: “I seek help from Allah against the pain of separation.”"},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "المناسب بكون القوم منادى مستغاثا أن يقال في التقدير: يا لقوم أو يا قوما.",
     "en": "What suits “the people” being a munādā called for help is that one say in the implied form: “yā la-qawmi” or “yā qawmā.”"},
]
