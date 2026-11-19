# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 117 (printed ١١٦)."""

PAGE_NUMBER = 117
PRINTED_PAGE = "١١٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The main commentary (matn) ----------------
    {"type": "matn",
     "ar": "(فشرطه) أي: شرط الألف والنون في منعهما من الصرف، وإفراد الضمير باعتبار أنهما سبب واحد[[١]]، أو شرط ذلك الاسم[[٢]] في امتناعه من الصرف[[٣]] (العلمية[[٤]]) تحقيقا للزوم زيادتهما، أو ليمتنع التاء[[٥]]، فيتحقق شبههما بألفي التأنيث، (كعمران[[٦]]",
     "en": "(So its condition) — that is, the condition of the alif and nūn for their preventing [the noun] from full inflection, the pronoun being made singular in view of their being a single cause; or the condition of that noun for its being barred from inflection — is (being a proper name), so as to realize the necessity of their being augmentative, or so that the tāʾ be barred, whereby their resemblance to the two alifs of the feminine is realized. (As in ʿImrān,"},
    {"type": "matn",
     "ar": "أو) كانا (في صفة[[٧]]، فانتفاء فعلانة) أي: إن كان الألف والنون في صفة، فشرطه انتفاء «فعلانة»، يعني: امتناع دخول تاء التأنيث عليه، ليبقى مشابهتهما لألفي التأنيث على حالها،",
     "en": "or) the two occur (in a qualifier, then [the condition is] the absence of a faʿlāna [feminine form]) — that is: if the alif and nūn occur in a qualifier, then its condition is the absence of “faʿlāna,” meaning that the tāʾ of femininity is barred from entering upon it, so that their resemblance to the two alifs of the feminine remains as it is;"},
    {"type": "matn",
     "ar": "ولهذا انصرف «عريان» مع أنه صفة؛ لأن مؤنثه «عريانة».",
     "en": "and for this reason “ʿuryān” (naked) is fully inflected, even though it is a qualifier, because its feminine is “ʿuryāna.”"},
    {"type": "matn",
     "ar": "(وقيل) شرطه: (وجود فعلى[[٨]])؛ لأنه متى كان مؤنثه «فعلى» لا يكون «فعلانة»، فيبقى مشابهتهما لألفي التأنيث على حالها.",
     "en": "(And it is said) that its condition is (the existence of a faʿlā [feminine form]); because whenever its feminine is “faʿlā” it cannot be “faʿlāna,” so their resemblance to the two alifs of the feminine remains as it is."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: ومن أجل المخالفة في الشرط (اختلف في رحمن) في أنه منصرف أو غير منصرف[[٩]]، فإنه ليس له مؤنث، لا «رحمى» ولا «رحمانة»؛ لأنه صفة خاصة لله تعالى، لا يطلق على غيره تعالى، لا على مذكر ولا على مؤنث.",
     "en": "(And from that point) — that is, on account of the divergence over the condition — (there is disagreement concerning Raḥmān) as to whether it is fully inflected or non-inflecting; for it has no feminine, neither “Raḥmā” nor “Raḥmāna,” because it is an attribute reserved for Allah, the Exalted — not applied to any other than Him, the Exalted, neither to a masculine nor to a feminine [referent]."},
    {"type": "matn",
     "ar": "فعلى مذهب من شرط انتفاء «فعلانة»، فهو غير منصرف.",
     "en": "So on the position of one who stipulated the absence of “faʿlāna,” it is non-inflecting."},
    {"type": "matn",
     "ar": "وعلى مذهب من شرط وجود «فعلى» فهو منصرف.",
     "en": "And on the position of one who stipulated the existence of “faʿlā,” it is fully inflected."},
    {"type": "matn",
     "ar": "(دون سكران)، فإنه لا خلاف في منع صرفه، لوجود الشرط على المذهبين؛",
     "en": "(Unlike sakrān, “drunk”) — for there is no disagreement over the prevention of its inflection, since the condition is present on both positions;"},

    {"type": "rule"},

    # ---------------- Footnotes ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أو مجموع وتثنية الضمير في قوله: إن كانا باعتبار تعددهما في أنفسهما.",
     "en": "Or [the pronoun refers to] the totality; and the pronoun is dualized in his words “if the two occur” in view of their multiplicity in themselves."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أنه يخالف الشروط السابقة، لكن يخلو عن لزوم تنافر بين اعتباري الواحدة والتعدد كما في التوجيه الأول.",
     "en": "Against this it may be said that it diverges from the preceding conditions; but it is free of the necessity of a clash between the two considerations of singularity and multiplicity, such as arose in the first construal."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا بعيد عن الفهم؛ لأنه صار في المعنى الأول كالعلم في هذا البحث، وإن كان يلائمه أن السبب الآخر في هذا الاسم لا يتحقق بدون العلمية.",
     "en": "This is remote from comprehension, because on the first sense it becomes like the proper name in this discussion — although it accords with it that the other cause in this noun is not realized without being a proper name."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "منهم من قال: إنها شرط وسبب. ومنهم من قال: إنها شرط محقق للمشابهة لا سبب؛ لأنهما كألفي التأنيث يقومان مقام علتين.",
     "en": "Among them are those who said that it is [both] a condition and a cause; and among them are those who said that it is a condition realizing the resemblance, not a cause — because these two, like the two alifs of the feminine, stand in the place of two causes."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أو ليتحقق سبب آخر، كما عرفت في التركيب.",
     "en": "Or so that another cause may be realized, as you learned in [the discussion of] composition."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وسلمان وعثمان. فقد جاء في الاسم حركات الفاء، وفي الصفة لم يجئ كسر الفاء، وجاء فتحها وضمها أيضا، لكن المؤنث حينئذ مع التاء.",
     "en": "And Salmān and ʿUthmān. For in the noun all the vowellings of the first radical (fāʾ) occur, whereas in the qualifier the kasra of the first radical does not occur, though its fatḥa and ḍamma do occur — but then the feminine takes the tāʾ."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فيه أنه عطف بـ«أو» على عاملين مختلفين، وليس على شرطه. قيل: الصواب الواو بدل «أو»؛ لأن الألف والنون توجدان في الاسم والصفة؟",
     "en": "Against this: it is a coordination by “or” upon two different governing agents, which is not according to its [proper] condition. It is said: the correct [reading] is “and” (wāw) in place of “or,” because the alif and nūn are found in both the noun and the qualifier?"},
    {"type": "pair",
     "ar": "وأجيب: بأن الترديد ليس باعتبار نفس الطبيعة، بل باعتبار فردها، وفردها لا يكون إلا في أحدهما. ويمكن أن يجاب: بأن «أو» للتنويع.",
     "en": "The reply is: the disjunction is not with respect to the nature itself, but with respect to its individual instance, and its individual instance can only be in one of the two. It may also be answered that “or” here is for [enumerating] the kinds (tanwīʿ)."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الظاهر أن فتح الفاء لم يكن شرطا فيه، لكن في أكثر موارده بالفتح.",
     "en": "The apparent [view] is that the fatḥa of the first radical is not a condition in it, but in most of its instances it comes with fatḥa."},

    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الأولى في أنه غير منصرف.",
     "en": "The preferable [view] is that it is non-inflecting."},
]
