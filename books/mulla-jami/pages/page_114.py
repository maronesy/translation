# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 114 (printed ١١٣)."""

PAGE_NUMBER = 114
PRINTED_PAGE = "١١٣"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[التركيب]",
     "en": "Compounding (al-Tarkīb)"},

    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(التركيب) وهو: «صيرورة كلمتين، أو أكثر كلمة واحدة[[١]] من غير حرفية جزء[[٢]]»، فلا يرد نحو: «النجم وبصري» علمين.",
     "en": "“Compounding (al-tarkīb)” — it is: “two words, or more, becoming a single word, without any part being a particle (ḥarf)”; so [names] like “al-Najm” and “Baṣrī,” [taken] as two proper names, do not come as counter-instances [against the definition]."},

    {"type": "matn",
     "ar": "(شرطه: العلمية[[٣]]) ليأمن من الزوال[[٤]]، فيحصل له قوة[[٥]]، فيؤثر بها في منع الصرف.",
     "en": "“Its condition is proper-name-hood (al-ʿalamiyya),” so that it may be secured against cessation, whereby a strength accrues to it, by which it exerts an effect in withholding declension."},

    {"type": "matn",
     "ar": "(وألا يكون بإضافة[[٦]])؛ لأن الإضافة[[٧]] تخرج المضاف إلى الصرف، أو إلى حكمه، فكيف تؤثر في المضاف إليه[[٨]] ما يضاده أعني: منع الصرف؟",
     "en": "“And that it not be by way of annexation (iḍāfa),” because annexation carries the annexed noun (al-muḍāf) toward declension, or toward its ruling; so how could it produce in the term of annexation (al-muḍāf ilayhi) its opposite — I mean, the withholding of declension?"},

    {"type": "matn",
     "ar": "(ولا بإسناد)؛ لأن الأعلام المشتملة على الإسناد من قبيل المبنيات[[٩]]، نحو: «تأبط شرا»،",
     "en": "“Nor by way of predication (isnād),” because proper names that comprise predication belong to the category of indeclinables (mabnīyāt), such as “Taʾabbaṭa Sharran”;"},

    {"type": "matn",
     "ar": "فإنها باقية في حال العلمية على ما كانت عليها قبل العلمية، فإن التسمية بها إنما هي لدلالتها على قصة غريبة،",
     "en": "for they remain, in the state of proper-name-hood, upon what they were before [becoming] proper names, since the naming by them is only on account of their signifying a curious tale;"},

    {"type": "matn",
     "ar": "فلو تطرق إليها التغيير يمكن أن تفوت تلك الدلالة، وإذا كانت من قبيل",
     "en": "so, were alteration to find its way to them, that signification could be lost; and when they are of the category…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ولا شبهة في أن التركيب الذي يناسب أن يعد من الأسباب تركيب يوجد في الأسماء، وهو المعرف ههنا لا مطلق التركيب، فصح التعريف جمعا.",
     "en": "There is no doubt that the compounding worthy of being counted among the causes [of preventing declension] is the compounding found in nouns — and it is what is being defined here, not compounding in the absolute; so the definition is sound, being comprehensive."},
    {"type": "pair",
     "ar": "لا يقال: فإذن لا حاجة إلى اشتراطه بالعلمية؛ لأن المركب المجعول كلمة واحدة لا يكون إلا علما؛",
     "en": "It is not to be objected: “in that case there is no need to stipulate proper-name-hood as its condition, because a compound made into a single word can only be a proper name”;"},
    {"type": "pair",
     "ar": "لأن نقول: لا نسلم الحصر لجواز أن ينقل أولا إلى معنى جنسي، أو ينقل أولا إلى معنى علمي، ثم ينقل إلى معنى جنسي كما إذا نكر ذلك العلم.",
     "en": "because we say: we do not concede the exclusive restriction (ḥaṣr), for it is possible that it be transferred first to a generic sense, or transferred first to a proper-name sense and then to a generic sense — as when that proper name is made indefinite."},
    {"type": "pair",
     "ar": "ولو سلم فنقول: العلمية شرط لتحققه وثبوته لا اشتراطه.",
     "en": "And even were it conceded, we say: proper-name-hood is a condition for its realization and establishment, not [a superfluous] stipulation of it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "إن قلت: اعتبار هذا القيد فيما أريد بالتركيب من غير اعتبار نفي الإضافة والإسناد تحكم؟",
     "en": "If you say: to take this restriction into account in what is meant by “compounding,” without taking into account the exclusion of annexation and predication, is arbitrary?"},
    {"type": "pair",
     "ar": "قلنا: الحرف لما كان شديد الالتصاق بالكلمة لم يظهر أثر تركيبهما، فلم يعدا من جنس التركيب الذي يناسب أن يعد سببا، بخلاف التركيب من الاسمين إسناديا كان أو إضافيا.",
     "en": "We say: since the particle is extremely tightly adjoined to the word, the effect of the compounding of the two does not appear, so the two are not counted of the genus of compounding worthy of being reckoned a cause — unlike the compounding of two nouns, whether it be predicative or annexational."},
    {"type": "pair",
     "ar": "ولما لم يوجد التركيب من الفعلين لم يحتج إلى نفيه بوجه.",
     "en": "And since compounding of two verbs does not occur, there was no need to exclude it in any way."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يجوز أن يكون الياء مصدرية، وأن تكون للنسبة كما لا يخفى.",
     "en": "The yāʾ may be the maṣdar-forming yāʾ, and it may be [the yāʾ] of the relative adjective (nisba), as is not hidden."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: بسبب الانحلال.",
     "en": "That is: on account of [its] dissolution (inḥilāl)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لزوم.",
     "en": "That is: [a strength of] permanence (luzūm)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الباء للملابسة، أي: ألا يكون ذلك التركيب ملابسا لهيئة الإضافة والإسناد.",
     "en": "The bāʾ [in bi-iḍāfa] denotes concomitance (mulābasa); that is, that that compounding not be clothed in the form of annexation and predication."},
    {"type": "pair",
     "ar": "وذلك لأن كل كلمة نقلت عن مركب إعرابها وبناؤها باعتبار المنقول عنه، ومعناها باعتبار المنقول إليه، فلا يصح اعتبار منع صرفها باعتبار وضعها العلمي لامتناع اعتبار حكمه.",
     "en": "And that is because every word transferred from a compound has its inflection and its indeclinability by consideration of that from which it was transferred, and its meaning by consideration of that to which it was transferred; so it is not correct to consider the withholding of its declension by consideration of its proper-name coinage, because considering its ruling is precluded."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو لأن تأثيرها إما في الجزء الأول، وهو باطل لما عرفت، أو إما في الجزء الثاني على قياس بعلبك، وهو أيضا باطل؛ لأنه مشغول بإعراب الحكاية.",
     "en": "Or because its effect is either in the first part — which is void, for the reason you have come to know — or else in the second part, on the analogy of “Baʿlabakk”; and this too is void, because it is occupied with the inflection of quotation (iʿrāb al-ḥikāya)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "أي: إذا كان في طبع شيء اقتضاء أمر لا يجوز أن يكون فيه اقتضاء ما يضاده سيما في مادة واحدة حكما، فإن المركب الإضافي في حكم كلمة واحدة.",
     "en": "That is: when there is in the nature of a thing a requiring of a [certain] matter, it is not admissible that there be in it a requiring of its contrary — especially in a single subject-matter, by ruling; for the annexational compound has the status of a single word."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "عند جماعة منهم المصنف. ومن قبيل المعربات المحكية عند جمع. ولا يبعد حينئذ أن يحكم بعدم انصرافه وإن لم يظهر أثره لفظا.",
     "en": "According to a group [of scholars], among them the author. And [it is] of the category of quoted inflected [nouns] (al-muʿrabāt al-maḥkiyya) according to [another] group. And it is then not far-fetched that it be ruled non-declinable, even if its effect does not appear in the wording."},
]
