# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 497 (printed ٤٩٦)."""

PAGE_NUMBER = 497
PRINTED_PAGE = "٤٩٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Begins a new paragraph; the previous page ended with a complete sentence.
    {"type": "matn",
     "ar": "(والواو) التي ينتصب بعدها المضارع بتقدير «أن» بعدها مشروط (بشرطين):",
     "en": "(And the wāw), after which the muḍāriʿ is put in the accusative; supposing “an” after it is conditional (on two conditions):"},
    {"type": "matn",
     "ar": "أحدهما: (الجمعية) أي: مصاحبة ما قبلها لما بعدها، وإلا فالواو[[١]] للجمع دائما.",
     "en": "The first of them is (togetherness (al-jamʿiyya)), that is, the accompaniment of what follows it by what precedes it; otherwise the wāw is always for conjoining."},
    {"type": "matn",
     "ar": "(و) ثانيهما: (أن يكون قبلها) أي: قبل الواو (مثل ذلك) أي: ما يماثل الواقع قبل الفاء في كونه أحد الأشياء الستة المذكورة،",
     "en": "(And) the second of them is (that there be before it), that is, before the wāw, (the like of that), that is, what resembles what occurs before the fāʾ in being one of the six things mentioned;"},
    {"type": "matn",
     "ar": "وأمثلتها أمثلة الفاء بعينها بإبدال الفاء بالواو كما تقول مثلا: «زرني وأكرمك» أي: ليجتمع الزيارة والإكرام[[٢]]،",
     "en": "and its examples are exactly the examples of the fāʾ, with the fāʾ replaced by the wāw; as you say, for instance, “zurnī wa-ukrimaka” (visit me and I will honour you), that is, “let the visit and the honouring come together”;"},
    {"type": "matn",
     "ar": "و«لا تأكل السمك وتشرب اللبن» أي: لا يجتمع منك أكل السمك مع شرب اللبن، وعلى هذا القياس.",
     "en": "and “lā taʾkuli al-samaka wa-tashraba al-labana” (do not eat fish and drink milk), that is, “let there not come together from you the eating of fish with the drinking of milk”; and so on by analogy."},
    {"type": "matn",
     "ar": "(و«أو») التي ينتصب[[٣]] المضارع بعدها بتقدير «أن» (بشرط معنى «إلى أن»، أو «إلا أن») أي: بشرط أن تكون[[٤]] بمعنى «إلى» أو «إلا» الداخلتين على «أن» المقدرة بعدها،",
     "en": "(And “aw”), after which the muḍāriʿ is put in the accusative by supposing “an”, (on condition of the sense of “ilā an” (until) or “illā an” (unless)), that is, on condition that it be in the sense of “ilā” or “illā”, the two of which enter upon the “an” supposed after it;"},
    {"type": "matn",
     "ar": "لا أن «أن» أيضا داخل في مفهومها، وإلا يلزم من تقدير «أن» بعدها تكرار،",
     "en": "not that “an” too is included in its meaning; otherwise supposing “an” after it would entail repetition;"},
    {"type": "matn",
     "ar": "(نحو: لألزمنك أو تعطيني حقي) أي: إلى أن تعطيني حقي، أو إلا أن تعطيني حقي،",
     "en": "(as in “la-alzamannaka aw tuʿṭiyanī ḥaqqī” (I shall stick to you until / unless you give me my due)), that is, “until you give me my due” or “unless you give me my due.”"},
    {"type": "matn",
     "ar": "فسيبويه يقدرها بـ«إلا» بتقدير مضاف أي: لألزمنك إلا وقت أن تعطيني حقي،",
     "en": "Sībawayh construes it as “illā”, supposing a first term of a genitive construction, that is, “I shall stick to you except at the time of your giving me my due”;"},
    {"type": "matn",
     "ar": "وغيره يقدرها بـ«إلى» بتأويل مصدر مجرور بـ«أو» التي بمعنى «إلى» أي: لألزمنك إلى إعطائك حقي.",
     "en": "and others construe it as “ilā”, by interpreting [what follows] as a verbal noun in the genitive governed by the “aw” that means “ilā”, that is, “I shall stick to you until your giving me my due.”"},
    {"type": "matn",
     "ar": "(والعاطفة) أي: الحروف العاطفة مطلقا سواء كانت من الحروف العاطفة المذكورة أو لا كـ«ثم»،",
     "en": "(And the coordinating [particle]), that is, the coordinating particles without restriction, whether they are among the coordinating particles mentioned or not, such as “thumma”;"},
    {"type": "matn",
     "ar": "وإذا كانت منها فمن غير اشتراط ما ذكر من الشروط لصحة تقدير «أن» بعدها",
     "en": "and if it is one of them, then without the stipulation of the conditions mentioned for the soundness of supposing “an” after it;"},
    {"type": "matn",
     "ar": "أي: ينتصب المضارع بها بتقدير «أن» (إذا كان المعطوف عليه اسما صريحا)،",
     "en": "that is, the muḍāriʿ is put in the accusative by it through supposing “an” (when the term coordinated upon is an explicit noun),…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: printed «أي: إلا ترد»; the sense suggests «أي: ألا ترد» or «لا ترد». Transcribed as printed.
    {"type": "pair",
     "ar": "أي: إلا ترد الجمعية بمعنى المصاحبة، بل مطلق الجمع كما هو المتبادر، فالواو للجمع المطلق دائما،",
     "en": "That is, if “togetherness” is not meant in the sense of accompaniment, but rather absolute conjoining, as is what first comes to mind, then the wāw is always for absolute conjoining;"},
    {"type": "pair",
     "ar": "فلا معنى لاشتراطه في الانتصاب، فالاشتراك قرينة على التخصيص.",
     "en": "so there is no sense in stipulating it for the accusative; the shared [meaning] is thus a contextual indication (qarīna) of the specific sense."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فالواو للمصاحبة مع عطف المصدر على المصدر.",
     "en": "So the wāw is for accompaniment, together with the coordination of a verbal noun upon a verbal noun."},
    # REVIEW: printed «ليكن زيادة منك» (increase); the parallel gloss on the previous page reads «زيارة» (visit). Transcribed as printed.
    {"type": "pair",
     "ar": "وهذا أولى من تقديرهم: ليكن زيادة منك وإكرام مني، فإنه لا يدل على المصاحبة.",
     "en": "This is better than their construal “let there be an increase [sic; read “a visit”] from you and honouring from me”, for that does not indicate accompaniment."},
    {"type": "pair",
     "ar": "وقال الشارح الرضي: إن هذه الواو إما للحال والمضارع بتأويل المصدر مبتدأ محذوف الخبر، فمعنى: قم وأقوم قم وقيامي ثابت أي: في حال ثبوت قيامي،",
     "en": "The commentator al-Raḍī said: this wāw is either circumstantial (li-l-ḥāl), with the muḍāriʿ, interpreted as a verbal noun, being a subject whose predicate is omitted; so the meaning of “qum wa-aqūma” is “stand, while my standing is established”, that is, in the state of my standing’s being established;"},
    {"type": "pair",
     "ar": "أو معنى مع أي: قم مع قيامي؛ لأن كون واو العطف للجمعية قليل، ولانتفاء المنصوصية على المعنى المقصود، وفيه مثل ما عرفت.",
     "en": "or it has the sense of “maʿa” (with), that is, “stand along with my standing”; because the coordinating wāw’s being for togetherness is rare, and because there is no explicit statement of the intended meaning. Against this is the like of what you have learned."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    # REVIEW: printed «لتقدير «إن»» (with kasra-hamza); the context concerns «أن». Transcribed as printed.
    {"type": "pair",
     "ar": "لم ينص ههنا على كون قوله: بشرط خبرا وإن الشرط لتقدير «إن» اكتفاء بما بعد.",
     "en": "He did not state explicitly here that his words “on condition” are a predicate and that the condition is for supposing “an”, relying on what comes after."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    # REVIEW: printed «الجموع» and «أو فما قيل»; both are odd as printed (perhaps «المجموع»). Transcribed as printed; the translation follows the apparent sense.
    {"type": "pair",
     "ar": "فقوله: إلى أن، أو إلا أن تركيب إضافي بملابسة الدخول والامتزاج حتى يلزم أن يكون الجموع معنى، أو فما قيل: إنه تكلف تكلف.",
     "en": "So his words “ilā an” or “illā an” are a compound by annexation, by virtue of the entering and blending, not such that the combination must be the meaning; so what has been said, that it is forced, is itself forced."},
]
