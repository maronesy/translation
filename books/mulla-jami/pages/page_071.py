# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 71 (printed ٧٠)."""

PAGE_NUMBER = 71
PRINTED_PAGE = "٧٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "وإنما جعل الإعراب في آخر الاسم المعرب[[١]]؛ لأن نفس الاسم يدل على المسمى، والإعراب على صفته[[٢]].",
     "en": "The iʿrāb (inflection) is placed only at the end of the declinable noun, because the noun itself indicates the named entity (al-musammā), while the iʿrāb indicates its attribute."},
    {"type": "matn",
     "ar": "ولا شك أن الصفة متأخرة عن الموصوف، فالأنسب أن يكون الدال عليها[[٣]] أيضا متأخرا عن الدال عليه،",
     "en": "There is no doubt that the attribute comes after the thing it qualifies (al-mawṣūf); hence it is most fitting that what indicates the attribute should likewise come after what indicates [the thing qualified]."},
    {"type": "matn",
     "ar": "وهو مأخوذ من «أعربه» إذا أوضحه، فإن الإعراب يوضح المعاني المقتضية، ومن «عربت معدته» إذا فسدت على أن تكون الهمزة للسلب، فيكون معناه حينئذ: إزالة الفساد، سمي به؛ لأنه يزيل التباس فساد بعض المعاني ببعض.",
     "en": "The term [iʿrāb] is derived from aʿrabahu, meaning “he made it clear,” for the iʿrāb clarifies the necessitating meanings; and [it is also derived] from ʿaribat maʿidatuhu, meaning “his stomach became corrupted,” on the assumption that the hamza [in aʿraba] is privative (li-l-salb), so that its meaning would then be “the removal of corruption” — it is so named because it removes the confusion of the corruption of some meanings with others."},
    {"type": "matn",
     "ar": "(وأنواعه) أي: أنواع إعراب الاسم ثلاثة[[٤]]: (رفع، ونصب، وجر) هذه الأسماء الثلاثة مختصة بالحركات والحروف الإعرابية.",
     "en": "“And its kinds” — that is, the kinds of iʿrāb of the noun are three: “rafʿ (nominative), naṣb (accusative), and jarr (genitive).” These three terms are specific to the inflectional vowels and letters."},
    {"type": "matn",
     "ar": "ولا تطلق على الحركات البنائية أصلا، بخلاف الضمة والفتحة والكسرة، فإنها مستعملة في الحركات البنائية غالبا، وفي الحركات الإعرابية على قلة.",
     "en": "They are never applied to the vowels of indeclinability (al-ḥarakāt al-bināʾiyya) at all — unlike the ḍamma, fatḥa, and kasra, which are used mostly for the vowels of indeclinability and only rarely for the inflectional vowels."},
    {"type": "matn",
     "ar": "(فالرفع) حركة كان أو حرفا (علم الفاعلية) أي: علامة كون الشيء فاعلا حقيقة أو حكما[[٥]]، ليشمل الملحقات بالفاعل أيضا، كالمبتدأ والخبر وغيرهما.",
     "en": "“So rafʿ” — whether a vowel or a letter — “is the mark of agenthood (ʿalam al-fāʿiliyya),” that is, the sign that the thing is an agent (fāʿil), either in reality or by legal status (ḥukman) — so as to include also what is annexed to the agent, such as the mubtadaʾ, the khabar, and others."},
    {"type": "matn",
     "ar": "(والنصب) حركة كان أو حرفا (علم المفعولية) أي: علامة كون الشيء مفعولا",
     "en": "“And naṣb” — whether a vowel or a letter — “is the mark of objecthood (ʿalam al-mafʿūliyya),” that is, the sign that the thing is an object (mafʿūl)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: الإعراب بالحركة التي هو الأصل أو الإعراب مطلقا في آخر المعرب حقيقة أو حكما، فإن الواقع بعد أكثر حروف الكلمة، كأنه الواقع بعد الكل؛ لأن الأكثر في حكم الكل، وكون الحركة بعد الكلمة يظهر بإشباعها.",
     "en": "That is: the iʿrāb by means of the vowel — which is the original form — or the iʿrāb absolutely, at the end of the declinable word, whether in reality or by status; for what occurs after most of the letters of the word is as though it occurred after all of them, since the majority has the ruling of the whole; and the vowel’s occurring after the [whole] word becomes manifest through its saturation (ishbāʿ)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: صفة المسمى والمدلول. وذلك بناء على أن الفاعلية ومقابلها صفات للمدلول.",
     "en": "That is: the attribute of the named entity and of the signified (al-madlūl). This is based on [the view] that agenthood and its counterpart are attributes of the signified."},
    {"type": "pair",
     "ar": "وقد جعلها الشيخ الرضي صفات للدال، وهي كونه عمدة أو فضلة. فقال: جعل الإعراب في الآخر؛ لأن الدال على الوصف بعد الموصوف.",
     "en": "Shaykh al-Raḍī, however, made them attributes of the signifier (al-dāll) — namely, its being a principal element (ʿumda) or a surplus one (faḍla). He said: the iʿrāb is placed at the end because that which indicates the attribute [comes] after the thing qualified."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: على الصفة.",
     "en": "That is: [indicating] the attribute."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أشار به إلى أن مجموع قوله: «رفع ونصب وجر» خبر واحد ليصح الحمل على قوله: «وأنواعه»، فيكون العطف مقدما على الحمل، كما في قولك: «البيت سقف وجدران».",
     "en": "By this he indicated that the totality of his words “rafʿ, naṣb, and jarr” is a single predicate, so that predication upon his words “and its kinds” may be valid; thus the conjunction precedes the predication, as in your saying: “the house is a roof and walls.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وذلك إذا كان الاسم عمدة. وهذا الوصف يستدعي الرفع، لكنه قد يتخلف عنه بعلة المشابهة بالفضلة.",
     "en": "That is [an agent by status] when the noun is a principal element (ʿumda). This attribute calls for rafʿ, but it may fail to appear on account of resemblance to the surplus element (faḍla)."},
    {"type": "pair",
     "ar": "ولا يخفى أن هذا التعميم هو الحق. والقول بأن الرفع والنصب والجر منسوبة للفاعلية والمفعولية، ويكون فيما يشابهها بطريق الاستعارة بعيد لا دليل عليه.",
     "en": "It is not hidden that this generalization is the correct view. The claim that rafʿ, naṣb, and jarr are ascribed [only] to agenthood and objecthood, and apply to what resembles them merely by way of metaphor, is far-fetched and unsupported."},
    {"type": "pair",
     "ar": "نعم الرفع والنصب أحق، ومن جعل الياء فيهما للنسبة، وأراد الخاصة المنسوبة إلى الفاعل والمفعول، فتوجيهه بحسب المعنى راجع إلى ما في الشرح، وتوجيه الشرح أقرب من توجيهه إلى الفهم.",
     "en": "Indeed, rafʿ and naṣb have the greater claim [to this]. As for one who takes the yāʾ in [fāʿiliyya and mafʿūliyya] as denoting relation (nisba), intending the property ascribed to the agent and the object, his construal, as to meaning, reverts to what is in the commentary; yet the commentary’s construal is closer to understanding than his."},
]
