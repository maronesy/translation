# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 129 (printed ١٢٨)."""

PAGE_NUMBER = 129
PRINTED_PAGE = "١٢٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text + commentary (matn) ----------------
    {"type": "matn",
     "ar": "وإنما قدمه؛ لأنه أصل المرفوعات عند الجمهور[[١]]؛ لأنه جزء الجملة الفعلية[[٢]] التي هي أصل الجمل[[٣]]، ولأن عامله أقوى[[٤]] من عامل المبتدأ.",
     "en": "He placed it (the fāʿil, the agent) first only because it is the foundation (aṣl) of the nominatives (al-marfūʿāt) according to the majority (al-jumhūr); because it is a part of the verbal sentence (al-jumla al-fiʿliyya), which is the foundation of [all] sentences; and because its governing agent (ʿāmil) is stronger than the governing agent of the mubtadaʾ (the subject of a nominal sentence)."},
    {"type": "matn",
     "ar": "وقيل[[٥]]: أصل المرفوعات المبتدأ؛ لأنه باق[[٦]] على ما هو الأصل في المسند إليه، وهو التقديم، بخلاف الفاعل،",
     "en": "It has [also] been said: the foundation of the nominatives is the mubtadaʾ, because it remains upon what is the original state of that to which predication is made (al-musnad ilayhi) — namely, being placed first — unlike the fāʿil;"},
    {"type": "matn",
     "ar": "ولأنه يحكم عليه بكل حكم[[٧]] جامد ومشتق، فكان أقوى، بخلاف الفاعل، فإنه لا يحكم عليه إلا بالمشتق[[٨]].",
     "en": "and because a judgment is passed upon it (the mubtadaʾ) by every kind of predicate, both underived (jāmid) and derived (mushtaqq), so it is stronger — unlike the fāʿil, upon which a judgment is passed only by a derived [predicate]."},
    {"type": "matn",
     "ar": "(وهو) أي: الفاعل (ما) أي: اسم حقيقة أو حكما؛ ليدخل فيه[[٩]] مثل قولهم[[١٠]]: «أعجبني أن ضربت زيدا» (أسند إليه)[[١١]]:",
     "en": "“(And it)” — that is, the fāʿil — “(is that which — mā),” that is, a noun, whether in reality or in ruling (ḥukman), so as to bring under it such [expressions] as their saying “aʿjabanī an ḍarabta Zaydan” (it pleased me that you struck Zayd) — “(to which is attributed):”"},
    {"type": "matn",
     "ar": "١-(الفعل) بالأصالة لا بالتبعية، ليخرج عن الحد توابع الفاعل[[١٢]].",
     "en": "1. “(the verb)” — by primacy (bi-l-aṣāla), not by dependency (bi-l-tabaʿiyya) — so as to exclude from the definition the appositives (tawābiʿ) of the fāʿil."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: أصل فيما بين أنواع المرفوعات عند الخليل وأتباعه. والأصل بمعنى ما يبتنى عليه الشيء.",
     "en": "That is: a foundation among the kinds of nominatives according to al-Khalīl and his followers. And “aṣl” means that upon which a thing is built."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولأنه لا يحذف بدون المسند، وفيه أنه قد يحذف كقولك: «ما ضرب وأكرم إلا أنا»، وقولهم: بدا لك أي رأى، ويدفع بأنه نادر،",
     "en": "And because it (the fāʿil) is not elided without the predicate (al-musnad); against which [it is objected] that it may be elided, as in your saying “mā ḍaraba wa-akrama illā anā” (none struck or honored but I), and their saying “badā laka,” meaning “he formed an opinion” — this is answered [by noting] that it is rare;"},
    {"type": "pair",
     "ar": "ولأنه لا ينتسخ بالعامل. وفيه أنه قد ينتسخ نحو: «كفى بالله»، ويدفع بأنه نادر غير مطرد، والحرف زائد.",
     "en": "and because it is not abrogated by a governing agent; against which [it is objected] that it may be abrogated, as in “kafā bi-Llāh” (Allah suffices) — this is answered [by noting] that it is rare and non-standard, and the [prepositional] particle is expletive (zāʾid)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن التركيب فيها أشد، وامتزاج أحد الجزئين، وهو الفعل بالآخر أكثر، ولأنها يشتمل الخبر والإنشاء وضعا بجوهرها من غير حاجة إلى التوسل بخارج منها بخلاف الاسمية،",
     "en": "Because the compounding (tarkīb) in it (the verbal sentence) is more intense, and the fusion of one of its two parts — namely the verb — with the other is greater; and because it encompasses both the declarative (khabar) and the performative (inshāʾ) by its very essence, without any need to resort to something external to it — unlike the nominal sentence."},
    {"type": "pair",
     "ar": "ومن جهات أصالة الفاعل أنه لا يحذف وحده بدون ما يقوم مقامه، وكأنه لم يلتفت إليه؛ لأنه ينتقض بنحو: «ما ضرب وأكرم إلا أنا»، وقولهم بدا لك أي: رأى،",
     "en": "Among the aspects of the primacy (aṣāla) of the fāʿil is that it is not elided by itself without something taking its place; but it is as though he (the author) paid no heed to this, because it is refuted by such [examples] as “mā ḍaraba wa-akrama illā anā,” and their saying “badā laka,” meaning “he formed an opinion.”"},
    {"type": "pair",
     "ar": "ومنها أن رفعه لا ينسخ بالنواسخ، وكأنه تركه لأنه أورد عليه نحو: كفى بالله، وإن اعتذر بأنه نادر غير مطرد، والباء زائدة، لكن حديث عدم الاطراد ضعيف لوجود كثير مطرد، نحو: «ما جاءني من أحد».",
     "en": "And among them [also] is that its rafʿ (nominative marking) is not abrogated by the abrogators (nawāsikh); and it is as though he abandoned this because such [an example] as “kafā bi-Llāh” was raised against it — even though it is excused as being rare and non-standard, and the bāʾ expletive — yet the claim of non-standardness is weak, given the existence of much that is standard, such as “mā jāʾanī min aḥad” (no one came to me)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لأنه موجود محسوس بخلاف عامل المبتدأ، فإنه عدمي معقول، وقوة المؤثر تقتضي قوة الأثر، فالفاعل في المرفوعية أقوى من المبتدأ.",
     "en": "Because it (the verb) is an existent, perceptible thing — unlike the governing agent of the mubtadaʾ, which is privative and [merely] intelligible; and the strength of the influencer entails the strength of the effect, so the fāʿil is stronger in [its] nominativity than the mubtadaʾ."},
    {"type": "pair",
     "ar": "ولا يعارضه ما ذكر في المبتدأ؛ لأنه لا يفيد قوة رفعه، بل يفيد فضيلة حاله.",
     "en": "And what was mentioned regarding the mubtadaʾ does not oppose this, because it does not indicate the strength of its rafʿ, but rather indicates the excellence of its state."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "القائل سيبويه ومن معه.",
     "en": "The one who says this is Sībawayh and those with him."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "ولأن ما عداه يصلح أن يرد إليه فهو أم المرفوعات، كما أن ألف الاستفهام أصل فيه لقيامها مقام كلماته.",
     "en": "And because whatever is besides it can be reduced to it, so it is the mother of the nominatives — just as the interrogative hamza (alif al-istifhām) is the root within it (interrogation), since it stands in place of its [other] words."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أو لأنه يحكم عليه بمتعدد، فله استيعاب، وهو فضيلة وكمال.",
     "en": "Or because a judgment is passed upon it (the mubtadaʾ) by multiple [predicates], so it possesses comprehensiveness (istīʿāb), which is an excellence and a perfection."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "حقيقة أو حكما، فإن المصدر العامل في قوة «أن» مع الفعل.",
     "en": "[Whether] in reality or in ruling, for the governing verbal noun (maṣdar) has the force of “an” together with the verb."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "فإن قلت: لم لم يعمل بعموم كلمة «ما» ليستغنى عن التعميم؟ قلت: لأن تخصيص كلمة «ما» في التعريفات بما يستدعيه المقام سنة مؤكدة يرى تركها سيئة.",
     "en": "If you say: why did he not employ the generality of the word “mā” so as to dispense with [expressly] generalizing? I say: because restricting the word “mā” in definitions to what the context calls for is a firmly established practice (sunna muʾakkada), the abandonment of which is regarded as a fault."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: ليدخل فيه الفاعل في مثل قولهم.",
     "en": "That is: so as to bring under it the fāʿil in such [expressions] as their saying [above]."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "الإسناد ههنا بمعنى النسبة ناقصة كانت أو تامة، خبرية أو إنشائية، مثبتة كانت أو منفية، محققة كانت أو مفروضة.",
     "en": "Attribution (isnād) here means relation (nisba), whether incomplete (nāqiṣa) or complete (tāmma), declarative or performative, affirmative or negative, actual or supposed."},

    # ---------------- Footnote 12 ----------------
    {"type": "note", "num": "١٢"},
    {"type": "pair",
     "ar": "قال بعض المحققين: المراد بإخراج التوابع إخراج بعضها، وهو المعطوف بالحرف والبدل؛ إذ لا إسناد إلى التوابع إلا فيهما، بخلاف النعت والتأكيد وعطف البيان.",
     "en": "Some of the verifying scholars (muḥaqqiqūn) said: what is intended by excluding the appositives (tawābiʿ) is the exclusion of only some of them — namely that which is coordinated by a particle (al-maʿṭūf bi-l-ḥarf) and the substitute (badal); for there is no attribution to the appositives except in these two, unlike the adjective (naʿt), the corroborative (taʾkīd), and the explicative apposition (ʿaṭf al-bayān)."},
]
