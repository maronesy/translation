# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 313 (printed ٣١٢)."""

PAGE_NUMBER = 313
PRINTED_PAGE = "٣١٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فصار المعنى باعتبار العطف «الواهب» at the foot of PDF p. 312.
    {"type": "matn",
     "ar": "عبدها»، فهو من باب «الضارب زيد» فكما لا يمتنع ذلك حيث أتى به بعض البلغاء لا يمتنع هذا.",
     "en": "…of its herdsman” (al-wāhib ʿabdihā), which belongs to the type “al-ḍārib Zaydin”; so just as that is not impossible, since one of the eloquent produced it, this is not impossible."},
    # REVIEW: the lemma prints «الماءة» (with hamza on the line) where the commentary and the verse below have «المائة»; transcribed as printed.
    {"type": "matn",
     "ar": "فأجاب المصنف عنه بقوله: (وضعف[[١]] «الواهب الماءة الهجان وعبدها») يعني: هذا القول ضعيف لا يقوى في الفصاحة بحيث يستدل به،",
     "en": "The author answered this with his words: (“al-wāhibu l-miʾati l-hijāni wa-ʿabdihā” is weak), meaning: this utterance is weak; it is not strong enough in eloquence to be cited as evidence,"},
    {"type": "matn",
     "ar": "لما عرفت من امتناع مثل: «الضارب زيد»[[٢]] لعدم الفائدة في الإضافة.",
     "en": "because of what you have learned of the impossibility of such as “al-ḍārib Zaydin,” for lack of benefit in the annexation."},
    {"type": "matn",
     "ar": "ولا يخفى أن فيه شوب مصادرة[[٣]] على المطلوب.",
     "en": "It is evident that there is a tinge of begging the question (muṣādara ʿalā al-maṭlūb) in this."},
    {"type": "matn",
     "ar": "اللهم إلا أن يقال[[٤]]: المراد به أنه ضعيف في الاستدلال به؛ إذ لا نص فيه على الجر[[٥]]،",
     "en": "Unless it is said that what is meant is that it is weak as evidence, since it is not explicit in the genitive;"},
    {"type": "matn",
     "ar": "فإنه يحتمل النصب حملا على المحل[[٦]] أو على أنه مفعول معه،",
     "en": "for it admits the accusative, by construing it on the [grammatical] position, or as a concomitant object (mafʿūl maʿahu);"},
    {"type": "matn",
     "ar": "أو لأنه قد يتحمل في المعطوف ما يتحمل في المعطوف عليه كما في «رب شاة وسخلتها» حيث جاز هذا التركيب ولم يجز «رب سخلتها» بإدخال «رب» على «سخلتها» بدون العطف،",
     "en": "or because what is tolerated in the coordinated term is [sometimes] what is tolerated in the term to which it is coordinated, as in “rubba shātin wa-sakhlatihā” (many a ewe and its lamb), where this construction is permitted, while “rubba sakhlatihā,” with “rubba” placed on “sakhlatihā” without coordination, is not."},
    {"type": "matn",
     "ar": "والبيت بتمامه:",
     "en": "The verse in full:"},
    {"type": "verse",
     "ar": "الواهب المائة الهجان وعبدها          عوذا يزجى خلفها أطفالها",
     "en": "The giver of the hundred white camels and their herdsman, / newly-delivered ones, their young driven along behind them."},
    {"type": "matn",
     "ar": "أي: ممدوحه الواهب المائة الهجان، أي: البيض من النوق يستوي فيه الجمع والواحد[[٧]]،",
     "en": "That is: the one he praises is the giver of the hundred hijān, that is, white she-camels; [the word hijān] is the same for plural and singular;"},
    {"type": "matn",
     "ar": "و«الهجان» صفة للمائة، أو بدل عنها أو من قبيل «الثلاثة الأثواب»[[٨]] كما هو مذهب الكوفيين،",
     "en": "“al-hijān” is an adjective of “al-miʾa,” or a substitute (badal) for it, or of the type “al-thalāthat al-athwāb,” as is the doctrine of the Kūfans;"},
    {"type": "matn",
     "ar": "و«عبدها» أي: راعيها[[٩]] تشبيها له بالعبد لقيامه بحق خدمتها، أو عبدها حقيقة بإضافته لأدنى ملابسة،",
     "en": "and “ʿabdihā,” that is, their herdsman, likening him to a slave because he fulfils the due of serving them; or their slave in the literal sense, its annexation [to them] resting on the slightest association;"},
    {"type": "matn",
     "ar": "«عوذا» -بالذال المعجمة- جمع عائذ أي:",
     "en": "“ʿūdhan,” with the dotted dhāl, is the plural of ʿāʾidh, that is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: print reads «ليسدل به» (expected «ليستدل به»); transcribed as printed.
    {"type": "pair",
     "ar": "الأولى أن يكون من التضعيف، يعني: ضعفه الفصحاء، فلم يكن موثوقا به ليسدل به. وحينئذ لا يتوجه مصادرة.",
     "en": "It is better that [ḍuʿʿifa] be from taḍʿīf (declaring weak), meaning: the eloquent declared it weak, so it is not reliable enough to be cited as evidence. In that case no charge of begging the question applies."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: امتناع «الضارب زيد» متقرر بحيث ينبغي أن يرد به ما يخالفه وإن كان قول الأعشى فلا يمكن أن يرد بقول الأعشى، وحينئذ لا شوب للمصادرة.",
     "en": "He means: the impossibility of “al-ḍārib Zaydin” is so firmly established that whatever contradicts it should be rejected by it, even if it is the saying of al-Aʿshā; so it cannot be rejected by al-Aʿshā’s saying. In that case there is no tinge of begging the question."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن إثبات المطلوب يتوقف على إبطال دليل الخصم، وإبطاله يتوقف على إثبات المطلوب.",
     "en": "Because establishing the thesis depends on refuting the opponent’s evidence, and refuting it depends on establishing the thesis."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا يخفى بعده لأن المتبادر ضعيف في التركيب لا في الاستدلال.",
     "en": "Its far-fetchedness is evident, because what first comes to mind is “weak in construction,” not “weak as evidence.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيه شيء؛ لأن رواية الجر مشهورة، وهي كافية في الاستدلال.",
     "en": "There is something [to be said] here, because the transmission with the genitive is well known, and that suffices as evidence."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: print reads «الحجر» (possibly for «الجر»); transcribed as printed.
    {"type": "pair",
     "ar": "فيه ضعف لأن مدار الاستدلال على نقل الموثوق به الحجر، ولولاه فيحمل المائة الهجان النصب على المفعولية، فلا يحتاج إلى دعوى نصب العبد حملا على المحل.",
     "en": "This is weak, because the argument turns on the reliable transmission of the ḥajr [as printed]; were it not for that, “al-miʾa al-hijān” would bear the accusative as an object, and there would be no need to claim the accusative for “al-ʿabd” by construing it on the position."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: هو مشترك بينهما كالفلك.",
     "en": "That is, it is shared between them, like “al-fulk” (ship, ships)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "وحينئذ يكون وجه آخر لضعف البيت.",
     "en": "In that case there would be another ground for the weakness of the verse."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    # REVIEW: «للمدوح» as printed (expected «للممدوح»); «بتعبد» as printed (perhaps «يتعبد»).
    # REVIEW: «الحديثان النتائج» as printed (sense unclear; perhaps «الحديثات النتاج»); transcribed as printed.
    {"type": "pair",
     "ar": "في إضافة العبد إلى المائة مزيد مدح للمدوح بأنه يهب عبدا بتعبد مائة من الإبل الحديثان النتائج مع أطفالها،",
     "en": "In annexing “al-ʿabd” to “al-miʾa” there is added praise of the one praised, in that he gives a slave who tends a hundred camels that have recently given birth [al-ḥadīthān al-natāʾij, as printed], together with their young;"},
    {"type": "pair",
     "ar": "وهذا أعز من المائة كثيرا ما يوجد بخلاف مثل هذا العبد.",
     "en": "and this is rarer than the hundred [camels], which is often found, unlike such a slave."},
]
