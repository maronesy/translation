# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 177 (printed ١٧٦)."""

PAGE_NUMBER = 177
PRINTED_PAGE = "١٧٦"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "section", "ar": "[ خبر إن وأخواتها ]",
     "en": "The Predicate of Inna and Its Sisters"},

    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(خبر «إن» وأخواتها) أي: من المرفوعات[[١]] خبر «إن»[[٢]] وأخواتها أي: أشباهها[[٣]] من الحروف الخمس الباقية،",
     "en": "(The predicate of “inna” and its sisters—khabaru inna wa-akhawātuhā), that is: among the nominatives (al-marfūʿāt) is the predicate of “inna” and its sisters, that is: its likes among the five remaining particles,"},
    {"type": "matn",
     "ar": "وهي: «إن، وكأن، ولكن، وليت، ولعل»،",
     "en": "namely: “inna, ka-anna, lākinna, layta and laʿalla.”"},
    {"type": "matn",
     "ar": "وهي مرفوع بهذه الحروف لا بالابتداء[[٤]] على المذهب الأصح؛",
     "en": "It is put in the nominative by these particles, not by inception (ibtidāʾ), according to the sounder doctrine;"},
    {"type": "matn",
     "ar": "لأنها لما شابهت[[٥]] الفعل المتعدي كما تجيء عملت رفعا ونصبا مثله.",
     "en": "because, since they resemble the transitive verb, as will come, they govern the nominative and the accusative as it does."},
    {"type": "matn",
     "ar": "(هو) أي: خبر «إن» وأخواتها (المسند) إلى شيء آخر (بعد دخول) أحد (هذه الحروف[[٦]]) عليهما.",
     "en": "(It—huwa), that is: the predicate of “inna” and its sisters, (is what is predicated—al-musnad) of something else (after the entry of—baʿda dukhūli) one of (these particles—hādhihi al-ḥurūfi) upon the two of them."},
    {"type": "matn",
     "ar": "فقوله: «المسند» شامل لخبر كان وخبر المبتدأ، وخبر \"لا\" التي لنفي الجنس وغيرها.",
     "en": "His word “what is predicated” covers the predicate of kāna, the predicate of the subject, the predicate of the “lā” that negates the genus (lā li-nafy al-jins), and others."},
    {"type": "matn",
     "ar": "وقوله: «بعد دخول هذه الحروف» خرج جميعها عنه.",
     "en": "By his words “after the entry of these particles” all of them are excluded from it."},
    {"type": "matn",
     "ar": "والمراد بدخول هذه الحروف عليهما ورودها عليهما لإيراث أثرها فيهما لفظا أو معنى[[٧]]، فلا ينتقض",
     "en": "What is meant by the entry of these particles upon the two is their coming upon them so as to impart their effect to them, in wording or in meaning; so [the definition] is not contradicted…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أشار به إلى أن قوله: خبر إن وأخواتها مبتدأ محذوف الخبر، وذلك بقرينة ما سبق.",
     "en": "By this he indicated that his words “the predicate of inna and its sisters” are a subject whose predicate is elided, as the context of what preceded shows."},
    {"type": "pair",
     "ar": "فقوله: هو المسند ابتداء كلام. ويحتمل أن يكون المسند خبره.",
     "en": "So his words “it is what is predicated” begin a new sentence. It is also possible that “what is predicated” is its predicate."},
    {"type": "pair",
     "ar": "وقوله: هو صيغة الفصل.",
     "en": "His word “huwa” is the form of separation (ṣīghat al-faṣl)."},
    {"type": "pair",
     "ar": "وإنما لم يقل: ومنهما لأنه في الأصل خبر المبتدأ، فلم يفصل بما هو مشعر بكونه بابا على حدة.",
     "en": "He did not say “and among them” only because it is originally the predicate of a subject; so he did not separate it off by what would suggest its being a chapter on its own."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يحتمل أن يكون مراده إن منها مقدر في نظم الكلام. وقوله: «خبر إن مع منها المحذوف» كلام برأسه.",
     "en": "It is possible that he means that “minhā” is implied in the arrangement of the utterance, and his words “the predicate of inna,” together with the elided “minhā,” are an independent sentence."},
    {"type": "pair",
     "ar": "ويحتمل أن يكون مجموع قوله: خبر إن وأخواتها هو المسند بعد دخولها كلاما واحدا، ولم يكن منها محذوفا فيه،",
     "en": "It is also possible that the whole of his words “the predicate of inna and its sisters is what is predicated after their entry” is a single sentence, with no “minhā” elided in it;"},
    {"type": "pair",
     "ar": "وقول الشارح أي: من المرفوعات إشارة إلى أنه ليس من خبر المبتدأ، بل ذكره؛ لأنه من المرفوعات.",
     "en": "and the commentator’s words “that is: among the nominatives” indicate that it does not belong to the predicate of the subject; rather, he mentioned it because it is among the nominatives."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "استعير الأخوات للأشباه والنظائر لما بينهما من التقارب والتماثل كما بين الأخوات.",
     "en": "“Sisters” is used metaphorically for likes and counterparts, because of the closeness and similarity between them, as between sisters."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كما ذهب إليه الكوفيون لضعف تلك العوامل عن عملين.",
     "en": "As the Kūfans held, because those governors are too weak for two [acts of] government."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولأن اقتضاءها للجزأين على السواء، فالأولى أن تعمل فيهما.",
     "en": "And because they require the two parts equally, so it is more fitting that they govern both."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "زاد لفظ «أحد» ليصدق التعريف على كل واحد من أفراد المعرف.",
     "en": "He added the word “one” (aḥad) so that the definition would hold true of each individual of the thing defined."},
    {"type": "pair",
     "ar": "إن قلت: المعرف إن كان مجموع أخبار تلك الحروف فلا خفاء في عدم صدقه عليها؛ لأنها ليست بعد دخول أحدها،",
     "en": "If you say: if the thing defined is the totality of the predicates of those particles, there is no obscurity in its not holding true of them, because they do not come after the entry of [only] one of them;"},
    {"type": "pair",
     "ar": "وإن كان كلا من خبر إن وأخواتها فلا يصدق على مجموع أخبار أخواتها أنها بعد دخول أحدها؟",
     "en": "and if it is each of the predicate of inna and its sisters, then it does not hold true of the totality of the predicates of its sisters that they come after the entry of one of them?"},
    {"type": "pair",
     "ar": "قلنا: المعرف حقيقة خبر هذا الباب.",
     "en": "We say: the thing defined is in reality the predicate of this chapter."},
    {"type": "pair",
     "ar": "وذلك إما بتقدير المضاف أي: خبر باب إن وأخواتها أو يجعل قوله: إن وأخواتها مجازا عن هذا المعنى.",
     "en": "That is either by supposing an elided annexed noun, that is: “the predicate of the chapter of inna and its sisters,” or by taking his words “inna and its sisters” as a figurative expression for this meaning."},
    {"type": "pair",
     "ar": "وإنما لم يحمل كلامه على توزيع يتضمن تعريفات كل واحد واحد؛ لأن المقام مقام التعريف، وأن المناسب للتوزيع: أخبار إن وأخواتها بصيغة الجمع.",
     "en": "His words were not construed as a distribution comprising definitions of each one individually only because the context is one of definition, and because what would suit distribution is “the predicates (akhbār) of inna and its sisters,” in the plural form."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أما لفظا، فبالعمل فيهما. وأما معنى، فلانسحاب معانيها إلى معانيهما،",
     "en": "In wording, by governing them; in meaning, by the extension of their meanings onto the meanings of the two;"},
    {"type": "pair",
     "ar": "فإن تأكيد الحكم مثلا ينسحب إلى المحكوم به وعليه.",
     "en": "for the corroboration of the judgment, for example, extends to the predicate and the subject of the judgment."},
    {"type": "pair",
     "ar": "وعلى كل تقدير لا ينتقض التعريف بمثل يقوم، وبخبر المبتدأ الذي بعد «إن»",
     "en": "On either supposition, the definition is not contradicted by such as “yaqūmu,” nor by the predicate of the subject that comes after “in”…"},
]
