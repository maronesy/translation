# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 316 (printed ٣١٥)."""

PAGE_NUMBER = 316
PRINTED_PAGE = "٣١٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأنه بتوسط العطف يصير» at the foot of PDF p. 315.
    {"type": "matn",
     "ar": "مثل: «الضارب زيد» كما عرفت، وإنما لم يحكم عليه بالامتناع بل بالضعف؛ لأنه قد يتحمل في المعطوف ما لا يتحمل في المعطوف عليه،",
     "en": "…like “al-ḍāribu Zaydin,” as you have learned. He judged it weak rather than impermissible only because what is not tolerated in the term coordinated to may be tolerated in the coordinated term."},
    {"type": "matn",
     "ar": "وحينئذ يندفع ما فيه من توهم شائبة المصادرة على المطلوب على التقدير الأول، وإرجاع كل من الصورتين الأخيرتين إلى مسألة ظاهرة، ويتضمن الرد على الفراء في الاستدلال بهما.",
     "en": "On this reading, the suspicion of begging the question (muṣādara ʿalā l-maṭlūb) that attaches to it on the first interpretation is removed, and each of the last two cases is referred back to an evident question, while it includes the rejection of al-Farrāʾ’s argument from them."},
    {"type": "matn",
     "ar": "(ولا يضاف موصوف إلى صفته) مع بقاء المعنى المفاد بالتركيب الوصفي بحاله؛ لأن لكل من هيئتي التركيب الوصفي والإضافي معنى آخر لا يقوم أحدهما مقام الآخر[[١]]",
     "en": "(A qualified noun is not annexed to its adjective) while the meaning conveyed by the adjectival construction remains as it is, because each of the two configurations, the adjectival construction and the annexational construction, has a distinct meaning, and neither takes the place of the other;"},
    {"type": "matn",
     "ar": "(و) لهذا المعنى بعينه (لا) يضاف (صفة إلى موصوفها) فلا يقال: «مسجد الجامع» بمعنى: «المسجد الجامع»، و«جرد قطيفة» بمعنى «قطيفة جرد» خلافا للكوفيين،",
     "en": "(and) for this very reason (an adjective is not) annexed (to its qualified noun). Thus one does not say “masjidu l-jāmiʿi” meaning “al-masjidu l-jāmiʿu” (the congregational mosque), nor “jardu qaṭīfatin” meaning “qaṭīfatun jardun” (a worn velvet cloth), contrary to the Kufans;"},
    {"type": "matn",
     "ar": "فإن «مسجد الجامع» عندهم بمعنى: «المسجد الجامع»، و«جرد قطيفة» بمعنى: «قطيفة جرد» من غير فرق.",
     "en": "for in their view “masjidu l-jāmiʿi” means “al-masjidu l-jāmiʿu,” and “jardu qaṭīfatin” means “qaṭīfatun jardun,” without difference."},
    {"type": "matn",
     "ar": "(و) يرد على القاعدة الأولى[[٢]]: وهي قوله: «ولا يضاف موصوف إلى صفته» (مثل: «مسجد الجامع، وجانب الغربي، وصلاة الأولى، وبقلة الحمقاء»)",
     "en": "(And) against the first rule—namely his words “a qualified noun is not annexed to its adjective”—there is the objection of (such as “masjidu l-jāmiʿi,” “jānibu l-gharbiyyi,” “ṣalātu l-ūlā,” and “baqlatu l-ḥamqāʾi”);"},
    {"type": "matn",
     "ar": "فإن في كل واحد من هذه التراكيب أضيف موصوف إلى صفته، فإن «الجامع» صفة المسجد، و«الغربي» صفة الجانب، و«الأولى» صفة الصلاة، و«الحمقاء» صفة البقلة، وقد أضيف إليه موصوفاتها.",
     "en": "for in each of these constructions a qualified noun has been annexed to its adjective: “al-jāmiʿ” is an adjective of the mosque, “al-gharbī” of the side, “al-ūlā” of the prayer, and “al-ḥamqāʾ” of the herb, and their qualified nouns have been annexed to them."},
    {"type": "matn",
     "ar": "وأجيب: بأن مثل هذه التراكيب (متأول) فـ«مسجد الجامع» متأول بمسجد الوقت الجامع[[٣]]، وذلك يحتمل على معنيين:",
     "en": "The answer given is that such constructions (are to be interpreted): “masjidu l-jāmiʿi” is interpreted as “the mosque of the gathering time,” and this admits of two meanings:…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيه بحث لأن لكل من هيئتي تركيب الإضافة وتركيب الصفة مع معمولها معنى آخر،",
     "en": "This is open to discussion, because each of the two configurations, the annexational construction and the construction of an adjective with what it governs, has a distinct meaning;"},
    {"type": "pair",
     "ar": "وقد قام هيئة الإضافة في الإضافة اللفظية مقام هيئة تركيب العامل مع المعمول.",
     "en": "yet in formal annexation (al-iḍāfa al-lafẓiyya) the configuration of annexation has taken the place of the configuration of the governor with what it governs."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ذهب الكوفيون إلى جواز إضافة الموصوف إلى صفته، وبالعكس للتخفيف مع إفادة التعريف أو التخصيص متمسكين بمسجد الجامع وأخواتها وجرد قطيفة وأمثاله،",
     "en": "The Kufans held it permissible to annex a qualified noun to its adjective, and the reverse, for lightening, while conveying definiteness or specification, relying on “masjidu l-jāmiʿi” and its sisters and on “jardu qaṭīfatin” and its like."},
    {"type": "pair",
     "ar": "فإن أصل مسجد الجامع المسجد الجامع أضيف للتخفيف بحذف اللام، وكسب التعريف من المضاف إليه؛ لأن المسجد هو الجامع بعينه،",
     "en": "For the origin of “masjidu l-jāmiʿi” is “al-masjidu l-jāmiʿu”; it was annexed for lightening, by dropping the article, and acquired definiteness from the term annexed to, since the mosque is the very same as the jāmiʿ;"},
    {"type": "pair",
     "ar": "بخلاف حسن الوجه، فإن حسنا وإن كان هو الوجه حقيقة، لكن جعلته لغيره في الظاهر بسبب الضمير المستكن.",
     "en": "unlike “ḥasanu l-wajhi,” for although “ḥasan” is in reality the face, you have made it belong to another in outward form, on account of the latent pronoun."},
    {"type": "pair",
     "ar": "وقس عليه أخواته، وأن أصل جرد قطيفة قطيفة جرد قدم جرد وأضيف للتخفيف بحذف التنوين والتخصيص.",
     "en": "Judge its sisters by analogy with it. And [they held] that the origin of “jardu qaṭīfatin” is “qaṭīfatun jardun”; “jard” was put first and annexed for lightening, by dropping the tanwīn, and for specification."},
    {"type": "pair",
     "ar": "وقس عليه أمثاله. وأجاب البصريون بالتأويل كما أشار إليه المصنف بقوله: ومسجد الجامع إلى آخره.",
     "en": "Judge its like by analogy with it. The Basrans answered by interpretation (taʾwīl), as the author indicates with his words “and masjidu l-jāmiʿi …” to the end."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وذلك الوقت هو يوم الجمعة كأن اليوم هذا جامع للناس في مسجده للصلاة، فإضافته كإضافة سيف الشجاع.",
     "en": "That time is Friday, as though this day gathers people in its mosque for prayer; so its annexation is like the annexation in “sayfu l-shujāʿi” (the sword of the brave one)."},
]
