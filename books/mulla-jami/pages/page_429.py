# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 429 (printed ٤٢٨)."""

PAGE_NUMBER = 429
PRINTED_PAGE = "٤٢٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «و«مائة وثلاثة وعشرون رجلا،» at the foot of PDF p. 428.
    {"type": "matn",
     "ar": "وثلاث وعشرون امرأة» إلى «مائة وتسعة وتسعين رجلا، وتسع وتسعين امرأة»، وكذا الحال في تثنية «المائة والألف» وجمعه،",
     "en": "…and thalāth wa-ʿishrūna imraʾatan” up to “miʾa wa-tisʿa wa-tisʿīna rajulan, and tisʿ wa-tisʿīna imraʾatan” (a hundred and ninety-nine men, or women); and likewise in the dual of “hundred” and “thousand” and its plural."},
    {"type": "matn",
     "ar": "ويجوز أن يعكس العطف في الكل، فتقول: «واحد ومائة» إلى آخر ما ذكرنا.",
     "en": "The conjunction may be reversed in all cases, so you say “wāḥid wa-miʾa” (one and a hundred), and so on to the end of what we have mentioned."},
    {"type": "matn",
     "ar": "(و) الأصل (في ثماني عشرة فتح الياء) لبناء صدور الأعداد المركبة على الفتح كـ«ثلاثة عشر»",
     "en": "(And) the rule (in thamāniya ʿashrata [eighteen, fem.] is a fatḥa on the yāʾ), since the first parts of compound numbers are indeclinable on the fatḥa, as in “thalāthata ʿashara”."},
    {"type": "matn",
     "ar": "(وجاء إسكانها) أي: إسكان الياء لتثاقل المركب بالتركيب كما في «معديكرب»[[١]]",
     "en": "(Its being made quiescent is attested), that is, making the yāʾ quiescent, because the compound is made heavy by compounding, as in “Maʿdīkarib”."},
    {"type": "matn",
     "ar": "(وشذ حذفها) أي: حذف الياء (بفتح النون)؛ لأنها إذا حذفت فالوجه بقاء الكسرة كما في قولك: «جاءني القاضي» إذا حذفت الياء",
     "en": "(Its elision is anomalous), that is, eliding the yāʾ (with a fatḥa on the nūn); for when it is elided, the proper course is for the kasra to remain, as in your saying “jāʾanī l-qāḍ[i]” when the yāʾ is elided;"},
    {"type": "matn",
     "ar": "إلا أن الذي يسوغ ذلك فيه كونه مركبا، فروعي زيادة استثقاله، فجعل موضع الكسرة فتحة.",
     "en": "but what permits this in it is its being a compound, so its added heaviness was taken into account and a fatḥa was put in place of the kasra."},
    {"type": "matn",
     "ar": "قال الشارح الرضي[[٢]]: ويجوز كسرها، ليدل على الياء المحذوفة،",
     "en": "The commentator al-Raḍī said: its kasra is permissible, to indicate the elided yāʾ;"},
    {"type": "matn",
     "ar": "لكن الفتح أولى، ليوافق أخواته؛ لأنها مفتوحة الأواخر مركبة مع العشرة.",
     "en": "but the fatḥa is preferable, so that it agrees with its sisters, since they end in fatḥa when compounded with ten."},
    {"type": "matn",
     "ar": "ولما فرغ من بيان حال أسماء الأعداد شرع في بيان حال مميزاتها، وابتدأ من الثلاثة؛ لأنه لا مميز للواحد والاثنين كما سيصرح به فقال:",
     "en": "Having finished explaining the state of the number nouns, he began to explain the state of their specifiers (mumayyiz), starting from three, because one and two have no specifier, as he will state explicitly. He said:"},
    {"type": "matn",
     "ar": "(ومميز الثلاثة إلى العشرة) و«الثلاث إلى العشر» (مخفوض[[٣]]) أي: مجرور (ومجموع[[٤]] لفظا) نحو: «ثلاثة رجال» (أو معنى[[٥]]) نحو: «ثلاثة رهط»",
     "en": "(The specifier of three to ten) and of “thalāth to ʿashr” (is in the oblique case), that is, genitive, (and plural in form), as in “thalāthat rijāl” (three men), (or in meaning), as in “thalāthat rahṭ” (three of a group)."},
    {"type": "matn",
     "ar": "أما كونه مخفوضا؛ لأنه لما كثر استعماله آثروا فيه جر التمييز بالإضافة للتخفيف؛ لأنها تسقط التنوين والنونين.",
     "en": "As for its being in the oblique case: since its use is frequent, they preferred to put the specifier (tamyīz) in the genitive by annexation (iḍāfa), for lightness, since annexation drops the tanwīn and the two nūns [of the dual and plural]."},
    {"type": "matn",
     "ar": "وأما كونه مجموعا ليطابق المعدود العدد",
     "en": "As for its being plural, it is so that the thing counted matches the number."},
    {"type": "matn",
     "ar": "(إلا في ثلاثمائة[[٦]] إلى تسعمائة) استثناء من قوله: «مجموع»؛",
     "en": "(Except in thalāthumiʾa [three hundred] to tisʿumiʾa [nine hundred]): an exception from his word “plural”;…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "مثال للتثاقل بالتركيب لا لجواز الإسكان بالتثاقل، فإن الإسكان في معديكرب واجب، صرح به الرضي.",
     "en": "An example of heaviness through compounding, not of the permissibility of making [the yāʾ] quiescent because of heaviness; for the sukūn in Maʿdīkarib is obligatory, as al-Raḍī stated explicitly."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "نبه بذلك على أن ما يتبادر من عبارة المصنف مما لا يرتضيه الرضي،",
     "en": "By this he drew attention to the fact that what first comes to mind from the author’s wording is something al-Raḍī does not accept;"},
    {"type": "pair",
     "ar": "فإن المتبادر منه أن حذف الياء مع الكسر غير شاذ، بل واقع من غير شذوذ، وعليه فحوى ما في الشرح المنسوب إلى المصنف.",
     "en": "for what first comes to mind from it is that eliding the yāʾ with the kasra is not anomalous but occurs without anomaly, and the import of what is in the commentary attributed to the author is to that effect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وأجاز سيبويه النصب في الشعر، والفراء مطلقا. وهذا إذا كان المعدود جامدا.",
     "en": "Sībawayh permitted the accusative in poetry, and al-Farrāʾ without restriction. This is when the thing counted is a non-derived noun (jāmid)."},
    {"type": "pair",
     "ar": "أو إذا كان صفة نحو قولك: ثلاثة صالحون، فالأحسن الإتباع، ثم النصب على الحال، ثم الإضافة،",
     "en": "Or if it is an adjective, as in your saying “thalātha ṣāliḥūn” (three righteous men), the best is apposition (itbāʿ), then the accusative as a ḥāl, then annexation;"},
    {"type": "pair",
     "ar": "وهو أضعفها لاستعمالها حينئذ استعمال الأسماء، كذا في شرح التسهيل.",
     "en": "and that is the weakest of them, because the adjective is then used as nouns are used. So it is in Sharḥ al-Tashīl."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جمع التكسير إن وجد، فإن كان له جمع قلة يؤتى به، ولا يؤتى بجمع الكثرة،",
     "en": "[That is,] the broken plural, if one exists; if it has a plural of paucity (jamʿ qilla), that is used, and the plural of multitude (jamʿ kathra) is not used;"},
    {"type": "pair",
     "ar": "وإن لم يوجد فجمع المؤنث السالم نحو: ثلاث عورات،",
     "en": "if none exists, then the sound feminine plural, as in “thalāth ʿawrāt” (three times of privacy);"},
    # REVIEW: «مجيئة» is printed with tāʾ marbūṭa (expected «مجيئه», "its occurrence"); transcribed as printed.
    {"type": "pair",
     "ar": "وقل مجيئة مع وجود المكسر نحو: سبع سنبلات مع وجود سنابل، ونحو: خمس زوجات وسبع بقرات.",
     "en": "its occurrence is rare when a broken plural exists, as in “sabʿ sunbulāt” (seven ears of grain) although sanābil exists, and as in “khams zawjāt” and “sabʿ baqarāt”."},
    {"type": "pair",
     "ar": "أما جمع المذكر السالم، فلا تمييز به.",
     "en": "As for the sound masculine plural, there is no specification by it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وهو اسم الجمع واسم الجنس، والأكثر فيه أن يكون مجرورا بـ«من».",
     "en": "That is the collective noun (ism al-jamʿ) and the generic noun (ism al-jins); most often it is put in the genitive with “min”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: إسقاط التاء في ثلاثة وأخواتها واجب إذا أضيف إلى مائة، وإثباتها واجب إذا أضيف إلى الألف؛",
     "en": "That is, dropping the tāʾ in thalātha and its sisters is obligatory when it is annexed to miʾa, and keeping it is obligatory when it is annexed to alf;"},
    {"type": "pair",
     "ar": "لأن مميزها في الظاهر لفظة «مائة»، وهو مؤنث، ولفظ «ألف» وهو مذكر.",
     "en": "because its specifier is outwardly the word “miʾa”, which is feminine, and the word “alf”, which is masculine."},
]
